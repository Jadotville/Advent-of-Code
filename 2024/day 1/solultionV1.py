# Open a file in read mode
with open('C:\\Users\\olive\\OneDrive\\Informatik\\Advent of Code\\2024\\day 1\\input.txt', 'r') as file:
    content = file.read()

# Print the content of the file
# print(content)
l1 =[]
l2 =[]

for line in content.split('\n'):    
    words = line.split()
    l1.append(words[0])
    l2.append(words[1])

l1.sort()
l2.sort()

sum = 0

for i in range(len(l1)):
    sum += abs(int(l1[i]) - int(l2[i]))
    
print(sum)

sum = 0

for i in l1:
    sum += l2.count(i)*int(i)

print(sum)
    