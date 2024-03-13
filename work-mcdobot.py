#Want fries?
#Derek Nong
#Feb 21 2024

#introduces to the user
print("Hello! I am Mcdobot!I will be continuing the rest of your order.")


#ask if they want fries
response = input("Would you like fries with your meal? Respond with either yes, or no.")


#accept yes or no answer and reply appropiately
if response.lower().strip(" !?.,") == "yes" :
    secondresponse = input("Alright, fries will be added to your meal. Would you like anything else? Respond with yes or no.")
elif response.lower().strip(" !?,.") == "no" :
    secondresponse = input("Alright, would you like anything else with your order? Respond with yes or no.")


#if user replies with anything else, repeat their answer back and say that it did not understand
else:
    print(f"Sorry I do not understand what {response} means. ")
