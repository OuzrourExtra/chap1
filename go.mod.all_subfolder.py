import os
import re
import subprocess

# Define the rules for a valid folder/module name
def is_valid_folder_name(name):
    # Go module and folder naming rules:
    # - no spaces
    # - must start and end with a letter or digit
    # - only letters, digits, hyphens (-), underscores (_), and periods (.)
    # - no special characters or slashes
    pattern = r'^[a-zA-Z0-9]([a-zA-Z0-9._-]*[a-zA-Z0-9])?$'
    return re.match(pattern, name)

# Print the rules
def print_rules():
    print("\n🚫 Invalid folder name. Please follow these rules:")
    print("- No spaces")
    print("- Only letters, numbers, hyphens (-), underscores (_), and periods (.)")
    print("- Must start and end with a letter or digit")
    print("- No special characters or slashes\n")

# Get the base directory and the parent folder name
base_dir = os.getcwd()
parent_folder_name = os.path.basename(base_dir)

# Ask for folder name and validate
while True:
    folder_name = input("Enter a valid folder name: ").strip()
    if is_valid_folder_name(folder_name):
        break
    else:
        print_rules()

# Full path for the new folder
new_folder_path = os.path.join(base_dir, folder_name)

# Create the new folder
try:
    os.makedirs(new_folder_path)
    print(f"✅ Created folder: {new_folder_path}")
except FileExistsError:
    print(f"⚠️ Folder '{folder_name}' already exists, using existing folder.")

# Build the Go module path
module_path = f"github.com/ouzrour/extra/{parent_folder_name}/{folder_name}"
print(f"🚀 Initializing Go module: {module_path}")

# Run `go mod init`
try:
    subprocess.run(['go', 'mod', 'init', module_path], cwd=new_folder_path, check=True)
    print("✅ Go module initialized successfully.")
except subprocess.CalledProcessError as e:
    print(f"❌ Error initializing Go module: {e}")

# Create main.go file with basic content
main_go_content = """package main

func main() {

}
"""

main_go_path = os.path.join(new_folder_path, "main.go")
with open(main_go_path, "w") as f:
    f.write(main_go_content)

print(f"✅ Created {main_go_path} with basic Go code.")
print("🚀 Go module and main.go file created successfully.")