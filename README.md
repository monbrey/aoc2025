# AoC 2025 — Python runner

This workspace provides a tiny Python development environment and a dynamic entrypoint to run functions defined in `dayN` modules.

Quick start (Windows PowerShell):

1. Create a virtual environment and activate it:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies (if any):

```powershell
pip install -r requirements.txt
```

3. Run a function:

```powershell
python main.py 1a
# or list available modules and callables
python main.py --list
```

Project layout:

- `main.py` — entrypoint, accepts a target like `1a` (run `a` in `day1`).
- `day1/` — example module. Add `day2`, `day3`, etc., each with public functions.
- `requirements.txt` — dependency list (empty for now).

Notes:

- The runner expects modules named `dayN` (e.g. `day1`) with an `__init__.py`.
- Target format is `<number><function_name>`, e.g. `10b` runs `b` in `day10`.
