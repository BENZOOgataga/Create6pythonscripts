import os
import pandas as pd
from fuzzywuzzy import process
import re
import argparse

# === ARGUMENT PARSING ===
parser = argparse.ArgumentParser(description="Check mod compatibility with Create 6")
parser.add_argument("mods_folder", type=str, help="Path to the mods folder")
parser.add_argument("--show-incompatible", action="store_true", help="Show incompatible mods")
parser.add_argument("--show-compatible", action="store_true", help="Show compatible mods")
parser.add_argument("--show-no-matches", action="store_true", help="Show mods with no match found")
parser.add_argument("--excel-file", type=str, default="c6.xlsx", help="Excel file with mod names and compatibility")
parser.add_argument("--fuzzy-threshold", type=int, default=85, help="Fuzzy match threshold (default: 85)")

args = parser.parse_args()

# === CONFIG ===
MODS_FOLDER = args.mods_folder  # Folder with mods
EXCEL_FILE = args.excel_file   # Excel file containing mod compatibility info
FUZZY_MATCH_THRESHOLD = args.fuzzy_threshold  # Fuzzy match threshold for the score

# === DISPLAY OPTIONS ===
SHOW_INCOMPATIBLE = args.show_incompatible
SHOW_COMPATIBLE = args.show_compatible
SHOW_NO_MATCHES = args.show_no_matches

# === LOAD MODS ===
mod_files = [f for f in os.listdir(MODS_FOLDER) if f.endswith(".jar")]

# === LOAD EXCEL ===
df = pd.read_excel(EXCEL_FILE)

# Clean Excel entries
df["Addon name"] = df["Addon name"].astype(str).str.lower().str.strip()
df["Does it work?"] = df["Does it work?"].astype(str).str.lower().str.strip()

compatible_mods = {
    name: compat
    for name, compat in zip(df["Addon name"], df["Does it work?"])
}

# === CLEANING FUNCTION ===
def clean_mod_name(name):
    name = name.lower().replace(".jar", "")
    name = re.sub(r"(^|[\W_])create([\W_]|$)", " ", name)  # Remove standalone 'create'
    name = re.sub(r"[^a-z0-9]+", " ", name)  # Keep alphanumeric
    return name.strip()

# === CHECK MODS ===
print("Checking mod compatibility...\n")

for mod_file in mod_files:
    raw_name = mod_file.lower().replace(".jar", "").strip()
    cleaned_name = clean_mod_name(raw_name)
    
    best_match, score = process.extractOne(cleaned_name, compatible_mods.keys())

    if score >= FUZZY_MATCH_THRESHOLD:
        compat = compatible_mods[best_match]
        if compat in ["yes", "true", "1"]:
            if SHOW_COMPATIBLE:
                print(f"✅ Compatible: {mod_file} (matched: {best_match}, score: {score})")
        else:
            if SHOW_INCOMPATIBLE:
                print(f"❌ Not compatible: {mod_file} (matched: {best_match}, score: {score})")
    else:
        if SHOW_NO_MATCHES:
            print(f"⚠️ No match found: {mod_file} (score: {score})")

print("\n✅ Done.")
