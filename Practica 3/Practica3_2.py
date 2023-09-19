import scipy.stats as stats
import math

std_deviation = 0.0015
sample_size = 75
sample_mean = 0.310
confidence_level = 0.95

standard_error_mean = std_deviation / math.sqrt(sample_size)

degrees_of_freedom = sample_size - 1
critical_value = stats.t.ppf((1 + confidence_level) / 2, df=degrees_of_freedom)

confidence_interval = (
    sample_mean - critical_value * standard_error_mean,
    sample_mean + critical_value * standard_error_mean
)

print(f"{confidence_level * 100}% confidence interval for the mean depth:")
print(f"({confidence_interval[0]:.5f}, {confidence_interval[1]:.5f}) inches")
