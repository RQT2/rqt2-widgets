from typing import Optional

from PySide6.QtWidgets import QLabel, QSizePolicy
from PySide6.QtCore import Qt, QSize, QTimer
from PySide6.QtGui import QPixmap


class ScaledIconLabel(QLabel):
    """QLabel that keeps an original QPixmap and rescales it on resize.

    Supports a non-linear scaling curve controlled by `scale_power` and a
    `base_size` which defines the reference size where scaling starts.

    - `base_size` (int): reference size in px (e.g. 96). When the available
      space equals `base_size`, displayed icon size is `base_size`.
    - `scale_power` (float): exponent applied to growth ratio. 1.0 = linear,
      >1.0 = accelerated (faster) growth, <1.0 = slower growth.

    Usage:
        lbl = ScaledIconLabel(parent, base_size=96, scale_power=2.0, max_size=256)
    """

    def __init__(self, parent=None, max_size: Optional[int] = 256, base_size: int = 128, scale_power: float = 1.0,
                 window_influence: float = 0.9, window_scale_factor: float = 0.45):
        super().__init__(parent)
        self._original = QPixmap()
        self.max_size = max_size or 0
        self.base_size = max(1, int(base_size))
        self.scale_power = float(scale_power)
        # how much the top-level window size influences scaling (0..1)
        self.window_influence = float(window_influence)
        # fraction of window smaller-dimension to consider as available space
        self.window_scale_factor = float(window_scale_factor)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setSizePolicy(QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred))

    def set_icon(self, path_or_pixmap):
        if isinstance(path_or_pixmap, QPixmap):
            self._original = path_or_pixmap
        else:
            self._original = QPixmap(path_or_pixmap)
        # immediate rescale and schedule a deferred rescale after layout
        self._rescale()
        QTimer.singleShot(0, self._rescale)

    def setPixmap(self, pixmap: QPixmap):
        # store source pixmap then rescale
        self._original = QPixmap(pixmap)
        # immediate rescale and schedule a deferred rescale after layout
        self._rescale()
        QTimer.singleShot(0, self._rescale)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self._rescale()

    def _rescale(self):
        if self._original.isNull():
            super().setPixmap(QPixmap())
            return
        w = max(1, self.width())
        h = max(1, self.height())
        local_avail = float(min(w, h))

        # consider top-level window size as an influence so icons can grow
        win = self.window()
        win_avail = 0.0
        try:
            ww = max(1, win.width())
            wh = max(1, win.height())
            win_avail = float(min(ww, wh)) * float(self.window_scale_factor)
        except Exception:
            win_avail = local_avail

        # blend local and window-derived available sizes
        avail = (1.0 - self.window_influence) * local_avail + self.window_influence * win_avail

        # --- Tiered override sizing (user preferences) ---
        # Prefer specific target sizes for certain top-level window ranges.
        # Rules (preferred):
        # - target 96px  when 670 < win.width() < 1200 and 550 < win.height() < 680
        # - target 256px when 1199 < win.width() <= 1500 and win.height() >= 699
        # - target 384px when win.width() > 1500 and win.height() > 700
        override_target = None
        try:
            tw = win.width()
            th = win.height()
            if tw < 1200 and th < 680:
                override_target = 96
            elif 1200 <= tw <= 1500 and 680 <= th <= 750:
                override_target = 256
            elif tw > 1500 and th > 750:
                override_target = 384
        except Exception:
            override_target = None

        # Dynamic symmetric mapping from available space to displayed size.
        # We map avail into a normalized value in [-1, 1] where 0==base_size,
        # -1 => smallest (use base_size/4 as hard minimum), +1 => max_size.
        # Then use a sign-preserving power to control steepness for both grow and shrink.
        bs = float(self.base_size)
        ms = float(self.max_size) if (self.max_size and self.max_size > 0) else max(bs * 4.0, bs)

        # Prevent division by zero
        span = max(1.0, ms - bs)
        norm = (avail - bs) / span
        if norm > 1.0:
            norm = 1.0
        if norm < -1.0:
            norm = -1.0

        # sign-preserving power
        if norm >= 0.0:
            factor = (norm ** self.scale_power)
        else:
            factor = -((abs(norm)) ** self.scale_power)

        # Map back to size: base_size + factor * span
        scaled_size = int(round(bs + factor * span))

        # If an override target was selected by window size, prefer it.
        if override_target is not None:
            scaled_size = int(override_target)

        # Also ensure we don't go below a sensible minimum (e.g., base_size/4)
        min_allowed = max(8, int(bs // 4))
        if scaled_size < min_allowed:
            scaled_size = min_allowed

        # Respect max_size
        if ms and ms > 0:
            scaled_size = min(scaled_size, int(ms))

        scaled = self._original.scaled(QSize(scaled_size, scaled_size), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        super().setPixmap(scaled)

    def set_max_size(self, max_size: int):
        self.max_size = max_size
        self._rescale()
