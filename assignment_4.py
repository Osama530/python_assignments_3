#Q:1
person = {
    "first_name" : "Junaid",
    "last_name" : "Akram",
    "age" : 30,
    "city" : "larachi"
}
#print each
print(person["first_name"])
print(person["last_name"])
print(person["age"])
print(person["city"])

#add new key value
person["qualifiication"]="bachlors"
print(person)

#update key value
person["qualifiication"]="masters"
print(person)

#delete key value
del person["qualifiication"]
print(person)

#Q:2
cities = {
    "islamabad": {
        "countary" : "pakistan",
        "population" : 550000,
        "fact" : "beautiful",
    },
    "lahore": {
        "countary" : "pakistan",
        "population" : 1550000,
        "fact" : "reach",
    },
     "karachi":{
        "countary" : "pakistan",
        "population" : 1770000,
        "fact" : "fast",
    },
}
print(cities["karachi"])
print(cities["lahore"])
print(cities["islamabad"])

# Q3:
temp = 0
while temp < 1 or temp > 100 :
    age = int(input("Enter your age : "))
    if age > 0 and age <=3 :
        print("you are free ")
    elif age > 3 and age <= 12 :
        print("please pay 10$ ")
    elif age > 12 and age <= 99 :
        print("please pay 15$ ")
    else:
        print("invalid input")
    temp = age

# Q3:
def favorite_book (title):
    print("one of my favorite book is ",title)

title = "alice in wonder land"
favorite_book(title)


from random import randint
temp = 0
answer = randint(1,100)
print(answer)
while temp!=3 :
    guess = int(input("gess a number between 0 and 100 : "))
    if guess < answer :
        print("your guess in smaller then number ")
    elif guess==answer:
        print("****you win***** ")
    else:
        print("your guess in larger then number ")
    temp +=1