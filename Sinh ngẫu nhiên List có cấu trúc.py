import random
import string
n = random.randint(50,100) #số phần tử trong list
print('Số phần tử trong mỗi list hiện tại:',n)
list1 = []
for i in range(n):
    m = random.randint(1,15) #Tạo giá trị ngẫu nhiên cho name: (chữ cái đầu tiên in hoa)
    name = random.choice(string.ascii_uppercase) 
    for i in range(m):
        name += random.choice(string.ascii_lowercase)
    k = random.randint(0,200)  #Tạo giá trị ngẫu nhiên cho age
    dic = {'name' :name, 'age':k}
    list1.append(dic)  #thêm dictonary mới tạo vào list
print(list1)