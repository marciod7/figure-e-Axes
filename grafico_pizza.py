import matplotlib.pyplot as plt
print('gráfico de pizza')
regions = ['New England', 'Mid-Atlantic', 'Midwest']
sales = [882703, 532648, 714406]

plt.pie(sales, labels=regions, autopct='%1.1f%%')
plt.title('Sales per region')
plt.show()
