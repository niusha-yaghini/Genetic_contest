import tree
import matplotlib.pyplot as plt
import children
import copy
import reading_data
import time
import datetime
import random
    
def Termination_condition(best_sofar_mse):
    if(best_sofar_mse<0.0001): return True
    else: return False

def Genetic(X, Y, iteration_number):

    amount_of_no_change = 0
    
    list_of_parents = tree.random_trees(population_size, max_depth, two_D_flag)
    parents_best_mse, best_parent_tree = tree.calculating_mse(list_of_parents, X, Y)
    
    best_mse_eachGen = []
    best_tree_eachGen = []
    best_sofar_mse = parents_best_mse
    best_mse_of_all = []
    
    best_mse_eachGen.append(parents_best_mse)
    best_tree_eachGen.append(best_parent_tree)
    best_mse_of_all.append(parents_best_mse)
    
    for i in range(amount_of_generations):
    
        if(Termination_condition(best_sofar_mse)):
            break
        
        if(amount_of_no_change>=no_change_limit):
            break

        print(f"iteration {iteration_number} generation {i+1}, best so far mse: {best_sofar_mse}, ", end='') 
        e = datetime.datetime.now()

        print ("time: %s:%s:%s" % (e.hour, e.minute, e.second))
 
        list_of_children = children.making_children(list_of_parents, k, pc, pm)
        best_mse, best_tree = tree.calculating_mse(list_of_children, X, Y)
        list_of_parents = list_of_children
                
        best_tree_eachGen.append(copy.deepcopy(best_tree))
        best_mse_eachGen.append(best_mse)
        best_sofar_mse = min(best_mse_eachGen)
        
        if(best_sofar_mse == best_mse_of_all[-1]):
            amount_of_no_change += 1
        else:
            amount_of_no_change = 0

        best_mse_of_all.append(best_sofar_mse)

    final_best_tree = None
    for bt in best_tree_eachGen:
        if bt.mse==best_sofar_mse:
            final_best_tree = bt
    
    final_best_tree_preorder = tree.PreorderTraversal(final_best_tree.root)   
    final_best_tree_inorder = tree.InorderTraversal(final_best_tree.root)   
    
    # print("after traversal")  
    
    return best_sofar_mse, i, final_best_tree_preorder, final_best_tree_inorder     

     
if __name__ == "__main__":
    
    # random.seed(1)
    
    input_file_name = '.\\GA\\c2.csv'
    two_D_flag = False

    X, Y = reading_data.input_output(input_file_name)
    
    no_change_limit = 50
    iteration_of_genetic = 30
    population_size = 1000
    amount_of_generations = 300
    max_depth = 3

    k = 3 # k tournoment parameter
    pc = 0.5 # the probblity of cross-over
    pm = 0.5 # the probblity of mutation

    # get the start time
    st = time.time()
    
    best_mses = []
    best_trees = []
    sum = 0

    file_execution_name = 'result_c2'

    for i in range(iteration_of_genetic):
        iteration_st = time.time()
        result = open(f'{file_execution_name}.txt', 'a')
        
        print(f"iteration number {i}:")
        mse, gen_num, preorder_tree, inorder_tree = Genetic(X, Y, i)
        print(f"mse = {mse}, generation nums = {gen_num} \n")
        best_mses.append(mse)
        sum += mse
        result.write(f"iteration number {i}: \n")        
        result.write(f"mse = {mse}, generation nums = {gen_num} \n")
        result.write(f"preorder = {preorder_tree} \n")
        result.write(f"inorder = {inorder_tree} \n")

        iteration_et = time.time()
        iteration_elapsed_time = iteration_et - iteration_st
        result.write(f"Execution time of iteration: {iteration_elapsed_time} seconds\n \n")
        
        result.close()

    result = open(f'{file_execution_name}.txt', 'a')
        
    # get the end time
    et = time.time()

    all_min = min(best_mses)
    avg = sum/iteration_of_genetic
    result.write(f"the best mse of all: {all_min} \n")
    result.write(f"the average mse of all: {avg} \n")

    elapsed_time = et - st
    print('Execution time:', elapsed_time, 'seconds')
    
    result.write(f'Execution time of all: {elapsed_time} seconds')

    result.close()
        
    # new generation is the children

    print()