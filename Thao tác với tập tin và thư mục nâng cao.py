import os
folders = input("Thư mục: ")
file=input("tên tệp:")+".txt"
folder =folders+"\\"+file
h = folder
k = open(file, mode = 'a')
k.write(input("Nội dung của văn bản bạn muốn nhập: "))
k.close()
os.rename(file,h)