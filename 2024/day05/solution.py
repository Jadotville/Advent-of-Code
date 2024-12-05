with open("input.txt", "r") as file:
    content = file.readlines()
    
    
def processa(content):
    rules = []
    updates = []
    for line in content:
        if line.strip() == "":
            updates = [[int(num) for num in line.strip().split(",")] for line in content[content.index(line) + 1:]]
            break
        rules.append([int(num) for num in line.strip().split("|") ])
    
    # print(rules)
    # print(updates)  
      
    sum = 0    
    
    for update in updates:
        # print(update)
        order = True
        for rule in rules:
            if rule[0] in update and rule[1] in update and update.index(rule[0]) > update.index(rule[1]):
                order = False
                break
        if order:
            # print("Order")
            # print(update[len(update) // 2])
            sum += update[len(update) // 2]
    return sum    
    
    
def processb(content):
    rules = []
    updates = []
    for line in content:
        if line.strip() == "":
            updates = [[int(num) for num in line.strip().split(",")] for line in content[content.index(line) + 1:]]
            break
        rules.append([int(num) for num in line.strip().split("|") ])
    
    # print(rules)
    # print(updates)  
      
    sum = 0    
    
    for update in updates:
        # print(update)
        order = True
        used_rules = []
        for rule in rules:
            if rule[0] in update and rule[1] in update:
                used_rules.append(rule)
                if update.index(rule[0]) > update.index(rule[1]):
                    order = False
                    # break
        if not order:
            # print("Order")
            print(update)
            # print(update[len(update) // 2])
            # print(used_rules)
            
            weird_sort(used_rules, update)
            print(used_rules)
            print(update)
            
            sum += update[len(update) // 2]
    return sum  


def weird_sort(used_rules, update):
    order = False
    while not order:
        
        for i in range(len(update)):
            for j in range(i+1, len(update)):
                if [update[j],update[i]] in used_rules:
                    update[j], update[i] = update[i], update[j]
        order = True
        for rule in used_rules:
            if rule[0] in update and rule[1] in update and update.index(rule[0]) > update.index(rule[1]):
                order = False
                break
        
        
        
        
        
        
        

# def weird_bubble_sort(used_rules, update):
#     # print(used_rules)

#     n = len(update)
#     for i in range(n):
#         for j in range(n-i-1):
#             if [update[j+1],update[j]] in used_rules:
#                 update[j], update[j+1] = update[j+1], update[j]
    
#     print(update)

# def weird_bubble_sort(used_rules, update):
#     for i in update:
#         for j in update:
#             if i == j:
#                 continue
#             if [i,j] in used_rules:
#                 update[update.index(i)], update[update.index(j)] = update[update.index(j)], update[update.index(i)]
    
#     order = True
#     for rule in used_rules:
#         if rule[0] in update and rule[1] in update and update.index(rule[0]) > update.index(rule[1]):
#             order = False
#             break
    
#     if order:
#         return update
#     else:
#         return weird_bubble_sort(used_rules, update)
        
print(processb(content))
