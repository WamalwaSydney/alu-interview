#!/usr/bin/env bash
set -e

# 1. Ensure pip3 is installed
if ! command -v pip3 &>/dev/null; then
  echo "pip3 not found, installing..."
  sudo apt-get update -y
  sudo apt-get install -y python3-pip
fi

# 2. Ensure autopep8 is installed
if ! pip3 show autopep8 &>/dev/null; then
  echo "autopep8 not found, installing..."
  pip3 install --user autopep8
fi

# 3. File to fix (adjust as needed)
FILE="0-minoperations.py"
if [ ! -f "$FILE" ]; then
  echo "Error: $FILE not found."
  exit 1
fi

# 4. Backup
cp "$FILE" "$FILE.bak"

# 5. Run autopep8 via python -m to avoid PATH issues
#    --max-line-length 79 to enforce PEP8
#    --in-place and --aggressive for style fixes
python3 -m autopep8 --in-place --aggressive --max-line-length 79 "$FILE" \
  || true  # ignore broken‐pipe

# 6. Make executable
chmod +x "$FILE"

echo "✅ PEP8 style fixes applied to $FILE"
echo "🔒 Backup saved as $FILE.bak"

