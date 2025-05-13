import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from scipy import stats

# Initial parameters
n = 10
p_init = 0.9
size = 1000

# Initial data
variables = stats.geom.rvs(p=p_init, size=size)

fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)  # Make space for slider

# Initial histogram
hist = ax.hist(variables, bins=10, density=True, alpha=0.5, 
               color='darkgreen', label='Simulated Data')
ax.set_title(f'Geometric Distribution (p={p_init:.2f})')
ax.set_xlabel('Number of Successes')
ax.set_ylabel('Density')
ax.legend()

# Slider axis: [left, bottom, width, height]
ax_p = plt.axes([0.2, 0.1, 0.65, 0.03])
slider_p = Slider(ax_p, 'p', 0.0, 1.0, valinit=p_init, valstep=0.01)

def update(val):
    p = slider_p.val
    ax.clear()
    variables = stats.geom.rvs(p=p, size=size)
    ax.hist(variables, bins=10, density=True, alpha=0.5, 
            color='darkgreen', label='Simulated Data')
    ax.set_title(f'Geometric Distribution (p={p:.2f})')
    ax.set_xlabel('Number of Successes')
    ax.set_ylabel('Density')
    ax.legend()
    fig.canvas.draw_idle()

slider_p.on_changed(update)

plt.show()