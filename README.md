🗂️ Python Data Handling & Visualization – Part 2

My continued journey in learning how to work with real-world datasets in Python and visualize meaningful patterns from them.

📚 About This Project

Welcome to my Python Data Handling & Visualization – Part 2 repository!
This project continues my data visualization learning journey — this time focusing on real-world datasets.

The exercises and code here are inspired by the Working with Data chapters from Python Crash Course by Eric Matthes.
Each file represents progress in handling structured data, extracting useful information, and visualizing it effectively using Matplotlib and Plotly.

The goal is to understand how real datasets are formatted, cleaned, and transformed into meaningful visuals that communicate insights clearly.

🚀 What This Project Covers

This repository includes a collection of Python scripts that explore how to process and visualize data from CSV and JSON files.

You’ll find examples such as:

📂 Loading and Parsing Data: Extracting values from CSV and JSON files using Python’s built-in libraries.

📊 Multi-Series Charts: Plotting multiple data series, like temperature highs and lows, on a single graph.

🌦️ Weather Data Visualization: Using historical climate data to understand temperature variations.

🌍 Earthquake Mapping: Displaying geographical earthquake data interactively on a world map.

🕒 Datetime Operations: Parsing and working with date-based data efficiently.

🎨 Custom Styling: Enhancing visualizations with color, shading, and labels for readability.

⚠️ Error Handling: Managing missing or incomplete data entries gracefully.

🧠 Concepts Learned

Extracting and reading data from CSV and JSON files.

Using Matplotlib for line charts and multiple data series.

Using Plotly for interactive visualizations and maps.

Working with the datetime module to manage time-based datasets.

Plotting global earthquake data on maps with customized markers.

Handling missing or corrupted data using proper exception management.

🧰 Tools & Libraries

Python — Core programming language

Matplotlib — For plotting temperature data and trends

Plotly — For interactive map-based visualizations

CSV & JSON modules — For reading structured datasets

Datetime — For parsing and formatting date values

📁 File Overview
learning-data_pt.2/
│
├── mapping_global_data_sets/        # Folder containing global mapping data files
├── the_csv_file_format/             # Folder containing sample CSV weather files
│
├── death_valley_highs_lows.py       # Plots highs & lows for Death Valley temperature data
├── sitka_highs.py                   # Plots Sitka temperature trends
├── sitka_highs_lows.py              # High/low temp plots with error handling for missing data
│
├── eq_data_readable.json            # Cleaned earthquake dataset in JSON format
├── eq_explore_data.py               # Extracts earthquake details from JSON
├── eq_world_map.py                  # Plots earthquake locations on Plotly world map
│
└── README.md                        # Project documentation (this file)

🧭 Learning Reflection

In this phase of my learning journey, I moved from synthetic data generation to working with real-world datasets.
Handling CSV and JSON files taught me how data often needs cleaning and structuring before visualization.

I learned to combine technical skills with visual storytelling — plotting meaningful insights from raw data, managing errors, and understanding trends over time.

This project helped strengthen my foundation for analyzing real datasets, visualizing global patterns, and preparing for more complex analytical and machine learning projects in the future.

🤝 Note

This repository is intended purely for learning and sharing knowledge.
Feel free to explore the scripts, modify the visualizations, and use these examples as inspiration for your own projects.
