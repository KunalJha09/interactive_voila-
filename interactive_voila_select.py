import pandas as pd
import ipyvuetify as v

# Define the dataframe
df = pd.DataFrame({'Division': ['A', 'A', 'A', 'B'], 'ID': [1, 1, 3, 4]})

# Get distinct values of Division and ID
divisions = df['Division'].unique().tolist()
ids = df['ID'].unique().tolist()

# Define the first select widget for Division
division_select = v.Select(items=divisions, v_model=None, label='Division', outlined=True)

# Define the second select widget for ID
id_select = v.Select(items=ids, v_model=None, label='ID', outlined=True)

# Define the callback function for when the Division select widget value changes
def update_id_select(change):
    if change['type'] == 'change' and change['name'] == 'v_model':
        selected_division = change['new']
        # Get the distinct IDs for the selected Division
        selected_ids = df.loc[df['Division'] == selected_division, 'ID'].unique().tolist()
        # Update the items in the ID select widget
        id_select.items = selected_ids

# Add the callback function to the Division select widget
division_select.observe(update_id_select)

# Display the widgets
v.Container(children=[division_select, id_select])
