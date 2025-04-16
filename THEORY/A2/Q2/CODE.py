import random

tasks = ['Task 1', 'Task 2', 'Task 3', 'Task 4', 'Task 5', 'Task 6', 'Task 7']
task_times = [5, 8, 4, 7, 6, 3, 9]
facilities = ['Facility 1', 'Facility 2', 'Facility 3']
facility_capacities = [24, 30, 28]
cost_matrix = [
    [10, 12, 9],
    [15, 14, 16],
    [8, 9, 7],
    [12, 10, 13],
    [14, 13, 12],
    [9, 8, 10],
    [11, 12, 13]
]


population_size = 6
crossover_rate = 0.8
mutation_rate = 0.2
generations = 100

def initialize_population():
    population = []
    for _ in range(population_size):
        chromosome = [random.randint(0, 2) for _ in range(len(tasks))]
        population.append(chromosome)
    return population

def calculate_fitness(chromosome):
    total_cost = 0
    facility_times = [0, 0, 0]
    for i in range(len(chromosome)):
        facility = chromosome[i]
        total_cost += cost_matrix[i][facility]
        facility_times[facility] += task_times[i]

    penalty = 0
    for i in range(len(facility_times)):
        if facility_times[i] > facility_capacities[i]:
            penalty += (facility_times[i] - facility_capacities[i]) * 100 
    fitness = total_cost + penalty
    return fitness

def roulette_wheel_selection(population, fitnesses):
    total_fitness = sum(fitnesses)
    if total_fitness == 0:
        return random.choices(population, k=2)
    probabilities = [f / total_fitness for f in fitnesses]
    selected = random.choices(population, weights=probabilities, k=2)
    return selected

def one_point_crossover(parent1, parent2):
    if random.random() < crossover_rate:
        crossover_point = random.randint(1, len(parent1) - 1)
        child1 = parent1[:crossover_point] + parent2[crossover_point:]
        child2 = parent2[:crossover_point] + parent1[crossover_point:]
        return child1, child2
    else:
        return parent1, parent2

def swap_mutation(chromosome):
    if random.random() < mutation_rate:
        idx1, idx2 = random.sample(range(len(chromosome)), 2)
        chromosome[idx1], chromosome[idx2] = chromosome[idx2], chromosome[idx1]
    return chromosome

def genetic_algorithm():
    population = initialize_population()
    for _ in range(generations):
        fitnesses = [calculate_fitness(chromosome) for chromosome in population]
        new_population = []
        for _ in range(population_size // 2):
            parent1, parent2 = roulette_wheel_selection(population, fitnesses)
            child1, child2 = one_point_crossover(parent1, parent2)
            child1 = swap_mutation(child1)
            child2 = swap_mutation(child2)
            new_population.extend([child1, child2])
        population = new_population
    best_chromosome = min(population, key=calculate_fitness)
    return best_chromosome

best_allocation = genetic_algorithm()
print("Best Allocation:", best_allocation)
print("Total Cost:", calculate_fitness(best_allocation))

facility_times = [0, 0, 0]
for i in range(len(best_allocation)):
    facility = best_allocation[i]
    facility_times[facility] += task_times[i]
print("Facility Times:", facility_times)
print("Facility Capacities:", facility_capacities)
