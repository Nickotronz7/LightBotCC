PLAIN = 0
LEVEL_1 = 1
LEVEL_2 = 2
WALL = 3
LIGHT = 4

WALK=0
RIGHT=1
LEFT=2

NUM_LIGHTS=2 #Número de luces por encender

maze = [
    [0,3,3,3,3,3,3,3],
    [0,0,4,0,0,3,3,3],
    [3,3,0,0,4,3,3,3],
    [3,3,3,3,3,3,3,3],
    [3,3,3,3,3,3,3,3]]

user_solution=[0,1,0,0,4,0,0,1,0,4]

SIZE = 8
solution = [[0]*SIZE for _ in range(SIZE)] #Ignorar, esto se va luego

#Algoritmo pseudo backtracking
def solvemaze(r, c, solution_i, lights_on, watching_at):
    print(r, c)    
    if(lights_on==NUM_LIGHTS):
        return True
    try:
        if(r<0 or c<0 or r>SIZE or c>SIZE or solution_i>=len(user_solution) or maze[r][c]==WALL):
            return False
    except:
        return False

    solution[r][c] = 9 #Ignorar, es para hacer pruebas
    
    #Validacion para moverse
    if((user_solution[solution_i]==LIGHT)and(maze[r][c]==LIGHT)):
        solvemaze(r, c, solution_i+1, lights_on+1, watching_at)

    if(user_solution[solution_i]==WALK):
        if(watching_at=="DOWN"):
            solvemaze(r+1, c, solution_i+1, lights_on, "DOWN")
        if(watching_at=="RIGHT"):
            solvemaze(r, c+1, solution_i+1, lights_on, "RIGHT")
        if(watching_at=="LEFT"):
            solvemaze(r, c-1, solution_i+1, lights_on, "LEFT")
        if(watching_at=="TOP"):
            solvemaze(r-1, c, solution_i+1, lights_on, "TOP")

    if(user_solution[solution_i]==RIGHT):
        if(watching_at=="RIGHT"):
            solvemaze(r, c, solution_i+1, lights_on, "DOWN")
        elif(watching_at=="LEFT"):
            solvemaze(r, c, solution_i+1, lights_on, "TOP")
        elif(watching_at=="DOWN"):
            solvemaze(r, c, solution_i+1, lights_on, "RIGHT")
        elif(watching_at=="TOP"):
            solvemaze(r, c, solution_i+1, lights_on, "RIGHT")
    if(user_solution[solution_i]==LEFT):
        if(watching_at=="LEFT"):
            solvemaze(r, c, solution_i+1, lights_on, "DOWN")
        elif(watching_at=="RIGHT"):
            solvemaze(r, c, solution_i+1, lights_on, "TOP")
        elif(watching_at=="DOWN"):
            solvemaze(r, c, solution_i+1, lights_on, "LEFT")
        elif(watching_at=="TOP"):
            solvemaze(r, c, solution_i+1, lights_on, "LEFT")
    
    return True


solvemaze(0, 0, 0, 0, "DOWN")
for i in solution:
    print (i)
