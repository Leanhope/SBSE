#!python3
import sys


def main(features, interactions):
    # TODO: to implement
    pass

def optimize(population):
    # TODO: to implement
    pass


def initialize_population(feature_size, pop_size):
    # TODO: to implement
    pass


def copy(solution):
    # TODO: to implement
    pass


def tweak(solution):
    # TODO: to implement
    pass


def select(population):
    # TODO: to implement
    pass


def crossover(solution_a, solution_b):
    # TODO: to implement
    pass


def assess_fitness(solution):
    # TODO: to implement
    pass

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