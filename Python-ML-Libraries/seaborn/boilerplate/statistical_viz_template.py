import seaborn as sns
import matplotlib.pyplot as plt

# 1. Load a built-in dataset
tips = sns.load_dataset("tips")

# 2. Set style
sns.set_theme(style="whitegrid")

# 3. Create a complex plot easily
# Scatter plot with regression line, separated by 'time' of day
sns.lmplot(data=tips, x="total_bill", y="tip", hue="smoker", col="time")

# 4. Final touches
plt.suptitle("Tips Analysis", y=1.05)
print("Seaborn plot rendered!")
plt.show()
