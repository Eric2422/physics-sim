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
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        self.data_frame = data_frame

        self.num_particles = len(data_frame[data_frame['t'] == 0])

        initial_data = data_frame[data_frame['t'] == 0]
        # Plot points, one for each particle.
        self.plot, = ax.plot(
            initial_data.x,
            initial_data.y,
            initial_data.z,
            linestyle="",
            marker="o"
        )

        ax.margins(1, 1, 1)
        plt.xlim(left=-25, right=25)
        plt.ylim(bottom=-25, top=25)
        ax.set_zlim(-25, 25)

        # The animation runs at real speed.
        self.plot_animation = animation.FuncAnimation(
            fig,
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
        # The particles are flattened into a single data frame,
        # so `start_index` is the index of the first particle,
        # and `end_index` is the index of the last particle
        start_index = num * self.num_particles
        end_index = start_index + 2

        # Stop the function from going out of bounds
        if end_index > len(self.data_frame):
            return self.plot,

        data = self.data_frame.loc[start_index: end_index]

        self.plot.set_data(data.x, data.y)
        self.plot.set_3d_properties(data.z)

        return self.plot,

    def show(self) -> None:
        """Display this plot and run the animation. """
        plt.show()
