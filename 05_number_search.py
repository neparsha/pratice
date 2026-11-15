# number search

#number list
list = [2, 68, 404, 7, 10]

#input
search = int(input("Search a number: "))

#boolean
found = False

#loop
for num in list:
    if num == search:
        print("Found")
        found = True
        break

#not condition
if not found:
    print("Not found")

#code complete

