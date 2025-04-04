from setuptools import setup
import py2exe
import glob
import os

# Ensure paths use forward slashes for compatibility
def fix_path(path):
    return path.replace("\\", "/")

setup(
    console=["main.py"],
    options={
        "py2exe": {
            "bundle_files": 1,   # Bundle everything into the executable
            "compressed": True,
            "optimize": 2,
            "includes": [],
        }
    },
    zipfile=None,  # Required when using bundle_files = 1
    data_files=[
        ("sprites", [fix_path(f) for f in glob.glob("sprites/*.json")]),
        ("sfx", [fix_path(f) for f in glob.glob("sfx/*.ogg") + glob.glob("sfx/*.wav")]),
        ("levels", [fix_path(f) for f in glob.glob("levels/*.json")]),
        ("img", [fix_path(f) for f in glob.glob("img/*.gif") + glob.glob("img/*.png")]),
        ("", ["settings.json"]),
    ],
)

