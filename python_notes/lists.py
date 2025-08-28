grocery_list = ["eggs", "milk", "cheese", "pasta"]
#In order to use Tuples Encase list of elements with () instead of []
planets = ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")

odd_numbers = [1 ,3 ,5 ,7, 9]

print("The first item on the list is " + grocery_list[0])
print("The second item on the list is " + grocery_list[1])

#Sets encased in curly brackets and removed duplicates

customers = {
"James Smith",
"Andrea Richards",
"Sam Sharp",
"Brenda Longmire",
"Veronica March",
"Sylvia Smith",
"James Smith",
"Vanessa Bush",
"Steve Hammersmith",
"Brenda Longmire",
"Sylvia Smith",
"Steve Hammersmith",
"Walt Hawkins"
}

print(customers)

#dictionaries are indexed lists of values. Like sets, they are surrounded
# by braces and don’t allow duplicates, and they are mutable (that is, editable).
# Each piece of data in a dictionary is referenced by a string or number.

customer1 = {
"name": "James Smith",
"age": 24,
"phone": "555-555-1941",
"email": "james@xyzinternet.net"
}
customer2 = {
"name": "Andrea Richards",
"age": 33,
"phone": "555-555-4928",
"email": "andrea@coffeeloversunite.us"
}

print(customer1["name"])

