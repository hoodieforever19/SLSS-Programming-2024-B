#chat bot
#Derek Nong
#march 8 2024

import random 
import time


#greets and asks how are you
reply = input("Hey user, how are you?")
time.sleep(2)

#respond with general statements 
    #and reaspond randomly

good_possible_resp = ["I'm really happy for you." , "That's really good news!!" , "That's awesone."]
bad_possible_resp = ["im sorry to hear that." , "I hope you are feeling better!","I sorry and I hope you feel better!"]

#randomly chose a response and print
if reply == "good" :
    chosen_response = random.choice(good_possible_resp)

    print(chosen_response)
elif reply == "bad":
    badchosen_respone = random.choice(bad_possible_resp)
    print(badchosen_respone)
else:
    print("thanks for the response ")

#say good bye
time.sleep(2)
print("Goodbye!")