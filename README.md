# Lua File Search and Replace Script

This script allows you to search for a specific word in all `.lua` files within a folder, replace it with another word, and optionally restore changes from a backup file.

## Prerequisites

- Python 3.x installed.
- The folder containing `.lua` files must be accessible.

## How to Use

### Step 1: Locate the Mods Folder Root

Before using the script, ensure you know the path to the "mods" folder (or the root folder containing your `.lua` files). This folder is the root directory where the script will search for `.lua` files.

If you're working with a specific game or mod, navigate to the folder where your mods are stored and locate the root folder containing the `.lua` files you want to search and modify.

### Step 2: Choose Mode

When running the script, you'll be prompted to choose one of two modes:

- **Replace Mode**: This mode will search for a specific word in the `.lua` files and replace it with a new word.
- **Restore Mode**: This mode will restore changes from a previously saved backup file.

### Step 3: Run the Script

To run the script, execute the following command in your terminal or command prompt:

```bash
python find_replace_or_backup_.py
