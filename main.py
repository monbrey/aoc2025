#!/usr/bin/env python3
"""Entry point to dynamically run functions in day modules.

Usage examples:
  python main.py 1a      # runs function `a` in module `day1`
  python main.py --list  # lists available `day*` modules and callables
"""
import argparse
import importlib
import re
import sys
from pathlib import Path


def run_target(target: str) -> None:
    m = re.match(r"^(\d+)([A-Za-z_][A-Za-z0-9_]*)$", target)
    if not m:
        raise SystemExit(f"Invalid target '{target}'. Use format like '1a' or '12b'.")
    day_num, func_name = m.groups()
    mod_name = f"day{int(day_num)}"
    try:
        mod = importlib.import_module(mod_name)
    except ModuleNotFoundError:
        raise SystemExit(f"Module '{mod_name}' not found. Make sure folder '{mod_name}' exists and has an __init__.py.")
    if not hasattr(mod, func_name):
        raise SystemExit(f"Function '{func_name}' not found in module '{mod_name}'.")
    fn = getattr(mod, func_name)
    if not callable(fn):
        raise SystemExit(f"Attribute '{func_name}' in module '{mod_name}' is not callable.")
    result = fn()
    if result is not None:
        print(result)


def list_modules() -> None:
    p = Path('.')
    days = sorted([d.name for d in p.iterdir() if d.is_dir() and d.name.startswith('day')])
    if not days:
        print('No day modules found.')
        return
    for d in days:
        try:
            mod = importlib.import_module(d)
        except Exception as e:
            print(f"{d}: import error: {e}")
            continue
        names = [name for name in dir(mod) if not name.startswith('_') and callable(getattr(mod, name))]
        print(f"{d}: {', '.join(names) if names else '(no public callables)'}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Run functions from day modules. Target like '1a' -> run 'a' in 'day1'.")
    parser.add_argument('target', nargs='?', help="Target to run, e.g. '1a'.")
    parser.add_argument('--list', action='store_true', help='List available day modules and callables')
    args = parser.parse_args()
    if args.list:
        list_modules()
        return
    if not args.target:
        parser.print_help()
        raise SystemExit(1)
    run_target(args.target)


if __name__ == '__main__':
    main()
