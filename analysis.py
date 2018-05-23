import seaborn as sns
import matplotlib.pyplot as plt

file = open("data.txt" , "r")
str = ''.join(file.readlines())
list = str.split()
print(list)

for i in range(len(list)):
    list[i] = float(i)

print(sum(list)/len(list))
sns.distplot(list)
plt.show()

