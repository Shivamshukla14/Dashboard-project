## Cricket Dashboard with Streamlit

![Screenshot (51)](https://github.com/Shivamshukla14/Dashboard-project/assets/80144030/60d8c931-019c-4ad7-9be9-7f0e1d6fd21b)

**Project Description**

This Streamlit application creates a Cricket Dashboard to explore data about the most runs scored in International Cricket (ODI, Test, T20).

**Features**

* **Player Statistics Overview:** Provides key metrics on player count, average matches played, strike rate, and average score.
* **Plotly Visualizations:**
    * **Pie Chart:** Distribution of runs scored by country.
    * **Bar Charts:** Top run scorers and player contribution by runs (horizontal bar chart).
    * **Scatter Plot:** Innings vs runs scored (country-wise).
    * **Comparison Bar Chart:** Compares two selected players across various metrics (matches, runs, high score, strike rate, 100s, 50s).

**Data Requirements**

The dashboard relies on a dataset named `most_runs_in_cricket.csv`. Ensure this file is placed in the same directory as the Python script.

**Running the Dashboard**

1. **Prerequisites:** Python and Streamlit installation are required.
2. **Save Script:** Save the Python code as `cricket_dashboard.py`.
3. **Run Script:** Execute the script using the command `streamlit run cricket_dashboard.py`.

**Code Structure**

The code is well-structured with clear sections for:

* **Page Layout & Streamlit Configuration:** Defines page title, icon, and hides unnecessary Streamlit elements.
* **Data Loading:** Loads the `most_runs_in_cricket.csv` dataset using Pandas.
* **Sidebar Navigation:** Creates a sidebar with navigation options for different dashboard sections (Home, Overview, Performance, Compare).
* **KPI & Visualization Functions:** Defines functions to calculate KPIs and generate various Plotly visualizations.
* **Layout for Navigation Options:** Each navigation option (Home, Overview, Performance, Compare) has its own dedicated layout section that builds the UI components and populates them with data and visualizations.

**Further Enhancements**

* **Data Filtering:** Allow filtering data by cricket format (ODI, Test, T20).
* **Player Search:** Implement a search bar for filtering players.
* **Downloadable Report:** Enable generation of downloadable reports summarizing the dashboard findings.

**Check it out on -** https://shivamshukla14-dashboard-project-app-caj1y0.streamlit.app/
