"""
CP1404/CP5632 Practical
Program:Color code finder from dictionary
Abid Hasan
Start date:03/03/2025
"""
colour_to_code = {
    "AliceBlue": "#f0f8ff","Absolute Zero": "0048ba", "AntiqueWhite": "#faebd7", "Aqua": "#00ffff", "Aquamarine": "#7fffd4",
    "Azure": "#f0ffff", "Beige": "#f5f5dc", "Bisque": "#ffe4c4", "Black": "#000000",
    "BlanchedAlmond": "#ffebcd", "Blue": "#0000ff"
}
for colour, code in colour_to_code.items():
    print(f"{colour:14} is {code}")
color_name = input("Enter color name: ").capitalize()
while color_name != "":
    try :
        print(f"The hexadecimal code for {color_name} is {colour_to_code[color_name]}")
    except KeyError:
        print("Invalid color name.")
    color_name = input("Enter color name: ").capitalize()

