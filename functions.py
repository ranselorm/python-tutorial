def print_5_times():
    counter = 0
    while counter < 5:
        print("This is printed 5 times using while loop.")
        counter += 1

print_5_times()



# Exercise
def shouter(str, num):
    if num > 10:
        print("You are too loud!")
    else:
        for _ in range(num):
            print(str.capitalize())
    return

shouter("hello! ", 12)