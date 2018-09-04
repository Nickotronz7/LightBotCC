class CheckSolution:
    PLAIN = 0
    LEVEL_1 = 1
    LEVEL_2 = 2
    WALL = 3
    LIGHT = 4

    WALK=0
    RIGHT=1
    LEFT=2

    win=False

    NUM_LIGHTS=2 #Número de luces por encender

    maze = [
    [0,3,3,3,3,3,3,3],
    [0,0,4,0,0,3,3,3],
    [3,3,0,0,4,3,3,3],
    [3,3,3,3,3,3,3,3],
    [3,3,3,3,3,3,3,3]]

    SIZE = 8
    solution = [[0]*8 for _ in range(8)] #Ignorar, esto se va luego

    #Algoritmo pseudo backtracking
    def solvemaze(self, r, c, solution_i, lights_on, watching_at, user_solution):
        print(r, c)    
        if(lights_on==self.NUM_LIGHTS):
            self.win=True
            return True
        try:
            if(r<0 or c<0 or r>self.SIZE or c>self.SIZE or solution_i>=len(user_solution) or self.maze[r][c]==self.WALL):
                return False
        except:
            return False

        self.solution[r][c] = 9 #Ignorar, es para hacer pruebas
        
        #Validacion para moverse
        if((user_solution[solution_i]==self.LIGHT)and(self.maze[r][c]==self.LIGHT)):
            self.solvemaze(r, c, solution_i+1, lights_on+1, watching_at, user_solution)

        if(user_solution[solution_i]==self.WALK):
            if(watching_at=="DOWN"):
                self.solvemaze(r+1, c, solution_i+1, lights_on, "DOWN", user_solution)
            if(watching_at=="RIGHT"):
                self.solvemaze(r, c+1, solution_i+1, lights_on, "RIGHT", user_solution)
            if(watching_at=="LEFT"):
                self.solvemaze(r, c-1, solution_i+1, lights_on, "LEFT", user_solution)
            if(watching_at=="TOP"):
                self.solvemaze(r-1, c, solution_i+1, lights_on, "TOP", user_solution)

        if(user_solution[solution_i]==self.RIGHT):
            if(watching_at=="RIGHT"):
                self.solvemaze(r, c, solution_i+1, lights_on, "DOWN", user_solution)
            elif(watching_at=="LEFT"):
                self.solvemaze(r, c, solution_i+1, lights_on, "TOP", user_solution)
            elif(watching_at=="DOWN"):
                self.solvemaze(r, c, solution_i+1, lights_on, "RIGHT", user_solution)
            elif(watching_at=="TOP"):
                self.solvemaze(r, c, solution_i+1, lights_on, "RIGHT", user_solution)
        if(user_solution[solution_i]==self.LEFT):
            if(watching_at=="LEFT"):
                self.solvemaze(r, c, solution_i+1, lights_on, "DOWN", user_solution)
            elif(watching_at=="RIGHT"):
                self.solvemaze(r, c, solution_i+1, lights_on, "TOP", user_solution)
            elif(watching_at=="DOWN"):
                self.solvemaze(r, c, solution_i+1, lights_on, "LEFT", user_solution)
            elif(watching_at=="TOP"):
                self.solvemaze(r, c, solution_i+1, lights_on, "LEFT", user_solution)
        
        return self.win
    
