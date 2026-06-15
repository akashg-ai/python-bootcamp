print(">>>> WELCOME TO ROLLER COSTER <<<<")
h=int(input("Enter your height in cm:"))
bil=0
if h>=125:
    print("you can enjoy your ride")
    age=int(input("enter your age:"))
    if age<=12:
        bil+=5
    elif age<=18:
        bil+=7
    else:
        bil+=10
    wp=input("enter if you whant photo enter y and n for yes and no")
    if wp=="y":
        bil+=10
    print(f"your total bil is :{bil}")
else:
    print("you can't ride!")
    
print
