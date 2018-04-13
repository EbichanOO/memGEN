import numpy as np

def trainModel(data):
    memory = {}#load memory
    for i in data:
        memory.append(i)
    return memory

def sample(memoey):
    i = np.rand(len(memoey))
    return memory[i]
