import matplotlib.pyplot as plt
import pandas as pd

# Климатические данные и PM10 (пылевая загрязненность) для Нукуса (пример выборки)
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    'Avg_Temp_C': [-1.5, 0.8, 7.5, 16.2, 23.1, 28.4, 30.2, 28.0, 21.5, 13.2, 5.8, 0.2],
    'Dust_Days_PM10': [2, 3, 5, 8, 12, 15, 18, 14, 9, 6, 3, 1]
}

df = pd.DataFrame(data)

# Расчет корреляции между температурой и частотой пылевых бурь
correlation = df['Avg_Temp_C'].corr(df['Dust_Days_PM10'])
print(f"Correlation between Temp and Dust Storm Days: {correlation:.2f}")

# Построение двойного графика
fig, ax1 = plt.subplots(figsize=(10, 5))

color = 'tab:red'
ax1.set_xlabel('Month')
ax1.set_ylabel('Avg Temp (°C)', color=color)
ax1.plot(df['Month'], df['Avg_Temp_C'], color=color, marker='o', linewidth=2)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()  
color = 'tab:gray'
ax2.set_ylabel('Dust Storm Days (PM10 High)', color=color)
ax2.bar(df['Month'], df['Dust_Days_PM10'], color=color, alpha=0.3)
ax2.tick_params(axis='y', labelcolor=color)

plt.title('Nukus: Monthly Temperature vs. Dust Storm Frequency', fontsize=12, fontweight='bold')
fig.tight_layout()  
plt.savefig('nukus_climate_dust.png', dpi=300)
print("Chart saved as 'nukus_climate_dust.png'")