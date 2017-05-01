import matplotlib.pyplot as plt

qpi = [3.75, 3.679, 3.553, 3.158, 3.0, 3.214, 3.5, 3.2, 3.75]
sem = [1, 2, 3, 4, 5, 6, 7, 8, 9]

plt.plot(sem, qpi)
plt.xlabel('Year-Semester')
plt.ylabel('QPI')
plt.title('Grades in AdNU')

plt.xticks([1, 2, 3, 4, 5, 6, 7, 8, 9],['1-1','1-2','2-1','2-2','3-1','3-2','3-3','4-1','4-2'])
plt.show()