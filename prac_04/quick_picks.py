import random

MAX_NUMBER=99
MIN_NUMBER=1
PICKS_PER_LINE =6

number_of_picks= int(input("How many quick picks :"))
for x in range(number_of_picks):
    quick_pick=[]
    while len(quick_pick) < PICKS_PER_LINE:
        number=random.randint(MIN_NUMBER,MAX_NUMBER)
        if number not in quick_pick:
            quick_pick.append(number)

    quick_pick.sort()
    print(" ".join(f"{num:2}" for num in quick_pick))
