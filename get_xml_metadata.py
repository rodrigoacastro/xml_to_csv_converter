# Convert XML into csv - Metadata

# Importing the required libraries
import pandas as pd
from get_xml_data_metadata import target_xml
from utils.all_functions import *

name_target_xml = target_xml.replace('.xml','')


# file_to_convert = 'T03_R.xml'  # temporary
file_to_convert = target_xml
# file_to_convert = input("Digite o nome do arquivo XML a ser convertido em CSV: ")
# print(file_to_convert)

file_to_convert = validate_file_format(
    filename=file_to_convert, fileformat='.xml')

# Parsing the XML file

# Parsing the XML file
xmlparse = get_xml_parse(filename=file_to_convert, source_folder='xml_source')
# print(xmlparse)

root = xmlparse.getroot()

# get tags and attributes under root
# print("Root Tags and attributes:")
# for i in root:
#     print(i.tag, i.attrib)


print('Capturing Project content')

event_data = []
event_type = []
project_data_dict = {}

for i in root.find("Project"):
    # tag = i.tag # each tag goes into a event_type column
    # get tags and attributes under Events
    event_type.append(i.tag)  # type of event
    event_data.append(i.attrib)  # variables with values

    if i.tag != "Languages":
        project_data_dict[i.tag] = i.text
    else:
        project_data_dict[i.tag] = i.attrib

# print(event_type)
# print(event_data)

# print(f'project_data_dict')

# print(f'Project: {project_data_dict}')
# {'FileName': 'C:\\Users\\Letra\\Desktop\\CROSS\\Projetos das Atividades\\T1_EL1.project',
# 'Description': 'example project description', 'versionString': None, 'useSourceText': 'true',
# 'promptSubjectName': 'true', 'useExtendedTranslations': 'false', 'showTimer': 'false', 'maxWindow': 'false',
# 'offlineGWM': 'false', 'fullScreen': 'false', 'lockWindows': 'false',
# 'Languages': {'source': 'pt', 'target': 'pt', 'task': 'revision'}}


# filter out Languages
filtered_no_language = {key: project_data_dict[key] for key in project_data_dict.keys() &
                        {'FileName', 'Description', 'versionString', 'useSourceText', 'promptSubjectName',
                         'useExtendedTranslations', 'showTimer', 'maxWindow', 'offlineGWM', 'fullScreen',
                         'lockWindows'}}

project_data_dict0 = filtered_no_language
project_data_dict0_df = convert_dict_to_df(project_data_dict0)
# save_csv_from_df(project_data_dict0_df,
#                  csv_output='project_metadata_general.csv', target_folder='csv_target')


project_data_dict1 = project_data_dict['Languages']
project_data_dict1_df = convert_dict_to_df(project_data_dict1)
# save_csv_from_df(project_data_dict1_df,
#                  csv_output='project_metadata_languages.csv', target_folder='csv_target')

project_data_dict = pd.concat(
    [project_data_dict0_df, project_data_dict1_df], axis=1)
# print(f'project_data_dict:\n{project_data_dict}')


# save dataframe as csv file
# project_data_df = convert_dict_to_df(project_data_dict)
# save_csv_from_df(project_data_df, csv_output='project_data_df.csv', target_folder='csv_target')

print('Capturing other content')

data_dict = {}

for x in root:
    # print(f'x.tag={x.tag}')
    if x.tag != "VersionString" and x.tag != "Project":
        # print (x.tag, x.attrib)
        # print(x.text)
        data_dict[x.tag] = x.text

# print('data_dict')
# print(data_dict)
# {'Subject': 'FBS105_T1_EL1', 'startTime': '2022-08-31T13:52:11.8241334-03:00',
# 'endTime': '2022-08-31T14:02:35.0951334-03:00'}

# print(list(data_dict.keys()))
# ['Subject', 'startTime', 'endTime']

# save dataframe as csv file
data_df = convert_dict_to_df(data_dict)
# save_csv_from_df(data_df, csv_output='data_df.csv', target_folder='csv_target')


# join metadata dataframes logically


metadata_df = join_metadata(df_tuple=(data_df.T, project_data_dict0_df.T, project_data_dict1_df.T),
                            axis=0, colnames=['metadata_property', 'value']
                            )

# metadata_df = pd.concat((data_df.T, project_data_dict0_df.T,project_data_dict1_df.T), axis=0)
# metadata_df.reset_index(inplace=True)
# metadata_df.columns = ['metadata_property','value']

save_csv_from_df(metadata_df, csv_output=f'{name_target_xml}_metadata_df.csv',
                 target_folder='csv_target')

print('All metadata extracted')

