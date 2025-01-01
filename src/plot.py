import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


class Plot():
    def __init__(self, data_frame: pd.DataFrame, tick_size: np.float64 = 1.0) -> None:
        """Create a 3D NumPy plot.

        Parameters
        ----------
        data_frame : pd.DataFrame
            A data frame with four columns: t, x, y, z
            Contains the time and position of particles.
        tick_size : np.float64, optional
            The amount of time between each frame, by default 1.0
        """
        self.figure = plt.figure()
        self.ax = self.figure.add_subplot(111, projection='3d')

        self.data_frame = data_frame
        print(data_frame)
        print()

        # Plot scatter points, one for each particle.
        self.plot, = self.ax.plot(
            data_frame[data_frame['t'] == 0].x,
            data_frame[data_frame['t'] == 0].y,
            data_frame[data_frame['t'] == 0].z, 
            linestyle="", 
            marker="o"
        )

        self.ax.margins(1, 1, 1)
        plt.xlim(left=-10, right=10)
        plt.ylim(bottom=-10, top=10)
        self.ax.set_zlim(-10, 10)

        self.tick_size = tick_size
        # The animation runs at real speed.
        self.plot_animation = animation.FuncAnimation(
            self.figure,
            self.update,
            interval=tick_size / 1000,  # Convert from seconds to milliseconds.
            blit=True
        )

    def update(self, num: int):
        """Update the plot points of the scatter. 

        Parameters
        ----------
        num : int
            The number of intervals that have elapsed.
        """
        if num >= len(self.data_frame):
            return self.plot,

        print(self.data_frame[])
        print(f't: {num * self.tick_size}')
        data = self.data_frame[self.data_frame['t'] == num * self.tick_size]
        print(f'data: {data}')
        print()

        self.plot.set_data_3d(data.x, data.y, data.z)

        return self.plot,

    def show(self) -> None:
        """Display this plot and run the animation. """
        plt.show()
