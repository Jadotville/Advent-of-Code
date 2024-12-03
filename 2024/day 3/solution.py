with open("input.txt", "r") as file:
    content = file.readlines()
    
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
numbersz = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

sum = 0

# for line in content:
#     print(line)
#     indices = [i for i in range(len(line)) if line.startswith("mul(", i) and i+7 < len(line)]
#     print(indices)
#     for i in indices:
#         if line[i+4] in numbersz and line[i+5] == "," and line[i+6] in numbersz and line[i+7] == ")":
#             sum += int(line[i+4]) * int(line[i+6])

enabled = True
for line in content:
    l = len(line)
    i = 0
    while i+4 < l:
        if line[i:i+4] == "do()":
            enabled = True
        if line[i:i+7] == "don't()":
            enabled = False
        n1 = 0
        n2 = 0
        # print(line[i:i+4])
        if line[i:i+4] == "mul(" and enabled:
            if line[i+4] in numbers and line[i+5] == ",":
                n1 = int(line[i+4])
                i+=6
            elif line[i+4] in numbers and line[i+5] in numbersz and line[i+6] == ",":
                n1 = int(line[i+4:i+6])
                i+=7
            elif line[i+4] in numbers and line[i+5] in numbersz and line[i+6] in numbersz and line[i+7] == ",":
                n1 = int(line[i+4:i+7])
                i+=8
            if n1 == 0:
                i += 4
                continue
            # print(n1)
            if i+1 < l and line[i] in numbers and line[i+1] == ")":
                n2 = int(line[i])
                i+=2
            elif i+2 < l and line[i] in numbers and line[i+1] in numbersz and line[i+2] == ")":
                n2 = int(line[i:i+2])
                i+=3
            elif i+3 < l and line[i] in numbers and line[i+1] in numbersz and line[i+2] in numbersz and line[i+3] == ")":
                n2 = int(line[i:i+3])
                i+=4
            if n2 == 0:
                i += 2
                continue
            # print(n2)
            sum += n1 * n2
        else:
            i+=1
            

print(sum) 
           
            
            
            # if line[i+4] in numbersz and line[i+5] == "," and line[i+6] in numbersz and line[i+7] == ")":
            #     sum += int(line[i+4]) * int(line[i+6])
            # elif i+8 < l and line[i+8] == ")":
            #     if line[i+4] in numbersz and line[i+5] in numbers and line[i+6] == "," and line[i+7] in numbersz:
            #         sum += int(line[i+4:i+6]) * int(line[i+7])
            #     elif line[i+4] in numbersz and line[i+5] == "," and line[i+6] in numbersz and line[i+7] in numbers:
            #         sum += int(line[i+4]) * int(line[i+6:i+8])
            # elif i+