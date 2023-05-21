import copy
import random as rnd
import tree


def replace_nodes(child_root1, choosed_node1, child_root2, choosed_node2):
    # change the specific node1 in tree1 with the specific node2 in tree2 with each other
    #       and making new trees as children
    
    queue1 = []
    queue1.append(child_root1)
    
    # making a cope of node1, because we will lose it after we change it with node2
    cn1 = copy.deepcopy(choosed_node1)
    
    # searching in tree1 untill we find our specific node, and changing it with node2
    flag1 = True
    while flag1:
        node = queue1.pop()
        if(node!=choosed_node1):
            for i in range(len(node.children)):
                queue1.append(node.children[i])
        else:
            node.depth = choosed_node2.depth
            node.operator = choosed_node2.operator
            node.children = copy.deepcopy(choosed_node2.children)
            node.is_leaf = choosed_node2.is_leaf
            flag1 = False
            
    queue2 = []
    queue2.append(child_root2)
         
    # searching in tree2 untill we find our specific node, and changing it with node1 (cn1)  
    flag2 = True
    while flag2:
        node = queue2.pop()
        if(node!=choosed_node2):
            for j in range(len(node.children)):
                queue2.append(node.children[j])
        else:
            node.depth = cn1.depth
            node.operator = cn1.operator
            node.children = copy.deepcopy(cn1.children)
            node.is_leaf = cn1.is_leaf
            flag2 = False          
        
def make_list_node(root, nodes):
    # making a list of all nodes in our tree
    
    nodes.append(root)
    if(len(root.children)!=0):
        for i in root.children:
            make_list_node(i, nodes)
                
    return nodes

def cross_over(parent1, parent2, pc):
    # doing the cross-over with the given cross-over-rate (pc), on 2 tree
    
    x = rnd.random()
    if(x<=pc):

        # making the child nodes for changing nodes        
        child1 = copy.deepcopy(parent1)
        child2 = copy.deepcopy(parent2)        
        
        # making a list of all nodes
        nodes1 = []
        make_list_node(child1.root, nodes1)
        nodes2 = []
        make_list_node(child2.root, nodes2)
        
        # choosing a node to change
        choosed_node1 = rnd.choice(nodes1)
        choosed_node2 = rnd.choice(nodes2)
        
        replace_nodes(child1.root, choosed_node1, child2.root, choosed_node2)

        return child1, child2
    
    else:
        return parent1, parent2
                   
def tournament(p_trees, k):
    # using the tournament preceture for selecting a couple tree
    # in this method we choose 3 tree randomly 2 times (2 times becuase we want a couple), and select the best-mae tree
    
    couple_parent = []
    for j in range(2):
        best_mae = float('inf')
        best_tree = None
        for z in range(k):
            t = rnd.choice(p_trees)  
            if(t.mae<best_mae):
                best_mae = t.mae
                best_tree = t
        couple_parent.append(best_tree)
    return couple_parent[0], couple_parent[1]       
        
def change_node(root, choosed_node):
    queue = []
    queue.append(root)
        
    # searching in tree1 untill we find our specific node, and changing it with node2
    flag = True
    while flag:
        node = queue.pop()
        if(node!=choosed_node):
            for i in range(len(node.children)):
                queue.append(node.children[i])
        else:
            d = node.depth
            t = tree.Tree(d)
            t._fit()
            node.depth = t.root.depth
            node.operator = t.root.operator
            node.children = t.root.children
            node.is_leaf = t.root.is_leaf
            flag = False
          
def mutation(children, pm):
    for child in children:
        x = rnd.random()
        if(x<=pm):

            nodes = []
            make_list_node(child.root, nodes)
            
            # choosing a node to change
            choosed_node = rnd.choice(nodes)
            
            change_node(child.root, choosed_node)
                      
def making_children(parent_trees, k, pc, pm):
    # we want to make children on base of a list of trees (parent_trees)
    
    lenght = len(parent_trees)
    children = []
    
    for i in range(int(lenght/2)):
        #returning a couple of parents
        parent1, parent2 = tournament(parent_trees, k)        
        # we pass our couple to cross-over function(that 'pc' percent will do it)
        child1, child2 = cross_over(parent1, parent2, pc)
        children.append(child1)
        children.append(child2)
    
    mutation(children, pm)

    # for c in children:
    #     c.print_tree()

    return children