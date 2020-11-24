import smtplib
import getpass
n=int(input("Số lần muốn gửi mail: "))
if n <= 0:
    print("Vui lòng nhập lại số lần muốn gửi mail")
else:
#Thông tin cơ bản
    email=input("Email của bạn là: ")
    password=getpass.getpass("Password:")
    addreas=input('Người nhận: ')
    msg=input("tin nhắn: ")
#Gửi mail
    client=smtplib.SMTP('smtp.gmail.com',587)
    client.starttls()
    try:
        for i in range(n):
            client.login(email,password)
            client.sendmail(email,addreas,msg)
            print('Đã gửi',n,' tin nhắn tới', address)
    except:
        print("Mật khẩu nhập sai vui lòng nhập lại")
    client.quit()
