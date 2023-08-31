import geopandas as gpd
import psycopg2
import matplotlib.pyplot as plt

# Establish a database connection
def connect_surface_area_db():
    return psycopg2.connect(
        dbname="country_surface_area",
        user="postgres",
        password="3204965",
        host="localhost",
        port="5432"
    )

# Execute the query and retrieve highlighted countries' ISO codes
def execute_query(query):
    conn = connect_surface_area_db()
    cursor = conn.cursor()
    cursor.execute(query)
    highlighted_iso_codes = [row[0] for row in cursor.fetchall()]
    conn.close()
    return highlighted_iso_codes

# Load built-in world geometries
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# Execute the query to get highlighted countries' ISO codes
query = """SELECT iso_code FROM countries_coastal;"""
highlighted_iso_codes = execute_query(query)

# Filter the world geometries to include only the highlighted countries
highlighted_world = world[world['iso_a3'].isin(highlighted_iso_codes)]

# Plot the world map
fig, ax = plt.subplots(figsize=(12, 8))

# Plot the world map first as the background
world.plot(ax=ax, color='lightgrey')

# Plot the highlighted countries on top of the world map
highlighted_world.plot(ax=ax, color='green', edgecolor='black', alpha=0.7, label='Highlighted Countries')

# Customize the plot
ax.set_title('World Map with Highlighted Coastal Countries')
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')
ax.legend()

# Show the plot
plt.show()
