with open("example.txt","w") as f:
    f.write("Hello, World!")
f1=open("data1.txt","w")
f2=open("data2.txt","w")
f1.write("First file content\n")
f2.write("Second file content\n")
f1.close()
f2.close()
print("Files written successfully")
try:
    with open("input.txt", "r") as data_file:
        data = data_file.readlines()
except FileNotFoundError:
    print("input.txt not found.")
    data = []

with open("output.txt", "w") as output:
    for line in data:
        output.write(line.upper())
print("Processing data")

try:
    with open("numbers.txt", "r") as f:
        nums = f.readlines()
except FileNotFoundError:
    print("numbers.txt not found.")
    nums = []

# Compute squares of numbers read from numbers.txt
squares = []
for num in nums:
    try:
        n = int(num.strip())
        squares.append(n ** 2)
    except ValueError:
        pass  # skip lines that are not integers

with open("squares.txt", "w") as f2:
    for sq in squares:
        f2.write(str(sq) + "\n")
print("Squares written")

