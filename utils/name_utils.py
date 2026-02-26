import re


def sanitize_item_name(raw: str, ext: str = "", default_base: str = "new_item") -> str:
    """Sanitize a user-supplied name for items (nodes, launches, files).

    Rules:
    - Replace spaces with underscores.
    - Allow only letters, digits, dot, hyphen and underscore.
    - Convert to lowercase.
    - Strip trailing dots.
    - If empty after cleaning, use `default_base`.
    - Ensure first character is a letter (prefix with 'a' if necessary).
    - Append `ext` if provided and not already present.

    Returns the sanitized name (including ext when provided).
    """
    if raw is None:
        raw = ""
    combined = raw.strip()
    combined = combined.replace(' ', '_')
    base = re.sub(r'[^A-Za-z0-9._-]', '', combined)
    base = (base or '').lower().rstrip('.')
    if not base:
        base = default_base
    if not base[0].isalpha():
        base = 'a' + base
    if ext and not base.endswith(ext):
        return base + ext
    return base
