#loops and iteration
#derek Nong
#April 9 2024

#print  "something 10 times"
for _ in range(10):
    print("something 10 times")

#print out every item in my grocery list

grocery_list = [
    "dishwasher tabs",
    "aluminium foil",
    "blueberry muffins",
    "RTX 4070 Super",
]

#stop when we reach blueberry muffins
for item in grocery_list:
    print("-------")
    print(f" * {item}")


    if item == "blueberry muffins":
        break 


#count from 0-9
for i in range(10) :
    print(i)

    # modulo, or what is the remainder of a diviision
    if i%2 == 0:
        print(f"{i} is an even number")


#rewrite the above loop as a while loop
counter = 0

while counter < 1000:
    if counter % 2 == 0:
        print(f"{counter} is an even number")
    else:
        print(counter)


    #increment counter by 1
    #counter = counter +1
    counter += 1