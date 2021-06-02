import os
import pathlib

if __name__ == "__main__":
    pp = pathlib.Path(os.path.join(os.getenv("pythonLocation", "/")))
    print(pp)
    ppcfg = pp / "etc" / "testpkg" / "testpkg.conf"
    print(ppcfg)
    with open(ppcfg) as h:
        print(h.read())
