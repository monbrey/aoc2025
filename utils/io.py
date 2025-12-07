from pathlib import Path
from typing import Optional


def read_input_for(module_file: str, strip: bool = True) -> str:
    """Read `input.txt` located in the same folder as the given module file.

    `module_file` should be `__file__` from the caller. Returns empty string
    if the file does not exist. If `strip` is True, trailing newlines are removed.
    """
    p = Path(module_file).resolve().parent / "input.txt"
    try:
        data = p.read_text(encoding="utf-8")
    except FileNotFoundError:
        return ""
    return data.rstrip("\n") if strip else data


def read_day_input(day: int, base_dir: Optional[Path] = None, strip: bool = True) -> str:
    """Read `input.txt` for a specific day folder like `day1`, `day2`.

    Useful when reading by day number from non-module contexts. `base_dir` defaults
    to the current working directory.
    """
    base = base_dir or Path.cwd()
    p = base / f"day{int(day)}" / "input.txt"
    try:
        data = p.read_text(encoding="utf-8")
    except FileNotFoundError:
        return ""
    return data.rstrip("\n") if strip else data
