from distutils.core import setup
from glob import glob
import py2exe
import shutil

print("clean-up dist\\*")
try:
    shutil.rmtree("dist")
except FileNotFoundError:
    pass

manifest = """\
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<assembly xmlns="urn:schemas-microsoft-com:asm.v1" manifestVersion="1.0">
<assemblyIdentity
    version="{version}"
    processorArchitecture="*"
    name="{name}"
    type="win32"
/>
<description></description>
<dependency>
    <dependentAssembly>
        <assemblyIdentity
            type="win32"
            name="Microsoft.Windows.Common-Controls"
            version="6.0.0.0"
            processorArchitecture="*"
            publicKeyToken="6595b64144ccf1df"
            language="*"
        />
    </dependentAssembly>
</dependency>
</assembly>"""

target = dict(
    script="example.py",
    version="1.0.0.0",
    name="Example",
    description="Test Description",
    copyright="k_hir@hotmail.com",
    other_resources=[(24, 1, manifest.format(name="Example", version="5.0.0.0"))]
)

options = dict(
    optimize=2,
    bundle_files=2,
    excludes=["tkinter"],
    dll_excludes=[]
)

setup(
    windows=[target],
    options={"py2exe": options}
)
