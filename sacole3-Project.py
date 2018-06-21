has_food = False
has_clothes = False
from sys import exit
import time

def song():
    print("""I'll be your dream, I'll be your wish, I'll be your fantasy.
    I'll be your hope, I'll be your love, be everything that you need.
    I love you more with every breath, truly madly deeply do
    I will be strong, I will be faithful 'cause I'm counting on a new beginning.
    A reason for living. A deeper meaning.
    I want to stand with you on a mountain.
    I want to bathe with you in the sea.
    I want to lay like this forever.
    Until the sky falls down on me
    And when the stars are shining brightly in the velvet sky,
    I'll make a wish send it to heaven then make you want to cry
    The tears of joy for all the pleasure and the certainty.
    That we're surrounded by the comfort and protection of
    The highest power, in lonely hours, the tears devour you
    I want to stand with you on a mountain,
    I want to bathe with you in the sea.
    I want to lay like this forever,
    Until the sky falls down on me
    Oh can you see it baby?
    You don't have to close your eyes
    'Cause it's standing right before you.
    All that you need will surely come
    I'll be your dream, I'll be your wish, I'll be your fantasy.
    I'll be your hope, I'll be your love, be everything that you need.
    I'll love you more with every breath, truly madly deeply do
    I want to stand with you on a mountain
    I want to bathe with you in the sea.
    I want to lay like this forever.
    Until the sky falls down on me
    I want to stand with you on a mountain
    I want to bathe with you in the sea.
    I want to live like this forever.
    Until the sky falls down on me.""")

def kitchen():
    global has_food
    global has_clothes
    print("""You enter the kitchen and you were pondering on what to get her.
    ('cat food') or ('human food').""")
    
    choice = input("")
    if "cat food" in choice:
       print("""You got a bowl and filled it with cat food but you died of heart attack.
       (Did you seriously think I'm gonna let you do that.)""")
       quit()

    if "human food" in choice:
        print("You got a cup of ramen and you filled it with fish.")
        has_food = True
        if has_clothes:
            living_room_()
        else:
            bed_room()

def bed_room():
    global has_clothes
    global has_food
    print("""You entered your bed room to get her clothes.
    Will you give her a ('black robe') or ('thread bear clothes').""")
    
    choice = input("")
    if "black robe" in choice:
       print("You went to your closet and got her a black robe and went back to the kicthen.")
       has_clothes = True
       if has_food:
            living_room_()
       else:
            kitchen()

    if "thread bear clothes" in choice:
        print("""You heard your window break but you fill pain in your head and you fell to the floor.
        (A little gift from me to you.(pays the sniper $2,000))""")
        quit()

def living_room_():
    print("""You enter the room and you place the stuff on the table and you notice that she is still asleep.
    You sit on the couch and waited for her to wake up.""")
    time.sleep(5)
    intro()

def intro():
    print("""I saw her shift around a little bit afterwards she woke up.
She looked around the room than at me. Will you ('greet first') or ('let her greet first').""")

    choice = input("")

    if choice == "greet first":
        print("Hello there, my name is (Y/N) what is yours?")
        time.sleep(4)
        print("My name is Ayami. Umm, where am I and how did I get here.")
        time.sleep(4)
        print("""I found you in the snow in the worst condition. So, I brought you here.
    As for where. This place is my house.""")
        time.sleep(10)
        print("Thank you, I appreciate your kindness.")
        time.sleep(4)
        print("No problem, besides anyone with a kind heart would do the same.")
        time.sleep(6)
        print("I got you something to eat and some clothes for you.")
        time.sleep(5)
        print("Thank you.(She looks at the food first and grew devious smile.")
        time.sleep(3)
        print("(She grabs the bowl and eats the food as she cries with a anime smile on her face.)")
        time.sleep(6)
        print('(After a while she finished eating)'"I'll leave you in some privacy")
        time.sleep(3)
        print("(You walk out of the room and in the one next to it.)")
        time.sleep(5)
        print("I'm properly clothed! (I heard as I reentered the room.)")
        time.sleep(2)
        print("Thank you again for your kindness.(She bows her head to me.)")
        time.sleep(4)
        print("It's getting late I'll show you to the guest room.")
        time.sleep(5)
        print("(You showed her the way to the guest room and she thanked you again for your courtesy)")
        time.sleep(4)
        print("(You headed towards your room and lyed down until you fell asleep.)")
        time.sleep(4)
        song()

        if choice == "let her greet first":
            print("You two stood there forever looking at each other")
            quit()
        

print("""You were strolling threw the snowy woods until you a beaten up neko girl on the ground.
Will you take her with you (#1) or will you leave her in the cold(#2).""")

answer = input("")

if answer == "1":
    print("You were a kind hearted person.")
    time.sleep(6)
    print("So you decided to take care of her.")
    time.sleep(6)

if answer == "2":
    print("You thought that the strong survives will the weak should learn.")
    time.sleep(6)
    print("So you left her.")
    time.sleep(6)
    print("Cruel End.")
    quit()

print("""You droped her off in the living room in front of the fire place.
Will you go to the ('kitchen') to get her food or to your ('bed room') to get her better clothing.""")

choice = input("")

if choice == "kitchen":
    kitchen()
elif choice == "bed room":
    bed_room()