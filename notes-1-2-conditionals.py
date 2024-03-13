#conditional
#Derek Nong
#Feb 14 2024

#implement the flowchart from the notes

#create thwo variables, xand y
x = 1_000_000
y = -5.2

#If x is less than y print that
#iF x is great than y, print that
#if x is equal to y print that
if x < y :
    print("x is less than y")
elif x > y :
    print("x is greater than y.")
else:
    print("x is equals to y.")

    
# if x >y : 
#     print("x is greater than y.")
# if x == y :
#     print("x is equals to y.")


#Ask the useer what their favourite fruite is
    fave_fruit = input("What's your favourite fruit?")

#ask user age
    user_age = input("how old are you?")

#if their answer is apple or orange
    
if fave_fruit == "apple" or fave_fruit == "orange" :
        print("delisious choice")
else: 
        print("nah uh")

#if they answer banna and they're 2 years old
if fave_fruit== "banana" and user_age == "2" :
            print("bananas are delisious")