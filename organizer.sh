#!/bin/bash

mkdir -p archive

shopt -s nullglob   # ensures *.csv expands to nothing if no match
for file in *.csv; do
    # Skip if file doesn't exist
    [ -f "$file" ] || continue

    # --- Step 3a: Generate timestamp ---
    base=$(basename "$file")
    timestamp=$(date +"%Y-%m-%d_%H-%M-%S")
    name_without_ext="${base%.csv}"
    new_name="${name_without_ext}-${timestamp}.csv"

    echo "----------------------------------------" >> organizer.log
    echo "Archived File: $base" >> organizer.log
    echo "New Name: $new_name" >> organizer.log
    echo "Timestamp: $timestamp" >> organizer.log
    echo "File Content:" >> organizer.log
    cat "$file" >> organizer.log
    echo "----------------------------------------" >> organizer.log
    echo "" >> organizer.log

    # --- Step 3c: Move the file into archive ---
    cp "$file" "archive/$new_name"

    echo "Archived $file → archive/$new_name"
done
