print("To count no of upper and Lower Case in a string")
def string_test(s):
    num={"UPPER_CASE":0, "LOWER_CASE":0}
    for a in s:
        if a.isupper():
           num["UPPER_CASE"]+=1
        elif a.islower():
           num["LOWER_CASE"]+=1
        else:
           pass
    print ("Original String : ", s)
    print ("No. of Upper case characters : ", num["UPPER_CASE"])
    print ("No. of Lower case Characters : ", num["LOWER_CASE"])

string_test('The quick Brown Fox')


print(" To check maximum of three numbers")
def max_of_three( x, y, z ):
    if x > y:
        return x
    return y
    if y>z:
        return y
    return z
print(max_of_three(4, 8, 3))

