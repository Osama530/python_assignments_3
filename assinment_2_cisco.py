# Q1:
sub_1 = int(input("Enter marks obtain in english out of 100 :"))
sub_2 = int(input("Enter marks obtain in Maths out of 100 :"))
sub_3 = int(input("Enter marks obtain in Urdu out of 100 :"))
sub_4 = int(input("Enter marks obtain in islamiat out of 100 :"))
sub_5 = int(input("Enter marks obtain in history out of 100 :"))
grad= '0'
total_obtain = sub_1+sub_2+sub_3+sub_4+sub_5
g_total = 500
percentage = (total_obtain/g_total)*100

if percentage>=80 and percentage<=100:
    grad = 'A'
elif percentage>=60 and percentage<=80:
    grad = 'B'
elif percentage>=40 and percentage<=60:
    grad = 'C'
else :
    grad ='F'
print("==========================Mark Sheet==============================")
print(f'subjects\t\tobtain\ttotal')
print(f'English\t\t\t\t{sub_1}\t{100}')
print(f'Maths\t\t\t\t{sub_2}\t{100}')
print(f'Urdu\t\t\t\t{sub_3}\t{100}')
print(f'Islamiat\t\t\t{sub_4}\t{100}')
print(f'History\t\t\t\t{sub_5}\t{100}')
print("==================================================================")
print(f'Remarks\t\tmarks ={total_obtain}/{g_total}\tgrade = {grad}')
print("==================================================================")

# Q2:
number = int(input("Enter marks obtain in history out of 100 :"))

if number % 2 == 0:
    print("the number entered is even")
else :
    print("the number entered is odd")

# Q3:
array = [4,8,8,7,6,4,3,2,9,4]
print("the length list is :",len(array))

# Q4:
print("the sum of items in a list is :",sum(array))

# Q5:
num = 0
for i in range(0,len(array)):
    if num<array[i]:
        num=array[i]
print("the largest number in a list is",num)

# Q6:
a = [1,1,2,3,5,8,13,21,34,55,89]
num = 5
for i in range(0,len(a)):
    if a[i]<num:
        print("the number in a list less then 5",a[i])