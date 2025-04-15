import os
import pandas as pd
from fuzzywuzzy import process

# === CONFIG ===
MODS_FOLDER = r"YOUR\MODS\FOLDER\PATH\HERE"  # You can copy paste it, it's fine
EXCEL_FILE = "c6.xlsx"
MOD_COLUMN_NAME = "Addon name"
COMPAT_COLUMN_NAME = "Does it work?"
FUZZY_MATCH_THRESHOLD = 75  # You can adjust this value for stricter/looser matching

# === DISPLAY OPTIONS ===
SHOW_INCOMPATIBLE = True      # ❌ Show mods that are known to be incompatible
SHOW_NO_MATCHES = False       # ⚠️ Show mods with no match in the Excel
SHOW_COMPATIBLE = False       # ✅ Optionally show mods that are compatible

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

# === CHECK MODS ===
print("Checking mod compatibility...\n")

for mod_file in mod_files:
    mod_name = mod_file.lower().replace(".jar", "").strip()
    best_match, score = process.extractOne(mod_name, compatible_mods.keys())

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
