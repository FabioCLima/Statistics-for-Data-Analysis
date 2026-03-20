# A/B Testing – Solutions Notebook

import numpy as np
import scipy.stats as stats

# ==============================
# SECTION 1 — SAMPLING DISTRIBUTION
# ==============================

# Q1
population_mean = 100
population_std = 20
n = 25

expected_mean = population_mean
standard_error = population_std / np.sqrt(n)

print("Expected Mean:", expected_mean)
print("Standard Error:", standard_error)

# ==============================
# Q2
population = np.random.normal(100, 20, 100000)

sample_means = []
for _ in range(1000):
    sample = np.random.choice(population, size=25)
    sample_means.append(np.mean(sample))

print("Empirical SE:", np.std(sample_means))
print("Theoretical SE:", standard_error)

# ==============================
# SECTION 3 — CONFIDENCE INTERVAL
# ==============================

mean = 52
std = 10
n = 100

se = std / np.sqrt(n)
z = 1.96

ci_lower = mean - z * se
ci_upper = mean + z * se

print("95% CI:", (ci_lower, ci_upper))

# ==============================
# SECTION 4 — HYPOTHESIS TEST
# ==============================

z_stat = (mean - 50) / se
p_value = 2 * (1 - stats.norm.cdf(abs(z_stat)))

print("Z-stat:", z_stat)
print("p-value:", p_value)

# ==============================
# SECTION 5 — A/B TEST
# ==============================

control_conv = 200
control_n = 2000

treatment_conv = 260
treatment_n = 2000

p1 = control_conv / control_n
p2 = treatment_conv / treatment_n

lift = (p2 - p1) / p1

print("Control:", p1)
print("Treatment:", p2)
print("Lift:", lift)

# Two proportion z-test
p_pool = (control_conv + treatment_conv) / (control_n + treatment_n)
se = np.sqrt(p_pool * (1 - p_pool) * (1/control_n + 1/treatment_n))

z_stat = (p2 - p1) / se
p_value = 2 * (1 - stats.norm.cdf(abs(z_stat)))

print("Z-stat:", z_stat)
print("p-value:", p_value)

# ==============================
# INTERPRETATION GUIDE
# ==============================

# If p-value < 0.05 → reject H0
# Always check effect size + business impact
# Never rely only on statistical significance

# END OF SOLUTIONS
