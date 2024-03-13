# lists and modules
#Derek Nong
#March 8 2024

import random

def coin_flip():
    # return head, tails or other?
    
    roll = random.random()

    if roll < 0.5:
        return "heads"
    elif roll < 0.99999999:
        return "tails"
    else:
        return "other"
    
def main():

    heads = 0
    tails = 0
    other = 0 

    for _ in range(100_000):
        result = coin_flip()
        if result == "heads":
            heads = heads + 1
        elif result == "tails":
            tails += 1
        else:
            other += 1
    
    print(f"Heads: {heads}")
    print(f"Tails: {tails}")
    print(f"Other: {other}")

main()