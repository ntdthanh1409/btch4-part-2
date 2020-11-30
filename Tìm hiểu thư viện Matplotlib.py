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
#box plot

    