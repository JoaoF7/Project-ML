import matplotlib.pyplot as plt
import numpy as np


def visualize_dimensionality_reduction(transformation, targets):
  # create a scatter plot of the t-SNE output
  plt.scatter(transformation[:, 0], transformation[:, 1], 
              c=np.array(targets).astype(int), cmap=plt.cm.tab10)

  labels = np.unique(targets)

  # create a legend with the class labels and colors
  handles = [plt.scatter([],[], c=plt.cm.tab10(i), label=label) for i, label in enumerate(labels)]
  plt.legend(handles=handles, title='Classes')

  plt.show()
  
