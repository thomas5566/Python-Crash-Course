from die import Die
import pygal

# Create a D6
die = Die(48)

# Make some rolls, and store results in a list
results = []
for roll_num in range(500000):
    result = die.roll()
    results.append(result)

# Analyze the results
frequencies = []
for value in range(1, die.num_sides + 1):
    frequency = results.count(value) # count how many times each number appears in results
    frequencies.append(frequency)

# Visualize the results
hist = pygal.Bar()

hist._title = "Results of rolling one D6 1000 times"
hist.x_labels = [str(x) for x in range(1, die.num_sides + 1)]

# for i in range(1, die.num_sides + 1):
#     hist.x_labels.append(i)

hist._x_title = "Result"
hist._y_title = "Frequency of Result"

hist.add('D6', frequencies)
hist.render_to_file('lutter_visual.svg')