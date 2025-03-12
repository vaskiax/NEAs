class Canvas():
    import matplotlib.pyplot as plt
    import numpy as np

    def __init__(self, width=10, height=10):
        self.fig, self.ax = self.plt.subplots(figsize=(width, height))
        self.ax.set_aspect('equal')
        self.ax.set_axis_off()

    def draw(self):
        self.plt.show()

    def save(self, filename):
        self.fig.savefig(filename)

    def plot(self, x, y, color='black', marker='o', markersize=5):
        self.ax.plot(x, y, color=color, marker=marker, markersize=markersize)

