import tree
import matplotlib.pyplot as plt
import children
import copy
import reading_data
    
def Termination_condition(best_sofar_mse):
    if(best_sofar_mse<0.0001): return True
    else: return False

def Genetic(X, Y):

    amount_of_no_change = 0
    
    # using domain 1D
    # two_D_flag = False

    # population number zero
    print("generation number 0\n")
    list_of_parents = tree.random_trees(population_size, max_depth, two_D_flag)
    parents_average_mse, parents_best_mse, best_parent_tree = tree.calculating_mse(list_of_parents, X, Y)
    
    # y_average_mse_of_each = []
    best_mse_eachGen = []
    best_mse_of_all = []
    best_tree_eachGen = []
    best_sofar_mse = None
    
    # y_average_mse_of_each.append(parents_average_mse)
    best_mse_eachGen.append(parents_best_mse)
    best_mse_of_all.append(parents_best_mse)
    best_tree_eachGen.append(best_parent_tree)
    
    for i in range(amount_of_generations):
    
        if(Termination_condition(best_sofar_mse)):
            break
        
        if(amount_of_no_change>=no_change_limit):
            break

        print(f"population number {i+1}")
        list_of_children = children.making_children(list_of_parents, k, pc, pm)
        average_mse, best_mse, best_tree = tree.calculating_mse(list_of_children, X, Y)
        list_of_parents = list_of_children
                
        best_tree_eachGen.append(copy.deepcopy(best_tree))
        best_mse_eachGen.append(best_mse)
        best_sofar_mse = min(best_mse_eachGen)
        print("best mse so far: ", best_sofar_mse)
        best_mse_of_all.append(best_sofar_mse)
        # y_average_mse_of_each.append(average_mse)
        
        if(best_sofar_mse == best_mse_of_all[-1]):
            amount_of_no_change += 1
        else:
            amount_of_no_change = 0


    print()    

    final_best_tree = None
    for i in best_tree_eachGen:
        if i.mse==best_sofar_mse:
            final_best_tree = i
            
    final_best_tree_in_order = tree.to_math_string(final_best_tree.root)            

     
    
if __name__ == "__main__":
    
    input_file_name = '.\\GA\\c1.csv'
    two_D_flag = True

    X, Y = reading_data.input_output(input_file_name)
    
    no_change_limit = 50
    iteration = 30
    population_size = 1000
    amount_of_generations = 300
    max_depth = 8

    k = 3 # k tournoment parameter
    pc = 0.5 # the probblity of cross-over
    pm = 0.5 # the probblity of mutation
    
    # be tedade iteration ha seda kon harbar tabee va mse ra bargardan
    Genetic(X, Y)
        
        
    # new generation is the children

    print()