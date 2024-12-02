def check_report(report):
    increase = True
    current_report = True
    if report[0] < report[1]:
        increase = False
    i = 0
    while (current_report and i < (len(report) - 1)):
        if report[i] < report[i+1] and increase:
            current_report = False
        if report[i] > report[i+1] and not increase:
            current_report = False
        if abs(report[i] - report[i+1]) == 0 or abs(report[i] - report[i+1]) > 3:
            current_report = False
        i += 1    
    return current_report


with open("input.txt", "r") as file:
    data = []
    for line in file:
        data.append([int(x) for x in line.strip().split(" ")])

sum = 0

for report in data: 
    if len(report) <= 2:
        sum += 1
    else:
        print(report)
        for i in range(len(report)):
            report_cut = report[:i] + report[i+1:]
            print(report_cut)
            if check_report(report_cut):
                sum += 1
                break
            

        
        
print(sum)
                

