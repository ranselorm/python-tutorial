from matplotlib import pyplot as plt
import emoji

x = [i for i in range(0, 11)]
y = [y ** 2 for y in x]


print(x)
print(y)

# Exercise: Create a line plot of the data
plt.plot(x, y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()

# Exercise: Create a scatter plot of the same data
plt.scatter(x, y, color='red')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot of y = x^2')
plt.show()

# Exercise: Create a bar chart of the same data
plt.bar(x, y, color='green')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')            
plt.title('Bar Chart of y = x^2')
plt.show()

# Exercise: Print emojis
print(emoji.emojize("Python is fun :red_heart:", variant="emoji_type"))