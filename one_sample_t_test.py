# import packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from scipy.stats import ttest_1samp, norm


# create mock data
population = norm.rvs(loc = 500, scale = 100, size = 1000, random_state = 42).astype(int)

np.random.seed(42)
sample = np.random.choice(population, 250)

plt.hist(population, density = True, alpha = 0.5)
plt.hist(sample, density = True, alpha = 0.5)
plt.show()

population_mean = population.mean()
sample_mean = sample.mean()
print(population_mean, sample_mean)


# set the hypotheses & acceptance criteria
null_hypothesis = "The mean of the sample is equal to the mean of the population"
alternate_hypothesis = "The mean of the sample is different to the mean of the population"
acceptance_criteria = 0.05


# execute hypothesis test
t_statistic, p_value = ttest_1samp(sample, population_mean)
print(t_statistic, p_value)


# print results (p-value)
if p_value <= acceptance_criteria:
    print(f"As our p_value of {p_value} is lower than our acceptance_criteria of {acceptance_criteria} - we reject the null hypothesis, and conclude that: {alternate_hypothesis}.")
else:
    print(f"As our p_value of {p_value} is higher than our acceptance_criteria of {acceptance_criteria} - we retain the null hypothesis, and conclude that: {null_hypothesis}.")





