import random
# import random is a simple library that implements the random number generator behavior

# Please read into the variables below the correct numbers. Use try and except to catch error.
# a simple example would be:
# hero_hp = int(input("how many hp does the hero have?"))
while True:
    try:
        hero_hp = input("what is the life of the hero?")
        hero_hp=int(hero_hp)
        break
    except:
        print("give a proper hero number")
while True:
    try:
        dragon_hp = input ("what is the life for the dragon?")
        dragon_hp=int(dragon_hp)
        break
    except:
        print("give a proper dragon number")
while True:
    try:
        hero_max_dmg = input ("what is the damage for the hero?")
        hero_max_dmg= int(hero_max_dmg)
        break
    except:
        print("give a proper hero number for damage")
while True:
    try:
        dragon_max_dmg = input("what is the damage for the dragon?")
        dragon_max_dmg=int(dragon_max_dmg)
        break
    except:
        print("give a proper dragon number for damage")

while True:

    print("The dragon with", dragon_hp, "hp attacks out hero with", hero_hp, "hp")


    dragon_attack = random.randint(1, dragon_max_dmg)
    # here you need to update the hero hp, you need to subtract the damage that the dragon did
    hero_hp=hero_hp-dragon_attack
    # add code on this line

    print("The dragon does", dragon_attack, "damage and the hero has", hero_hp, "hp left")
    # add an if condition to check if the hero was killed by the dragon
    if hero_hp<=0:
        print("Unfortunately the dragon killed our hero. RIP sir Bravealot")
        break

    hero_attack = random.randint(1, hero_max_dmg)
    # here you need to update the dragon hp, you need to subtract the damage that the hero did
    # add code on this line

    print("The hero does", hero_attack, "damage and the dragon has", dragon_hp, "hp left")
    # add an if condition to check if the dragon was killed by the hero
    if dragon_hp<1:
        print("Our valiant hero has slain the dragon!")
        break


    input("Round over. Press any key")