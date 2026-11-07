# Duplicate File Finder

A beginner Python project that finds files with matching contents,
even when their filenames or folder locations differ.

## Features

- Scans a selected folder and its subfolders.
- Groups files by their SHA-256 hashes.
- Reads files in 64 KB chunks.
- Reports matching groups and extra copies.
- Calculates the total content size of extra copies.
- Saves results to duplicate_report.txt.
- Does not delete files.

## Requirements

- Python 3.8 or newer.
- No third-party packages required.

## How to Run

1. Open duplicate_finder.py in Python IDLE.
2. Select Run > Run Module, or press F5.
3. Paste the folder path to scan and press Enter.
4. Read the results in the Shell.
5. Open duplicate_report.txt beside the script.

Each successful scan replaces the previous report.

## Manual Tests Completed

- Identical files were grouped together.
- Editing a copied file removed it from the matching group.
- Matching files in subfolders were detected.
- An invalid folder path displayed a helpful message.
- Three matching files were counted as two extra copies.
- Two extra copies of a 21-byte file totalled 42 bytes.

## Current Limitations

- Matches are based on hashes; byte-by-byte verification is not implemented.
- Unreadable files may interrupt the scan.
- Files should not be modified while scanning.
- Reported sizes are content sizes, not guaranteed recoverable disk space.

## What I Am Learning

Python paths, loops, dictionaries, file handling, hashing,
input validation, and manual testing.