import matplotlib.pyplot as plt

x = [1,2,3,4,5]
xl = ['Rare','Medium rare','Medium','Medium Well','Well']
y = [23,166,132,75,36]

plt.bar(x,y)
plt.xticks(x,xl)
plt.xlabel('How done')
plt.ylabel('People')
plt.title('How do you like your steak prepared?')
plt.show()