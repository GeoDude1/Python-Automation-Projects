name = input("What name?: ")

file = open("files_test.txt", "a")
file.write(f"{name}\n")
file.close