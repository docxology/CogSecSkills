"""Read-only CogSecSkills discovery from a prepared checkout."""

import os
from pathlib import Path
import subprocess
import sys


_COMMANDS = ("route", "list", "show")
_USAGE = "usage: library.py {route,list,show} [arguments]"
_TIMEOUT_SECONDS = 30

# Use the runner from this checkout and dependencies from its prepared environment.
_RUNNER = """
import sys

root = sys.argv[1]
sys.path.insert(0, root + "/src")
try:
    from cogsecskills.cli import main
except ModuleNotFoundError as exc:
    if exc.name not in {"yaml", "tomli"}:
        raise
    sys.exit(f"CogSecSkills gateway: missing {exc.name}. Run 'uv sync --locked' in {root}.")

sys.exit(main(["--root", root, *sys.argv[2:]]))
"""


def _error(message: str, status: int = 1) -> int:
    print(f"CogSecSkills gateway: {message}", file=sys.stderr)
    return status


def main() -> int:
    args = sys.argv[1:]
    if args in (["-h"], ["--help"]):
        print(_USAGE)
        return 0
    if not args or args[0] not in _COMMANDS:
        return _error(f"expected route, list, or show. {_USAGE}", status=2)

    root = Path(__file__).resolve().parent.joinpath("../../../..").resolve()
    if not (root / "src/cogsecskills/cli.py").is_file():
        return _error(
            "checkout not found. Run the gateway from the checkout or a symlink."
        )

    if not (root / "registry/skills.yaml").is_file() or not next(
        (root / "skills").glob("*/*/skill.yaml"), None
    ):
        return _error("checkout is incomplete. Restore the registry and skill files.")

    python = (
        root / ".venv" / ("Scripts/python.exe" if os.name == "nt" else "bin/python")
    )
    setup = f"Run 'uv sync --locked' in {root}."
    if not python.is_file():
        return _error(f"checkout Python environment is missing. {setup}")

    try:
        return subprocess.run(
            [str(python), "-I", "-B", "-c", _RUNNER, str(root), *args],
            cwd=root,
            stdin=subprocess.DEVNULL,
            timeout=_TIMEOUT_SECONDS,
            check=False,
        ).returncode
    except OSError as exc:
        return _error(
            f"could not start the checkout's Python ({exc.strerror}). {setup}"
        )
    except subprocess.TimeoutExpired:
        return _error(f"{args[0]} exceeded {_TIMEOUT_SECONDS} seconds.")


if __name__ == "__main__":
    raise SystemExit(main())
