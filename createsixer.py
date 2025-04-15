import os
import pandas as pd
from fuzzywuzzy import process
import re

# === CONFIG ===
MODS_FOLDER = r"C:\Users\mrdar.DESKTOP-B6LKOPF\curseforge\minecraft\Instances\test create 6\mods"
EXCEL_FILE = "c6.xlsx"
MOD_COLUMN_NAME = "Addon name"
COMPAT_COLUMN_NAME = "Does it work?"
FUZZY_MATCH_THRESHOLD = 75  # Adjust for stricter/looser matching

# === DISPLAY OPTIONS ===
SHOW_INCOMPATIBLE = True
SHOW_NO_MATCHES = True
SHOW_COMPATIBLE = False

# === LOAD MODS ===
mod_files = [f for f in os.listdir(MODS_FOLDER) if f.endswith(".jar")]

# === LOAD EXCEL ===
df = pd.read_excel(EXCEL_FILE)

# Clean Excel entries
df[MOD_COLUMN_NAME] = df[MOD_COLUMN_NAME].astype(str).str.lower().str.strip()
df[COMPAT_COLUMN_NAME] = df[COMPAT_COLUMN_NAME].astype(str).str.lower().str.strip()

compatible_mods = {
    name: compat
    for name, compat in zip(df[MOD_COLUMN_NAME], df[COMPAT_COLUMN_NAME])
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
