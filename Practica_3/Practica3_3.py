import scipy.stats as stats
import math

population_mean = 3
standard_deviation = 1.6
sample_size = 48
confidence_level = 0.95

standard_error_mean = standard_deviation / math.sqrt(sample_size)

degrees_of_freedom = sample_size - 1
critical_value = stats.t.ppf((1 + confidence_level) / 2, df=degrees_of_freedom)

confidence_interval = (
    population_mean - critical_value * standard_error_mean,
    population_mean + critical_value * standard_error_mean
)

print(f"{confidence_level * 100}% confidence interval for the mean price:")
print(f"(${confidence_interval[0]:.2f}, ${confidence_interval[1]:.2f}) per kilogram")
