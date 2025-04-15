import os

def list_files_and_folders(path):
    try:
        print(f"\nContents of: {path}\n")
        for item in os.listdir(path):
            full_path = os.path.join(path, item)
            if os.path.isdir(full_path):
                print(f"[Folder] {item}")
            else:
                print(f"[File]   {item}")
    except Exception as e:
        print(f"Error: {e}")

# Example usage
windows_path = r"C:\Users\mrdar.DESKTOP-B6LKOPF\curseforge\minecraft\Instances\test create 6\mods"
list_files_and_folders(windows_path)
