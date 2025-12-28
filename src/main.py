import os, shutil, sys

from copystatic import copy_files_recursive
from gencontent import generate_pages_recursive

dir_path_static = "./static"
dir_path_public = "./docs"
dir_path_content = "./content"
template_path = "./template.html"
default_basepath = "/"
    
def main():
    basepath = default_basepath
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    if not basepath.endswith("/"):
        basepath = f'{basepath}/'

    print(f'Using basepath: {basepath}')
    
    print(f"Deleting {dir_path_public} directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print(f"Copying static files from {dir_path_static} to {dir_path_public} directory...")
    copy_files_recursive(dir_path_static, dir_path_public)
    
    print(f"Generating content from {dir_path_content} into {dir_path_public}...")
    generate_pages_recursive(dir_path_content, template_path, dir_path_public, basepath)
    
if __name__ == "__main__":
    main()
