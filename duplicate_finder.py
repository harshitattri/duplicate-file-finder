from pathlib import Path
import hashlib

folder_path = input("Paste the folder path to scan: ").strip().strip('"')
folder = Path(folder_path)

report_path = Path(__file__).resolve().parent / "duplicate_report.txt"
file_groups = {}
report_lines = []
files_scanned = 0

if not folder_path or not folder.is_dir():
    print("Folder not found. Check its name and location.")
else:
    for item in sorted(folder.rglob("*")):
        if item.resolve() == report_path:
            continue

        if item.is_file():
            hasher = hashlib.sha256()

            with item.open("rb") as file:
                while chunk := file.read(65536):
                    hasher.update(chunk)

            fingerprint = hasher.hexdigest()
            files_scanned += 1

            if fingerprint not in file_groups:
                file_groups[fingerprint] = []

            file_groups[fingerprint].append(item)

    group_count = 0
    extra_copies = 0
    extra_bytes = 0

    for files in file_groups.values():
        if len(files) > 1:
            group_count += 1
            copies_in_group = len(files) - 1
            file_size = files[0].stat().st_size
            group_extra_bytes = file_size * copies_in_group

            extra_copies += copies_in_group
            extra_bytes += group_extra_bytes

            report_lines.append(f"\nMatching group {group_count}:")

            for file_path in files:
                relative_path = file_path.relative_to(folder)
                report_lines.append(f" - {relative_path}")

            report_lines.append(f"Size of each file: {file_size} bytes")
            report_lines.append(
                f"Extra-copy size in this group: {group_extra_bytes} bytes"
            )

    if group_count == 0:
        report_lines.append("No duplicates found.")

    report_lines.append("\nSCAN SUMMARY")
    report_lines.append(f"Files scanned: {files_scanned}")
    report_lines.append(f"Matching groups: {group_count}")
    report_lines.append(f"Extra copies: {extra_copies}")
    report_lines.append(f"Total extra-copy size: {extra_bytes} bytes")
    report_lines.append("No files were deleted.")

    report_text = "\n".join(report_lines)
    print(report_text)

    report_path.write_text(report_text, encoding="utf-8")
    print("\nReport saved to:", report_path)
