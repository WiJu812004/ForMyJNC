d1 = {111: "Introduction to Programming and Computation", 113: "Introduction to EEE Systems", 118: "EEE Laboratory 1"}

d1[111] = "Programming 1"
d1[121] = "Data Structures and Algorithms"

for k, v in d1.items():
	print('k =', k, 'v =', v)
print()

d2 = {"R"+str(i):i*1000 for i in range(1, 6)}
print(d2)
del d2["R2"]
print('del d2["R2"]:', d2)
p = d2.pop("R4")
print('d2.pop("R4"):', d2, "\np =", p)
