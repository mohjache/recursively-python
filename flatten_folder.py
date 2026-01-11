import os
import shutil

def move_contents_to_root(root_dir):
   for dirpath, dirnames, filenames in os.walk(root_dir):
        # Skip the top-level directory itself
        if dirpath == root_dir:
            continue
        for filename in filenames:
            relative_path = os.path.relpath(dirpath, root_dir)
            new_filename =  f"{relative_path.replace(os.sep, '_')}_{filename}"
            src_path = os.path.join(dirpath, filename)
            dest_path = os.path.join(root_dir, new_filename)
            print(f"Moving {src_path} -> {dest_path}")
            shutil.move(src_path, dest_path)