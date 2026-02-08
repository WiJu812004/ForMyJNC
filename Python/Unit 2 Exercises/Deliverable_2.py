from math import cos, pi, sin
import matplotlib.pyplot as plt

R = 1.0
L = 0.120
C = 1e-6

f = 1000
I_peak_to_peak = 0.001
I_final_peak = I_peak_to_peak / 2
omega = 2 * pi * f

num_cycles = 10
T = 1 / f
num_points = 1000
end_time = num_cycles * T
t = [i * end_time / num_points for i in range(num_points + 1)]

i_t = [I_final_peak * cos(omega * ti) for ti in t]

vR = [R * i for i in i_t]
vL = [L * (-omega * I_final_peak * sin(omega * ti)) for ti in t]
vC = [(1/C) * (I_final_peak / omega) * sin(omega * ti) for ti in t] 

plt.figure(figsize=(10, 6))
plt.plot(t, vR, label="Resistor")
plt.plot(t, vL, label="Inductor")
plt.plot(t, vC, label="Capacitor")
plt.legend()
plt.grid(True)
plt.show()