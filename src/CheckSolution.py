##################################
#Valida la jugada y retorna los movimientos
#que se dibujarán en la matriz física
##################################

class CheckSolution:
    PLAIN = 0
    LEVEL_1 = 1
    LEVEL_2 = 2
    LEVEL_3 = 3
    LIGHT = 4
    WALL = 8

    WALK=0
    RIGHT=1
    LEFT=2
    JUMP=3

    win=False
    user_level=0
    solution_i_aux=0

    NUM_LIGHTS=0 #Número de luces por encender

    maze = []

    SIZE = 8
    solution = [[0]*8 for _ in range(8)] #Ignorar, esto se va luego

    def reset_parameters(self):
        self.win=False
        self.user_level=0
        self.solution_i_aux=0
        
    #Algoritmo backtracking para validar la jugada
    def solvemaze(self, r, c, solution_i, lights_on, watching_at, user_solution):
        #print(r, c)
        #print("Luces encendidas: ", lights_on)

        self.solution_i_aux=solution_i
        if(lights_on==self.NUM_LIGHTS):
            self.win=True
            return user_solution[0:self.solution_i_aux]
        try:
            if(r<0 or c<0 or r>self.SIZE or c>self.SIZE or solution_i>=len(user_solution) or self.maze[r][c]==self.WALL
                or ((self.maze[r][c]==self.PLAIN) and (self.user_level==self.LEVEL_2 or self.user_level==self.LEVEL_3)) 
                or ((self.maze[r][c]==self.LEVEL_2 or self.maze[r][c]==self.LEVEL_3) and self.user_level==self.PLAIN)
                or (self.maze[r][c]==self.LEVEL_3 and self.user_level==self.LEVEL_1)):
                self.win=False

                return user_solution[0:self.solution_i_aux]
        except Exception as e:
            print(e)
            self.win=False
            return user_solution[0:self.solution_i_aux]

        
        if(self.maze[r][c]==self.LIGHT):
            self.user_level=self.PLAIN
        else:
            self.user_level=int(str(self.maze[r][c])[0])

        self.solution[r][c] = 9 #Ignorar, es para hacer pruebas
        
        #Validacion para moverse
        if((user_solution[solution_i]==self.LIGHT)and((self.maze[r][c]%10)==4)and(not self.light_on)):
            self.light_on=True
            self.solvemaze(r, c, solution_i+1, lights_on+1, watching_at, user_solution)

        self.light_on=False

        if(user_solution[solution_i]==self.WALK):
            if(watching_at=="DOWN"):
                if((int(str(self.maze[r+1][c])[0])>self.user_level) and (int(str(self.maze[r+1][c])[0])!=4)):
                    return user_solution[0:self.solution_i_aux];
                self.solvemaze(r+1, c, solution_i+1, lights_on, "DOWN", user_solution)
            if(watching_at=="RIGHT"):
                if((int(str(self.maze[r][c+1])[0])>self.user_level) and (int(str(self.maze[r][c+1])[0])!=4)):
                    return user_solution[0:self.solution_i_aux];
                self.solvemaze(r, c+1, solution_i+1, lights_on, "RIGHT", user_solution)
            if(watching_at=="LEFT"):
                if((int(str(self.maze[r][c-1])[0])>self.user_level) and (int(str(self.maze[r][c-1])[0])!=4)):
                    return user_solution[0:self.solution_i_aux];
                self.solvemaze(r, c-1, solution_i+1, lights_on, "LEFT", user_solution)
            if(watching_at=="TOP"):
                if((int(str(self.maze[r-1][c])[0])>self.user_level) and (int(str(self.maze[r-1][c])[0])!=4)):
                    return user_solution[0:self.solution_i_aux];
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

        if(user_solution[solution_i]==self.JUMP):
            if(watching_at=="DOWN"):
                if((int(str(self.maze[r+1][c])[0])-self.user_level)>1):
                    return user_solution[0:self.solution_i_aux];
                self.solvemaze(r+1, c, solution_i+1, lights_on, "DOWN", user_solution)
            if(watching_at=="RIGHT"):
                if((int(str(self.maze[r][c+1])[0])-self.user_level)>1):
                    return user_solution[0:self.solution_i_aux];
                self.solvemaze(r, c+1, solution_i+1, lights_on, "RIGHT", user_solution)
            if(watching_at=="LEFT"):
                if((int(str(self.maze[r][c-1])[0])-self.user_level)>1):
                    return user_solution[0:self.solution_i_aux];
                self.solvemaze(r, c-1, solution_i+1, lights_on, "LEFT", user_solution)
            if(watching_at=="TOP"):
                if((int(str(self.maze[r-1][c])[0])-self.user_level)>1):
                    return user_solution[0:self.solution_i_aux];
                self.solvemaze(r-1, c, solution_i+1, lights_on, "TOP", user_solution)
        
        return user_solution[0:self.solution_i_aux]
    
#user_solution=[3,1,0,4,1,0,3,0]
#test=CheckSolution()

#print(test.solvemaze(0,0,0,0,"DOWN",user_solution))

#for var in test.solution:
#    print(var)
