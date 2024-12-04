with open("input.txt", "r") as file:
    content = file.readlines()
    
    
def processa(content):
    xmas_count = 0
    grid = [list(line.strip()) for line in content]
    
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == "X":
                if x+3 < len(grid[y]) and grid[y][x+1] == "M" and grid[y][x+2] == "A" and grid[y][x+3] == "S":
                    xmas_count += 1
                if x-3 >= 0 and grid[y][x-1] == "M" and grid[y][x-2] == "A" and grid[y][x-3] == "S":
                    xmas_count += 1
                if y+3 < len(grid) and grid[y+1][x] == "M" and grid[y+2][x] == "A" and grid[y+3][x] == "S":
                    xmas_count += 1
                if y-3 >= 0 and grid[y-1][x] == "M" and grid[y-2][x] == "A" and grid[y-3][x] == "S":
                    xmas_count += 1
                if x+3 < len(grid[y]) and y+3 < len(grid) and grid[y+1][x+1] == "M" and grid[y+2][x+2] == "A" and grid[y+3][x+3] == "S":
                    xmas_count += 1
                if x-3 >= 0 and y-3 >= 0 and grid[y-1][x-1] == "M" and grid[y-2][x-2] == "A" and grid[y-3][x-3] == "S":
                    xmas_count += 1
                if x-3 >= 0 and y+3 < len(grid) and grid[y+1][x-1] == "M" and grid[y+2][x-2] == "A" and grid[y+3][x-3] == "S":
                    xmas_count += 1
                if x+3 < len(grid[y]) and y-3 >= 0 and grid[y-1][x+1] == "M" and grid[y-2][x+2] == "A" and grid[y-3][x+3] == "S":
                    xmas_count += 1                 
    
    return xmas_count

def processb(content):
    mas_count = 0
    grid = [list(line.strip()) for line in content]
    
    for y in range(1,len(grid)-1):
        for x in range(1, len(grid[y])-1):
            if grid[y][x] == "A":
                if grid[y-1][x-1] == "M" and grid[y+1][x+1] == "S":
                    if grid[y-1][x+1] == "M" and grid[y+1][x-1] == "S":
                        mas_count += 1
                    if grid[y-1][x+1] == "S" and grid[y+1][x-1] == "M":
                        mas_count += 1
                if grid[y-1][x-1] == "S" and grid[y+1][x+1] == "M":
                    if grid[y-1][x+1] == "M" and grid[y+1][x-1] == "S":
                        mas_count += 1
                    if grid[y-1][x+1] == "S" and grid[y+1][x-1] == "M":
                        mas_count += 1
    
    return mas_count


print(processb(content))