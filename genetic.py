import numpy as np
import itertools

def fitness(solution, nonogram_rows, nonogram_cols):
    def check_line(line, rules):
        groups = [len(list(group)) for is_one, group in itertools.groupby(line) if is_one]
        return groups == rules
    
    row_fitness = sum(check_line(row, rule) for row, rule in zip(solution, nonogram_rows))
    col_fitness = sum(check_line(col, rule) for col, rule in zip(solution.T, nonogram_cols))
    
    return row_fitness + col_fitness

def initialize_population(pop_size, nonogram_size):
    population = []
    for _ in range(pop_size):
        individual = np.random.randint(2, size=nonogram_size)
        population.append(individual)
    return np.array(population)

def select_parents(population, fitness_values):
    fitness_sum = np.sum(fitness_values)
    selection_probs = fitness_values / fitness_sum
    parents = population[np.random.choice(len(population), size=2, p=selection_probs)]
    return parents

def crossover(parent1, parent2):
    crossover_point = np.random.randint(len(parent1))
    child1 = np.concatenate([parent1[:crossover_point], parent2[crossover_point:]])
    child2 = np.concatenate([parent2[:crossover_point], parent1[crossover_point:]])
    return child1, child2

def mutate(individual, mutation_rate):
    for i in range(len(individual)):
        if np.random.rand() < mutation_rate:
            individual[i] = 1 - individual[i]
    return individual

def genetic_algorithm(nonogram_rows, nonogram_cols, pop_size, generations, mutation_rate):
    nonogram_size = (len(nonogram_rows), len(nonogram_cols))
    population = initialize_population(pop_size, nonogram_size)
    best_fitness = 0
    best_individual = None
    with open('genetic_results.txt', 'w') as file:
        for generation in range(generations):
            fitness_values = np.array([fitness(individual, nonogram_rows, nonogram_cols) for individual in population])
            new_population = []
            for _ in range(pop_size // 2):
                parent1, parent2 = select_parents(population, fitness_values)
                child1, child2 = crossover(parent1, parent2)
                new_population.append(mutate(child1, mutation_rate))
                new_population.append(mutate(child2, mutation_rate))
            population = np.array(new_population)
            best_fitness = np.max(fitness_values)
            file.write(f"Generation {generation}: Best Fitness = {best_fitness}\n")
        best_individual = population[np.argmax(fitness_values)]
    return best_individual

nonogram_rows = [[4, 2], [4, 2], [1, 4, 2], [2, 4], [3, 4], [2, 3], [3, 3], [2, 2, 2], [3, 3], [3, 3], [2, 2], [2, 1], [2, 2], [2, 1], [2, 2], [1, 2], [1, 2], [3], [3], [1], [1]]
nonogram_cols = [[1, 1, 1], [2, 2], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [2, 1], [2, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]]

solution = genetic_algorithm(nonogram_rows, nonogram_cols, pop_size=100, generations=1000, mutation_rate=0.01)

with open('genetic_solution.txt', 'w') as file:
    file.write(f"Found solution: \n{solution}")
