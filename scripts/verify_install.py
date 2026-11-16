"""Assert that CI tests the installed wheels, not a source/workspace import."""

import importlib.util
import json
import sys
from importlib.metadata import distribution
from pathlib import Path

import app

import dfe_copilot

for module in (app, dfe_copilot):
    assert Path(module.__file__).resolve().is_relative_to(Path(sys.prefix).resolve())
for name in ("copilot-core", "dfe-copilot"):
    direct = json.loads(distribution(name).read_text("direct_url.json"))
    assert not direct.get("dir_info", {}).get("editable", False)
assert importlib.util.find_spec("iic_copilot") is None
from dfe_copilot.resources import DATA_DIR, UI_DIR

assert DATA_DIR.is_relative_to(Path(sys.prefix))
assert (UI_DIR / "index.html").is_file()
print("Installed core/product wheels and fiscal resources verified")
