# Gas-Station-Finder 🗺️⛽

A desktop GIS application built with Python that allows users to input their location and find the nearest gas stations within a 5 km radius using spatial queries in PostgreSQL/PostGIS. The app features an interactive map, database integration, and a user-friendly GUI.

## 🚀 Features

- Input coordinates and store them in a PostgreSQL/PostGIS database
- Perform spatial queries using `ST_DWithin` to find nearby gas stations
- Display results in the GUI and optionally on the map
- Add and remove user location points
- Interactive map with left and right click events
- Marker placement and visualization using `tkintermapview`

## 🛠️ Technologies Used

- **Python 3**
- **Tkinter** – GUI framework
- **tkintermapview** – Map widget for Tkinter
- **PostgreSQL** – Relational database
- **PostGIS** – Spatial extension for PostgreSQL
- **psycopg2** – PostgreSQL adapter for Python

## 📦 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/gas-station-finder.git
   cd gas-station-finder
   ```
