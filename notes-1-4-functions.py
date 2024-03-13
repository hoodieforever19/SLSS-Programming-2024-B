#Functions
#Derek Nong
#26 February 2024

#Create a function called say_hello
#when you call it, it prints hello

def say_hello():
    print("Hello")

#Create a function called say_hello_params
    #The parameter we pass in is the name of
    #the person that we're greeting

def say_hello_params(name):
    print(f"Hello {name.capitalize()}")


#Create a function that takes a number
    # it will tell yoy how big that number is

def how_big(num):
    if num < 0 :
        return "very small" #stops exucution of a function and returns a value, in this case very small
    if num < 10:
        return "pretty small"
    if num < 100:
        return "big"
    if num < 1000: 
        return "pretty big"
    return "humongus"


# say_hello()
# say_hello_params("sebastian")
#  say_hello_params("Thomas")
# say_hello_params("thomas")

print( how_big(-1)) #"very small"