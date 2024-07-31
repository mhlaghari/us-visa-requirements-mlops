import os
from pathlib import Path

def get_project_root() -> Path:
    current_path = Path(__file__).resolve()
    for parent in current_path.parents:
        if (parent / '.project-root').exists() or (parent / '.git').exists():
            return parent
    raise FileNotFoundError("Could not find project root. Make sure there's a '.project-root' file or a '.git' directory in your project.")

def from_root(*paths: str) -> Path:
    return get_project_root().joinpath(*paths)

def from_here(*paths: str) -> Path:
    return Path(__file__).resolve().parent.joinpath(*paths)