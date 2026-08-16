from pathlib import Path
import shutil
def organizer(directory):
    p = Path(directory)
    files = p.iterdir()

    dictionary= {
        "DOCUMENTS": [".pdf", ".doc", ".docx", ".txt", ".rtf", ".odt"],
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg", ".bmp", ".tiff"],
        "Videos": [".mp4", ".mov", ".avi", ".mkv", ".webm"],
        "Audios": [".mp3", ".wav", ".m4a"],
        "Codes": [".py", ".cpp", ".java", ".c", ".h", ".js", ".html", ".css", ".php", ".sql", ".json"],
        "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
        "Executables": [".exe", ".msi", ".apk", ".deb"]
    }
    count = {}
    for category in dictionary:
        count[category] = 0
    count["Other"] = 0
    Other = p / "Others"
    Other.mkdir(exist_ok=True)
    for category in dictionary:
        path = p / category
        path.mkdir(exist_ok=True)

    for f in files:
        if f.is_file():
            extension = f.suffix.lower()
            found = False
            for category,extensions in dictionary.items():
                if extension in extensions:
                    destination = p / category / f.name
                    if destination.exists():
                        counter = 1
                        while destination.exists():
                            filename = f"{f.stem}_{counter}{f.suffix}"
                            destination = p / category / filename
                            counter+=1

                    shutil.move(f ,destination)
                    count[category] +=1
                    found = True
                    break
            if not found:
                shutil.move(f ,p / Other / f.name)
                count["Other"] +=1
    return count
directory = input("Enter the directory name that you want to organize: ")

summary = organizer(directory)

print("\n========================================")
print("       FILE ORGANIZATION COMPLETE")
print("========================================\n")

for category, number in summary.items():
    print(f"{category:<15}: {number}")

print("----------------------------------------")

total = sum(summary.values())

print(f"{'TOTAL FILES':<15}: {total}")

print("========================================")


