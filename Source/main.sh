#!/bin/bash
set -e

src="index.html"
dest="../index.html"

# 1. Run Python script to generate the new index.html
echo "Running SpaceMasterMap.py to generate a fresh index.html..."
python3 SpaceMasterMap.py

# Function to print timestamp of a file if it exists
print_timestamp() {
    if [[ -f "$1" ]]; then
        echo "Timestamp for $1:"
        stat -c "  Modified: %y" "$1"
    else
        echo "$1 does not exist."
    fi
}

echo "Checking timestamps:"

print_timestamp "$src"
print_timestamp "$dest"
# 3. Compare modification times
if [[ -f "$dest" ]]; then
    if [[ "$src" -nt "$dest" ]]; then
        echo "New index.html is newer than the old one. Proceeding..."
    else
        echo "WARNING: New index.html is NOT newer than the one in the parent directory."
        echo "Aborting move to avoid overwriting with an older file."
        exit 1
    fi
else
    echo "No index.html in parent directory. Proceeding with move..."
fi


echo ""
echo "Moving $src → $dest (overwriting if exists)..."
mv -f "$src" "$dest"

echo "Done."

echo ""
echo "New timestamp of replaced file:"
print_timestamp "$dest"

