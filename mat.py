import matplotlib.pyplot as plt

X = [ 16, 17, 18, 19, 20, 21, 22, 23, 24, 25 ]
y = [ 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0 ]

plt.plot( X, y, color='green', marker='o', linestyle='dashed', linewidth=2, markersize=12 )
plt.xlabel('X')
plt.ylabel('y')
plt.title('Line Plot')
plt.show()