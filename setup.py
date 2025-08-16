import os

structure = {
    "Notes": [
        "networking.md",
        "linux_basics.md",
        "recon_tools.md"
    ],
    "Scripts": [
        "simple_port_scanner.py",
        "password_strength_checker.py"
    ],
    "Projects": [
        "vm_setup.md",
        "practice_lab_walkthrough.md"
    ]
}

# Create directories and files
for folder, files in structure.items():
    os.makedirs(folder, exist_ok=True)
    for f in files:
        path = os.path.join(folder, f)
        with open(path, "w") as file:
            file.write("")  # create empty file
        print(f"Created {path}")

print("\n✅ Project structure created successfully.")
