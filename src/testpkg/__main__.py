import os

if __name__ == "__main__":
    p = os.path.join(os.getenv("pythonLocation", "/"), "etc/testpkg/testpkg.conf")
    print(p)
    with open(p) as pp:
        print(pp.read())
