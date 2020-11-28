import random
import string
name = random.choice(string.ascii_letters)
m = random.randint(0,200)
n = random.randint(0,200)
for i in range(n):
    name += random.choice(string.ascii_letters)
dic={'name':name,'age':m}
print("Số kí tự của name :",n)
print(dic)
