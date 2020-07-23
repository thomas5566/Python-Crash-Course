from die import Die
import pygal

# Create a D6
die = Die()

# Make some rolls, and store results in a list
# results = []
# for roll_num in range(1000):
#     result = die.roll()
#     results.append(result)
results = [die.roll() for roll_num in range(1000)]

# Analyze the results
# frequencies = []
# for value in range(1, die.num_sides + 1):
#     frequency = results.count(value) # count how many times each number appears in results
#     frequencies.append(frequency)
frequencies = [results.count(value) for value in range(1, die.num_sides + 1)]

# Visualize the results
hist = pygal.Bar()

hist._title = "Results of rolling one D6 1000 times"
# hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_labels = [str(x) for x in range(1, die.num_sides + 1)]
hist._x_title = "Result"
hist._y_title = "Frequency of Result"

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')