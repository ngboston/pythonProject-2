myEmptyTuple1 = ()
myEmptyTuple2 = tuple()

myList1 = ['element1', 12, 35.5, False]
myTuple2 = tuple(myList1)
print(myTuple2)
print(type(myTuple2))

userTypes = ("admin", "student", "teacher", "moderator", "admin","admin")

user1, *u3 = userTypes

"""testTuple = userTypes * 10

for u in range(len(testTuple)):
    print(testTuple[u])"""

if "Student" in userTypes:
    print("yeaaah")

print(len(123))