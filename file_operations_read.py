fp=open("text.txt", "r")
print(fp.read())
fp.close()

# same thing using context manager
# this is more pythonic!
with open("text.txt", "r") as f:
    print(f.read())
# no need to close

# read the file line by line
print("now we read it line by line")
with open("text.txt") as f:
    for line in f:
        print(line,end="")