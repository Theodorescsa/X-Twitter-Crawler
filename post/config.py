import os
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]


def env(key: str, default=None, cast=str):
    v = os.environ.get(key, default)
    if v is None:
        return None
    if cast is bool:
        return str(v).lower() in ("1", "true", "yes", "y", "on")
    try:
        return cast(v)
    except Exception:
        return default