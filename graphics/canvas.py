import matplotlib.pyplot as plt
import numpy as np

class Canvas:
    def __init__(self):
        self.fig, self.ax = plt.subplots()
        self.ax.set_aspect('equal')
        plt.xlabel('$a$ (AU)')
        plt.ylabel('$e$ (eccentricity)')
        plt.title('Intercepting orbits')
        plt.axhline(y=0, color='gray', linestyle='--', linewidth=0.5)
        plt.axvline(x=1, color='gray', linestyle='--', linewidth=0.5)
        plt.grid(True, linestyle='--', alpha=0.5)


    def save(self, filename):
        self.fig.savefig(filename)

    def plot(self, x, y, label=None, real_data = False, color='black'):

        if not real_data:
            self.ax.plot(x, y, label=label, linestyle='--', linewidth=1)
            if label:
                plt.legend(loc='best')
        else:
            self.ax.plot(x, y, marker='o', markersize=2, c=color)

    def fill(self, bounds: tuple[float, float], bounds_names: tuple[str, str], x_range: np.ndarray, colors:tuple[str, str], color_fill='gray', alpha=0.3):
        """
        Fill the area between two curves.

        Parameters:
        bounds: tuple[float, float]
            Lower and upper bounds of the area to fill.
        bounds_names: tuple[str, str]
            Names of the bounds.
        x_range: np.ndarray
            Range of x values.
        color: str
            Color of the filled area.
        alpha: float
            Transparency of the filled area.

        Returns: None
        """
        plt.fill_between(x_range, bounds[0], bounds[1], color=color_fill, alpha=alpha)
        plt.plot(x_range, bounds[0], color=colors[0], label=bounds_names[0])
        plt.plot(x_range, bounds[1], color=colors[1], label=bounds_names[1])
        plt.ylim(-0.03, 1)
        plt.xlim(min(x_range), max(x_range))        
        plt.legend(loc='best')
        
