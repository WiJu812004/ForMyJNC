from math import cos, pi
import matplotlib.pyplot as plt

def cos_wave(time, frequency):
    return [cos(2 * pi * frequency * t) for t in time]

starting_time = 0.0
ending_time = 0.010
num_points = 1000
time_step = (ending_time - starting_time) / num_points

t = [starting_time + i * time_step for i in range(num_points)]
frequency = 1000
y = cos_wave(t, frequency)

plt.plot(t, y)
plt.show()