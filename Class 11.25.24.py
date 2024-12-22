# try:
#     amount = int(input("Entee the amount of recived items: "))
#     item_type = input("enter the tupe of items: ")
#     part_number = int("Enter the part number: ")
#     parts_amount = amount / part_number
#     print(amount, item_type)
#     print(parts_amount)
# except ZeroDivisionError:
#     print("Куди ти ділиш??")
# except ValueError:
#     print(ValueError)
# finally:
#     print("Try suc done")


# try:
#     f = open("tect.txt", 'w')
#     print(" Do op with file")
# finally:
#     f.close()

# try:
#     apples = int(input("Eneter a number apple u have: "))
#     if apples < 0:
#         raise Exception
#     print(f"U have {apples} apples")
# except Exception:
#     print(f"negative apples?")
#     apples = 0
# except ZeroDivisionError:
#      print("Куди ти ділиш??")
#  except ValueError:
#      print(ValueError)
#  finally:
#      print("Try suc done")

try:
    x = 1 / 0
except Exception as ex:
    print(type(ex))

