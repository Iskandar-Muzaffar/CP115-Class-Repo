import physics_constants

thrown_upward = 2

ball_position = (physics_constants.intial_velocity * thrown_upward) - (0.5 * physics_constants.standard_gravity * thrown_upward ** 2) + physics_constants.building_height
velocity = physics_constants.intial_velocity - (physics_constants.standard_gravity * thrown_upward)
kinetic_energy = 0.5 * physics_constants.ball_mass * velocity ** 2

# Initial conditions
print(f"Initial velocity: {physics_constants.intial_velocity} m/s")
print(f"Building height: {physics_constants.building_height} m")
print(f"Ball mass: {physics_constants.ball_mass} kg")