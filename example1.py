# importing the module
import pandas as pd
import stemgraphic as sg

data = [16, 25, 47, 56, 23, 45, 19, 55, 44, 27]
y = pd.Series(data)

# Create the stem and leaf plot
fig, ax = sg.stem_graphic(y)
