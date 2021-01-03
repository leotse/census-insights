from typing import Optional


def parseInt(value: str, default=0) -> Optional[int]:
    try:
        return int(value)
    except ValueError:
        return default
