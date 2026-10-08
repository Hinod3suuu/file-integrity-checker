# File Integrity Checker

A lightweight Python-based file integrity verification utility designed to detect modifications to registered files using SHA-256 cryptographic hashing. The application generates file fingerprints, stores them in a local JSON database, and compares them against current file hashes to identify changes.

This project demonstrates fundamental cybersecurity concepts, including cryptographic hashing, file integrity verification, and baseline comparison.

## Features

- SHA-256 cryptographic file hashing
- File registration and fingerprint storage
- Integrity verification against saved fingerprints
- Detection of modified files
- JSON-based fingerprint database
- Binary file processing with memory-efficient chunking
- Error handling for missing files and access restrictions
- Support for Windows, Linux, and macOS
- No external dependencies required

## Tech Stack

- Python 3
- Hashlib
- JSON
- Pathlib
- File I/O
- Git & GitHub

## Project Structure

```text
file-integrity-checker/
├── .gitignore
├── integrity.py
├── LICENSE
└── README.md
```

The `hashes.json` database and local test files are intentionally excluded from version control through `.gitignore`.

## Installation

Clone the repository:

```bash
git clone https://github.com/Hinod3suuu/file-integrity-checker.git
cd file-integrity-checker
```

No additional Python packages are required.

## Usage

Run the application with:

```bash
python integrity.py
```

On Windows, the Python launcher can also be used:

```powershell
py integrity.py
```

The application displays an interactive menu:

```text
=== File Integrity Checker ===
1. Register file
2. Verify file
```

### File Registration

To register a file, select option `1` and provide its path.

Example:

```text
Choose an option (1/2): 1
Enter file path: example.txt

[REGISTERED] File fingerprint saved.
SHA-256: <generated_hash>
```

The application calculates the file's SHA-256 fingerprint and stores it in `hashes.json`.

Registering an existing file again updates its saved fingerprint.

### File Verification

To verify a registered file, select option `2` and provide its path.

Example:

```text
Choose an option (1/2): 2
Enter file path: example.txt
```

If the file remains unchanged:

```text
[UNCHANGED] File integrity verified.
```

If the file has been modified:

```text
[MODIFIED] WARNING: File contents have changed!
```

If the file has not been registered:

```text
[UNKNOWN] File has not been registered.
```

## Modification Detection

When a registered file is verified, the application:

1. Retrieves the original SHA-256 fingerprint from the JSON database.
2. Reads the current file contents in binary mode.
3. Calculates a new SHA-256 fingerprint.
4. Compares the current fingerprint against the registered baseline.
5. Reports whether the file remains unchanged or has been modified.

This provides a simple demonstration of file integrity verification and change detection.

## Security

File fingerprints are generated using SHA-256, a cryptographic hashing algorithm commonly used for integrity verification.

The application processes files in chunks to avoid loading entire files into memory.

The `.gitignore` configuration prevents the local `hashes.json` database from being tracked by Git, keeping locally registered file paths out of the public repository.

The application does not modify files during verification.

However, the fingerprint database is not protected against tampering. An attacker with sufficient access could modify both a file and its stored fingerprint.

Matching fingerprints indicate consistency with the registered baseline but do not guarantee that a file is safe or free from malware.

## Limitations

- Files must be registered before verification.
- Verification is performed manually rather than continuously.
- The application detects modifications but cannot identify who made them.
- The local JSON database is not protected against unauthorized modifications.
- Registering an existing file again replaces its original fingerprint.
- File verification requires access to the registered file.

## Future Improvements

Potential extensions include recursive directory scanning, batch file registration, continuous integrity monitoring at configurable intervals, persistent verification logs, and automated notifications when file modifications are detected.

Additional improvements could include fingerprint database protection, integrity report generation, and support for multiple hashing algorithms.

## Author

**Hinod3suuu**

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.