#!/bin/bash
# Read from the file words.txt and output the word frequency list to stdout.
# Problem 192: Word Frequency
# 
# For simplicity sake, you may assume:
# - words.txt contains only lowercase characters and space ' ' characters.
# - Each word must consist of lowercase characters only.
# - Words are separated by one or more whitespace characters.

# Check if file argument is provided
if [ $# -eq 0 ]; then
    # If no argument provided, use words.txt as default
    input_file="words.txt"
elif [ $# -eq 1 ]; then
    input_file="$1"
else
    echo "Usage: $0 [filename]"
    echo "If no filename provided, will use words.txt"
    exit 1
fi

# Check if the input file exists
if [ ! -f "$input_file" ]; then
    echo "Error: File '$input_file' not found."
    exit 1
fi

# Solution: Read words, count frequency, and sort by frequency (descending) then by word (ascending)
# Method 1: Using tr, sort, uniq, and awk
cat "$input_file" | tr -s ' ' '\n' | sort | uniq -c | sort -rn | awk '{print $2, $1}'

# Alternative Method 2: Using awk only (more efficient)
# awk '{
#     for (i = 1; i <= NF; i++) {
#         if ($i != "") {
#             freq[$i]++
#         }
#     }
# } 
# END {
#     for (word in freq) {
#         print word, freq[word]
#     }
# }' "$input_file" | sort -k2,2nr -k1,1