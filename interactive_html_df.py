import pandas as pd
from ipywidgets import interact
import ipyvuetify as v

# Create a sample Pandas DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'Gender': ['Female', 'Male', 'Male']}
df = pd.DataFrame(data)

# Define a function to create an HTML table from a Pandas DataFrame
def create_table(df):
    # Create a list of column names
    columns = df.columns.tolist()
    
    # Create a list of table rows, where each row is a list of table cells
    rows = []
    for i in range(len(df)):
        row = []
        for col in columns:
            # Create a dropdown widget for each cell value
            options = ['Female', 'Male'] if col == 'Gender' else None
            cell_widget = v.Select(items=options, value=df.loc[i, col])
            row.append(cell_widget)
        rows.append(row)
    
    # Create the HTML table using Vuetify components
    table = v.DataTable(
        headers=columns,
        items=rows,
        class_='elevation-1'
    )
    return table

# Display the interactive table using ipywidgets
interact(create_table, df=v.fixed(df));
