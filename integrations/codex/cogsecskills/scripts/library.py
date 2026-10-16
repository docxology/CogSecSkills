"""Forward gateway arguments to the repository CLI without depending on cwd."""

from pathlib import Path
import subprocess
import sys


def main() -> int:
    root = Path(__file__).resolve().parents[4]
    return subprocess.run(
        [
            "uv", "run", "--project", str(root), "python", "-m", "cogsecskills",
            "--root", str(root), *sys.argv[1:],
        ],
        check=False,
    ).returncode


if __name__ == "__main__":
    raise SystemExit(main())
