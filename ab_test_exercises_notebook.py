# A/B Testing – Exercise Notebook (Questions Only)

# This notebook is structured to simulate a real technical interview / applied data science workflow.
# Do NOT jump to conclusions. Show reasoning, formulas, and interpretation.

# ==============================
# SECTION 1 — SAMPLING DISTRIBUTION
# ==============================

# Q1: Population vs Sample
# You have a population with mean = 100 and std = 20.
# You take samples of size n = 25.
#
# a) What is the expected mean of the sampling distribution?
# b) What is the standard error?
# c) Explain intuitively why standard error decreases with n.


# Q2: Simulation of Sampling Distribution
# Generate a population using a normal distribution (mean=100, std=20, size=100000).
# Draw 1000 samples of size 25 and compute their means.
#
# a) Plot the distribution of sample means
# b) Compare empirical std with theoretical standard error


# ==============================
# SECTION 2 — CENTRAL LIMIT THEOREM
# ==============================

# Q3: CLT Understanding
#
# a) Explain why the sampling distribution becomes approximately normal
# b) At what conditions does CLT fail or become unreliable?


# ==============================
# SECTION 3 — CONFIDENCE INTERVALS
# ==============================

# Q4: Confidence Interval
# A sample has mean = 52, std = 10, n = 100
#
# a) Compute 95% CI
# b) Interpret the interval correctly (frequentist interpretation)


# Q5: Practical Interpretation
# Why is "there is a 95% chance the true mean is inside the interval" incorrect?


# ==============================
# SECTION 4 — HYPOTHESIS TESTING
# ==============================

# Q6: Z-test
# Null hypothesis: mean = 50
# Sample mean = 52, std = 10, n = 100
#
# a) Compute Z-statistic
# b) Compute p-value
# c) Decision at alpha=0.05


# Q7: Type I and II Errors
#
# a) Define both errors
# b) Which one is more dangerous in a product A/B test context?


# ==============================
# SECTION 5 — A/B TEST FUNDAMENTALS
# ==============================

# Q8: Conversion Rate
# Control: 200 conversions out of 2000 users
# Treatment: 260 conversions out of 2000 users
#
# a) Compute conversion rates
# b) Compute lift


# Q9: Two-Proportion Z-Test
#
# a) Compute pooled probability
# b) Compute standard error
# c) Compute Z-statistic
# d) Interpret result


# ==============================
# SECTION 6 — STATISTICAL POWER
# ==============================

# Q10: Power Analysis
#
# a) Define statistical power
# b) What increases power?
# c) What happens if sample size is too small?


# ==============================
# SECTION 7 — PRACTICAL PITFALLS
# ==============================

# Q11: Peeking Problem
# Why is checking results daily dangerous?


# Q12: Multiple Testing
# What happens if you run 20 experiments simultaneously?


# ==============================
# SECTION 8 — BUSINESS INTERPRETATION
# ==============================

# Q13: Practical Significance vs Statistical Significance
#
# Treatment improves conversion from 10% to 10.2% with p < 0.01
#
# a) Is it worth deploying?
# b) What additional information do you need?


# Q14: Experiment Validity
#
# List at least 5 threats to validity in A/B testing


# END OF NOTEBOOK
