from pathlib import Path
import sys
import os
import shutil

exclude = [
    ".git",
    ".gitkeep",
    "CNAME",
    "README.md",
]

root_name = Path().cwd().stem.split("-")[0]
target = Path.cwd().parent / f"{root_name}.github.io"
print(f"deploying to {target}\n")

def unknown(item):
    print(f"UNKNOWN ITEM: {item}")
    sys.exit(1)

print(f"removing:", end=' ')
for item in target.iterdir():
    if item.name in exclude:
        continue
    print(f"{item.name}", end=', ')
    if item.is_file():
        item.unlink()
    elif item.is_dir():
        shutil.rmtree(item)
    else:
        unknown(item)

print(f"\n\ncopying:", end=' ')
for src in (Path.cwd() / "public").iterdir():
    print(f"{src.name}", end=', ')
    if src.is_file():
        shutil.copy(src, target)
    elif src.is_dir():
        shutil.copytree(src, target / src.name)
    else:
        unknown(src)
print("\n")
# print(Path.cwd() / "404")
# print(target/ "404")
# shutil.copytree(Path.cwd() / "404", target / "404")
# shutil.copy((Path.cwd() / "404.html"), target)
# shutil.copytree(Path.cwd() / "htmlbook", target / "htmlbook")

# CNAME = Path.cwd() / "CNAME"
# if CNAME.exists():
#     print("copying CNAME")
#     shutil.copy(CNAME, target)
