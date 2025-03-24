import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Function to check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Generate prime numbers up to 10,000
primes = [i for i in range(1, 10000) if is_prime(i)]
df = pd.Series(primes)

# Calculate prime gaps
prime_gaps = df.diff().dropna()

# --- Prime Gap Line Plot ---
plt.figure(figsize=(10, 5))
plt.plot(prime_gaps, color="blue", alpha=0.7)
plt.xlabel("Index (Nth Prime)")
plt.ylabel("Prime Gap")
plt.title("Gaps Between Consecutive Primes")
plt.grid(True)
plt.savefig("prime gap line plot")

# --- Prime Gap Histogram ---
plt.figure(figsize=(10, 5))
plt.hist(prime_gaps, bins=20, edgecolor="black", alpha=0.7)
plt.xlabel("Prime Gap Size")
plt.ylabel("Frequency")
plt.title("Distribution of Prime Gaps")
plt.grid(True)
plt.savefig("prime gap histogram")

# --- Cumulative Sum of Prime Gaps ---
plt.figure(figsize=(10, 5))
plt.plot(prime_gaps.cumsum(), color="g")
plt.xlabel("Index (Nth Prime)")
plt.ylabel("Cumulative Sum of Prime Gaps")
plt.title("Cumulative Growth of Prime Gaps")
plt.grid(True)
plt.savefig("sum of prime gaps")

# --- Prime Gaps vs. Logarithmic Growth ---
log_values = np.log(df[1:])  # log of prime numbers

plt.figure(figsize=(10, 5))
plt.plot(df[1:], prime_gaps, label="Prime Gaps", color="b")
plt.plot(df[1:], log_values, label="log(n)", color="r", linestyle="dashed")
plt.xlabel("Prime Numbers")
plt.ylabel("Prime Gap")
plt.title("Prime Gaps vs. Logarithmic Growth")
plt.legend()
plt.grid(True)
plt.savefig("prime gaps vs log growth")

