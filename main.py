# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants for planetary orbits (semi-major axis in astronomical units - AU)
# These values are approximate and not exact
# One AU is the distance from Earth to the Sun
AU = 1.496e11  # meters
G = 6.67430e-11  # gravitational constant in m^3 kg^-1 s^-2
Msun = 1.989e30  # mass of the Sun in kg
day_to_seconds = 86400  # 1 day in seconds

# Dictionary containing planet orbital data (planet: [semi-major axis (AU), orbital period (days)])
planets_data = {
    'Mercury': [0.387, 88],
    'Venus': [0.723, 225],
    'Earth': [1.000, 365],
    'Mars': [1.524, 687],
    'Jupiter': [5.204, 4331],
    'Saturn': [9.582, 10747],
    'Uranus': [19.201, 30589],
    'Neptune': [30.047, 59800],
}

# Function to calculate the positions of a planet at a given time (theta = 2πt/T)
def calculate_orbit(semi_major_axis, orbital_period, time_days):
    """Calculate the position of a planet in its elliptical orbit."""
    theta = 2 * np.pi * time_days / orbital_period  # Angular position in orbit
    x = semi_major_axis * np.cos(theta)  # x-coordinate in AU
    y = semi_major_axis * np.sin(theta)  # y-coordinate in AU
    return x, y

# Initialize the plot
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_aspect('equal')
ax.set_xlim(-35, 35)
ax.set_ylim(-35, 35)

# Add the Sun at the center of the plot
sun = plt.Circle((0, 0), 0.1, color='yellow', label="Sun")
ax.add_artist(sun)

# Initialize a dictionary to store the planetary orbits and points for each planet
orbits = {}
points = {}

# Create plot lines for each planet's orbit and its current position (point)
for planet in planets_data:
    semi_major_axis = planets_data[planet][0]  # Semi-major axis in AU
    orbital_period = planets_data[planet][1]   # Orbital period in days
    
    # Add the orbit as a line and initialize the point for the planet
    orbits[planet], = ax.plot([], [], label=planet)  # Line for orbit
    points[planet], = ax.plot([], [], 'o', markersize=5)  # Point for planet

# Set labels, title, and legend
ax.set_xlabel('x (AU)')
ax.set_ylabel('y (AU)')
ax.set_title('Trajectories of Planets in the Solar System')
ax.legend(loc='upper right')

# Define the initialization function for the animation
def init():
    """Initialize the animation."""
    for planet in planets_data:
        orbits[planet].set_data([], [])
        points[planet].set_data([], [])
    return orbits.values(), points.values()

# Define the update function for the animation (called for each frame)
def update(frame):
    """Update the positions of planets for the current frame (time step)."""
    time_days = frame  # Time in days (1 frame = 1 day)
    
    # Update positions for each planet
    for planet in planets_data:
        semi_major_axis, orbital_period = planets_data[planet]
        
        # Calculate the planet's current position in its orbit
        x, y = calculate_orbit(semi_major_axis, orbital_period, time_days)
        
        # Update orbit and point data
        orbits[planet].set_data([0, x], [0, y])  # Draw line from the Sun to the planet
        points[planet].set_data(x, y)  # Update the planet's current position
    
    return orbits.values(), points.values()

# Create the animation
ani = FuncAnimation(fig, update, frames=np.arange(0, 59800, 10), init_func=init, interval=50, blit=True)

# Show the animation
plt.show()
