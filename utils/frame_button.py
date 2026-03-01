from __future__ import annotations

import os
from typing import List, Optional

from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QPixmap, QCursor, QIcon
from PySide6.QtWidgets import QLabel, QFrame, QVBoxLayout, QApplication

try:
    from .scaled_icon_label import ScaledIconLabel
except Exception:
    # support loading the module when executed via importlib.spec_from_file_location
    import importlib.util as _il, os as _os
    _spec = _il.spec_from_file_location("scaled_icon_label", _os.path.join(_os.path.dirname(__file__), "scaled_icon_label.py"))
    _mod = _il.module_from_spec(_spec)
    _spec.loader.exec_module(_mod)
    ScaledIconLabel = _mod.ScaledIconLabel

try:
    from . import icon_loader
except Exception:
    import importlib.util as _il, os as _os
    _spec = _il.spec_from_file_location("icon_loader", _os.path.join(_os.path.dirname(__file__), "icon_loader.py"))
    _mod = _il.module_from_spec(_spec)
    _spec.loader.exec_module(_mod)
    icon_loader = _mod


class FrameButtonWidget(QFrame):
    """Interactive frame that behaves like a button with icon, title and info.

    Uses `ScaledIconLabel` and `icon_loader` to resolve and load icons from
    a list of `icon_dirs` with a placeholder fallback.
    """

    clicked = Signal()

    def __init__(self, icon_path: Optional[str] = None, title: str = "", info: str = "",
                 parent=None, icon_dirs: Optional[List[str]] = None, max_size: int = 512,
                 apply_theme_from_palette: bool = True):
        super().__init__(parent)
        self.setCursor(QCursor(Qt.PointingHandCursor))
        # objectName kept for compatibility; use properties for styling (role/variant/state)
        self.setObjectName("FrameButtonWidget")
        # role acts like a CSS class; variant can be 'primary', 'secondary', etc.
        self.setProperty('role', 'frame-button')
        # default visual variant
        self.setProperty('variant', 'default')
        # state: 'normal' | 'pressed' — QSS can match [state="pressed"]
        self.setProperty('state', 'normal')
        self.icon_dirs = icon_dirs or []
        self.max_size = max_size

        self.icon = ScaledIconLabel(max_size=self.max_size, parent=self)
        # Use nonlinear scaling: base 96px but accelerated growth (power 2.0)
        self.icon = ScaledIconLabel(max_size=self.max_size, parent=self, base_size=128, scale_power=1.8)
        self.title = QLabel(title, parent=self)
        self.title.setProperty('role', 'title')
        self.info = QLabel(info, parent=self)
        self.info.setProperty('role', 'info')

        layout = QVBoxLayout(self)
        layout.setContentsMargins(8, 8, 8, 8)
        layout.setSpacing(6)
        layout.addWidget(self.icon, 1)
        layout.addWidget(self.title, 0)
        layout.addWidget(self.info, 0)

        if icon_path:
            pix = self._load_pix(icon_path)
            if pix and not pix.isNull():
                self.icon.setPixmap(pix)

                # Apply a lightweight QSS based on the current QApplication palette so
                # the FrameButton matches the platform button appearance by default.
                # This uses `palette(...)` in QSS so it follows theme changes where
                # supported. If an application-level QSS later defines rules for
                # role="frame-button" those rules can override visuals.
        if apply_theme_from_palette:
            try:
                self._apply_palette_style()
            except Exception:
                pass

    def _apply_palette_style(self):
        # Build a widget-scoped stylesheet using palette() references so the
        # frame adopts the current theme's button colors.
        variant = self.property('variant') or 'default'
        style = f"""
QFrame[role="frame-button"][variant="{variant}"] {{
    background: palette(button);
    color: palette(button-text);
    border: 1px solid palette(mid);
    border-radius: 6px;
    padding: 6px;
}}
QFrame[role="frame-button"][variant="{variant}"]:hover {{
    background: palette(alternate-base);
}}
QFrame[role="frame-button"][variant="{variant}"][state="pressed"] {{
    background: palette(mid);
}}
QFrame[role="frame-button"][variant="{variant}"] QLabel[role="title"] {{
    color: palette(button-text);
    font-weight: 600;
}}
"""
        # Apply only to this widget and its children
        self.setStyleSheet(style)

    def enterEvent(self, event):
        super().enterEvent(event)
        try:
            self.setProperty('hover', True)
            self.style().unpolish(self)
            self.style().polish(self)
            self.update()
        except Exception:
            pass

    def leaveEvent(self, event):
        super().leaveEvent(event)
        try:
            self.setProperty('hover', False)
            self.style().unpolish(self)
            self.style().polish(self)
            self.update()
        except Exception:
            pass

    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        try:
            self.setProperty('state', 'pressed')
            self.style().unpolish(self)
            self.style().polish(self)
            self.update()
        except Exception:
            pass

    def mouseReleaseEvent(self, event):
        super().mouseReleaseEvent(event)
        try:
            # restore state before emitting clicked to allow QSS to reflect press
            self.setProperty('state', 'normal')
            self.style().unpolish(self)
            self.style().polish(self)
            self.update()
        except Exception:
            pass
        self.clicked.emit()

    def setVariant(self, variant: str):
        """Set visual variant used by QSS selectors (e.g. 'primary')."""
        try:
            self.setProperty('variant', variant)
            self.style().unpolish(self)
            self.style().polish(self)
            self.update()
        except Exception:
            pass

    def _load_pix(self, rel_path: str) -> QPixmap:
        # Prefer explicit resolution so we can surface useful diagnostics
        base = os.path.normpath(os.path.join(os.path.dirname(__file__), '..'))

        # 1) Prefer icon_loader._resolve_icon (it may return recolored temp SVG)
        try:
            if hasattr(icon_loader, 'recolor_svg_to_temp'):
                temp_svg = icon_loader.recolor_svg_to_temp(rel_path)
            else:
                temp_svg = rel_path
            if temp_svg and os.path.exists(temp_svg):
                pm = QPixmap(temp_svg)
                if pm and not pm.isNull():
                    return pm
                try:
                    ico = QIcon(temp_svg)
                    pm2 = ico.pixmap(min(self.max_size or 256, 512), min(self.max_size or 256, 512))
                    if pm2 and not pm2.isNull():
                        return pm2
                except Exception:
                    pass
        except Exception as e:
            print(f"[FrameButtonWidget] _resolve_icon error: {e}")

        # fallback: try resolve_icon_path
        resolved = None
        try:
            if hasattr(icon_loader, 'resolve_icon_path'):
                resolved = icon_loader.resolve_icon_path(self.icon_dirs, rel_path)
                if resolved and os.path.exists(resolved):
                    pm = QPixmap(resolved)
                    if pm and not pm.isNull():
                        return pm
                    try:
                        ico = QIcon(resolved)
                        pm2 = ico.pixmap(min(self.max_size or 256, 512), min(self.max_size or 256, 512))
                        if pm2 and not pm2.isNull():
                            return pm2
                    except Exception:
                        pass
        except Exception as e:
            print(f"[FrameButtonWidget] resolve_icon_path error: {e}")

        # 2) Try icon_loader.load_qpixmap which may handle SVG/QIcon internals
        try:
            pix = icon_loader.load_qpixmap(rel_path, icon_dirs=self.icon_dirs)
            if pix and not pix.isNull():
                return pix
        except Exception as e:
            print(f"[FrameButtonWidget] load_qpixmap error: {e}")

        # 3) If rel_path is absolute, try it directly
        if os.path.isabs(rel_path) and os.path.exists(rel_path):
            return QPixmap(rel_path)

        # 4) Try several plausible candidates relative to known locations
        candidates = [
            os.path.normpath(os.path.join(base, 'icons', rel_path)),
            os.path.normpath(os.path.join(base, '..', 'rqt2-components', 'assets', 'branding', rel_path)),
            os.path.normpath(os.path.join(base, '..', 'rqt2-components', 'assets', 'icons', rel_path)),
            os.path.normpath(rel_path),
        ]
        for p in candidates:
            if os.path.exists(p):
                try:
                    return QPixmap(p)
                except Exception:
                    pass

        # 5) Fallback to package placeholder if present
        placeholder = os.path.join(base, 'icons', 'placeholder.svg')
        if os.path.exists(placeholder):
            print(f"[FrameButtonWidget] icon not found: {rel_path!r}. Using placeholder. Candidates checked: {candidates}")
            return QPixmap(placeholder)

        # 6) Nothing found — emit diagnostic and return empty pixmap
        print(f"[FrameButtonWidget] icon not found: {rel_path!r}. Candidates checked: {candidates}")
        return QPixmap()

    def setTitle(self, text: str):
        self.title.setText(text)

    def setInfo(self, text: str):
        self.info.setText(text)

    def setIcon(self, path: str):
        pix = self._load_pix(path)
        if pix and not pix.isNull():
            self.icon.setPixmap(pix)
