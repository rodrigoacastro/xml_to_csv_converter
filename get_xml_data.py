# Convert XML into csv - data

# Importing the required libraries
from utils.all_functions import *

# convert xml to df - Events

convert_events_xml_tag_df(filename='T03_R.xml', tagname='Events',
                          export_csv=True, csv_output='data_event.csv')

print('Event data extracted')
print('Exported file data_event.csv to the folder csv_target')

# implement solution for SourceTextChar and FinalTextChar tags

sourceTextChar_df = convert_xml_tag_df(filename='T03_R.xml', tagname='SourceTextChar',
                                       export_csv=False)
sourceTextChar_df['Type'] = 'source'
change_column_order(dataframe=sourceTextChar_df, colname='Type', newposition=0)

# print(f'sourceTextChar_df:\n{sourceTextChar_df}')

targetTextChar_df = convert_xml_tag_df(filename='T03_R.xml', tagname='FinalTextChar',
                                       export_csv=False)

targetTextChar_df['Type'] = 'target'

change_column_order(dataframe=targetTextChar_df, colname='Type', newposition=0)

# print(f'targetTextChar_df:\n{targetTextChar_df}')


data_textChar = join_metadata(df_tuple=(sourceTextChar_df, targetTextChar_df), axis=0,
                                  reset_index=False, colnames=list(sourceTextChar_df.columns))


# print(list(sourceTextChar_df.columns))
# print(f'metadata_textChar:\n{data_textChar}')

save_csv_from_df(data_textChar, csv_output='data_textChar.csv',
                 target_folder='csv_target')

print('All data extracted')
