text = input("Enter somthing:")

with open("data.txt", "w") as f:
    f.write(text)

print("Saved to data.txt")