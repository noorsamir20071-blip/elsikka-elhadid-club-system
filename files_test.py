file = open("names.txt", "w")

file.write("Yassin - Basketball\n")
file.write("Salah - Football\n")

file.close()

print("File created successfully! 🎉")


file = open("names.txt", "r")

content = file.read()
print("\n--- 📖 File Content ---")
print(content)

file.close()
with open("names.txt", "a") as file:
    file.write("Shikabala - Football\n")
    # بنضيف اسم جديد من غير ما نمسح القديم باستخدام "a"
with open("names.txt", "a") as file:
    file.write("Shikabala - Football\n")

# بنقرأ الملف سطر سطر بالـ Loop
print("\n--- 📖 Reading Line by Line ---")
with open("names.txt", "r") as file:
    for line in file:
        # strip() بتشيل الفواصل والسطور الفاضية الزيادة
        print(f"Player Data: {line.strip()}")