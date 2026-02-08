d1 = {111: "Introduction to Programming and Computation", 113: "Introduction to EEE Systems", 118: "EEE Laboratory 1"}
d2 = {"R1": 1000, "R2": 470, "R3": 5600}

print('d1[111] =', d1[111])
print('d2["R2"] =', d2["R2"])
print()

k = list(d1.keys())
print('d1.keys():', k)
print('k[1] =', k[1])
v = list(d2.values())
print('d2.values():', v)
print('v[1] =', v[1])
print()

k[1] = "Herp"
v[1] = "Derp"
print(d1)
print(d2)
