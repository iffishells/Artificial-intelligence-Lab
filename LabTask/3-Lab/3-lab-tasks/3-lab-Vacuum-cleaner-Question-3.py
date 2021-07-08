import random as rn
class Environment:
    
    ## There are only four room as simple as 2 by 2 grid
    
    def __init__(self):
        self.locationCondition = {
            "A":'0',
            "B":'0',
            "C":'0',
            "D":'0',
            
        }
        
        self.locationCondition["A"] = rn.randint(0,1)
        self.locationCondition["B"] = rn.randint(0,1)
        self.locationCondition["C"] = rn.randint(0,1)
        self.locationCondition["D"] = rn.randint(0,1)
        
class SimpleReflexVacuumAgent(Environment):
    def __init__(self, Environment):
        print (Environment.locationCondition)
        # Instantiate performance measurement
        score = 100
        dirty = 1
        time  = 5 # in seconed
        unit = 15 # Required energy of cleaner
        # you can use alphabet A or B for randomization, i am using indexes 0 or 1
        # place vacuum at random location

        vacuumLocation = rn.randint(0, 1)

        ## using given table 
        ## there are four block . The block can be dirty and can be cleaned
#         if the block is dirty cleaned it otherwise move left or right


#         --------------------------------------------
#         | A                 |B                      |
#         |                   |                       |
#         |                   |                       |
#         |                   |                       |
#         |--------------------------------------------          
#         |D                  |C                      |
#         |                   |                       |
#         |                   |                       |
#         |                   |                       |
#         |--------------------------------------------
        
    
        ## because condition is at most only two room can dirty
        
        
        ## meausure to performance on the base of actin moves and sucks
#         suck will take 100 points
#         Dirty will take 1 point
#         suck time will take 5 point
#         energy will take 15 point


        lookup_table = {
            ("A","Dirty") : "suck",
            ("B","Dirty") : "suck",
            ("C","Dirty") : "suck",
            ("D","Dirty") : "suck",
            
            ("A","clean") : "right",
            ("B","clean") : "Down",
            ("C","clean") : "left",
            ("D","clean") : "up",
            ## because condition is at most only two room can dirty
            
            (("A","Dirty"), ("B","Dirty")):"suck",
            (("A","Dirty") ,("C","Dirty")):"suck",
            (("A","Dirty") ,("D","Dirty")):"suck",
            (("B","Dirty") ,("C","Dirty")):"suck",
            (("B","Dirty") ,("D","Dirty")):"suck",
            (("C","Dirty"), ("D","Dirty")):"suck",
            
            
            
            
        }
        
        vacuumLocation = rn.randint(0, 1)
        
        ## because vacuum cleaner will always on the first location which is A
        ## and his face on the right its mean they will move in the location D
        
        if vacuumLocation ==0 or vacuumLocation==1:
            
            if lookup_table[("A","Dirty")]=="suck":
                print("Location A is Dirty")
                #because already initilizaed
#                 score +=1
#                 dirty+=1
#                 time+=
#                 unit+=15
#                 Environment.locationCondition["A"]=0
                print("Location A dirty has scuked")
            if lookup_table[("A","clean")]=="right":
                print("Location A is clean")
                score +=1
                print("Moving toward location B")
                
            if lookup_table[("B","Dirty")]=="suck":
                print("Location B is Dirty")
                score +=1
                dirty+=1
                time +=2
                unit +=2
                Environment.locationCondition["B"]=0
                print("Location B has sucked")
            
            if lookup_table[("B","clean")]=="down":
                print("Location B is Clean")
                score +=1

                print("Moving toward Down location C")
                
            if lookup_table[("C","Dirty")]=="suck":
                print("Location C is dirty")
                score +=1
                dirty+=1
                time +=2
                unit +=2
                Environment.locationCondition["C"]=0
                print("Location C has sucked")
                
            
            if lookup_table[("C","clean")]=="left":
                score+=1
                print("Location C is cleaned")
                print("Moving toward left Location D")
                
            if lookup_table[("D","Dirty")]=="suck":
                print("Location D is dirty")
                score +=1
                dirty+=1
                time +=2
                unit +=2
                Environment.locationCondition["D"]=0
                print("Location D has sucked")
                
            
            if lookup_table[("C","clean")]=="up":
                score+=1
                print("Location D is cleaned")
                print("Moving toward up Location A")
                
            if lookup_table[(("A","Dirty"), ("B","Dirty"))]=="suck":
                
                print("Location A and B is Dirty")
                
                 
                Environment.locationCondition["A"]=0
                print("Location A has sucked")
                print("Moving toward right location B")
                
                score +=1
                dirty+=1
                time +=2
                unit +=2
                Environment.locationCondition["B"]=0
                print("Location B has sucked")
            if lookup_table[(("A","Dirty"), ("C","Dirty"))]=="suck":
                
                print("Location A and C is Dirty")
                
                 
                Environment.locationCondition["A"]=0
                print("Location A has sucked")
                score+=1
                print("Moving toward right location B")
                score+=1
                print("location B is clean")
                score+=1
                print("Moving toward Down C")
                
                print("location C is dirty")
                dirty+=1
                time +=2
                unit +=2
                Environment.locationCondition["C"]==0
                print("Location C has sucked")
                
            if lookup_table[(("A","Dirty"), ("D","Dirty"))]=="suck":
                
                print("Location A and D is Dirty")
                
                 
                Environment.locationCondition["A"]=0
                print("Location A has sucked")
                
                score+=1
                print("Moving toward right location B")
                
                print("location B is clean")
                
                score+=1
                print("Moving toward Down C")
                
                print("location C is clean")
                
                score+=1 
                print("moving toward left location D")
                
                print("location D is dirty")
                dirty+=1
                time +=2
                unit +=2
                Environment.locationCondition["D"]==0
                print("Location D has sucked")
                
            
            if lookup_table[(("B","Dirty"), ("C","Dirty"))]=="suck":
                
                print("Location B and C is Dirty")
                
                print("Location A is clean")
                
                score+=1 
                print("Moving toward right location B")
                
                print("location B is dirty")
                dirty+=1
                time+=2
                unit+=2
                Environment.locationCondition["B"]=0
                print("Location B is cleaned")
                 
                score+=1
                print("Moving toward Down location B")
                
                print("Location C is dirty")
                dirty+=1
                time+=2
                unit+=2
                Environment.locationCondition["C"]=0
                print("Location C is cleaned")
                
            if lookup_table[(("B","Dirty"), ("D","Dirty"))]=="suck":
                
                print("Location B and D is Dirty")
                
                print("Location A is clean")
                
                score+=1 
                print("Moving toward right location B")
                
                print("location B is dirty")
                dirty+=1
                time+=2
                unit+=2
                Environment.locationCondition["B"]=0
                print("Location B is cleaned")
                 
                score+=1
                print("Moving toward Down location C")
                
                print("Location C is clean")
                
                score+=1 
                print("Moving toward right location D")
                print("Location D is dirty")
                dirty+=1
                time+=2
                unit+=2
                Environment.locationCondition["D"]=0
                print("Location D is cleaned")
            if lookup_table[(("C","Dirty"), ("D","Dirty"))]=="suck":
                
                print("Location C and D is Dirty")
                
                print("Location A is clean")
                
                score+=1 
                print("Moving toward right location B")
                
                print("Location B is clean")
                
                score+=1
                print("Moving toward down location C")
                
                
                
                print("location C is dirty")
                dirty+=1
                time+=2
                unit+=2
                Environment.locationCondition["C"]=0
                print("Location C is cleaned")
                
                

                print("Moving toward right location D")
                print("Location D is dirty")
                dirty+=1
                time+=2
                unit+=2
                Environment.locationCondition["D"]=0
                print("Location D is cleaned")
            
                
                
            
        print (Environment.locationCondition)
        print ("Performance Measurement(score): " + str(score))
        print ("Performance Measurement(dirty): " + str(dirty))
        print ("Performance Measurement(energy): " + str(unit) + "Kw/h")
        print ("Performance Measurement(time): " + str(score)+"Sec")

theEnvironment = Environment()
theVacuum = SimpleReflexVacuumAgent(theEnvironment)
                
        
        