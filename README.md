# IncomeHappiness
Project Title: Income and Happiness Analysis

Overview
This project involves analyzing a dataset initially provided in JSON format, which was converted into CSV for further processing. The workflow included importing the data into SQL Server, querying it, and visualizing the results using Power BI.

Steps Taken
Convert JSON to CSV:

Converted the JSON file to CSV format using Python. This step involved reading the JSON data and saving it as a CSV file for easier handling in SQL Server.
Create SQL Database and Table:

Created a new database and table in SQL Server to store the imported data. This setup prepared the structure for data insertion and analysis.
Import CSV Data into SQL:

Imported the CSV file into the SQL table using SQL Server Management Studio (SSMS). Addressed issues related to data types and cleaned up the data for accurate import.
Analyze Data with SQL Queries:

Performed SQL queries to extract meaningful insights from the data. This analysis helped in understanding key metrics and relationships within the dataset.
Visualize Data in Power BI:

Imported the data into Power BI and created visualizations. Designed a line chart with a trend line to analyze the relationship between income and happiness, added slicers for filtering, and built an interactive dashboard.
Issues Faced
Data Type Conversion Issues:

Faced challenges with data type mismatches during import. Resolved by adjusting column types and ensuring data consistency.
Handling Invisible Characters:

Removed invisible characters from data columns to ensure clean data import.
Power BI Slicer Functionality:

Encountered issues with slicer visibility. Resolved by updating to the latest version of Power BI Desktop and exploring its features.
Technologies Used
Python: For converting JSON to CSV.
SQL Server: For database management and data import.
Power BI: For data visualization and dashboard creation.
Files
convert_json_to_csv.py: Python script for converting JSON to CSV.
SQLQuery1.sql: SQL script for creating the database and table.
FinalDashboard.pbix: Power BI file with visualizations and dashboard.

Contributors:
I want to remind you of the collaborators or resources used if you don't mind.
https://data.world/
