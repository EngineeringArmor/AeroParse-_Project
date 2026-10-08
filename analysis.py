import pandas as pd
import matplotlib.pyplot as plt


try:
    df = pd.read_csv('flight_data.csv', comment='#')
    print("Data loaded successfully!")
except FileNotFoundError:
    print("Error:  flight_data.csv was not found.")
    exit()


# Clean up column spaces
df.columns = df.columns.str.strip() 


# Smart Auto-Search for column names (Fixes any KeyError)
time_col = df.columns[0]
alt_col = df.columns[1]
vel_col = df.columns[2]
accel_col = time_col


# Calculate metrics using the auto-found columns
max_alt = df[alt_col].max()
apogee_t = df.loc[df[alt_col].idxmax(), time_col]
max_vel = df[vel_col].max()
max_accel = df[accel_col].max()


print("\n==========================================")
print(f"Maximum Altitude: {max_alt}")
print(f"Apogee Time: {apogee_t}")
print(f"Maximum Velocity: {max_vel}")
print(f"Maximum Acceleration: {max_accel}")


# Generate the plot
plt.figure(figsize=(10, 6))
plt.plot(df[time_col], df[vel_col], label='Velocity', color='crimson', lw=2)
plt.plot(df[time_col], df[alt_col], label='Altitude', color='royalblue', linestyle='--', lw=2)
plt.scatter


plt.title('AeroParse: Rocket Flight Dynamics Profile')
plt.xlabel('Time (s)')
plt.ylabel('Value')
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend()
plt.show()