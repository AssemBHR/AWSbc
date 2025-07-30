name = input ("what is your name?")
char_class = input ("what is your class?")
age = int(input ("what is your age?"))
weapon = input ("what is your weapon of choice?") .strip ()
blessing_from_the_elders = input ("do you have a blessing from the elders?")

if name == "doomwraith" and char_class == "rouge" and age == 666 and weapon == "dagger" and blessing_from_the_elders == "yes" :
    print ("Master of Shadows. Enter the Hall of Echoes.")
elif char_class == "warrior" and weapon == "axe" :
    print ("Strength, steel, and spirit. Welcome, berserker.")
elif char_class == "mage" and age <120 and weapon == "staff" :
    print ("Young sorcerer, your magic is raw but promising. You may enter.")
elif age <16 :    
    print ("You are too young to face this realm. Return when your beard grows.")
else :
    print ("The gate remains closed. Your fate lies elsewhere.")
