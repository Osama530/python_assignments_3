Q1:
num_1 = float(input("Enter 1st number "))
fun = str(input("enter function to be perform i.e(+,-,*,/,^) :"))
num_2 = float(input("Enter 2nd number"))
result = 0
if fun == '+' :
    result = num_1+num_2
elif fun == '-' :
    result = num_1-num_2
elif fun == '*' :
    result = num_1*num_2
elif fun == '/' :
    result = num_1/num_2
elif fun == '^' :
    result = num_1**num_2
print(f'{num_1} {fun} {num_2} = {result}')

# Q2:
A = ["aasas","e","f","f","2"]
num = []

for i in A:
    if i.isnumeric() :
        num.append(i)

print("the numeric values are :",num)

# Q3:
my_dic = {
    "color" : "red",
    "book" : "pthysics",
    "auther" : "griffith"
}
print(my_dic["color"])
my_dic["volume"] = "2nd"
print(my_dic)

# Q4:
num_dic = {
    "color" : "87",
    "book" : "3",
    "auther" : "griffith"
}
sum = 0
for key, value in num_dic.items() :
    if value.isnumeric() :
        sum = sum + int(value)
print(sum)

# Q5:
data = [4,8,9,4,8,3,7,6]
dup = []
for values in data :
    if values not in dup :
        dup.append(values)
print(dup)

