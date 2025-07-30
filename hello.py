name = input ("What is your name boy?") .lower ()
age = int (input ("What is your age?"))
mood = input("What is your mood?") .strip().lower()

if name == "doomwraith" and age == 666 :
    print ("🟢Inner Circle access granted. Welcome back, master.")
elif age >= 21 and mood == "pumped":
    print("🟢 Welcome, warrior. Prepare for battle.")
elif age >= 18 and age <= 20:
    print("🟠 Wait in the lounge. Your time is near.")
elif age < 18 and (mood == "tired" or mood == "lazy"):
    print("🔴 Go back home and level up, rookie.")
else:
    print("🔒 Access denied. This realm isn’t for you.")