import pandas as pd
import matplotlib.pyplot as plt

data_dict = {
    'year': [1629, 1630, 1631, 1632, 1633, 1634, 1635, 1636, 1637, 1638],
    'boys': [5218, 4858, 4422, 4994, 5158, 5035, 5106, 4917, 4703, 5359],
    'girls': [4683, 4457, 4102, 4590, 4841, 4912, 4928, 4783, 4661, 5473]
}

df = pd.DataFrame(data_dict)

plt.figure(figsize=(12, 6))
plt.plot(df['year'], df['boys'], label='Boys')
plt.plot(df['year'], df['girls'], label='Girls')
plt.xlabel('Year')
plt.ylabel('Births')
plt.title('Births of Boys and Girls Over the Years')
plt.legend()
plt.show()

df['total_births'] = df['boys'] + df['girls']
df['prop_boys'] = df['boys'] / df['total_births']
df['prop_girls'] = df['girls'] / df['total_births']
df['comparison'] = df['prop_boys'] > df['prop_girls']

print(df)

