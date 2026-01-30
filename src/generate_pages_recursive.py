import os

from generate_page import generate_page


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    for entry in os.listdir(dir_path_content):
        entry_path = os.path.join(dir_path_content, entry)

        if os.path.isfile(entry_path):
            if not entry_path.endswith(".md"):
                continue

            relative_path = os.path.relpath(entry_path, dir_path_content)
            relative_html_path = relative_path.replace(".md", ".html")
            dest_path = os.path.join(dest_dir_path, relative_html_path)

            generate_page(entry_path, template_path, dest_path, basepath)
        else:
            new_dest_dir = os.path.join(dest_dir_path, entry)
            generate_pages_recursive(entry_path, template_path, new_dest_dir, basepath)

