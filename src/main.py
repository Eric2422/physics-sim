import sys

import numpy as np

from files import Files
from particle import Particle

class Simulation():
    def __init__(self, particles: list, delta_time: float = 1.0) -> None:
        """
        Creates one simulation.

        Parameters
        ----------
        particles : list
            A list of particles that are interacting with each other
        delta_time : float, optional
            The amount of time between each tick in seconds, by default 1.0
        """
        self.particles = particles

        self.delta_time = delta_time
        pass


if __name__ == '__main__':
    # Check if the user supplied a config file
    if len(sys.argv) < 2:
        print('Please enter the name of the config file.')
        sys.exit()

    file_data = Files.read_config_file(sys.argv[1])
    particles = [
        Particle(
            np.array((line[0], line[1], line[2])), 
            line[3],
            line[4]         
        )
        for line in file_data
    ]

    print(particles[0].coulumbs_law(particles[1]))