def askPersonalInfo():
    while True:
        firstName = input("Input u first name: ")
        lastName = input("Input u last name: ")
        yearBirth = input("Input u year of birth: ")
        gender = input("Input u gender (M, F): ")

        if firstName == "" or lastName == "" or yearBirth == "" or gender == "" or gender not in ('F', 'M'):
            print("Frond data")
        else:
            return firstName, lastName, yearBirth, gender


def askHobby():
    hobbyInd = 1
    hobbyList = []
    while True:
        hobbyName = input(f"Name of the hobby #{hobbyInd}: ")
        if hobbyName == "":
            print("no info. Input stopped")
            break
        else:
            hobbyList.append(hobbyName)
            hobbyInd += 1
        if len(hobbyList) > 0:
            print(f"You have {hobbyInd - 1} hobbies.")
        else:
            print("U have no hobbies at all")

    return  hobbyList

personalInfo = askPersonalInfo()
print(personalInfo)
print(type(personalInfo))
hobbiesInfo = askHobby()
print(hobbiesInfo)
print(type(hobbiesInfo))