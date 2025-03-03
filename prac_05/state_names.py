"""
CP1404/CP5632 Practical
Program:State names finder from dictionary
Abid Hasan
Start date:03/03/2025
"""
CODE_TO_NAME = {
    "QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
    "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania", "SA": "South Australia"
}
for state, name in CODE_TO_NAME.items():
    print(f"{state:3} is {name}")

state_code = input("Enter short state: ").upper()
while state_code != "":
    try:
        print(state_code, "is", CODE_TO_NAME[state_code])
    except KeyError:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()

