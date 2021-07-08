import random


class Environment():
    def __init__(self):
        # instantiate locations and conditions
        # 0 indicates Clean and 1 indicates Dirty
        self.locationCondition = {'A': '0', 'B': '0'}
        # randomize conditions in locations A and B
        self.locationCondition['A'] = random.randint(0, 1)
        self.locationCondition['B'] = random.randint(0, 1)





class SimpleReflexVacuumAgent(Environment):
    def __init__(self, Environment):
        print (Environment.locationCondition)
        # Instantiate performance measurement
        Score = 0
        # you can use alphabet A or B for randomization, i am using indexes 0 or 1
        # place vacuum at random location

        vacuumLocation = random.randint(0, 1)

        ## using given table 
        ## there are four block . The block can be dirty and can be cleaned
#         if the block is dirty cleaned it otherwise move left or right
        
        
        table_driven = {
            ("A" , "Dirty") : "clean",
            ("A" , "clean") : "left",
            ("B" , "Dirty") : "clean",
            ("B" , "clean") : "right",
            (("A" , "Dirty"),("B" , "Dirty")) : 'clean',
            (("A" , "clean"),("B" , "clean")) : "right",
            (("A" , "clean") , ("B" , "Dirty") ) : "left",
            (("B" , "Dirty"),("A" , "clean")) : "clean"
            
            
        } 
        
        # if vacuum cleaner at location A
        
        if vacuumLocation == 0:
            ## location A 
            print("Vacuum cleaner randomly at location A")
            
            if table_driven[("A" , "Dirty")]=="clean":
                print("Location A is dirty")
                
                # suck the dirt  and mark it clean
                Environment.locationCondition['A'] = 0
                Score += 1
                print ("Location A has been Cleaned.")
            if table_driven[("A" , "clean")]=="left":
                print("Location A is cleaned")
                
                print("move toward left")
                Score -= 1
                
            if table_driven[("B" , "Dirty")]=="clean":
                print("Location B is Dirty")
                
                Environment.locationCondition['B'] = 0
                Score += 1

            if table_driven[("B" , "clean")]=="left":
                print("Location B is cleaned")
                
                print("Move toward right")
                Score -= 1
                
            if table_driven[(("A" , "Dirty"),("B" , "Dirty"))]=="clean":
                print("Location A is dirty")
                print("location B is dirty")
                # suck the dirt  and mark it clean
                Environment.locationCondition['A'] = 0
                Score += 1
            if table_driven[(("A" , "clean") , ("B" , "Dirty") )]=="left":
                print("Location A is clean")
                print("Location B is dirty")
                
                print("Move to left")
                Score -= 1
                
            if table_driven[("B" , "Dirty")]=="clean":
                print("Location B is Dirty")
                
                Environment.locationCondition['B'] = 0
                Score += 1
                
                print("location B is cleaned Now!")
                
        elif (vacuumLocation==0):
            print("Vacuum cleaner location randomly at B")
            
            if table_driven[("B" , "Dirty")]=="clean":
                print("Location A is dirty")
                
                # suck the dirt  and mark it clean
                Environment.locationCondition['B'] = 0
                Score += 1
                print ("Location A has been Cleaned.")
            if table_driven[("B" , "clean")]=="right":
                print("Location B is cleaned")
                
                print("move toward right")
                Score -= 1
                
            if table_driven[("A" , "Dirty")]=="clean":
                print("Location A is Dirty")
                
                Environment.locationCondition['A'] = 0
                Score += 1

            if table_driven[("A" , "clean")]=="right":
                print("Location A is cleaned")
                
                print("Move toward right")
                Score -= 1
                
            if table_driven[(("B" , "Dirty"),("A" , "Dirty"))]=="clean":
                print("Location B is dirty")
                print("location A is dirty")
                # suck the dirt  and mark it clean
                Environment.locationCondition['B'] = 0
                Score += 1
            if table_driven[(("B" , "clean") , ("A" , "Dirty") )]=="right":
                print("Location B is clean")
                print("Location A is dirty")
                
                print("Move to left")
                Score -= 1
                
            if table_driven[("A" , "Dirty")]=="clean":
                print("Location A is Dirty")
                
                Environment.locationCondition['B'] = 0
                Score += 1
                
                print("location A is cleaned Now!")
            
            
                
                
        
        
        print (Environment.locationCondition)
        print ("Performance Measurement: " + str(Score))


theEnvironment = Environment()
theVacuum = SimpleReflexVacuumAgent(theEnvironment)


table_driven = {
            ("A" , "Dirty") : "clean",
            ("A" , "clean") : "left",
            ("B" , "Dirty") : "clean",
            ("A" , "clean") : "right",
            
}
print(table_driven[ ("A" , "Dirty")])