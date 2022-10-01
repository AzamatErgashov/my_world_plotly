import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.express as px

df = pd.read_csv("world_population.csv")

my_px = px.scatter_geo(df,
                       locations="CCA3",
                       projection="orthographic",
                       color="Country",
                       opacity=0.8,
                       hover_name="Country",
                       hover_data=["2020 Population","Capital"])
my_px.show()
