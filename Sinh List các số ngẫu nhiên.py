import random
list=[]
list.append(random.randrange(50, 1001))
print("Số ngẫu nhiên của list: "+ str(list))
n = random.randint(-100,100)
m = random.randint(-100,100)
list1 = []
list2 = []
if n < 0:
    print("Vui lòng nhập số nguyên dương để chạy list1")
elif n == 0:
    print("List rỗng "+ str(list1))
elif n > 0:
    for i in range(n):
        list1.append(random.randrange(-1000,1001))
    print("list1 có "+str(n)+" giá trị và "+"tập hợp các phần tử của list1: "+str(list1))
if m < 0:
    print("Vui lòng nhập số nguyên dương để chạy list2")
elif m == 0:
    print("List rỗng "+ str(list2))
elif m > 0:
    for i in range(m):
        list2.append(random.uniform(-1000, 1001))
    print("list2 có "+str(m)+" giá trị và "+"Tập hợp các phần tử của list2: "+str(list2))