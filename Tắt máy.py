import os
check = input("Want to shutdown your computer ? (y/n): ")
if check == 'n' or check == "N":
    print("Không muốn tắt máy")
else:
    os.system("shutdown /s /t 5")