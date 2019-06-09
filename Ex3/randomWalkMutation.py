import random

def randomWalkMutation(size, min, max, p, c, b):

    vector = initializePopulation(size, min, max)
    heads_trials = 0

    '''
    counts how many trials needed for heads with
    probability 'c' which is then used as count of
    random walk mutations
    '''
    rand_val = random.random()
    while c < rand_val:
        heads_trials = heads_trials + 1
        rand_val = random.random()


    '''
    random walk on initial population. Mutates 'heads_trials'
    times with a probability of 'p'. Add '-1' or '1' to element
    in the population if the result is still valid, with a
    probability 'b' times.
    '''
    for i in range (1, heads_trials):
        if p < random.random():
            rand_val = random.random()
            while b < rand_val:
                rand_val = random.random()
                n = random.choice([-1, 1])
                if inBounds(vector[i] + n, min, max):
                    vector[i] = vector[i] + n
                elif inBounds(vector[i] - n, min, max):
                    vector[i] = vector[i] - n

    return vector


def initializePopulation(population_size, min_value, max_value):
    '''
    initializes a 1D-Integervector of size 'population_size'
    and fills it with random integer values between a given min & max
    '''
    vector = [random.randrange(min_value, max_value, 1) for _ in range(population_size)]
    return vector


def inBounds(value, min_value, max_value):
    '''
    Checks if given value is still valid by seeing if
    it is still withing a min and max
    '''
    if value >= min_value and value <= max_value:
        return True
    return False


if __name__ == "__main__":

    min_value = 0
    max_value = 100
    population_size = 100
    p = 1/size
    c = 0.01
    b = 0.1

    vector = randomWalkMutation(population_size, min_value, max_value, p, c, b)
    print(vector)
