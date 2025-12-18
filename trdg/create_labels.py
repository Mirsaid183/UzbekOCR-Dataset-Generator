import os

#Rasimlar turgan joy
IMAGE_DIR = "dataset/images/"
#Label fayl turadigan joy
LABEL_FILE = "dataset/labels.txt"

def create_labels():
    if not os.path.exists(IMAGE_DIR):
        print(f"XATOLIK: '{IMAGE_DIR}' papkasi topilmadi!")
        return
    
    print(f"'{IMAGE_DIR}' papkasidan rasmlar o'qilmoqda...")
    
    files = os.listdir(IMAGE_DIR)
    #Faqat rasm fayllarini olish
    images = [f for f in files if f.endswith('.jpg') or f.endswith('.png')]
    
    if len(images) == 0:
        print("XATOLIK: Hech qanday rasm fayllari topilmadi!")
        return
    
    count = 0
    with open(LABEL_FILE, "w", encoding="utf-8") as f:
        for filename in images:
            try:
                # trdg fayl nomi formati: "Matn_tasodifiyRaqam.jpg"
                # Bizga "_" dan oldingi hamma narsa kerak.
                # rsplit('_', 1) - o'ng tomondan birinchi uchragan "_" dan qirqadi
                
                name_body = os.path.splitext(filename)[0] # .jpg ni olib tashlaymiz
                text = name_body.rsplit('_', 1)[0] # Raqamni olib tashlaymiz
                
                # Agar matnda xato bo'lsa yoki bo'sh bo'lsa tashlab ketamiz
                if text:
                    # Format: rasm_nomi.jpg  matn
                    f.write(f"{filename}\t{text}\n")
                    count += 1
            except Exception as e:
                print(f"Xato fayl: {filename} - {e}")

    print("------------------------------------------------")
    print(f"✅ TUGADI! Jami {count} ta rasm 'labels.txt' ga yozildi.")
    print(f"Fayl manzili: {LABEL_FILE}")

if __name__ == "__main__":
    create_labels()