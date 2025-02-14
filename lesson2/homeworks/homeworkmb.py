# numbers and integers
# task1
a=float(input())
print(f"{a:.2f}")
# task2 undone
a=float(input())
b=float(input())
c=float(input())
if a>b and a>c:
    print(a)
# task3
kilometer=3.23
meter=1000*kilometer
santimeter=100000*kilometer
print(meter , santimeter)
# task4
num1=int(input())
num2=int(input())
print(num1//num2, num1%num2)
# task5
celcius=float(input("enter celcius "))
farenheit=(celcius*9/5)+32
print("farenheit",farenheit)
# task6
number=int(input("Enter a number: "))
last_digit = number%10
print(last_digit)
# task7
number1=int(input())
boolen=not(bool(number1%2))
print(boolen)

# strings
# task1
name = input("What is your name? ")
dateofbirth = input("date of birth: ")
print("your age is:", 2025-int(dateofbirth))
# task2
txt="LMaasleitbtui"
print(txt[1:3]+txt[5]+txt[7]+txt[9]+txt[11])
# task3
str=input("enter a string")
print(len(str))
print(str.lower())
print(str.upper())
# task4
string="madam"
a=len(string)
bstr=string[a//2:a]

print(string[0:a//2+1]==bstr[::-1])
# task7
sentence="I love apples"
print(sentence.replace("apples","oranges",7))
# task8
string=input("enter a string: ")
print("the first character "+string[0],"the last character "+string[-1] )
# task9
string2=input("Enter a string: ")
print(string2[::-1])
# task10
string1=input("Enter a string: ")
print(len(string1))
# task11 undone
str1=input("Enter a string: ")
print(str1.isdigit())
# task12
astring=input("Enter a string: ")
bstring=input("Enter a string: ")
cstring=input("Enter a string: ")
print(bstring.join([astring,cstring]))
# task13
str1=input("Enter a string: ")
print(str1.replace(" ",""))
# task14
string1=input("Enter a string: ")
string2=input("Enter a string: ")
print(string1.__eq__(string2) )
# task15
string=input("Enter a string: ")
string.split()
print(string.rsplit())
# task16
string=input("Enter a string: ")
char=input("Enter a character: ")
print(string.replace(char,''))
# task17
string=input("Enter a string: ")
print(string.replace('a',"*").replace('u',"*").replace("e","").replace("i","").replace("o",""))

# task18
string="Python is fun!"
print(f" the text starts with this {string.split()[0]} and ends with {string.split()[-1]}")



# boolen

# task1
username=input("Enter your username: ")
password=input("Enter your password: ")
print(bool(username), bool(password))
# task2
a=12
b=15
print(f"these values are equal: {bool(a==b)}")
# task3
a=13
print(bool(a>0 and a%2==0))
# task4
num1=12
num2=13
num3=114
print(bool(num1!=num2 and num1!=num3 and num2!=num3))
# task5
string1="a"
string2="asdjfn"
print(bool(len(string1)==len(string2)))
# task6
num=15
print(bool(num%3==0 and num%5==0 ))
# task7
num1=12
num2=34
print(num1+num2>50.8)
print(10<=num1<=20)