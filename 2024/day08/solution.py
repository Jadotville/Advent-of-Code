with open("input.txt", "r") as file:
    content = file.readlines()
    content = [list(x.strip()) for x in content]
    
    
def processa(content):
    antennas = {}
    leny = len(content)
    # print(leny)
    lenx = len(content[0])
    # print(lenx)
    
    for y in range(leny):
        for x in range(lenx): 
            if content[y][x] != ".":
                if content[y][x] not in antennas:
                    antennas[content[y][x]] = [[y, x]]
                else:
                    antennas[content[y][x]].append([y, x])
    
    # print(antennas)
    
    antinodes = []
    
    for antenna in antennas:
        # print()
        # print(antenna)
        # print()
        for i in range(len(antennas[antenna])):
            for j in range(i+1, len(antennas[antenna])):
                                
                node1 = antennas[antenna][i]
                node2 = antennas[antenna][j]

                # print(node1, node2)
                
                # if node1[0] <= node2[0]:
                #     y0 = node1[0] - (node2[0]-node1[0])
                #     y1 = node2[0] + (node2[0]-node1[0])  
                #     if node1[1] <= node2[1]:
                #         x0 = node1[1] - (node2[1]-node1[1])
                #         x1 = node2[1] + (node2[1]-node1[1])
                #     else:
                #         x0 = node2[1] + (node1[1]-node2[1])
                #         x1 = node1[1] - (node1[1]-node2[1])  
                # else:
                #     y0 = node2[0] - (node1[0]-node2[0])
                #     y1 = node1[0] + (node1[0]-node2[0])                                        
                #     if node1[1] <= node2[1]:
                #         x0 = node2[1] + (node2[1]-node1[1])
                #         x1 = node1[1] - (node2[1]-node1[1])
                #     else:
                #         x0 = node2[1] - (node1[1]-node2[1])
                #         x1 = node1[1] + (node1[1]-node2[1])                    
                        
                        
                if node1[0] <= node2[0] and node1[1] <= node2[1]:
                    y0 = node1[0] - (node2[0]-node1[0])
                    x0 = node1[1] - (node2[1]-node1[1])
                    y1 = node2[0] + (node2[0]-node1[0])
                    x1 = node2[1] + (node2[1]-node1[1])
                elif node1[0] <= node2[0] and node1[1] > node2[1]:
                    y0 = node1[0] - (node2[0]-node1[0])
                    x0 = node1[1] + (node1[1]-node2[1])
                    y1 = node2[0] + (node2[0]-node1[0])
                    x1 = node2[1] - (node1[1]-node2[1])
                elif node1[0] > node2[0] and node1[1] <= node2[1]:
                    y0 = node2[0] - (node1[0]-node2[0])
                    x0 = node2[1] + (node2[1]-node1[1])
                    y1 = node1[0] + (node1[0]-node2[0])
                    x1 = node1[1] - (node2[1]-node1[1])
                elif node1[0] > node2[0] and node1[1] > node2[1]:
                    y0 = node2[0] - (node1[0]-node2[0])
                    x0 = node2[1] - (node1[1]-node2[1])
                    y1 = node1[0] + (node1[0]-node2[0])
                    x1 = node1[1] + (node1[1]-node2[1])

                    
                        
                new_antinodes = [[y0, x0], [y1, x1]]

                # print(new_antinodes)

                for na in new_antinodes:
                    if na[0] < leny and na[0] >= 0 and na[1] < lenx and na[1] >= 0 and na not in antinodes:
                        antinodes.append(na)



    # print()
    # print(antinodes)

    
    
    return len(antinodes)

def processb(content):
    antennas = {}
    leny = len(content)
    # print(leny)
    lenx = len(content[0])
    # print(lenx)
    
    for y in range(leny):
        for x in range(lenx): 
            if content[y][x] != ".":
                if content[y][x] not in antennas:
                    antennas[content[y][x]] = [[y, x]]
                else:
                    antennas[content[y][x]].append([y, x])
    
    # print(antennas)
    
    antinodes = []
    
    for antenna in antennas:
        # print()
        # print(antenna)
        # print()
        for i in range(len(antennas[antenna])):
            for j in range(i+1, len(antennas[antenna])):
                                
                node1 = antennas[antenna][i]
                node2 = antennas[antenna][j]

                # print(node1, node2)   
                
                dist_vec = [node2[0]-node1[0], node2[1]-node1[1]]        
                
                # print(dist_vec)    
                
                n = node1
                while n[0] < leny and n[0] >= 0 and n[1] < lenx and n[1] >= 0:                        
                    if n not in antinodes:
                        antinodes.append(n)
                    n = [n[0]+dist_vec[0], n[1]+dist_vec[1]]
                
                n = node1
                while n[0] < leny and n[0] >= 0 and n[1] < lenx and n[1] >= 0:                        
                    if n not in antinodes:
                        antinodes.append(n)
                    n = [n[0]-dist_vec[0], n[1]-dist_vec[1]]
                        
                        


                    
                        
                # new_antinodes = [[y0, x0], [y1, x1]]


                # for na in new_antinodes:
                #     if na[0] < leny and na[0] >= 0 and na[1] < lenx and na[1] >= 0 and na not in antinodes:
                #         antinodes.append(na)



    # print()
    # print(antinodes)

    
    
    return len(antinodes)


print(processb(content))