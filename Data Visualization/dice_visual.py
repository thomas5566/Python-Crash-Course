import pygal
from die import Die

# Create two D6 dice
die_1 = Die()
die_2 = Die()

# Make some rolls, and store results in a list
# results = []
# for roll_num in range(1000):
#     result = die_1.roll() + die_2.roll()
#     results.append(result)
results = [die_1.roll() + die_2.roll() for roll_num in range(1000)]

# Analyze the results
max_result = die_1.num_sides + die_2.num_sides
frequencies = [results.count(value) for value in range(2, max_result + 1)]

# for value in range(2, max_result + 1):
#     frequency = results.count(value) # count how many times each number appears in results
#     frequencies.append(frequency)

# Visualize the results
hist = pygal.Bar()

hist._title = "Results of rolling two D6 dice 1000 times"
# hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
hist.x_labels = [str(x) for x in range(2, max_result + 1)]
hist._x_title = "Result"
hist._y_title = "Frequency of Result"

hist.add('D6 + D6', frequencies)
hist.render_to_file('two_die_visual.svg')