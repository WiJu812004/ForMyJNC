from math import cos, pi, sin
import matplotlib.pyplot as plt

R = 1.0
L = 0.120
C = 1e-6

I_peak_to_peak = 0.001
I_final_peak = I_peak_to_peak / 2

freq_start = 100
freq_end = 10000
freq_step = 100
frequencies = list(range(freq_start, freq_end + freq_step, freq_step))
V_peak_to_peak_list = []  

num_points = 1000

for f in frequencies:
    omega = 2 * pi * f
    T = 1 / f
    t = [i * T / num_points for i in range(num_points + 1)]

    vR = [R * I_final_peak * cos(omega * ti) for ti in t]
    vL = [-L * omega * I_final_peak * sin(omega * ti) for ti in t]
    vC = [(I_final_peak / (C * omega)) * sin(omega * ti) for ti in t]

    # Total voltage
    v_total = [vR[i] + vL[i] + vC[i] for i in range(len(t))]

    # Peak-to-peak voltage
    V_peak_to_peak = max(v_total) - min(v_total)
    V_peak_to_peak_list.append(V_peak_to_peak)

plt.figure(figsize=(10, 6))
plt.plot(frequencies, V_peak_to_peak_list)
plt.grid(True)
plt.show()

# Based on the graph, Vpp is max near the resonant freq of the circuit. At high freq, inductor impedance dominates while at low freq, capactior impedance dominates; hence V decreases.