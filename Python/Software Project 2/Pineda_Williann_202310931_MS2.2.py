from math import sqrt #gets access to sqrt that is used in this code

pts, bits = map(int, input().split()) #reads the first line of input, splits it into two, converts it to integer, and designates them in variables pts, bits respectively

times = [] #creates an empty list that will store time values for each point
voltages = [] #creates an empty list that will store voltage values for each point
rms_values = [] #creates an empty list that will store calculated RMS value for each bit segment

for a in range(pts): #starts a loop that will iterate pts times
    t, v = map(float, input().split()) #reads a line of input (which has two values: time and voltage), splits it into a list of two integers, converts them into floats, and places them in variables t and v respectively
    times.append(t) #adds t to times list
    voltages.append(v) #adds v to voltages list

pts_per_bit = pts / bits #solves for the ideal number of samples that corresponds to a single bit duration

for b in range(bits): #starts another loop that will iterate bits times
    start = int(round(b * pts_per_bit)) #calculates the starting index for the current bit signal segment, rounded, then converted to int
    end = int(round((b + 1) * pts_per_bit)) #calculates the ending index — the only difference from the code above is that it's b + 1, not b

    if end > pts: #starts an if-else statement
        end = pts #makes sure that end doesn't exceed len(voltages)

    segment = voltages[start:end] #extracts the voltage data segment corresponding to current bit

    sum_of_squares = 0.0 #initializes sum of squares to be equal to 0
    for v in segment: #starts yet another loop that will go through each value in the segment
        sum_of_squares += v * v #squares input in v and adds it to sum_of_squares
    rms = sqrt(sum_of_squares / len(segment)) #calculates the root mean square value for the segment, and designates it as variable rms

    rms_values.append(rms) #adds the rms value to rms_values list

minimum_rms = min(rms_values) #finds the smallest rms value in the list rms_values and designates it as minimum_rms
maximum_rms = max(rms_values) #finds the largest rms value in the list rms_values and designates it as maximum_rms
threshold = (minimum_rms + maximum_rms) / 2 #creates a threshold for making the decision by calculating the midway value of the min and max rms

bit_string = "" #initializes an empty string to store the recovered binary data

for rms in rms_values: #creates one last loop that will iterate through all values in list rms_values
    if rms < threshold: #if rms value lower than threshold
        bit_string += "0" #adds 0 to bit string list
    else: #if rms value higher than threshold
        bit_string += "1" #adds 1 to bit string list

print(bit_string) #prints the recovered binary string