"""Script for fix notebook from Google Colab."""  # noqa: INP001

import json
import pathlib

HERE = pathlib.Path(__file__).parent.resolve()


def fix_json(path: pathlib.Path) -> None:
    """Fix json file."""
    data = path.read_bytes()
    content = json.loads(data)
    try:
        widgets = content["metadata"]["widgets"]
        widget = widgets["application/vnd.jupyter.widget-state+json"]
        widget["state"] = {}
        print(f"Fixed {path} !")
    except KeyError:
        pass
    path.write_text(json.dumps(content, separators=(",", ":")) + "\n", "utf-8")


def fix_notebooks() -> None:
    """Fix notebooks."""
    fix_json(HERE / "attack_model.ipynb")
    fix_json(HERE / "recreate_model.ipynb")


if __name__ == "__main__":
    fix_notebooks()
