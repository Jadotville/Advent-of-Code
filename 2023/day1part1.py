with open("day1.txt", "r") as file:
    lines = file.readlines()

sum=0
for line in lines:
    num = 0
    found=False
    for char in line:
        if char in ['0','1','2','3','4','5','6','7','8','9'] and not found:
            num+=10*int(char)
            found=True
    found=False
    for char in line[::-1]:
        if char in ['0','1','2','3','4','5','6','7','8','9'] and not found:
            num+=int(char)
            found=True
    sum+=num  
print(sum)