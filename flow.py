# while loop example
counter = 0 

while counter <= 10:
    print("Counter is:", counter)
    if counter == 5:
        print("Counter reached 5")
    counter += 1
print("Finished counting up to 10.")


# for loop example
# for i in range(10):
#     print("Iteration:", i)
#     if i == 3:
#         print("Iteration reached 3")

# Exercise
for x in range(1, 6):
    if x == 2:
        print("the value is 2")
    elif x == 5:
        print("the last item " * 6)
    else:
        print("the value is not 2")
