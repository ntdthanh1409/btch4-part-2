from matplotlib import pyplot
import numpy as np
years = [2000,2002,2004,2005]
companyA = [1000,2000,300,4000]
companyB = [2000,4000,40,532]
#Biểu đồ Line
pyplot.title('Line Char')
pyplot.xlabel("years")
pyplot.ylabel("Doanh thu($)")
pyplot.plot(years, companyA, color="red", marker= ".", markersize=15)
pyplot.plot(years, companyB, color='blue', marker= ".",markersize=10)
pyplot.legend(["companyA","companyB"])
pyplot.show()

#Biểu đồ Bar
pyplot.title('Bar Chart')
pyplot.xlabel("years")
pyplot.ylabel("Doanh thu($)")
pyplot.bar(years, companyA, color="red")
pyplot.bar(years, companyB, color='blue')
pyplot.legend(["companyA","companyB"])
pyplot.show()
#column 
import matplotlib.pyplot as plt, numpy as np

bt, bt_std = (4, 7, 3, 5, 2), (3, 4, 5, 2, 3)
btvn, btvn_std = (1, 1, 9, 13, 7), (4, 6, 3, 4, 4)
ind = np.arange(len(bt))
width = 0.35
fig, ax = plt.subplots()
rects1 = ax.bar(ind - width/2, bt, width, yerr=bt_std,
                label='Bài tập ',color='#74b9ff')
rects2 = ax.bar(ind + width/2, btvn, width, yerr=btvn_std,
                label='BTVN',color='#d63031')
ax.set_xticks(ind)
ax.set_xticklabels(('Tháng 1', 'Tháng 2', 'Tháng 3', 'Tháng 4', 'Tháng 5'))
plt.title('''   Biểu đồ thể hiện so bai tap
   bài tập lập trình ''')
plt.xlabel("Thời gian trải qua")
plt.ylabel("Số bài tập ")
ax.legend()
plt.show()
#box plot
import matplotlib.pyplot as plt, numpy as np
x = np.random.randn(30) + np.arange(0, 30)*0.75 + 10
y = np.random.randn(10) + np.arange(0, 10)*1.0 +20
z = np.random.randn(10) + np.arange(0, 10)*0.5 + 5
t = np.random.randn(40) + np.arange(0, 40)*0.4 + 0.0

plt.boxplot([x, y, z, t],
            labels = ['Mùa Xuân', 'Mùa Hạ', 'Mùa Thu','Mùa Đông'],
            showfliers = True)

plt.title('''bieu do the hien su bien thien nhiet do''')
plt.xlabel('Mùa')
plt.ylabel('Chỉ số nhiệt độ ')
plt.show()

    
