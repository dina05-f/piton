










    #num1=4
#num2=5
#print(num1<=num2)

#age=int(input("enter your age:"))
#a=age%10==0 or age>=50
#print(a)


#a=int(input("enter the number "))
#if a>0:
    #print("Positive")
#elif a==0:
   # print("Zero")
#else:
    #print("Negative")


person=(input("status of the person "))
if person=='student' or person=='school 10th' or person=='school 11th':
    Print(f'student more than 15years')
else:
    print(f'student less than 15years')


person=(input("status of the person "))
if person=='student' or person=='school 10th' or person=='school 11th':
    print(f'student more than 15years')
else:
    print(f'student less than 15years')


age = input("enter your age: ")

try:
    age=int(age)
except:
    print("error")

if type(age)!=int:
    print("not age. Enter your age correctly")

elif age < 18:
    print("ребенок")
elif age >= 18 and age < 35:
    print("взрослый")
elif age >= 35 and age < 65:
    print("старший")
else age >=65:
    print("пенсионер")




list1=[2,2,"Tom","Sam"]
If "Sasha" not in list1:
    print("yes")
else:
    print("no") 

name = 'today is rainy day'
if 'rainy' in name:
    print('yes')