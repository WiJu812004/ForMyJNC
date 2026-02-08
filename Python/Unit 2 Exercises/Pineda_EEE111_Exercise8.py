def octals(n):
    if n == 1:
        return [str(a) for a in range(8)]
    previous_num = octals(n - 1)
    octals_list = []
    for digit in range(8):
        for num in previous_num:
            octals_list.append(str(digit) + num)
    return octals_list
print(octals(3))

print("-----------------------")

def pascals(n):
    if n == 1:
        return [1]
    previous_num = pascals(n - 1)
    new_line = [1]
    for b in range(len(previous_num) - 1):
        new_line.append(previous_num[b] + previous_num[b + 1])
    new_line.append(1)
    return new_line
print(pascals(2))