import pandas as pd

df = pd.read_csv("Average_CO2.csv")

groupby_year = df["Average CO2 in ppm"].groupby(df["Year"]).mean()

groupby_year.to_csv("Average_CO2_mean.csv")