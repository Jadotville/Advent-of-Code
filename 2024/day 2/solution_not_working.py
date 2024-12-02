def check_report(report, rec_counter):
    print(report)
    increase = True
    current_report = True
    if len(report) <= 2 and rec_counter == 0:
        return True
    if report[0] < report[1]:
        increase = False
    i = 0
    while current_report and i < len(report) - 1:
        if report[i] < report[i+1] and increase:
            current_report = False
        if report[i] > report[i+1] and not increase:
            current_report = False
        if abs(report[i] - report[i+1]) < 1 or abs(report[i] - report[i+1]) > 3:
            current_report = False
        i += 1
    if i == len(report) - 1 and current_report:
        return True
    if not current_report and rec_counter == 0:
        if check_report(report[:i]+report[i+1:], 1):
            return True
        if check_report(report[:i-1]+report[i:], 1):
            return True
    
    return current_report


with open("input_darius.txt", "r") as file:
    data = []
    for line in file:
        data.append([int(x) for x in line.strip().split(" ")])

sum = 0
for report in data:
    if check_report(report, 0):
        sum += 1

        
        
print(sum)
              
# input: 465
# input_darius.txt: 540  

