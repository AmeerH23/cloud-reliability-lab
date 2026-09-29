from pathlib import Path

project_dir = Path.cwd()
app_dir = project_dir / "app"

print(f"Project directory: {project_dir}")
print(f"Application directory: {app_dir}")

print("\nPython files:")

for file in app_dir.iterdir():
    if file.suffix == ".py":
        print(f"- {file.name}")
