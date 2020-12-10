  
import string , random , os
def randomstr(): 
    name = random.choice(string.ascii_letters)
    for i in range(999999):
        name += random.choice(string.ascii_letters)
    return name
path = input('Nhập đường dẫn nơi bạn muốn tạo thư mục')+'\\'
path = path + input('Tên thư mục bạn muốn tạo:')
os.mkdir(path)
os.chdir(path)  
size = float(input('Nhập dung lượng dữ liệu (1MB-1024MB): '))
size = size * 1024 * 1024 
n =int(size // 1024000) 
m =int(size - n * 1024000)  
for i in range(1,n):
    k = 'file'+str(i)+'.txt'
    k = open(k, mode= 'w')
    k.write(randomstr())
    k.close()
if m != 0:
    k = 'file'+ str(n + 1) +'.txt'
    k = open(k, mode= 'w')
    name = random.choice(string.ascii_letters)
    for i in range(m - 1):
        name += random.choice(string.ascii_letters)
        k.write(randomstr())
        k.close()
print('Đã tạo:', (n+1),'file!')
