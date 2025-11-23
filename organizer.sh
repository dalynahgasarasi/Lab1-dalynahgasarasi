#!/bin/bash

mkdir -p archive

shopt -s nullglob   
for file in *.csv; do
    [ -f "$file" ] || continue

   
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

    
    cp "$file" "archive/$new_name"

    echo "Archived $file → archive/$new_name"
done
