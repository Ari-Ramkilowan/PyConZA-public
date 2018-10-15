
import numpy as np
from scipy.stats import kendalltau
import matplotlib.pyplot as plt
import seaborn as sns

rs = np.random.RandomState(42)
x = rs.gamma(2, size=1000)
y = -0.5 * x + rs.normal(size = 1000)

sns.jointplot(x, y, kind="hex", stat_func=kendalltau, color = "#4271f4")
plt.show()