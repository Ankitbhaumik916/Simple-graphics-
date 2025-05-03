import matplotlib.pyplot as plt
import numpy as np

plt.style.use('dark_background')
theta = np.linspace(0, 2 * np.pi, 100)
r = np.abs(np.sin(5 * theta))  # Star-shaped curve

x = r * np.cos(theta)
y = r * np.sin(theta)

plt.plot(x, y, color='cyan', linewidth=2)
plt.fill(x, y, alpha=0.3, color='magenta')
plt.axis('off')
plt.gca().set_aspect('equal')
plt.show()
