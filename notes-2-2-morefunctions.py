#more functions
#Ubial
#3 April 2024


#implement stars function

def stars(num):
    """Returns specified number of stars"""
    value = "" # placeholder for return value


    if num == 0 or num == 1:
        value = "*"
    elif num > 1:
        value = "*" * num
    else: 
        value = "sorry cannot take negative numbers."

    return value
#elif number greater than one, retrun that num * star

#else return negitive number are not allowed


#multiply strings
# greeting = "hello"
# print(greeting * 5)

# print("the quick brown fox jumps over the lazy dog" * 2)
print(stars(0))
print(stars(1))
print(stars(100))  #"**********"
print(stars(-1))
