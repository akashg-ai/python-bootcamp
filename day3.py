import random


sissors='''
    _______
---'   ____)____
          ______)
      __________)
      (____)
---.__(___)

'''
stone='''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''
papper='''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)

'''
yc=input("stone,papper or sissors:")
if yc=="stone":
    print(f"your choice:\n{stone}")
elif yc=="papper":
    print(f"your choice:\n{papper}")
else :
    print(f"your choice:\n{sissors}")
rn=random.randint(0,2)
if rn==0:
    print(f"computer choise:\n{stone}")
elif rn==1:
    print(f"computer choise:\n{papper}")
else:
    print(f"computer choise:\n{sissors}")
    
if yc=="stone" and rn!=0:
    if yc=="stone" and rn==1:
        print("you lost!")
    elif yc=="stone" and rn ==2:
        print("you win!")
elif yc=="stone" and rn==0:
     print("draw")
    
if yc=="papper" and rn!=1:
    if yc=="papper" and rn==2:
        print("you lost!")
    elif yc=="papper" and rn==0:
        print("you win!")
elif yc=="papper" and rn==1:
    print("draw")
    
if yc=="sissors" and rn!=2:
    if yc=="sissors" and rn==0:
        print("you lost!")
    elif yc=="sissors" and rn==1:
        print("you win!")
elif yc=="sissors" and rn==2:
    print("draw")

    
    
