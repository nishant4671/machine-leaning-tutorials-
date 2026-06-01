# Matplotlib Common Patterns 💡

### 1. The "Object-Oriented" Way
The preferred way for complex layouts.
```python
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.plot([1, 2, 3], [10, 20, 30])
ax.set_title('Professional Plot')
plt.show()
```

### 2. Multi-plot Layouts
Comparing different views of data.
```python
import matplotlib.pyplot as plt
plt.subplot(1, 2, 1) # 1 row, 2 cols, index 1
plt.plot(x, y)
plt.subplot(1, 2, 2) # index 2
plt.scatter(x, y)
```

### 3. Customizing Styles
Making it look modern.
```python
import matplotlib.pyplot as plt
plt.style.use('ggplot')
plt.plot([1, 2, 3], [4, 5, 6], color='skyblue', linewidth=2)
```
