import cProfile
import os
import pandas as pd

def Read_File(file):
    input_file = pd.read_csv(file, encoding='latin-1', low_memory=False)

    output_file = input_file[['Sku Code', 'Style Code', 'Style Name', 'Colour Name', 'Size Code', 'Specification', 'Retail Description',
         'Product Feature 1', 'Product Feature 2', 'Product Feature 3',
         'Washing Instructions', 'Fabric', 'Product Type', 'Single Price', 'Item Weight in KG',
         'Colour Image']]
    final_output = output_file.rename(
        columns={'Sku Code': 'SKU', 'Style Code': 'Parent', 'Style Name': 'Name', 'Colour Name': 'Attribute 1 value(s)',
                 'Size Code': 'Attribute 2 value(s)',
                 'Specification': 'Short Description',
                 'Retail Description': 'Description',
                 'Product Feature 1': 'Meta: product-feature-1',
                 'Product Feature 2': 'Meta: product-feature-2',
                 'Product Feature 3': 'Meta: product-feature-3',
                 'Washing Instructions': 'Meta: washing-instructions',
                 'Fabric': 'Meta: fabric', 'Product Type': 'Categories',
                 'Single Price': 'Regular price', 'Item Weight in KG': 'Weight (kg)',
                 'Colour Image': 'Images'})

    final_output.insert(0, "Type", "")
    final_output.insert(4, "Published", 1)
    final_output.insert(5, "Is featured?", 0)
    final_output.insert(6, "Allow customer reviews?", 1)
    final_output.insert(7, "Visibility in catalogue", "visible")
    final_output.insert(8, "Attribute 1 name", "")
    final_output.insert(10, "Attribute 1 default", "")
    final_output.insert(11, "Attribute 1 visible", "")
    final_output.insert(12, "Attribute 1 global", "")
    final_output.insert(13, "Attribute 2 name", "")
    final_output.insert(15, "Attribute 2 default", "")
    final_output.insert(16, "Attribute 2 visible", "")
    final_output.insert(17, "Attribute 2 global", "")

    # Singles values conditions
    single_conditions_1 = final_output['Parent'] == ""
    single_condition_2 = final_output['Attribute 1 value(s)'] == ""
    # Variable values conditions

    variable_condition_1 = final_output['Type'] == "variable"

    # Variation values conditions

    variation_condition_1 = final_output['Description'] == ""
    variation_condition_2 = final_output['Categories'] == ""

    # Les mises en valeurs
    final_output.loc[single_conditions_1 & single_condition_2, 'Type'] = "single"

    final_output.loc[single_conditions_1 == False, ['Type', 'Attribute 1 name', 'Attribute 2 name']] = ["variation",
                                                                                                        "color", "size"]
    # final_output.to_csv("premier.csv", index=False)
    return final_output

def Create_Variable(input):
    r, c = input.shape
    data_reverse = input.iloc[::-1]
    for index in range(r + 1):
        if data_reverse.iloc[index]['Parent'] != data_reverse.iloc[index + 1]['Parent']:
            new_row = {"Type": "variable", "SKU": data_reverse.iloc[index]['Parent'],
                   "Name": data_reverse.iloc[index]['Name'],
                   "Published": 1,
                   "Is featured?": 0,
                   "Allow customer reviews?": 1,
                   "Visibility in catalogue": data_reverse.iloc[index]['Visibility in catalogue'],
                   "Attribute 1 default": "",
                   "Attribute 1 name": data_reverse.iloc[index]['Attribute 1 name'],
                   "Attribute 1 visible": data_reverse.iloc[index]['Attribute 1 visible'],
                   "Attribute 1 global": "",
                   "Parent": "",
                   "Attribute 1 value(s)": "",
                   "Attribute 2 default": "",
                   "Attribute 2 name": data_reverse.iloc[index]['Attribute 2 name'],
                   "Attribute 2 value(s)": "",
                   "Attribute 2 visible": "",
                   "Attribute 2 global": "",
                   "Short Description": data_reverse.iloc[index]['Short Description'],
                   "Description": data_reverse.iloc[index]['Description'],
                   "Meta: product-feature-1": data_reverse.iloc[index]['Meta: product-feature-1'],
                   "Meta: product-feature-2": data_reverse.iloc[index]['Meta: product-feature-2'],
                   "Meta: product-feature-3": data_reverse.iloc[index]['Meta: product-feature-3'],
                   "Meta: washing-instructions": data_reverse.iloc[index]['Meta: washing-instructions'],
                   "Meta: fabric": data_reverse.iloc[index]['Meta: fabric'],
                   "Categories": data_reverse.iloc[index]['Categories'],
                   "Regular price": "", "Weight (kg)": "",
                   'Images': ""}
            new_df = pd.DataFrame(new_row, index=[len(data_reverse)])
            data_reverse = pd.concat([data_reverse, new_df])

    data_final = data_reverse.iloc[::-1]
    data_final = data_final.reset_index(drop=True)

    return data_final

def Get_Attribut_Value (data):
    result_final_one = []
    result_final_two = []
    grouped_data = data.groupby('Parent')
    for group, data in grouped_data:
        col3_values_1 = data['Attribute 1 value(s)'].tolist()
        col3_values_2 = data['Attribute 2 value(s)'].tolist()
        result_final_one.append(col3_values_1)
        result_final_two.append(col3_values_2)

    my_list_one = [[x for x in inner_list if x != ''] for inner_list in result_final_one]
    my_list_one = [x for x in my_list_one if x != []]
    final_list_one = [list(set(subL)) for subL in my_list_one]

    my_list_two = [[x for x in inner_list if x != ''] for inner_list in result_final_two]
    my_list_two = [x for x in my_list_two if x != []]
    final_list_two = [list(set(subL)) for subL in my_list_two]
    return final_list_one, final_list_two


# attribute_one, attribute_two = Get_Attribut_Value(data_final)

def Change_to_String(data_final , attribute_one, attribute_two ):
    for i in range(len(data_final)):
        if data_final.iloc[i]['Parent'] == "":
            my_string_1 = ', '.join(map(str, attribute_one[i]))
            my_string_2 = ', '.join(map(str, attribute_two[i]))
            data_final.loc[i, 'Attribute 1 value(s)'] = my_string_1
            data_final.loc[i, 'Attribute 2 value(s)'] = my_string_2

    return data_final

# print(final_output["Attribute 1 value(s)"] , final_output['Attribute 2 value(s)'])
# final_output.to_csv("mine.csv", index=False)

input_file = pd.read_csv("input.csv", encoding='latin-1', low_memory=False)

needs_columns = ['Sku Code', 'Style Code', 'Style Name', 'Colour Name', 'Size Code', 'Specification',
                 'Retail Description',
                 'Product Feature 1', 'Product Feature 2', 'Product Feature 3',
                 'Washing Instructions', 'Fabric', 'Product Type', 'Single Price', 'Item Weight in KG',
                 'Colour Image']

output_file = input_file[needs_columns]
final_output = output_file.rename(
    columns={'Sku Code': 'SKU', 'Style Code': 'Parent', 'Style Name': 'Name',
             'Colour Name': 'Attribute 1 value(s)',
             'Size Code': 'Attribute 2 value(s)',
             'Specification': 'Short Description',
             'Retail Description': 'Description',
             'Product Feature 1': 'Meta: product-feature-1',
             'Product Feature 2': 'Meta: product-feature-2',
             'Product Feature 3': 'Meta: product-feature-3',
             'Washing Instructions': 'Meta: washing-instructions',
             'Fabric': 'Meta: fabric', 'Product Type': 'Categories',
             'Single Price': 'Regular price', 'Item Weight in KG': 'Weight (kg)',
             'Colour Image': 'Images'})

final_output.insert(0, "Type", "")
final_output.insert(4, "Published", 1)
final_output.insert(5, "Is featured?", 0)
final_output.insert(6, "Allow customer reviews?", 1)
final_output.insert(7, "Visibility in catalogue", "visible")
final_output.insert(8, "Attribute 1 name", "")
final_output.insert(10, "Attribute 1 default", "")
final_output.insert(11, "Attribute 1 visible", "")
final_output.insert(12, "Attribute 1 global", "")
final_output.insert(13, "Attribute 2 name", "")
final_output.insert(15, "Attribute 2 default", "")
final_output.insert(16, "Attribute 2 visible", "")
final_output.insert(17, "Attribute 2 global", "")

# Singles values conditions
single_conditions_1 = final_output['Parent'] == ""
single_condition_2 = final_output['Attribute 1 value(s)'] == ""
# Variable values conditions

variable_condition_1 = final_output['Type'] == "variable"

# Variation values conditions

variation_condition_1 = final_output['Description'] == ""
variation_condition_2 = final_output['Categories'] == ""

# Les mises en valeurs
final_output.loc[single_conditions_1 & single_condition_2, 'Type'] = "single"

final_output.loc[single_conditions_1 == False, ['Type', 'Attribute 1 name', 'Attribute 2 name']] = [
    "variation", "color", "size"]

r, c = final_output.shape
data_reverse = final_output.iloc[::-1]
my_string = ""
result = []
repeated_element = []
count = 0
# Filter DataFrame to include only rows where Parent is different from the previous row
mask = data_reverse['Parent'] != data_reverse['Parent'].shift(1)
filtered_df = data_reverse[mask]

# Create a list of dictionaries for the new rows
new_rows = []
for i, row in filtered_df.iterrows():
    new_row = {
        "Type": "variable",
        "SKU": row['Parent'],
        "Name": row['Name'],
        "Published": 1,
        "Is featured?": 0,
        "Allow customer reviews?": 1,
        "Visibility in catalogue": row['Visibility in catalogue'],
        "Attribute 1 default": "",
        "Attribute 1 name": row['Attribute 1 name'],
        "Attribute 1 visible": row['Attribute 1 visible'],
        "Attribute 1 global": "",
        "Parent": "",
        "Attribute 1 value(s)": "",
        "Attribute 2 default": "",
        "Attribute 2 name": row['Attribute 2 name'],
        "Attribute 2 value(s)": "",
        "Attribute 2 visible": "",
        "Attribute 2 global": "",
        "Short Description": row['Short Description'],
        "Description": row['Description'],
        "Meta: product-feature-1": row['Meta: product-feature-1'],
        "Meta: product-feature-2": row['Meta: product-feature-2'],
        "Meta: product-feature-3": row['Meta: product-feature-3'],
        "Meta: washing-instructions": row['Meta: washing-instructions'],
        "Meta: fabric": row['Meta: fabric'],
        "Categories": row['Categories'],
        "Regular price": "", "Weight (kg)": "",
        'Images': ""
    }
    new_rows.append(new_row)

# Create a new DataFrame from the list of dictionaries
new_df = pd.DataFrame(new_rows)

# Concatenate the original DataFrame with the new DataFrame
data_reverse = pd.concat([data_reverse, new_df], ignore_index=True)
data_final = data_reverse.iloc[::-1]
data_final = data_final.reset_index(drop=True)

result_final_one = []
result_final_two = []
grouped_data = data_final.groupby('Parent')
for group, data in grouped_data:
    col3_values_1 = data['Attribute 1 value(s)'].tolist()
    col3_values_2 = data['Attribute 2 value(s)'].tolist()
    result_final_one.append(col3_values_1)
    result_final_two.append(col3_values_2)

my_list_one = [[x for x in inner_list if x != ''] for inner_list in result_final_one]
my_list_one = [x for x in my_list_one if x != []]
final_list_one = [list(set(subL)) for subL in my_list_one]

my_list_two = [[x for x in inner_list if x != ''] for inner_list in result_final_two]
my_list_two = [x for x in my_list_two if x != []]
final_list_two = [list(set(subL)) for subL in my_list_two]

print(final_list_two)

for i, row in data_final.iterrows():
        if row['Parent'] == "":
            my_string_1 = ', '.join(map(str, final_list_one[i]))
            my_string_2 = ', '.join(map(str, final_list_two[i]))
            data_final.at[i, 'Attribute 1 value(s)'] = my_string_1
            data_final.at[i, 'Attribute 2 value(s)'] = my_string_2

print(data_final['SKU'])
data_final.to_csv("final.csv", index=False)