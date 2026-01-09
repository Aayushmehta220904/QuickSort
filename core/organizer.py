from pathlib import Path
import shutil

CATEGORIES = {
    "PDF": {".pdf"},
    "Word": {".doc", ".docx", ".rtf", ".odt"},
    "Excel": {".xls", ".xlsx", ".csv", ".ods"},
    "PowerPoint": {".ppt", ".pptx", ".odp"},
    "Text": {".txt", ".md", ".log"},

    "Python": {".py"},
    "JavaScript": {".js", ".mjs", ".cjs"},
    "TypeScript": {".ts", ".tsx"},
    "Web": {".html", ".css", ".scss", ".sass"},
    "C": {".c", ".h"},
    "C++": {".cpp", ".cc", ".cxx", ".hpp", ".hh", ".hxx"},
    "Java": {".java"},
    "CSharp": {".cs"},
    "Go": {".go"},
    "Rust": {".rs"},
    "PHP": {".php"},
    "Ruby": {".rb"},
    "Kotlin": {".kt"},
    "Swift": {".swift"},
    "Shell": {".sh", ".zsh", ".bash"},
    "SQL": {".sql"},
    "Data": {".json", ".xml", ".yaml", ".yml"},
    "Notebooks": {".ipynb"},

    "Images": {".jpg", ".jpeg", ".png", ".gif", ".webp", ".heic"},
    "Videos": {".mp4", ".mkv", ".avi", ".mov"},
    "Music": {".mp3", ".wav", ".m4a"},
    "Archives": {".zip", ".rar", ".7z", ".tar", ".gz"}
}

def get_category(extension):
    if not extension:
        return "Others"

    extension = extension.lower()

    for category, extensions in CATEGORIES.items():
        if extension in extensions:
            return category

    return "Others"

def get_unique_destination(dest_path):
    counter = 1
    new_path = dest_path

    while new_path.exists():
        new_path = dest_path.with_stem(f"{dest_path.stem}_{counter}")
        counter += 1

    return new_path

def organize_folder(target_path):
    target = Path(target_path)

    if not target.exists() or not target.is_dir():
        raise ValueError("Invalid folder path")

    for item in target.iterdir():
        if item.is_dir():
            continue

        category = get_category(item.suffix)
        category_folder = target / category
        category_folder.mkdir(exist_ok=True)

        destination = category_folder / item.name
        destination = get_unique_destination(destination)

        shutil.move(str(item), str(destination))