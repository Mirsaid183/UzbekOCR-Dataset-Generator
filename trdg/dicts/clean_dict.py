import os

# 1. Fayllar manzili
INPUT_FILE = "uz.txt"       # Hozirgi kir fayl
OUTPUT_FILE = "uz_clean.txt" # Yangi toza fayl

# 2. Biz ruxsat bergan "HALOL" belgilar
# O'zbek alifbosi + tinish belgilari + raqamlar
ALLOWED_CHARS = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ‘'’ʻ-_?!.,() "

def is_word_clean(word):
    for char in word:
        if char not in ALLOWED_CHARS:
            return False # Agar begona harf bo'lsa, o'tkazmaymiz
    return True

def clean_dictionary():
    print("🧹 Lug'at tozalanmoqda...")
    
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()

    clean_lines = []
    dirty_count = 0

    for line in lines:
        word = line.strip()
        # So'z bo'sh emasligini va ichida yomon harf yo'qligini tekshiramiz
        if word and is_word_clean(word):
            clean_lines.append(line)
        else:
            dirty_count += 1

    # Yangi faylga yozamiz
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.writelines(clean_lines)

    print("-" * 30)
    print(f"Jami so'zlar: {len(lines)}")
    print(f"❌ O'chirildi (yomon harflar): {dirty_count}")
    print(f"✅ Qoldi (toza so'zlar): {len(clean_lines)}")
    print(f"Yangi fayl: {OUTPUT_FILE}")

    # Eskisini o'chirib, yangisini o'rniga qo'yamiz (ixtiyoriy)
    # os.remove(INPUT_FILE)
    # os.rename(OUTPUT_FILE, INPUT_FILE)

if __name__ == "__main__":
    clean_dictionary()