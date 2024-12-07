import itertools

with open("input.txt", "r") as file:
    content = file.readlines()    
    content = [x.strip().split(" ") for x in content]
    content = [[int(x[0].strip(":"))] + [int(num) for num in x[1:]] for x in content]
    
    
def processa(content):
    sum = 0
    for equation in content:
        if possible_combination_a(equation):
            sum += equation[0]    
    return sum

def processb(content):
    sum = 0
    for equation in content:
        if possible_combination_b(equation):
            sum += equation[0]    
    return sum

def possible_combination_b(equation):
    length = len(equation)
    operator_combinations=list(itertools.product(["+", "*", "||"], repeat=length-2))
    # print(equation)
    for operator_combination in operator_combinations:
        # print(operator_combination)
        result = equation[1]
        # print(result)
        for i in range(length-2):
            num = equation[i+2]
            # print(num)
            if operator_combination[i] == "||":
                result = int(str(result) + str(num))
            elif operator_combination[i] == "+":
                result = result + num
            else: 
                result = result * num
            # print(result)
        if result == equation[0]:
            return True
            
    return False

def possible_combination_a(equation):    
    length = len(equation)
    operator_combinations=list(itertools.product(["+", "*"], repeat=length-2))
    # print(equation)
    for operator_combination in operator_combinations:
        # print(operator_combination)
        result = equation[1]
        # print(result)
        for i in range(length-2):
            num = equation[i+2]
            # print(num)
            result = result * num if operator_combination[i] == "*" else result + num
            # print(result)
        if result == equation[0]:
            return True
            
    return False


print(processb(content))