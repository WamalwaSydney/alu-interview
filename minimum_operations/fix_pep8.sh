#!/bin/bash

# Check if 0-minoperations.py exists
if [ ! -f "0-minoperations.py" ]; then
    echo "Error: 0-minoperations.py file not found."
    exit 1
fi

# Fix line too long errors in the file
sed -i 's/    Calculates the fewest number of operations needed to result in exactly$/    Calculates the fewest number of operations needed to result in/' 0-minoperations.py
sed -i 's/    n '\''H'\'' characters in the file.$/    exactly n '\''H'\'' characters in the file./' 0-minoperations.py

# Fix second long line error (docstring return line)
sed -i 's/        int: The minimum number of operations, or 0 if n is impossible to achieve$/        int: The minimum number of operations, or 0 if n is impossible/' 0-minoperations.py
sed -i '/        int: The minimum number of operations, or 0 if n is impossible/ a\\        to achieve' 0-minoperations.py

# Make the script executable
chmod +x 0-minoperations.py

echo "PEP 8 style errors fixed in 0-minoperations.py"
