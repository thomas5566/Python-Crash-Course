from matplotlib import  pyplot as plt

# Defint Data
x_value = [1, 2, 3, 4, 5]
cube = [1, 8, 27, 64, 125]

# Make plot
plt.scatter(x_value, cube, edgecolors='none', s=40)

# Customize plot
plt.title("Cubel", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel('Cube of value', fontsize=14)

# Show plot
plt.show()