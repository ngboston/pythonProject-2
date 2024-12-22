from  uuid import uuid4

x = str(uuid4())

class UserBank:
    def __init__(self, name, age, logPhone):
        self.__name = name
        self.__age = age
        self.__guid = str(uuid4())
        self.__balanse = 0
        self.__loginPhone = logPhone
        self.__password = str(uuid4())[0:8:-1]

    def changePassword(self):
       while True:
           anw = input("Enter old password: ")
           if anw == self.__password:
               while True:
                   new_pass1 = input("Enter new password: ")
                   new_pass2 = input("Confirm u pass:")
                   if new_pass1 == new_pass2:
                       self.__password = new_pass1
                       break

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,newName):
        self.__name = newName

    @property
    del loginPhone(self):
    return self.__loginPhonew



    def getPassword(selfs):
        password = str(uuid4())
        return password[0:8]

    def showInfo(self):
        print(f"user id = {self.__guid} pass = {self.__password}")

tom = UserBank("Tom", 18, 17814924457)
tom.showInfo()




