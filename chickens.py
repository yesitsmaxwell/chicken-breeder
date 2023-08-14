import random

chickens = ['australorp', 'rhode island red', 'wyandotte', 'buff orpington', 'white silkie', 'brown silkie', 'black silkie', 'game hen', 'isa brown', 'plymouth rock', 'aracuna']

# all the characteristics
characteristics = {
    "australorp": {
            "size": "big",
            "colour": "black",
            "noise": "loud",
            "friendliness": "very friendly",
            "speed": "moderatley speedy",
            "eggspeed": "fast",
            "eggsize": "big",
            "broodiness": "kind of",
            "inquisitiveness": "kind of",
        },
    "rhode island red": {
            "size": "big",
            "colour": "red",
            "noise": "loud",
            "friendliness": "very friendly",
            "speed": "slow",
            "eggspeed": "moderate",
            "eggsize": "big",
            "broodiness": "not",
            "inquisitiveness": "not very",
        },
    "wyandotte": {
            "size": "medium",
            "colour": "speckled white+black",
            "noise": "quiet",
            "friendliness": "very friendly",
            "speed": "fast",
            "eggspeed": "moderate",
            "eggsize": "medium",
            "broodiness": "pretty",
            "inquisitiveness": "highly",
        },
    "buff orpington": {
            "size": "ginourmous",
            "colour": "golden",
            "noise": "quiet",
            "friendliness": "not friendly",
            "speed": "moderatley speedy",
            "eggspeed": "moderate",
            "eggsize": "ginourmous",
            "broodiness": "not",
            "inquisitiveness": "not very",
        },
    "white silkie": {
            "size": "tiny",
            "colour": "white",
            "noise": "quiet",
            "friendliness": "moderatley friendly",
            "speed": "fast",
            "eggspeed": "low",
            "eggsize": "small",
            "broodiness": "not",
            "inquisitiveness": "very highly",
        },
    "brown silkie": {
            "size": "tiny",
            "colour": "brown",
            "noise": "quiet",
            "friendliness": "moderatley friendly",
            "speed": "fast",
            "eggspeed": "low",
            "eggsize": "small",
            "broodiness": "not",
            "inquisitiveness": "very highly",
        },
    "black silkie": {
            "size": "tiny",
            "colour": "black",
            "noise": "quiet",
            "friendliness": "moderatley friendly",
            "speed": "fast",
            "eggspeed": "low",
            "eggsize": "small",
            "broodiness": "not",
            "inquisitiveness": "very highly",
        },
    "game hen": {
            "size": "tiny",
            "colour": "golden",
            "noise": "loud",
            "friendliness": "not friendly",
            "speed": "very fast",
            "eggspeed": "low",
            "eggsize": "small",
            "broodiness": "not",
            "inquisitiveness": "very highly",
        },
    "isa brown": {
            "size": "big",
            "colour": "brown",
            "noise": "quiet",
            "friendliness": "moderatley friendly",
            "speed": "moderatley fast",
            "eggspeed": "fast",
            "eggsize": "big",
            "broodiness": "not",
            "inquisitiveness": "moderatley",
        },
    "plymouth rock": {
            "size": "big",
            "colour": "white",
            "noise": "quiet",
            "friendliness": "very friendly",
            "speed": "moderatley fast",
            "eggspeed": "medium",
            "eggsize": "big",
            "broodiness": "kind of",
            "inquisitiveness": "very highly",
        },
    "aracuna": {
            "size": "medium",
            "colour": "brown",
            "noise": "quiet",
            "friendliness": "friendly",
            "speed": "fast",
            "eggspeed": "moderate",
            "eggsize": "medium",
            "broodiness": "not",
            "inquisitiveness": "very highly",
        },
    }

# function to determine the chickens you get
def chickenlist():

    chicken1 = (random.choice(chickens))
    chickens.remove(chicken1)
    chicken2 = (random.choice(chickens))
    chickens.remove(chicken2)
    chicken3 = (random.choice(chickens))
    chickens.remove(chicken3)
    return [chicken1, chicken2, chicken3]

# function to pick 1 chicken
def breeder1():

    breed1 = input("Choose one chicken. ")

    if breed1 == c[0]:
        print("You own", c[0])
    elif breed1 == c[1]:
        print("You own", c[1])
    elif breed1 == c[2]:
        print("You own", c[2])
    else:
        print("You don't own that chicken. Choose another. Make sure to use all lowercase letters and correct spelling.")
        breed1 = breeder1()
    return (breed1)

# function to pick another chicken
def breeder2():

    breed2 = input("Choose another chicken. ")

    if breed2 == c[0]:
        print("You own", c[0])
    elif breed2 == c[1]:
        print("You own", c[1])
    elif breed2 == c[2]:
        print("You own", c[2])
    else:
        print("You don't own that chicken. Choose another. Make sure to use all lowercase letters and correct spelling.")
        breed2 = breeder2()
    return (breed2)

# function to generate a new chicken
def newchicken():

    newsize = (random.choice(breeds))
    newcolour = (random.choice(breeds))
    newnoise = (random.choice(breeds))
    newfriendliness = (random.choice(breeds))
    newspeed = (random.choice(breeds))
    neweggspeed = (random.choice(breeds))
    neweggsize = (random.choice(breeds))
    newbroodiness = (random.choice(breeds))
    newinquisitiveness = (random.choice(breeds))
    return [newsize, newcolour, newnoise, newfriendliness, newspeed, neweggspeed, neweggsize, newbroodiness, newinquisitiveness]

def printchicken():

    print(name, "is a", characteristics[newchicken[0]]["size"], characteristics[newchicken[1]]["colour"], characteristics[newchicken[2]]["noise"], characteristics[newchicken[3]]["friendliness"], characteristics[newchicken[4]]["speed"], "chicken with", characteristics[newchicken[5]]["eggspeed"], "egg speed, laying", characteristics[newchicken[6]]["eggsize"], "eggs.", name, "is", characteristics[newchicken[7]]["broodiness"], "broody and is", characteristics[newchicken[8]]["inquisitiveness"], "inquisitive. Their parents were a", c[0], "and a", c[1])

# get 3 chickens
c = chickenlist()

# print the chickens you got
print("You got a", c[0], "a", c[1], "and a", c[2])

# print their characteristics
print("Your", c[0], "is a", characteristics[c[0]]["size"], characteristics[c[0]]["colour"], characteristics[c[0]]["noise"], characteristics[c[0]]["friendliness"], characteristics[c[0]]["speed"], "chicken with", characteristics[c[0]]["eggspeed"], "eggspeed laying", characteristics[c[0]]["eggsize"], "eggs. It is", characteristics[c[0]]["broodiness"], "broody and", characteristics[c[0]]["inquisitiveness"], "inquisitive.")
print("Your", c[1], "is a", characteristics[c[1]]["size"], characteristics[c[1]]["colour"], characteristics[c[1]]["noise"], characteristics[c[1]]["friendliness"], characteristics[c[1]]["speed"], "chicken with", characteristics[c[1]]["eggspeed"], "eggspeed laying", characteristics[c[1]]["eggsize"], "eggs. It is", characteristics[c[1]]["broodiness"], "broody and", characteristics[c[1]]["inquisitiveness"], "inquisitive.")
print("Your", c[2], "is a", characteristics[c[2]]["size"], characteristics[c[1]]["colour"], characteristics[c[2]]["noise"], characteristics[c[2]]["friendliness"], characteristics[c[2]]["speed"], "chicken with", characteristics[c[2]]["eggspeed"], "eggspeed laying", characteristics[c[2]]["eggsize"], "eggs. It is", characteristics[c[2]]["broodiness"], "broody and", characteristics[c[2]]["inquisitiveness"], "inquisitive.")

# choose the chickens to breed
breed1 = breeder1()
breed2 = breeder2()
breeds = [breed1, breed2]

name = input("Name your chicken: ")

# generate and print the new chicken
newchicken = newchicken()

# print what the new chicken is
fc = printchicken()
