import tree
import matplotlib.pyplot as plt
import children
    
def Genetic_one_D_input(X, Y):

    # using domain 1D
    two_D_flag = False

    # population number zero
    print("population number 0\n")
    list_of_parents = tree.random_trees(amount_of_trees, max_depth, two_D_flag)
    parents_average_mae, parents_best_mae, best_parent_tree = tree.calculating_mae(list_of_parents, X, Y)
    
    # making lists for showing 
    x_generation_number = []
    y_average_mae_of_each = []
    y_best_mae_of_each = []
    y_best_mae_of_all = []
    y_best_tree = []
    y_min_mae = None
    
    # appending 0 generation information
    x_generation_number.append(0)
    y_average_mae_of_each.append(parents_average_mae)
    y_best_mae_of_each.append(parents_best_mae)
    y_best_mae_of_all.append(parents_best_mae)
    y_best_tree.append(best_parent_tree)
    
    
    for i in range(amount_of_generations):
    
        print(f"population number {i+1}")
        list_of_children = children.making_children(list_of_parents, k, pc, pm)
        average_mae, best_mae, best_tree = tree.calculating_mae(list_of_children, X, Y)
        list_of_parents = list_of_children
        
        x_generation_number.append(i+1)
        y_best_tree.append(best_tree)
        y_best_mae_of_each.append(best_mae)
        y_min_mae = min(y_best_mae_of_each)
        print("best mae so far: ", y_min_mae)
        y_best_mae_of_all.append(y_min_mae)
        y_average_mae_of_each.append(average_mae)

    print()    

    final_best_tree = None
    for i in y_best_tree:
        if i.mae==y_min_mae:
            final_best_tree = i
            
    final_best_tree_in_order = tree.to_math_string(final_best_tree.root)            

     
def Genetic_two_D_input(X, Y):

    # using domain 2D
    two_D_flag = True

    # population number zero
    print("population number 0\n")
    list_of_parents = tree.random_trees(amount_of_trees, max_depth, two_D_flag)
    parents_average_mae, parents_best_mae, best_parent_tree = tree.calculating_mae(list_of_parents, X, Y)
    
    # making lists for showing 
    x_generation_number = []
    y_average_mae_of_each = []
    y_best_mae_of_each = []
    y_best_mae_of_all = []
    y_best_tree = []
    y_min_mae = None
    
    # appending 0 generation information
    x_generation_number.append(0)
    y_average_mae_of_each.append(parents_average_mae)
    y_best_mae_of_each.append(parents_best_mae)
    y_best_mae_of_all.append(parents_best_mae)
    y_best_tree.append(best_parent_tree)

    for i in range(amount_of_generations):
    
        print(f"population number {i+1}")
        list_of_children = children.making_children(list_of_parents, k, pc, pm)
        average_mae, best_mae, best_tree = tree.calculating_mae(list_of_children, X, Y)
        list_of_parents = list_of_children
        
        x_generation_number.append(i)
        y_best_tree.append(best_tree)
        y_best_mae_of_each.append(best_mae)
        y_min_mae = min(y_best_mae_of_each)
        print("best mae so far: ", y_min_mae)
        y_best_mae_of_all.append(y_min_mae)
        y_average_mae_of_each.append(average_mae)

    # print(y_min_mae)
    # print(min(y_best_mae_of_all))

    final_best_tree = None
    
    for t in y_best_tree:
        # print(t.mae)
        if t.mae==y_min_mae:
            final_best_tree = t 
            
    final_best_tree_in_order = tree.to_math_string(final_best_tree.root)

    
if __name__ == "__main__":
    
    input_file_name = 'c1.csv'
    
    
    amount_of_trees = 100
    max_depth = 8

    k = 3 # k tournoment parameter
    pc = 0.5 # the probblity of cross-over
    pm = 0.5 # the probblity of mutation

    amount_of_generations = 50

    
    two_D = True
    input_file_name = '2D_in_out3.txt'

    if(two_D==False):
        Genetic_one_D_input(X, Y)
    else:
        Genetic_two_D_input(X, Y)
        
    # new generation is the children

    print()