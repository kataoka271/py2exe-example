from distutils.core import setup
from glob import glob
import py2exe
import shutil

print("clean-up dist\\*")
try:
    shutil.rmtree("dist")
except FileNotFoundError:
    pass

target = dict(
    script="example.py",
    version="1.0.0.0",
    name="Example",
    description="Test Description",
    copyright="k_hir@hotmail.com",
)

options = dict(
    optimize=2,
    bundle_files=2,
    excludes=["tkinter"],
    dll_excludes=[]
)

setup(
    console=[target],
    options={"py2exe": options}
)
