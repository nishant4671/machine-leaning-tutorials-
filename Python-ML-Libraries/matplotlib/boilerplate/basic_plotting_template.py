import matplotlib.pyplot as plt
import numpy as np

# 1. Prepare data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# 2. Create plot
plt.figure(figsize=(8, 4))
plt.plot(x, y, label='Sine Wave', color='teal', linestyle='--')

# 3. Add labels and style
plt.title('My First Plot')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True, alpha=0.3)
plt.legend()

# 4. Save and Show
# plt.savefig('plot.png')
print("Plot generated successfully!")
plt.show()
