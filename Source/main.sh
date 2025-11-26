#!/bin/bash
set -e

src="index.html"
dest="../index.html"

# Force overwrite using mv -f
mv -f "$src" "$dest"

