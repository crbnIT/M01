guess_me = 7
number = 6
while number != guess_me:
    if number < guess_me:
        print("Too low")
        number += 1
    elif number > guess_me:
        print("oops")
        break
