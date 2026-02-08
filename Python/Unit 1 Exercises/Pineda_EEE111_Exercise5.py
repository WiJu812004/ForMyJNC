def anagram_check(str_in1, str_in2):
    str_in1 = str_in1.lower()
    str_in2 = str_in2.lower()
    list1 = list(str_in1.replace(" ", ""))
    list2 = list(str_in2.replace(" ", ""))
    if len(list1) != len(list2):
        return False
    list1.sort()
    list2.sort()
    return list1 == list2

print(anagram_check("peaches", "cheaps"))
print(anagram_check("Dormitory", "Dirty Room"))
print()

def digit_sum(number):
    number = abs(number)
    return sum(int(digit) for digit in str(number))

print(digit_sum(123456789))
print(digit_sum(111222333444555))