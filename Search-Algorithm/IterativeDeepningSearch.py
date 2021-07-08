class Probelm:
    '''
    arg:
     class take probelm in the from of Map(dict) and initial Node
     and Goal Node
    '''
    def __init__(self,Dict_Graph,initial_Node , goal_node ):
        self.graph = Dict_Graph or {}
        self.initial_Node = initial_Node
        self.goal_node = goal_node
        
        
        
#         self.expend("Bucharest")
        # print(self.interative_Deeping_search(6))
    
    def expendChild(self,CurrentNode):
        
        child_list = []
        for node in self.graph[CurrentNode].keys():
            child_list.append(node)
            
        return child_list

    
    def dfs(self,node,limit):
    '''
    arg : 
    node : its node which is update every call mean current node
    limit : limit of depth
    '''    
        if node == self.goal_node:
            return True
        
        if limit<=0:
            return False
        
        ## explore the value of the key and check the limit of every iteration
        else:
            print("parent node : ",node)
            print("Chdilrend : ",self.graph[node].keys())
            for node in self.graph[node].keys():
                print("Node --> ",node)
                if (self.dfs(node , limit-1)):
                    return True
            return False
    
    def interative_Deeping_search(self, depth_limit):
        
        for path_limit in range(0,depth_limit):
            print("Depth limit is  : ",path_limit)
            if  (self.dfs(self.initial_Node, depth_limit)) ==True:
                return "Reached Goal State"
        
        return  "Not found"
        
            
            
romania_map = Probelm(dict( {'Arad': {'Zerind': 75, 'Sibiu': 140, 'Timisoara': 118},
                           
             'Bucharest': {'Urziceni': 85, 'Pitesti': 101, 'Giurgiu': 90, 'Fagaras': 211}, 
                           
             'Craiova': {'Drobeta': 120, 'Rimnicu': 146, 'Pitesti': 138}, 
                           
             'Drobeta': {'Mehadia': 75, 'Craiova': 120}, 
                           
             'Eforie': {'Hirsova': 86}, 
                           
             'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
                           
             'Hirsova': {'Urziceni': 98, 'Eforie': 86},
                           
             'Iasi': {'Vaslui': 92, 'Neamt': 87},
                           
             'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
                           
             'Oradea': {'Zerind': 71, 'Sibiu': 151},
                           
             'Pitesti': {'Rimnicu': 97, 'Bucharest': 101, 'Craiova': 138},
                           
             'Rimnicu': {'Sibiu': 80, 'Craiova': 146, 'Pitesti': 97},
                           
             'Urziceni': {'Vaslui': 142, 'Bucharest': 85, 'Hirsova': 98},
                           
             'Zerind': {'Arad': 75, 'Oradea': 71},
                           
             'Sibiu': {'Arad': 140, 'Fagaras': 99, 'Oradea': 151, 'Rimnicu': 80},
                           
             'Timisoara': {'Arad': 118, 'Lugoj': 111},
                           
             'Giurgiu': {'Bucharest': 90}, 
                           
             'Mehadia': {'Drobeta': 75, 'Lugoj': 70},
                           
             'Vaslui': {'Iasi': 92, 'Urziceni': 142},
                           
             'Neamt': {'Iasi': 87}}),
             initial_Node="Arad",goal_node="Hirsova")

romania_map.interative_Deeping_search(limit =4)