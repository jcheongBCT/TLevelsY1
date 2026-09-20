dummy_nose = "achoo"
dummy_mouth = "3"

def choose_hair(style="normal"):
    if style == "spiky":
        return "    "
    elif style == "waves":
        return "    "
    elif style == "":
        return "     "
    elif style == "american":
        return "  /$$$$$$$$\\ "
    else:
        return "   ._______.  "
    #PROBLEM: There are TWO hairstyles missing, as well as one option and it's style


def choose_eyes(expression="normal"):
    if expression == "happy":
        return ""
    elif expression == "wink":
        return "o  "
    elif expression == "asleep":
        return ""
    elif expression == "":
        return ""
    elif expression == "mad":
        return "{}   []"
    return "o   o"
    #PROBLEM: There are some missing and most of the eyes are incomplete, fix this!

def get_nose():
    return ""   #PROBLEM: ADD THE DIFFERENT NOSE STYLES!


def get_mouth(expression="normal"):
    #PROBLEM: ADD THE DIFFERENT MOUTH STYLES!!!!
    return "_____"


def draw_face(hair_style="normal", expression="normal"):
    hair = choose_hair(hair_style)
    eyes = choose_eyes(expression)
    #PROBLEM: I HAVE NO NOSE AND I MUST SMELL
    #PROBLEM: I HAVE NO MOUTH AND I MUST SCREAM

    face = f"""
{hair}
 /  {eyes}  \\
| (  {dummy_nose}  ) |
 |  {dummy_mouth}  |
  \\       /
   '-----'
"""
    print(face)

print("This is your face, let's do something about that:")
draw_face()

print("What style of hair do you want? ")
print("Your options are: ")
print("spiky")
print("waves")
#PROBLEM: OPTIONS ARE INCOMPLETE
chosen_hair = str(input("Enter your choice here: "))

print("How are you emotionally? ")
print("Your options are: ")
print("happy")
print("wink")
print("asleep")
print("danger")
print("mad")
#PROBLEM: ARE YOU GOING TO ASK ME ABOUT MY EYES
chosen_eyes = ""

draw_face(chosen_hair, chosen_eyes)