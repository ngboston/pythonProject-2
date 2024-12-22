try:

    fileHandler = open("text.txt")
# if fileHandler:
# print("файл С")
# print("2 part:")
# print(fileHandler.readline(5))
# str1 = fileHandler.readlines()
# str2 = fileHandler.read()
# print(type(str1))
    for i in range(5):
        fileHandler.write(f"line {i}\n")
        mylist = ["1\n","3","4","red","black","doc","cat"]
        fileHandler.writelines(mylist)

    fileHandler2 = open("test2.txt", "w+")
    n = fileHandler2.write("test text write in second files")
except: