# -*- coding: utf-8 -*-
"""BST-helping-function.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ouPQuZCIX5kC0ZV0gBOsaB-z2mM26Rfk
"""

class TreeNode:

  def __init__(self,x):
    self.val = x 
    self.left = None
    self.right = None

from graphviz import Digraph

def visualize_tree(tree):
    if tree is None:
      return "Nothin in the tree"

    def add_nodes_edges(tree,dot=None):
      # Create digraph object
      if dot is None:
        dot = Digraph()
        dot.attr('node', shape='circle')
        dot.node(name=str(tree), label=str(tree.val))
      for child in [tree.left, tree.right]:
        if child is not None:
          if child == tree.left: dot.attr('node', shape='circle', style='filled',
          fillcolor='lightblue')
          if child == tree.right: dot.attr('node', shape='doublecircle', style='filled',
          fillcolor='seashell')
          dot.node(name=str(child) ,label=str(child.val))
          dot.edge(str(tree), str(child))
          dot = add_nodes_edges(child, dot=dot) # recursive call
    
      return dot
  # Add nodes recursively and create a list of edges
    dot = add_nodes_edges(tree)
  # Visualize the graph
    display(dot)

def print_tree(tree, level=0, label='.'):
  print(' ' * (level*2) + label + ' : ', tree.val)
  for child, lbl in zip([tree.left, tree.right], ['L', 'R']):
    if child is not None:
      print_tree(child, level+1, lbl)





t1 = TreeNode(1)

t1.left = TreeNode(4)
t1.right = TreeNode(12)
t1.left.left = TreeNode(14)
t1.left.right = TreeNode(20)
t1.right.left = TreeNode(50)

visualize_tree(t1)

## Tree Traversal - Depth first Search

def dfs(self):

  print(self.val)

  if self.left:
    self.left.dfs()
  if self.right:
    self.right.dfs()

TreeNode.dfs = dfs

t1.dfs()

def dfs_inorder(self):

  if self.right:
    self.left.dfs_inorder()

  print(self.val)

  if self.right:
    self.right.dfs_inorder()

TreeNode.dfs_inorder = dfs_inorder

t1.dfs_inorder()

def dfs_postOrder(self):

  if self.left:
    self.left.dfs_postOrder()

  if self.right:
    self.right.dfs_postOrder()

  print(self.val)

TreeNode.dfs_postOrder = dfs_postOrder

t1.dfs_postOrder()

visualize_tree(t1)

def bfs(self):

  to_visit = [self]

  while to_visit:
    current = to_visit.pop(0)

    print(current.val)

    if current.left :
      to_visit.append(current.left)

    if current.right:
      to_visit.append(current.right)

TreeNode.bfs = bfs

t1.bfs()

## Perform Arbitrary Task on all Nodes

visualize_tree(t1)

def dfs_apply(self,fn):
  fn(self)

  if self.left:
    self.left.dfs_apply(fn)

  if self.right:
    self.right.dfs_apply(fn)

TreeNode.dfs_apply = dfs_apply

## Binary Search Tree

class TreeNode:

  def __init__(self,x):

    self.val = x
    self.left = None
    self.right = None

class BST(TreeNode):

  def __init__(self,val,parent=None):
    super().__init__(val)
    self.parent = parent


  def insert(self,val):

    if val< self.val:
      if self.left is None:
        new_node = BST(val,parent=self)
        self.left = new_node
      else:
        self.left.insert(val)
    else: ## greater
      if self.right is None:
        self.right = BST(val,parent=self)
      else:
        self.right.insert(val)


def bfs(self):

  to_visit = [self]
  list_=[]
  while to_visit:
    current = to_visit.pop(0)
    list_.append(current.val)  
    # print(current.val)

    if current.left :
      to_visit.append(current.left)

    if current.right:
      to_visit.append(current.right)


  return list_

TreeNode.bfs = bfs

def lifosearch(self,val):
  list_= bfs(self)  ## getting list from the BFS
  # print(list_)
  # use first in first out concpet here!
  # checking here the last element if target is same then yes!

  for number in list_:
    num = list_.pop()
    if val== num:
      return num
  return "Not in Tree"

TreeNode.lifosearch = lifosearch


def dfs_inorder(self):
  list_=[]
  if self.right:
    self.left.dfs_inorder()

  print(self.val)
  list_.append(self.val)

  if self.right:
    self.right.dfs_inorder()

TreeNode.dfs_inorder = dfs_inorder

def fifosearch(self,val):
  list_ = dfs_inorder(self)
  print(list_)
  
  

TreeNode.fifosearch = fifosearch

b = BST(50)
b.insert(30)
b.insert(15)
b.insert(35)
b.insert(7)
b.insert(22)
b.insert(31)
b.insert(70)
b.insert(62)
b.insert(87)
b.insert(89)
b.insert(91)
b.insert(52)
b.insert(34)
b.insert(6)





visualize_tree(b)

# b.bfs()
# b.lifosearch(52)
b.fifosearch(32)





## deletion from the BST

## first we make helper functions

def find_root(self):

  ''' find the absolute root fo the BST to whicj self belong. keep going untilll reach parent '''
  temp = self

  while temp.parent is not None:
    temp = temp.parent

  return temp

BST.find_root = find_root

def find_min(self):

  """find the minimum value start from the self.
  in BST this is simple , keep going left untill no more left is left"""

  min_node = self
  if self.left is not None:
    min_node = find_min(self.left)

  return min_node


BST.find_min = find_min

visualize_tree(b)
print("min is : ",b.find_min().val)

def set_for_parents(self,new_ref):
  """Disconnect self from parent and attach new_ref to parent in self place """

  if self.parent is None:
    return

  if self.parent.right == self:
    self.parent.right=new_ref

  if self.parent.left == self:
    self.parent.left=new_ref

BST.set_for_parents =set_for_parents

def replace_with_node(self,node):
  """Replace self with node which is a child). Make sure to fix the parent of the 
  of the node and parent to node.Assue we have no children other than node """

  self.set_for_parents(node) # connect new to parent on proper locations
  node.parent=  self.parent   # set node paent correctly
  self.parent = None   # disconnect self from the parent
  return node.find_root()  # find root again

BST.replace_with_node = replace_with_node

def delete(self,val):
  ## first if we are alone , on the root and no chikdren plus the value matches just retunr the None
  if self.parent is None and self.right is None and self.left is None and self.val == val:
    return None
  
  ## we are node to be deleted

  if self.val==val:

    #check if we are leaf

    if self.right is None and self.left is None:
      self.set_for_parent(None)  ## set in place of the self a None
      return self.find_root()

    ## check if we have just a left node

    if self.right is None:
      return self.replace_with_node(self.left)

    #3 check if we have just a righ node

    if self.left is None:
      return self.repace_with_node(self.right)

    ## now we have both children. find the successor and replace "self" with it.
    ## (our succ is definitly in our right child and it can;t have two children)
    ## becuase ledt child will always be smaller
    successor = self.right.find_min()

    ## copy successor val here

    self.val = successor.val

    return self.right.delete(successor.val)

    # ^ delete the sucessor node, which is in our right child BST.
    # ^ its guaranteed that is a simpler case since successor cannot have a leeft child

    # we were not the node to be deleted , go to the children

    if val<self.val:
      if self.left is not None:
        return self.left.delete(val)
      else:
        return self.din_root() ## nothing to delete
    else:
      if self.right is not None:
        return self.right.delete(val)
      else:
        return self.find_root()


BST.delete = delete

b = BST(30)
b.insert(1)
b.insert(2)
b.insert(3)
b.insert(4)
b.insert(5)

visualize_tree(b)

b.delete(4)

visualize_tree(b)



"""### **Graph**"""

! pip install networks

# Commented out IPython magic to ensure Python compatibility.
import networks as nx
import matplotlib.pyplot as plt

# for Notebook
# %matplotlib inline
import warnings
warnings.filterwarnings("ignore")

def draw_graph_with_nx(G):

  pos = nx.spring_layout(G,iterations=200)

  options = {
      'node_color':"white",
      'alpha':1,
      'node_size':2000,
      'width':0.002,
      'font_color':'darked',
      'font_size':25,
      'arrows':True,
      'edge_color':'brown',
      'arrowstyle': 'fancy ,head_lenght=1,head_width=1,tail_width=.4'
  }
  labels = nx.get_node_attribute(G,'lable')
  nx.draw(G,pos,labels=labels,**options)
  plt.show()

class Digraph:
  def __init__(self):
    self.g={}

  def add_node(self,node):
    if node in self.g:
      raise ValueError("Node in already in graph")
    
    self.g[node] = []

  def add_edge(self,src,dest):
    # sanity check

    if src not in self.g:
      raise ValueError("Source node not in graph")
    if dest not in self.g:
      raise ValueError("Dest Node not in graph")

    nexts = self.g[src]
    if dest in nexts:
      return
    nexts.append(dest)

    def draw_graph(self):
      G=nx.Digraph()
      for src in self.g:
        G.add_node(src,label=src)
        for dest in self.g[src]:
          G.add_edge(src,dest)

      draw_graph_with_nx(G)

g = Digraph()

nodes = ['a','b','c','d','e','f']

for n in nodes:
  g.ad_node(n)