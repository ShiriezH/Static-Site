import sys

from copy_static import copy_static
from generate_pages_recursive import generate_pages_recursive


def main():
    basepath = "/"
    out_dir = "docs"

    if len(sys.argv) > 1:
        basepath = sys.argv[1]

    # If basepath is not "/", build inside docs/<repo_name>/
    if basepath != "/":
        out_dir = "docs" + basepath.rstrip("/")

    copy_static("static", out_dir)
    generate_pages_recursive("content", "template.html", out_dir, basepath)


main()
