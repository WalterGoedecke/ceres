"""
module: MeteoPlot
"""

import numpy
import pandas
#from matplotlib import pyplot
import matplotlib 
import seaborn

# Set universal plot preferences upon module import.
matplotlib.pyplot.rcParams.update(
    {"figure.dpi" : 300,
     "font.size" : 14,
     "mathtext.default" : "regular",
     "axes.grid.which" : "both",
     "axes.titlesize" : 14,
     "axes.labelsize" : 14,
     "xtick.labelsize" : 12,
     "ytick.labelsize" : 12,
     "lines.linewidth" : 4,
     "grid.linewidth" : 2,
     "legend.frameon" : True,
     "legend.shadow" : True,
     "legend.loc" : "upper left",
     "legend.fontsize" : 12})

