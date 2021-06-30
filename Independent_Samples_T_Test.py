# import packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from scipy.stats import ttest_ind, norm


# create mock data
sample_A = norm.rvs(loc = 500, scale = 100, size = 250, random_state = 42).astype(int)
sample_B = norm.rvs(loc = 550, scale = 150, size = 100, random_state = 42).astype(int)

plt.hist(sample_A, density = True, alpha = 0.5)
plt.hist(sample_B, density = True, alpha = 0.5)
plt.show()

sample_A_mean = sample_A.mean()
sample_B_mean = sample_B.mean()
print(sample_A_mean, sample_B_mean)


# set the hypotheses & acceptance criteria
null_hypothesis = "The mean of Sample A is equal to the mean of Sample B"
alternate_hypothesis = "The mean of Sample A is different to the mean of Sample B"
acceptance_criteria = 0.05


# execute hypothesis test
t_statistic, p_value = ttest_ind(sample_A, sample_B)
print(t_statistic, p_value)


# print results (p-value)
if p_value <= acceptance_criteria:
    print(f"As our p_value of {p_value} is lower than our acceptance_criteria of {acceptance_criteria} - we reject the null hypothesis, and conclude that: {alternate_hypothesis}.")
else:
    print(f"As our p_value of {p_value} is higher than our acceptance_criteria of {acceptance_criteria} - we retain the null hypothesis, and conclude that: {null_hypothesis}.")



# WELCH'S T-TEST

# execute hypothesis test
t_statistic, p_value = ttest_ind(sample_A, sample_B, equal_var = False)
print(t_statistic, p_value)

# print results (p-value)
if p_value <= acceptance_criteria:
    print(f"As our p_value of {p_value} is lower than our acceptance_criteria of {acceptance_criteria} - we reject the null hypothesis, and conclude that: {alternate_hypothesis}.")
else:
    print(f"As our p_value of {p_value} is higher than our acceptance_criteria of {acceptance_criteria} - we retain the null hypothesis, and conclude that: {null_hypothesis}.")











