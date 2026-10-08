import hashlib
import json
from pathlib import Path


DATABASE = Path("hashes.json")


def calculate_hash(file_path):
    """Calculate the SHA-256 hash of a file."""

    sha256 = hashlib.sha256()

    with open(file_path, "rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            sha256.update(chunk)

    return sha256.hexdigest()


def load_hashes():
    """Load previously saved file hashes."""

    if DATABASE.exists():
        with open(DATABASE, "r", encoding="utf-8") as file:
            return json.load(file)

    return {}


def save_hashes(hashes):
    """Save file hashes to the database."""

    with open(DATABASE, "w", encoding="utf-8") as file:
        json.dump(hashes, file, indent=4)


def register_file(file_path):
    """Register a file's original fingerprint."""

    hashes = load_hashes()

    file_hash = calculate_hash(file_path)

    hashes[str(Path(file_path).resolve())] = file_hash

    save_hashes(hashes)

    print("\n[REGISTERED] File fingerprint saved.")
    print(f"SHA-256: {file_hash}")


def verify_file(file_path):
    """Verify a file against its saved fingerprint."""

    hashes = load_hashes()

    file_key = str(Path(file_path).resolve())

    if file_key not in hashes:
        print("\n[UNKNOWN] File has not been registered.")
        return

    current_hash = calculate_hash(file_path)
    original_hash = hashes[file_key]

    if current_hash == original_hash:
        print("\n[UNCHANGED] File integrity verified.")
    else:
        print("\n[MODIFIED] WARNING: File contents have changed!")


def main():
    print("\n=== File Integrity Checker ===")
    print("1. Register file")
    print("2. Verify file")

    choice = input("\nChoose an option (1/2): ").strip()

    if choice not in ("1", "2"):
        print("\n[ERROR] Invalid option.")
        return

    file_path = input("Enter file path: ").strip().strip('"')

    try:
        if choice == "1":
            register_file(file_path)

        elif choice == "2":
            verify_file(file_path)

    except FileNotFoundError:
        print("\n[ERROR] File not found.")

    except PermissionError:
        print("\n[ERROR] Permission denied.")

    except IsADirectoryError:
        print("\n[ERROR] Please select a file, not a directory.")

    except (json.JSONDecodeError, OSError) as error:
        print(f"\n[ERROR] {error}")


if __name__ == "__main__":
    main()