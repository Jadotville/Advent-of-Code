with open("input.txt", "r") as file:
    data = []
    for line in file:
        data.append([int(x) for x in line.strip().split(" ")])
        
print(data)