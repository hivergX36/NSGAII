from NSGAIIAlgorithm import NSGAIIAlgorithm
import random
import os


fileName = "knapsack.txt"


NSGAII = NSGAIIAlgorithm(30,10)
NSGAII.parseKnapsack(fileName)
NSGAII.resolve(12)


