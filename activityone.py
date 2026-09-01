print("=== Smart school day planner ===")
print("answer 3 quick questions and I will plan your day!\n")

day    =input("what day is it? (monday to sunday:").strip().lower()
weather=input("whatis the weather (sunny/rainy/cloudy").strip().lower()
homework=input("is your homework done(yes/no").strip().lower()

print()
print(f"=== your plan for {day} ===")
print("-" * 35)

if day in ("saturday","sunday"):
    print("day type    : weekend - enjoy your free time!")
elif day == "monday":
    print("day type   : first day of the week. Pack your weekly planner.")
elif day == "friday":
    print("day type    : last school day. Return libary books today.")
elif day in ("tuesday","wednesday","thursday"):
    print("day type   : regular school day. stay focused!")
else:
    print("day type     : day not recognised. please check your spelling")

if weather == "rainy" or weather == "cloudy":
    print("weather tip: bring an umbrella-it may get wet outside")

if not (homework == "yes"):
    print("homework   : not done yet. finish it before going out!")

if weather == "rainy" and not (homework=="yes"):
    print("best plan:  stay in do your homework and watch your favorite show.")
elif weather == "sunny" and homework == "yes" and not (day in ("saturday","sunday")):
    print("best plan  : all set for a great school day-you are prepared!")
elif day in ("saturday","sunday") and weather == "sunny":
    print("best plan  : good weekend weather-head outside and have fun!")
else:
    print("best plan  : take it one step at a time - you have got this!")

    print()
    print("plan complete! have a wonderful day!")
