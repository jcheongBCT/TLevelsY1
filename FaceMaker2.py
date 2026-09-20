def choose_hair(style="normal"):
    if style == "spiky":
        return "  /\\/\\/\\/\\/\\  "
    elif style == "waves":
        return "  (wwwwwww)  "
    elif style == "shaved":
        return "   .-------.  "
    elif style == "american":
        return "  /$$$$$$$$\\ "
    else:
        return "   ._______.  "


def choose_eyes(expression="normal"):
    if expression == "happy":
        return "^   ^"
    elif expression == "wink":
        return "o   ~"
    elif expression == "asleep":
        return "_   _"
    elif expression == "danger":
        return "O   O"
    elif expression == "mad":
        return "{}   []"
    return "o   o"


def get_nose():
    return "^"


def get_mouth(expression="normal"):
    if expression == "happy":
        return "\\___/"
    elif expression == "surprised":
        return "  O  "
    return "_____"


def draw_face(hair_style="normal", expression="normal"):
    hair = choose_hair(hair_style)
    eyes = choose_eyes(expression)
    nose = get_nose()
    mouth = get_mouth(expression)

    face = f"""
{hair}
 /  {eyes}  \\
| (  {nose}  ) |
 |  {mouth}  |
  \\       /
   '-----'
"""
    print(face)


# Example usage:
print("This is your face, let's do something about that:")
draw_face()

print("What style of hair do you want? ")
print("Your options are: ")
print("spiky")
print("waves")
print("shaved")
print("american")
chosen_hair = str(input("Enter your choice here: "))

print("How are you emotionally? ")
print("Your options are: ")
print("happy")
print("wink")
print("asleep")
print("danger")
print("mad")
chosen_eyes = str(input("Enter your choice here: "))

draw_face(chosen_hair, chosen_eyes)