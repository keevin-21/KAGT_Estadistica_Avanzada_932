import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

male_heights = np.array([175, 180, 170, 185, 178, 172, 188, 182, 177, 169])
female_heights = np.array([162, 165, 160, 168, 158, 163, 166, 164, 159, 161])

mean_male = np.mean(male_heights)
std_deviation_male = np.std(male_heights, ddof=1)
mean_female = np.mean(female_heights)
std_deviation_female = np.std(female_heights, ddof=1)

n_male = len(male_heights)
n_female = len(female_heights)

confidence = 0.95

mean_difference = mean_male - mean_female
standard_error = np.sqrt((std_deviation_male**2 / n_male) +
                         (std_deviation_female**2 / n_female))
margin_error = stats.t.ppf((1 + confidence) / 2, df=(n_male + n_female - 2)) * standard_error
confidence_interval = (mean_difference - margin_error, mean_difference + margin_error)

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.hist(male_heights, bins=10, alpha=0.5, color='blue', label='Hombres')
plt.hist(female_heights, bins=10, alpha=0.5, color='red', label='Mujeres')
plt.title('Histograma de Alturas')
plt.xlabel('Altura (cm)')
plt.ylabel('Frecuencia')
plt.legend()
plt.subplot(1, 2, 2)
plt.bar(['Diferencia de Medias'], [mean_difference],
        yerr=margin_error, color='green', alpha=0.7)
plt.title('Diferencia de Medias con Intervalo de Confianza')
plt.xlabel('Diferencia de Medias')
plt.ylabel('Intervalo de Confianza')
plt.tight_layout()
plt.show()

print("Diferencia de medias:", mean_difference)
print("Intervalo de confianza al {}%:".format(int(confidence * 100)), confidence_interval)
