with open("input2.txt", "r") as file:
    content = file.readlines()
    
    
def processa(content):
    grid = []
    for line in content:
        grid.append(list(line.strip()))
        for i in range(len(grid[-1])):
            if grid[-1][i] == "^":
                start = {"x": i, "y": len(grid) - 1}
        
    while True:
        if grid[start["y"]][start["x"]] == "^":
            if start["y"] == 0:
                grid[start["y"]][start["x"]] = "X"
                break
            
            if grid[start["y"] - 1][start["x"]] == "#":
                grid[start["y"]][start["x"]] = ">"
                continue
            
            if grid[start["y"] - 1][start["x"]] == "." or grid[start["y"] - 1][start["x"]] == "X":    
                grid[start["y"]][start["x"]] = "X"
                start["y"] -= 1
                grid[start["y"]][start["x"]] = "^"
                continue
            
        if grid[start["y"]][start["x"]] == ">":
            if start["x"] == len(grid[0]) - 1:
                grid[start["y"]][start["x"]] = "X"
                break
            
            if grid[start["y"]][start["x"] + 1] == "#":
                grid[start["y"]][start["x"]] = "v"
                continue
            
            if grid[start["y"]][start["x"] + 1] == "." or grid[start["y"]][start["x"] + 1] == "X":    
                grid[start["y"]][start["x"]] = "X"
                start["x"] += 1
                grid[start["y"]][start["x"]] = ">"
                continue
        
        if grid[start["y"]][start["x"]] == "v":
            if start["y"] == len(grid) - 1:
                grid[start["y"]][start["x"]] = "X"
                break
            
            if grid[start["y"] + 1][start["x"]] == "#":
                grid[start["y"]][start["x"]] = "<"
                continue
            
            if grid[start["y"] + 1][start["x"]] == "." or grid[start["y"] + 1][start["x"]] == "X":    
                grid[start["y"]][start["x"]] = "X"
                start["y"] += 1
                grid[start["y"]][start["x"]] = "v"
                continue
        
        if grid[start["y"]][start["x"]] == "<":
            if start["x"] == 0:
                grid[start["y"]][start["x"]] = "X"
                break
            
            if grid[start["y"]][start["x"] - 1] == "#":
                grid[start["y"]][start["x"]] = "^"
                continue
            
            if grid[start["y"]][start["x"] - 1] == "." or grid[start["y"]][start["x"] - 1] == "X":    
                grid[start["y"]][start["x"]] = "X"
                start["x"] -= 1
                grid[start["y"]][start["x"]] = "<"
                continue
    
    x_count = sum(row.count("X") for row in grid)
    
    return x_count



def processb(content):
    grid = []
    for line in content:
        grid.append(list(line.strip()))
        for i in range(len(grid[-1])):
            if grid[-1][i] == "^":
                start = {"x": i, "y": len(grid) - 1}
    
    sum = 0
    
    i = 0
    j = 0
    while True:
        # print(i)
        i+=1
        # p = False
        # if i == 129:
        #     p = True
        #     check_obstacle(grid, start, p)
        if check_obstacle(grid, start):
            sum += 1
        
        if grid[start["y"]][start["x"]] == "^":
            if start["y"] == 0:
                grid[start["y"]][start["x"]] = "^"
                break
            
            if grid[start["y"] - 1][start["x"]] == "#":
                grid[start["y"]][start["x"]] = ">"
                j+=1
                continue
            
            else:    
                start["y"] -= 1
                grid[start["y"]][start["x"]] = "^"
                continue
            
        if grid[start["y"]][start["x"]] == ">":
            if start["x"] == len(grid[0]) - 1:
                grid[start["y"]][start["x"]] = ">"
                break
            
            if grid[start["y"]][start["x"] + 1] == "#":
                grid[start["y"]][start["x"]] = "v"
                j+=1
                continue
            
            else:
                start["x"] += 1
                grid[start["y"]][start["x"]] = ">"
                continue
        
        if grid[start["y"]][start["x"]] == "v":
            if start["y"] == len(grid) - 1:
                grid[start["y"]][start["x"]] = "v"
                break
            
            if grid[start["y"] + 1][start["x"]] == "#":
                grid[start["y"]][start["x"]] = "<"
                j+=1
                continue
            
            else:   
                start["y"] += 1
                grid[start["y"]][start["x"]] = "v"
                continue
        
        if grid[start["y"]][start["x"]] == "<":
            if start["x"] == 0:
                grid[start["y"]][start["x"]] = "<"
                break
            
            if grid[start["y"]][start["x"] - 1] == "#":
                grid[start["y"]][start["x"]] = "^"
                j+=1
                continue
            
            else:    
                start["x"] -= 1
                grid[start["y"]][start["x"]] = "<"
                continue
    
    print(i)
    print(j) 
    return sum

def check_obstacle(grid, start, p=False):
    
    grid_copy = [row.copy() for row in grid]
    pos = {"x": start["x"], "y": start["y"]}
    
    current_direction = grid_copy[pos["y"]][pos["x"]]
    
    if current_direction == "^":
        if pos["y"] == 0:
            return False
        if grid_copy[pos["y"] - 1][pos["x"]] == "#":
            return False
        grid_copy[pos["y"] - 1][pos["x"]] = "#"
        current_direction = ">"
    
    elif current_direction == ">":
        if pos["x"] == len(grid_copy[0]) - 1:
            return False
        if grid_copy[pos["y"]][pos["x"] + 1] == "#":
            return False
        grid_copy[pos["y"]][pos["x"] + 1] = "#"
        current_direction = "v"
    
    elif current_direction == "v":
        if pos["y"] == len(grid_copy) - 1:
            return False
        if grid_copy[pos["y"] + 1][pos["x"]] == "#":
            return False
        grid_copy[pos["y"] + 1][pos["x"]] = "#"
        current_direction = "<"
        
    else:
        if pos["x"] == 0:
            return False
        if grid_copy[pos["y"]][pos["x"] - 1] == "#":
            return False
        grid_copy[pos["y"]][pos["x"] - 1] = "#"
        current_direction = "^"
    
    positions = []
    positions.append([pos["x"], pos["y"], current_direction])
    
    
    j=0
    while True:
        if p:
            print(positions)
        # if j > 10000:
        #     return False
        j+=1
        
        
        if current_direction == "^":
            if pos["y"] == 0:
                return False
            if p:
                print("up")
            if grid_copy[pos["y"] - 1][pos["x"]] == "#":
                current_direction = ">"
            else:
                pos["y"] -= 1

        elif current_direction == ">":
            if pos["x"] == len(grid_copy[0]) - 1:
                return False
            
            if grid_copy[pos["y"]][pos["x"] + 1] == "#":
                current_direction = "v"
            else:
                pos["x"] += 1
                
        elif current_direction == "v":
            if pos["y"] == len(grid_copy) - 1:
                return False
            
            if grid_copy[pos["y"] + 1][pos["x"]] == "#":
                current_direction = "<"
            else:   
                pos["y"] += 1
        
        else:
            if pos["x"] == 0:
                return False
            
            if grid_copy[pos["y"]][pos["x"] - 1] == "#":
                current_direction = "^"
            else:
                pos["x"] -= 1
    
        
        if [pos["x"], pos["y"], current_direction] in positions:
            return True
        else:   
            positions.append([pos["x"], pos["y"], current_direction])
        
        
    


def processc(content):
    grid = []
    for line in content:
        grid.append(list(line.strip()))
        for i in range(len(grid[-1])):
            if grid[-1][i] == "^":
                start = {"x": i, "y": len(grid) - 1}
    
    sum = 0
    
    i=0
    while True:
        i+=1
        print(i)
        if check(grid, start):
            sum += 1
            
            

            
        if grid[start["y"]][start["x"]] == "^":
            if start["y"] == 0:
                grid[start["y"]][start["x"]] = "X"
                break
            
            if grid[start["y"] - 1][start["x"]] == "#":
                grid[start["y"]][start["x"]] = ">"
                continue
            
            if grid[start["y"] - 1][start["x"]] == "." or grid[start["y"] - 1][start["x"]] == "X":    
                grid[start["y"]][start["x"]] = "X"
                start["y"] -= 1
                grid[start["y"]][start["x"]] = "^"
                continue
            
        if grid[start["y"]][start["x"]] == ">":
            if start["x"] == len(grid[0]) - 1:
                grid[start["y"]][start["x"]] = "X"
                break
            
            if grid[start["y"]][start["x"] + 1] == "#":
                grid[start["y"]][start["x"]] = "v"
                continue
            
            if grid[start["y"]][start["x"] + 1] == "." or grid[start["y"]][start["x"] + 1] == "X":    
                grid[start["y"]][start["x"]] = "X"
                start["x"] += 1
                grid[start["y"]][start["x"]] = ">"
                continue
        
        if grid[start["y"]][start["x"]] == "v":
            if start["y"] == len(grid) - 1:
                grid[start["y"]][start["x"]] = "X"
                break
            
            if grid[start["y"] + 1][start["x"]] == "#":
                grid[start["y"]][start["x"]] = "<"
                continue
            
            if grid[start["y"] + 1][start["x"]] == "." or grid[start["y"] + 1][start["x"]] == "X":    
                grid[start["y"]][start["x"]] = "X"
                start["y"] += 1
                grid[start["y"]][start["x"]] = "v"
                continue
        
        if grid[start["y"]][start["x"]] == "<":
            if start["x"] == 0:
                grid[start["y"]][start["x"]] = "X"
                break
            
            if grid[start["y"]][start["x"] - 1] == "#":
                grid[start["y"]][start["x"]] = "^"
                continue
            
            if grid[start["y"]][start["x"] - 1] == "." or grid[start["y"]][start["x"] - 1] == "X":    
                grid[start["y"]][start["x"]] = "X"
                start["x"] -= 1
                grid[start["y"]][start["x"]] = "<"
                continue
        
    return sum
    

def check(grid, start):
    grid_copy = [row.copy() for row in grid]
    pos = {"x": start["x"], "y": start["y"]}
    direction = grid_copy[pos["y"]][pos["x"]]
    positions = []
    
    
    
    if direction == "^":
        if pos["y"] == 0:
            return False
        if grid_copy[pos["y"] - 1][pos["x"]] == "#":
            return False
        grid_copy[pos["y"] - 1][pos["x"]] = "#"
        positions.append([pos["x"], pos["y"], direction])
        direction = ">"
    
    elif direction == ">":
        if pos["x"] == len(grid_copy[0]) - 1:
            return False
        if grid_copy[pos["y"]][pos["x"] + 1] == "#":
            return False
        grid_copy[pos["y"]][pos["x"] + 1] = "#"
        positions.append([pos["x"], pos["y"], direction])
        direction = "v"
    
    elif direction == "v":
        if pos["y"] == len(grid_copy) - 1:
            return False
        if grid_copy[pos["y"] + 1][pos["x"]] == "#":
            return False
        grid_copy[pos["y"] + 1][pos["x"]] = "#"
        positions.append([pos["x"], pos["y"], direction])
        direction = "<"
    
    elif direction == "<":
        if pos["x"] == 0:
            return False
        if grid_copy[pos["y"]][pos["x"] - 1] == "#":
            return False
        grid_copy[pos["y"]][pos["x"] - 1] = "#"
        positions.append([pos["x"], pos["y"], direction])
        direction = "^"

    while True:

        if direction == "^":
            if pos["y"] == 0:
                return False
            elif grid_copy[pos["y"] - 1][pos["x"]] == "#":
                direction = ">"
            else:   
                pos["y"] -= 1
            
        elif direction == ">":
            if pos["x"] == len(grid_copy[0]) - 1:
                return False
            elif grid_copy[pos["y"]][pos["x"] + 1] == "#":
                direction = "v"
            else:   
                pos["x"] += 1
        
        elif direction == "v":
            if pos["y"] == len(grid_copy) - 1:
                return False
            elif grid_copy[pos["y"] + 1][pos["x"]] == "#":
                direction = "<"
            else:   
                pos["y"] += 1
        
        elif direction == "<":
            if pos["x"] == 0:
                return False
            elif grid_copy[pos["y"]][pos["x"] - 1] == "#":
                direction = "^"
            else:   
                pos["x"] -= 1

        if [pos["x"], pos["y"], direction] in positions:
            return True
         
        positions.append([pos["x"], pos["y"], direction])
        
        
    
    
    

# print(processb(content))

print(processc(content))


#     sum = 0
#     while True:
        
#         if check_obstacle(grid, start):
#             sum += 1

        
#         if grid[start["y"]][start["x"]] == "^":
#             if start["y"] == 0:
#                 break
            
#             if grid[start["y"] - 1][start["x"]] == "#":
#                 grid[start["y"]][start["x"]] = ">"
#                 continue
            
#             else:
#                 start["y"] -= 1
#                 grid[start["y"]][start["x"]] = "^"
#                 continue
            
#         if grid[start["y"]][start["x"]] == ">":
#             if start["x"] == len(grid[0]) - 1:
#                 break
            
#             if grid[start["y"]][start["x"] + 1] == "#":
#                 grid[start["y"]][start["x"]] = "v"
#                 continue
            
#             else:
#                 start["x"] += 1
#                 grid[start["y"]][start["x"]] = ">"
#                 continue
        
#         if grid[start["y"]][start["x"]] == "v":
#             if start["y"] == len(grid) - 1:
#                 break
            
#             if grid[start["y"] + 1][start["x"]] == "#":
#                 grid[start["y"]][start["x"]] = "<"
#                 continue
            
#             else:
#                 start["y"] += 1
#                 grid[start["y"]][start["x"]] = "v"
#                 continue
        
#         if grid[start["y"]][start["x"]] == "<":
#             if start["x"] == 0:
#                 break
            
#             if grid[start["y"]][start["x"] - 1] == "#":
#                 grid[start["y"]][start["x"]] = "^"
#                 continue
            
#             else:
#                 start["x"] -= 1
#                 grid[start["y"]][start["x"]] = "<"
#                 continue
        
    
#     # print(new_obstacles)
#     return sum
    
# def check_obstacle(grid, start):
#     grid_copy = [row.copy() for row in grid]
#     pos = {"x": start["x"], "y": start["y"]}
#     start_direction = grid_copy[pos["y"]][pos["x"]]
#     current_direction = start_direction
#     positions = []
#     positions.append([pos["x"], pos["y"], current_direction])

    
#     if current_direction == "^":
#         if pos["y"] == 0:
#             return False
#         if grid_copy[pos["y"] - 1][pos["x"]] == "#":
#             return False
#         grid_copy[pos["y"] - 1][pos["x"]] = "#"
#         current_direction = ">"
    
#     elif current_direction == ">":
#         if pos["x"] == len(grid_copy[0]) - 1:
#             return False
#         if grid_copy[pos["y"]][pos["x"] + 1] == "#":
#             return False
#         grid_copy[pos["y"]][pos["x"] + 1] = "#"
#         current_direction = "v"
        
#     elif current_direction == "v":
#         if pos["y"] == len(grid_copy) - 1:
#             return False
#         if grid_copy[pos["y"] + 1][pos["x"]] == "#":
#             return False
#         grid_copy[pos["y"] + 1][pos["x"]] = "#"
#         current_direction = "<"
    
#     else:
#         if pos["x"] == 0:
#             return False
#         if grid_copy[pos["y"]][pos["x"] - 1] == "#":
#             return False
#         grid_copy[pos["y"]][pos["x"] - 1] = "#"
#         current_direction = "^"
    
    

#     i=0
#     while True:
#         if i > 100000:
#             return False
#         i+=1
        
#         if [pos["x"], pos["y"], current_direction] in positions:
#             return True
        
#         positions.append([pos["x"], pos["y"], current_direction])
        
        
        
        
#         # print(grid_copy)
        
#         if current_direction == start_direction and pos["x"] == start["x"] and pos["y"] == start["y"]:
#             return True 
        
#         if current_direction == "^":
#             if pos["y"] == 0:
#                 return False
            
#             if grid_copy[pos["y"] - 1][pos["x"]] == "#":
#                 current_direction = ">"
#                 continue
            
#             else:
#                 pos["y"] -= 1
#                 continue
        
#         if current_direction == ">":
#             if pos["x"] == len(grid_copy[0]) - 1:
#                 return False
            
#             if grid_copy[pos["y"]][pos["x"] + 1] == "#":
#                 current_direction = "v"
#                 continue
            
#             else:
#                 pos["x"] += 1
#                 continue
            
#         if current_direction == "v":
#             if pos["y"] == len(grid_copy) - 1:
#                 return False
            
#             if grid_copy[pos["y"] + 1][pos["x"]] == "#":
#                 current_direction = "<"
#                 continue
            
#             else:
#                 pos["y"] += 1
#                 continue
            
#         if current_direction == "<":
#             if pos["x"] == 0:
#                 return False
            
#             if grid_copy[pos["y"]][pos["x"] - 1] == "#":
#                 current_direction = "^"
#                 continue
            
#             else:
#                 pos["x"] -= 1
#                 continue
        
        
        
        
        
        


# print(processb(content))

# grid_copy = [row.copy() for row in grid]
#     pos = {"x": start["x"], "y": start["y"]}

        
#     current_direction = grid_copy[pos["y"]][pos["x"]]
    
#     if current_direction == "^":
#         if pos["y"] == 0:
#             return False
#         if grid_copy[pos["y"] - 1][pos["x"]] == "#":
#             return False
#         grid_copy[pos["y"] - 1][pos["x"]] = "#"
#         current_direction = ">"
#     elif current_direction == ">":
#         if pos["x"] == len(grid_copy[0]) - 1:
#             return False
#         if grid_copy[pos["y"]][pos["x"] + 1] == "#":
#             return False
#         grid_copy[pos["y"]][pos["x"] + 1] = "#"
#         current_direction = "v"
#     elif current_direction == "v":
#         if pos["y"] == len(grid_copy) - 1:
#             return False
#         if grid_copy[pos["y"] + 1][pos["x"]] == "#":
#             return False
#         grid_copy[pos["y"] + 1][pos["x"]] = "#"
#         current_direction = "<"
#     else:
#         if pos["x"] == 0:
#             return False
#         if grid_copy[pos["y"]][pos["x"] - 1] == "#":
#             return False
#         grid_copy[pos["y"]][pos["x"] - 1] = "#"
#         current_direction = "^"
#     i=0
#     while True:
#         if i > 10000:
#             return False
#         i+=1
#         # print(grid_copy)
#         # print(start)
#         # print(pos)
#         # print(current_direction)
#         # if pos["x"] == start["x"] and pos["y"] == start["y"]:
#         #     print("exit")
        
#         if current_direction == "^":
#             # print("up")
#             if pos["y"] == 0:
#                 return False
            
#             if grid_copy[pos["y"] - 1][pos["x"]] == "#":
#                 current_direction = ">"
#                 continue
                            
#             else:
#                 # print("else")
#                 pos["y"] -= 1
#                 if pos["x"] == start["x"] and pos["y"] == start["y"]:
#                     return True
#                 continue         
          
#         if current_direction == ">":
#             if pos["x"] == len(grid_copy[0]) - 1:
#                 return False
            
#             if grid_copy[pos["y"]][pos["x"] + 1] == "#":
#                 current_direction = "v"
#                 continue
            
#             else:
#                 pos["x"] += 1
#                 if pos["x"] == start["x"] and pos["y"] == start["y"]:
#                     return True
#                 continue
            
#         if current_direction == "v":
#             if pos["y"] == len(grid_copy) - 1:
#                 return False
            
#             if grid_copy[pos["y"] + 1][pos["x"]] == "#":
#                 current_direction = "<"
#                 continue
            
#             else:
#                 pos["y"] += 1
#                 if pos["x"] == start["x"] and pos["y"] == start["y"]:
#                     return True
#                 continue
            
#         if current_direction == "<":
#             if pos["x"] == 0:
#                 return False
            
#             if grid_copy[pos["y"]][pos["x"] - 1] == "#":
#                 current_direction = "^"
#                 continue
            
#             else:
#                 pos["x"] -= 1
#                 if pos["x"] == start["x"] and pos["y"] == start["y"]:
#                     return True
#                 continue
            

# def processb(content):
#     grid = []
#     for line in content:
#         grid.append(list(line.strip()))
#         for i in range(len(grid[-1])):
#             if grid[-1][i] == "^":
#                 start = {"x": i, "y": len(grid) - 1}

#     sum = 0
#     new_obstacles = []
#     while True:
        
#         if check_obstacle(grid, start):
#             # print(grid)
#             # print()
#             sum += 1
#             # if grid[start["y"]][start["x"]] == "^":
#             #     new_obstacles.append({"x": start["x"], "y": start["y"]-1})
#             # elif grid[start["y"]][start["x"]] == ">":
#             #     new_obstacles.append({"x": start["x"]+1, "y": start["y"]})
#             # elif grid[start["y"]][start["x"]] == "v":
#             #     new_obstacles.append({"x": start["x"], "y": start["y"]+1})
#             # else:
#             #     new_obstacles.append({"x": start["x"]-1, "y": start["y"]})
        
#         if grid[start["y"]][start["x"]] == "^":
#             if start["y"] == 0:
#                 break
            
#             if grid[start["y"] - 1][start["x"]] == "#":
#                 grid[start["y"]][start["x"]] = ">"
#                 continue
            
#             else:
#                 start["y"] -= 1
#                 grid[start["y"]][start["x"]] = "^"
#                 continue
            
#         if grid[start["y"]][start["x"]] == ">":
#             if start["x"] == len(grid[0]) - 1:
#                 break
            
#             if grid[start["y"]][start["x"] + 1] == "#":
#                 grid[start["y"]][start["x"]] = "v"
#                 continue
            
#             else:
#                 start["x"] += 1
#                 grid[start["y"]][start["x"]] = ">"
#                 continue
        
#         if grid[start["y"]][start["x"]] == "v":
#             if start["y"] == len(grid) - 1:
#                 break
            
#             if grid[start["y"] + 1][start["x"]] == "#":
#                 grid[start["y"]][start["x"]] = "<"
#                 continue
            
#             else:
#                 start["y"] += 1
#                 grid[start["y"]][start["x"]] = "v"
#                 continue
        
#         if grid[start["y"]][start["x"]] == "<":
#             if start["x"] == 0:
#                 break
            
#             if grid[start["y"]][start["x"] - 1] == "#":
#                 grid[start["y"]][start["x"]] = "^"
#                 continue
            
#             else:
#                 start["x"] -= 1
#                 grid[start["y"]][start["x"]] = "<"
#                 continue
        
    
#     # print(new_obstacles)
#     return sum


    # if current_direction == "^":
    #     if pos["y"] == 0:
    #         return False
    #     if grid_copy[pos["y"] - 1][pos["x"]] == "#":
    #         return False
    #     current_direction = ">"
    # elif current_direction == ">":
    #     if pos["x"] == len(grid_copy[0]) - 1:
    #         return False
    #     if grid_copy[pos["y"]][pos["x"] + 1] == "#":
    #         return False
    #     current_direction = "v"
    # elif current_direction == "v":
    #     if pos["y"] == len(grid_copy) - 1:
    #         return False
    #     if grid_copy[pos["y"] + 1][pos["x"]] == "#":
    #         return False
    #     current_direction = "<"
    # else:
    #     if pos["x"] == 0:
    #         return False
    #     if grid_copy[pos["y"]][pos["x"] - 1] == "#":
    #         return False
    #     current_direction = "^"
    
    # while True:
    #     if current_direction == "^":
    #         if pos["y"] == 0:
    #             return False
            
    #         if grid_copy[pos["y"] - 1][pos["x"]] == "#":
    #             if grid_copy[pos["y"]][pos["x"]] == ">":
    #                 return True
    #             return False
            
    #         else:
    #             pos["y"] -= 1
    #             if grid_copy[pos["y"]][pos["x"]] == "^":
    #                 return True
    #             continue
            
    #     if current_direction == ">":
    #         if pos["x"] == len(grid_copy[0]) - 1:
    #             return False
            
    #         if grid_copy[pos["y"]][pos["x"] + 1] == "#":
    #             if grid_copy[pos["y"]][pos["x"]] == "v":
    #                 return True
    #             return False
            
    #         else:
    #             pos["x"] += 1
    #             if grid_copy[pos["y"]][pos["x"]] == ">":
    #                 return True
    #             continue
            
    #     if current_direction == "v":
    #         if pos["y"] == len(grid_copy) - 1:
    #             return False
            
    #         if grid_copy[pos["y"] + 1][pos["x"]] == "#":
    #             if grid_copy[pos["y"]][pos["x"]] == "<":
    #                 return True
    #             return False
            
    #         else:
    #             pos["y"] += 1
    #             if grid_copy[pos["y"]][pos["x"]] == "v":
    #                 return True
    #             continue
            
    #     if current_direction == "<":
    #         if pos["x"] == 0:
    #             return False
            
    #         if grid_copy[pos["y"]][pos["x"] - 1] == "#":
    #             if grid_copy[pos["y"]][pos["x"]] == "^":
    #                 return True
    #             return False
            
    #         else:
    #             pos["x"] -= 1
    #             if grid_copy[pos["y"]][pos["x"]] == "<":
    #                 return True
    
    # # while True:
    #     if current_direction == "^":
    #         if pos["y"] == 0:
    #             break
            
    #         if grid_copy[pos["y"] - 1][pos["x"]] == ">":
                
            
    #         if grid_copy[pos["y"] - 1][pos["x"]] == "#":
    #             turn_count += 1
    #             current_direction = ">"
    #             continue
            
    #         else:
    #             pos["y"] -= 1
    #             if pos == start:
    #                 return_to_start = True
    #                 break
    #             continue
        
    #     if current_direction == ">":
    #         if pos["x"] == len(grid_copy[0]) - 1:
    #             break
            
    #         if grid_copy[pos["y"]][pos["x"] + 1] == "#":
    #             turn_count += 1
    #             current_direction = "v"
    #             continue
            
    #         else:
    #             pos["x"] += 1
    #             if pos == start:
    #                 return_to_start = True
    #                 break
    #             continue
        
    #     if current_direction == "v":
    #         if pos["y"] == len(grid_copy) - 1:
    #             break
            
    #         if grid_copy[pos["y"] + 1][pos["x"]] == "#":
    #             turn_count += 1
    #             current_direction = "<"
    #             continue
            
    #         else:
    #             pos["y"] += 1
    #             if pos == start:
    #                 return_to_start = True
    #                 break
    #             continue
        
    #     if current_direction == "<":
    #         if pos["x"] == 0:
    #             break
            
    #         if grid_copy[pos["y"]][pos["x"] - 1] == "#":
    #             turn_count += 1
    #             current_direction = "^"
    #             continue
            
    #         else:
    #             pos["x"] -= 1
    #             if pos == start:
    #                 return_to_start = True
    #                 break
    #             continue
          
    # while True:
    #     if current_direction == "^":
    #         if pos["y"] == 0:
    #             return False
            
    #         if grid_copy[pos["y"] - 1][pos["x"]] == "#":
    #             if grid_copy[pos["y"]][pos["x"]] == ">":
    #                 return True
    #             return False
            
    #         else:
    #             pos["y"] -= 1
    #             if grid_copy[pos["y"]][pos["x"]] == "^":
    #                 return True
    #             continue
            
    #     if current_direction == ">":
    #         if pos["x"] == len(grid_copy[0]) - 1:
    #             return False
            
    #         if grid_copy[pos["y"]][pos["x"] + 1] == "#":
    #             if grid_copy[pos["y"]][pos["x"]] == "v":
    #                 return True
    #             return False
            
    #         else:
    #             pos["x"] += 1
    #             if grid_copy[pos["y"]][pos["x"]] == ">":
    #                 return True
    #             continue
            
    #     if current_direction == "v":
    #         if pos["y"] == len(grid_copy) - 1:
    #             return False
            
    #         if grid_copy[pos["y"] + 1][pos["x"]] == "#":
    #             if grid_copy[pos["y"]][pos["x"]] == "<":
    #                 return True
    #             return False
            
    #         else:
    #             pos["y"] += 1
    #             if grid_copy[pos["y"]][pos["x"]] == "v":
    #                 return True
    #             continue
            
    #     if current_direction == "<":
    #         if pos["x"] == 0:
    #             return False
            
    #         if grid_copy[pos["y"]][pos["x"] - 1] == "#":
    #             if grid_copy[pos["y"]][pos["x"]] == "^":
    #                 return True
    #             return False
            
    #         else:
    #             pos["x"] -= 1
    #             if grid_copy[pos["y"]][pos["x"]] == "<":
    #                 return True