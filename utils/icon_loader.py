import os
from typing import Iterable, Optional

from PySide6.QtGui import QIcon, QPixmap


def resolve_icon_path(icon_dirs: Optional[Iterable[str]], rel_path: str) -> str:
    """Return the first existing absolute path for rel_path under icon_dirs.

    If no match is found, return rel_path unchanged (caller may try it as-is).
    """
    if not icon_dirs:
        return rel_path

    # single string -> treat as one base
    if isinstance(icon_dirs, str):
        icon_dirs = [icon_dirs]

    for base in icon_dirs:
        try:
            # candidate as-joined
            cand = os.path.normpath(os.path.join(base, rel_path))
        except Exception:
            continue
        if os.path.exists(cand):
            return cand
        # if rel_path includes a leading 'icons/' and base already points to an icons folder,
        # avoid duplicating 'icons/icons/...'
        parts = rel_path.replace('\\', '/').lstrip('/').split('/')
        if parts and parts[0] == 'icons':
            tail = '/'.join(parts[1:])
            try:
                cand2 = os.path.normpath(os.path.join(base, tail))
            except Exception:
                cand2 = None
            if cand2 and os.path.exists(cand2):
                return cand2

    return rel_path


def load_qicon(rel_path: str, icon_dirs: Optional[Iterable[str]] = None, fallback: Optional[str] = None) -> QIcon:
    """Load a QIcon from resolved path or fallback.

    - `rel_path` is a relative path like 'icons/code/default.svg' or 'logo.svg'.
    - `icon_dirs` is iterable of base dirs to search in order.
    - `fallback` is an optional path to use when nothing is found.
    """
    path = resolve_icon_path(icon_dirs, rel_path)
    ico = QIcon()
    if os.path.exists(path):
        ico.addFile(path)
        return ico
    if fallback and os.path.exists(fallback):
        ico.addFile(fallback)
        return ico
    return ico


def load_qpixmap(rel_path: str, icon_dirs: Optional[Iterable[str]] = None, fallback: Optional[str] = None) -> QPixmap:
    """Load a QPixmap from resolved path or fallback.

    Returns an empty QPixmap if nothing is found.
    """
    path = resolve_icon_path(icon_dirs, rel_path)
    pix = QPixmap()
    if os.path.exists(path):
        pix.load(path)
        return pix
    if fallback and os.path.exists(fallback):
        pix.load(fallback)
        return pix
    return pix


def _resolve_icon(icon_dirs: Optional[Iterable[str]], rel_path: str) -> str:
    """Backwards-compatible helper used by generated forms named `_resolve_icon`.

    Delegates to `resolve_icon_path`.
    """
    return resolve_icon_path(icon_dirs, rel_path)
