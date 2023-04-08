# 7.4
# creating list and storing it in variable
things = ["mozzarella", "cinderella", "salmonella"]

# 7.5
# capitalizes first letter of second element
things[1] = things[1].title()
print(things)

# 7.6
# converts first element to uppercase
things[0] = things[0].upper()
print(things)

# 7.7
# removes last element from list
things.pop()
print(things)

# 9.1
# defining a function to return a list
def good():
    list1 = ['Harry', 'Ron', 'Hermione']
    return list1

# 9.2
# creating a generator function that returns all odd values in range 10
def get_odds(first=1, last=10, step=2):
    number = first
    while number < last:
        yield number
        number += step
# iterating through and printing each result
odd = get_odds()
for i in odd:
    print(i)
# 3rd value returned is 5