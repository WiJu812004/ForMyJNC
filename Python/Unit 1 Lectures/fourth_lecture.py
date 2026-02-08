def pal_check(str_in):
    for i in range(len(str_in)//2):
        if str_in[1] != str_in[-(i+1)]:
        #print "not a palindrome"
            return False
    return True

def pal_check2(str_in):
    str_in = str_in.lower()
    str_in = str_in.replace(" ", "")
    return str_in == str_in[::-1]

in_str = "not a palindrome"
print(in_str, pal_check(in_str))
print("Racecar", pal_check2("Racecar"))

s = "Python"
#s[4] = 'a' error
s = s[:4] + 'a' + s[:5]
print(s)