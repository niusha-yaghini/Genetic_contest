import random as rnd
from sklearn.metrics import mean_squared_error
import math

# choosing the operator
def my_operator():
    op = ['+', '-', '*', '/', '**', 'sin', 'cos']
    return(rnd.choice(op))

# choosing the leaf
def my_leaf_one_D():
    num = rnd.randint(1, 9)
    var = 'x'
    x = rnd.random()
    if(x<=0.5): return num
    else: return var

def my_leaf_two_D():
    num = rnd.randint(1, 9)
    var = ['x1', 'x2']
    x = rnd.random()
    if(x<=0.5): return num
    else: return rnd.choice(var)

# checking type of function (1 child needed or 2 childs needed)
def single_op(op):
    if(op=='sin' or op=='cos' or op=='tan' or op=='cot'):
        return True
    else: 
        return False

class Node:
    # my node class 
    
    def __init__(self, _depth, _operator, _children = [], _is_leaf = False):
        self.operator = _operator
        self.depth = _depth
        self.children = _children
        self.is_leaf = _is_leaf

class Tree:
    # my tree class

    def __init__(self, _max_depth = None, _two_D_flag = None):
        self.max_depth = _max_depth
        self.two_D_flag = _two_D_flag
        self.root = None
        self.mse = None        
        
    def _fit(self):
        self.root = self._grow_tree(self.max_depth, self.two_D_flag)
        
    def _grow_tree(self, max_depth, two_D_flag, CS = 2):
        
        # choosing a rnd depth each time (between 0 to max given depth)
        depth = max_depth
          
        # choosing the operator for current node
        x = my_operator()
        
        # check the type of our function and fix the amount of our children needed number
        if(single_op(x)):
            CS = 1
        else: 
            CS = 2

        children = []
        
        # building the tree base on current depth and children needed
        if(depth==0):
            if(two_D_flag):
                x = my_leaf_two_D()
            else:
                x = my_leaf_one_D()
        else:
            for i in range(CS):
                children.append(self._grow_tree(depth-1, two_D_flag))

        # making the node 
        n = Node(depth, x, children)
        if(depth==0): n.is_leaf = True
        return n          

def PreorderTraversal(node):
    if(node.is_leaf):
        return f"{node.operator},"
    else:
        if(len(node.children)) == 1:
            return f"{node.operator},{PreorderTraversal(node.children[0])},"
        else:
            return f"{node.operator},{PreorderTraversal(node.children[0])},{PreorderTraversal(node.children[1])},"
        
def InorderTraversal(node):
    if(node.is_leaf):
        return f"{node.operator}"
    else:
        if(len(node.children)) == 1:
            return f"{node.operator}({InorderTraversal(node.children[0])})"
        else:
            return f"({InorderTraversal(node.children[0])}{node.operator}{InorderTraversal(node.children[1])})"

def random_trees(amount, max_depth, two_D_flag):
    # making a list of all random trees (generation 0)

    trees = []
    for i in range(amount):
        t = Tree(max_depth, two_D_flag)
        t._fit()
        trees.append(t)
    return trees
        
def calculator(two_D_flag, root, x, flag):
    # doing the calculating for each function that we have made with given input
    
    if(flag):
        return
    
    if(root.is_leaf):
        if(two_D_flag):
            if(root.operator == 'x1'): 
                return x[0]
            elif(root.operator == 'x2'): 
                return x[1]                
            else: 
                return root.operator        
        else:
            if(root.operator == 'x'): 
                return x
            else: 
                return root.operator
    else:
        if(len(root.children)==1):
            val = calculator(two_D_flag, root.children[0], x, flag)
        else:       
            left_val = calculator(two_D_flag, root.children[0], x, flag)
            right_val = calculator(two_D_flag, root.children[1], x, flag)
        if (root.operator == 'sin'):
            # print("we are in sin")
            try:
                return math.sin(val)
            except:
                flag = True
                return 1
        elif (root.operator == 'cos'):
            # print("we are in cos")
            try:
                return math.cos(val)
            except:
                flag = True
                return 1
        elif (root.operator == '+'):
            return left_val + right_val
        elif (root.operator == '-'):
            return left_val - right_val
        elif (root.operator == '*'):
            # print("we are in *")
            try:
                return left_val * right_val
            except:
                flag = True
                return 1                
        elif (root.operator == '/'):
            # print("we are in /")
            try:
                return left_val / right_val
            except:
                flag = True
                return 1                
        elif (root.operator == '**'):
            # print("we are in **")
            if(left_val==0 and right_val<0):
                flag = True
                return 1
            else: 
                if(right_val==0):
                    return 1
                x = 1
                i = 0
                while(not flag and i<right_val):
                    x = x*left_val
                    i+=1
                    if(x>100000 or x<-100000):
                        flag = True
                        return 1
                return x
                
def _mse(tree, list_x, list_y):
    # calculating each tree mse with given inputs and outputs
    
    trees_y = []
    for single_x in list_x:
        flag = False
        t_y = calculator(tree.two_D_flag, tree.root, single_x, flag)

        if(flag==True or t_y>100000 or t_y<-100000):
            t_y = 100000

        trees_y.append(t_y)
    mse = mean_squared_error(list_y, trees_y)

    return mse

def calculating_mse(tree_list, X, Y):
    # calculating the average-mse and best-mse for all of our trees and given inputs and outputs
    
    mse_sum = 0
    best_mse = float('inf')
    best_tree = None
    for t in tree_list:
        t.mse = _mse(t, X, Y)
        mse_sum += t.mse
        if (t.mse<best_mse):
            best_mse = t.mse
            best_tree = t

    return best_mse, best_tree