import pygad, matplotlib as plt
import numpy as np
plt.style.use("default")


def nonogram_ga(nonogram, image_name, printing=True):
    gene_space = [0,1]
    
    nonogram_size = len(nonogram[0]) 
    num_genes = nonogram_size**2
    keep_parents = 2
    

    if (nonogram_size == 5):
        sol_per_pop = 120
        num_parents_mating = 60
        num_generations = 40
        parent_selection_type = "sss"
        crossover_type = "single_point"
        mutation_type = "random"
        mutation_percent_genes = 4
        
    elif (nonogram_size == 10):
        sol_per_pop = 300
        num_parents_mating = 100
        num_generations = 500
        parent_selection_type = "sss"
        crossover_type = "two_points"
        mutation_type = "random"
        mutation_percent_genes = 1


    
    elif (nonogram_size == 15):
        sol_per_pop = 300
        num_parents_mating = 150
        num_generations = 700
        parent_selection_type = "sss"
        crossover_type = "two_points"
        mutation_type = "random"
        mutation_percent_genes = 1
        
    else:
        print("Error: Nonogram size is not 5x5, 10x10 or 15x15!")
        return False
        

    def fitness_sequence(sequence, clues):
        fitness = 0
        seq_id = 0
        
        for clue in clues:        
            while seq_id < len(sequence) and sequence[seq_id] == 0:
                seq_id += 1
                
            if seq_id == len(sequence):
                break
            
            block_len = 0
            while seq_id < len(sequence) and sequence[seq_id] == 1:
                block_len += 1
                seq_id += 1   
            if block_len == clue:
                fitness += 1
        
        if(seq_id < len(sequence)):
            fitness -= np.sum(sequence[seq_id:])*5
        
        return fitness
    def fitness_func(model, solution, solution_idx):
        col_clues = np.array(nonogram[0], dtype=object)
        row_clues = np.array(nonogram[1], dtype=object)
        
        grid = solution.reshape((len(row_clues), len(col_clues)))
        score = 0
        
        for i in range(len(col_clues)):
            col_score = fitness_sequence(grid[:, i], col_clues[i])
            score += col_score
            
        for j in range(len(row_clues)):
            row_score = fitness_sequence(grid[j, :], row_clues[j])
            score += row_score
        return score

        
    ga_instance = pygad.GA(fitness_func=fitness_func,
                           gene_space=gene_space,
                           num_genes=num_genes,
                           sol_per_pop=sol_per_pop,
                           num_parents_mating=num_parents_mating,
                           num_generations=num_generations,
                           keep_parents=keep_parents,
                           parent_selection_type=parent_selection_type,
                           crossover_type=crossover_type,
                           mutation_type=mutation_type,
                           mutation_percent_genes=mutation_percent_genes
                           )
    
    
    ga_instance.run()
    
    solution, solution_fitness, solution_idx = ga_instance.best_solution()
    
    def accuracy_sol(nonogram, sol_fitness):
        col = np.concatenate( nonogram[0])
        row = np.concatenate(nonogram[1])
        clue_length = col.size + row.size
        return round(((sol_fitness*100)/clue_length),2)
    
    if (printing):
        print("Nonogram: ", nonogram)
        
        print("Best solution:")
        for i in range(0,len(nonogram[0])**2,len(nonogram[0])):
            print(solution[i:i+len(nonogram[0])])
            
        print("Solution score: ", solution_fitness)
        
        print("Accuracy: ", accuracy_sol(nonogram, solution_fitness),"%")
        
        ga_instance.plot_fitness().savefig(f"images/{image_name}.png")
        
    return accuracy_sol(nonogram, solution_fitness)


