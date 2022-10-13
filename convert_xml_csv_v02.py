# Convert XML into csv

# Importing the required libraries
import xml.etree.ElementTree as Xet
import pandas as pd
import csv
from pipe import dedup, groupby, where, select, sort
from utils.all_functions import convert_xml_tag_df
# cols = ["name", "phone", "email", "date", "country"]
cols = []
rows = []

file_to_convert = 'T03_R.xml' # temporary
# file_to_convert = input("Digite o nome do arquivo XML a ser convertido em CSV: ")
print(file_to_convert)

# Check input format
if (file_to_convert[-4:] == '.xml'):
    pass
else:
    file_to_convert = f'{file_to_convert}.xml'

# Parsing the XML file

# Parsing the XML file
# xmlparse = Xet.parse(f'xml_source/{file_to_convert}')
xmlparse = Xet.parse(f'xml_source/{file_to_convert}')
print(xmlparse)


root = xmlparse.getroot()

# get tags and attributes under root
print("Root Tags and attributes:")
for i in root:    
    print(i.tag,i.attrib)

# get tags and attributes under Project
print("Project Tags and attributes:")

# for i in root.iter("Project"):    
#     # print(i.tag,i.attrib)

#     filename = i.find('Filename').text
    # print(filename)


##########################################
# IMPORTANT
# the code below WORKS for Events

# print("Events Tags and attributes:")

event_data = []
event_type = []

for i in root.find("Events"):
    # tag = i.tag # each tag goes into a event_type column
    # get tags and attributes under Events
    event_type.append (i.tag) # type of event
    event_data.append(i.attrib) # variables with values

# print(event_type)
# print(event_data)

# convert dict to df
event_df = pd.DataFrame.from_dict(event_data)
event_df['event_type'] = event_type # NEED to reorder and put it in the front
print(event_df)

# save csv
csv_output = 'event_df.csv'

event_df.to_csv(f'csv_target/{csv_output}',index=False)

# values = i.attrib 

# Tag:
# Eye
# Attribute:
# {'Time': '268899', 'TT': '268843', 'Win': '0', 'Xl': '-1283', 'Yl': '-995', 'Xr': '-1283', 'Yr': '-995', 'pl': '-1', 'pr': '-1', 'Cursor': '0'}

##############################

# implement solution for SourceTextChar and FinalTextChar tags
    
convert_xml_tag_df (tagname= 'SourceTextChar', csv_output= 'sourcetextchar.csv')
convert_xml_tag_df (tagname= 'FinalTextChar', csv_output= 'Finaltextchar.csv')
