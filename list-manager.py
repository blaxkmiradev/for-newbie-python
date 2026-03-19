items = []

while True:
    item = input("Add item (or 'exit'): ")
    if item == "exit":
        break
    items.append(item)

print("Your list:", items)