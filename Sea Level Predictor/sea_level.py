import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # 1. Import data
    df = pd.read_csv("D:\\Data Analytics\\Sea Level Predictor\\epa-sea-level.csv")

    # 2. Scatter plot
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])

    # 3. First line of best fit (all data)
    res = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])

    # Extend years to 2050
    years_extended = list(range(df["Year"].min(), 2051))
    sea_level_pred = [res.slope * year + res.intercept for year in years_extended]

    plt.plot(years_extended, sea_level_pred, color="red")

    # 4. Second line of best fit (from year 2000)
    df_recent = df[df["Year"] >= 2000]

    res_recent = linregress(df_recent["Year"], df_recent["CSIRO Adjusted Sea Level"])

    years_recent = list(range(2000, 2051))
    sea_level_recent_pred = [res_recent.slope * year + res_recent.intercept for year in years_recent]

    plt.plot(years_recent, sea_level_recent_pred, color="green")

    # 5. Labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")

    # 6. Save and return
    plt.savefig("sea_level_plot.png")
    return plt.gca()

draw_plot()
plt.show()
