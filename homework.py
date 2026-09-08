print("swimming pool entry checker")
print("answer 3 questions and I will tell you which pool you can use.\n")
age=input(int("how old are you?"))
can_swim=("can you swim?").lower()
adult_here=input("is an adult there with you?").lower

if age<=4:
    print("you can only use the splash pool with and adult")
elif age<=12:
    print("main pool with an adult")
elif age<=18:
    print("you can use the main pool alone if you can swim")
else:
    print("all pools open to you")

swim_known=True
adult_known=True
if can_swim:not"yes"and not"no"
print("error swim not known")
swim_known=False

if adult_here: not"yes"or"no"
print("error adult not known")
adult_known=False

if adult_known==True and adult_here=="yes" and can_swim=="yes":
    print("you can use the deep pool")

if can_swim=="no" and age<=12:
    ("you can use the shallow pool but be careful")

if adult_known==True and adult_here=="no":
    print("be careful there is no lifeguard")

if adult_known==True and swim_known==True and can_swim=="yes" and adult_here=="yes"and age>4:
    print("you can swim in the deep pool")
elif adult_known==True and swim_known==True and can_swim=="no" and adult_here=="yes"or"no"and age>4:
    print("you can swim in the shallow pool")
elif adult_known==True and swim_known==True and age<4:
    print("you can use the splash pool")
else:
    print("your answers were unclear")


print()
print("have a safe swim")

