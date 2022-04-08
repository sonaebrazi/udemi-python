rows = int(input("enter number of rows:"))
spaces = stumpspaces = rows -1
hashes = 1
while rows >= 1:
    for i in range(spaces):
        print(" ", end="")
    for j in range(hashes):
        print('#', end="")
    print()
    spaces -= 1
    hashes += 2
    rows -= 1
for i in range(stumpspaces):
    print(' ', end="")
    # Prints the hash stump
print("#")