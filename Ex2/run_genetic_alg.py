#!python3
import sys
import random
import numpy as np
from copy import deepcopy


def main(features, interactions):
    population_size = 50
    feature_size = 17
    num_cycles = 1000

    population = initialize_population(feature_size, population_size)
    population_Scores = [None] * len(population)
    best = None
    best_Score = -1

    while num_cycles >= 0:
        for i in range (0, len(population)):
            parent_Score = assess_fitness(population[i], features, interactions)
            population_Scores[i] = parent_Score

            if best is None or parent_Score > best_Score:
                best_Score = population_Scores[i]
                best = population[i]

        Q = []
        count = 0;
        while count < (population_size / 2):
            parent_a, parent_b = stochasticUniversalSampling(population, population_Scores, 2)
            child_a, child_b = uniformCrossover(parent_a, parent_b)
            Q.extend([mutate(child_a), mutate(child_b)])
            count += 1

        population = Q
        num_cycles -= 1

    print("--------------------------------------------------------------------------------------")
    print("")
    print(" > Population size: \t\t", population_size)
    print(" > Best feature selection: \t", best)
    print(" > Highest (Best) Fitness: \t", best_Score)
    print("")
    print("--------------------------------------------------------------------------------------")

    return 0

def initialize_population(feature_size, pop_size):
    # init population with random feature configuration
    population = [None] * pop_size
    for i in range (0, pop_size):
        tmp_p = [None] * feature_size
        for j in range (0, feature_size):
            tmp_p[j] = random.randint(0,1)
        population[i] = tmp_p
    return population

def copy(solution):
    copy = deepcopy(solution)
    return copy

def mutate(solution):
    # flips any given value in solution with a 5% chance
    mutation_percentage = 0.05
    mutation = copy(solution)

    for i in range (0, len(mutation)):
        if(random.random() <= mutation_percentage):
            mutation[i] = (mutation[i] + 1) % 2

    return mutation

def stochasticUniversalSampling(population, population_Scores, num_select):
    # https://medium.com/@vishalkhanna/introduction-to-ai-algorithms-part-2-genetic-algorithms-e732b4a4baeb
    total_fitness = 0
    for score in population_Scores:
        total_fitness += score

    point_distance = total_fitness / len(population)
    start_point = np.random.uniform(0, point_distance)
    points = [start_point + i * point_distance for i in range(num_select)]

    parents = []
    while len(parents) < num_select:
        random.shuffle(population)
        idx = 0
        while idx < len(points) and len(parents) < num_select:
            idx = idx + 1
            parents.append(population[idx])

    return parents

def assess_fitness(solution, features, interactions):
    # adds up the values of features selected by the solution
    # then adds the interaction values to fitness if iteraction
    # is spezified in the solution

    fitness = 0
    selected_interactions = []
    for i in range (0, len(solution)):
        if solution[i] == 1:
            fitness += list(features.values())[i]
            selected_interactions.append(list(features.keys())[i])

    for i in range (0, len(interactions)):
        interaction_exists = False

        for j in range (0, len(interactions[i][0])):
            if interactions[i][0][j] not in selected_interactions:
                interaction_exists = False
                break
            else:
                interaction_exists = True

        if(interaction_exists):
            fitness += interactions[i][1]

    return fitness

def towPointCrossover(solution_a, solution_b):
    # chose random Indexes
    rIndex1 = random.randint(0, len(solution_a) - 1)
    rIndex2 = random.randint(0, len(solution_a) - 1)

    # sort random indexes after size
    if(rIndex1 > rIndex2):
        tmp = rIndex2
        rIndex2 = rIndex1
        rIndex1 = tmp

    # concatinate list segments at indexes
    child_a = copy(solution_a[0:rIndex1]) + copy(solution_b[rIndex1:rIndex2]) + copy(solution_a[rIndex2:len(solution_a)])
    child_b = copy(solution_b[0:rIndex1]) + copy(solution_a[rIndex1:rIndex2]) + copy(solution_b[rIndex2:len(solution_a)])

    return child_a, child_b

def uniformCrossover(solution_a, solution_b):
    child_a = copy(solution_a)
    child_b = copy(solution_b)

    # chose at random indexes wich are then swapped
    for i in range (0, len(solution_a)):
        if(random.randint(0,1) == 0):
            tmp = child_a[i]
            child_a[i] = child_b[i]
            child_b[i] = tmp

    return child_a, child_b

def read_lines(path):
    with open(path, "r") as f:
        lines = f.readlines()
    return lines

def get_features(path):
    lines = read_lines(path)
    features = {}
    for line in lines:
        if len(line) <= 0:
            continue
        key = line.split(" ")[0][:-1]
        value = float(line.split(" ")[1])
        features[key] = value
    return features

def get_interactions(path):
    interactions = []
    lines = read_lines(path)
    for line in lines:
        if len(line) <= 0:
            continue
        interaction_key = line.split(" ")[0][:-1].split("#")
        value = float(line.split(" ")[1])
        interactions.append([interaction_key, value])
    return interactions

if __name__ == "__main__":
    # input scheme: run_genetic_alg.py model_features.txt model_interactions.txt
    if len(sys.argv) != 3:
        print("Not a valid input! Please use:" + \
        "python3 run_genetic_alg.py model_features.txt model_interactions.txt")
        sys.exit(0)

    features = get_features(sys.argv[1])
    interactions = get_interactions(sys.argv[2])
    main(features, interactions)
