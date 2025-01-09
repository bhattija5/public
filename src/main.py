from textnode import TextNode, TextType


import os
import shutil

def delete_directory_contents(dest_dir):
    """Delete all contents of the destination directory."""
    for item in os.listdir(dest_dir):
        item_path = os.path.join(dest_dir, item)
        if os.path.isdir(item_path):
            shutil.rmtree(item_path)
        else:
            os.remove(item_path)

def copy_directory_contents(src_dir, dest_dir):
    """Recursively copy all contents from src_dir to dest_dir."""
    # Ensure the destination directory exists
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    
    # Delete existing contents of the destination directory
    delete_directory_contents(dest_dir)
    
    # Walk through the source directory
    for root, dirs, files in os.walk(src_dir):
        # Determine the relative path of the current directory
        rel_path = os.path.relpath(root, src_dir)
        dest_root = os.path.join(dest_dir, rel_path)
        
        # Create subdirectories in the destination directory
        if not os.path.exists(dest_root):
            os.makedirs(dest_root)
        
        # Copy each file from the source to the destination
        for file in files:
            src_file = os.path.join(root, file)
            dest_file = os.path.join(dest_root, file)
            
            # Log the file being copied
            print(f"Copying: {src_file} -> {dest_file}")
            
            # Copy the file
            shutil.copy(src_file, dest_file)

def main():
    src_dir = "static"  # Replace with your source directory
    dest_dir = "public"  # Replace with your destination directory
    
    # Copy contents from static to public
    copy_directory_contents(src_dir, dest_dir)

if __name__ == "__main__":
    main()