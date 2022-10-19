# all functions

import pandas as pd
import xml.etree.ElementTree as Xet
# import csv
# from pipe import dedup, groupby, where, select, sort
# index
'''
def validate_file_format (filename: str, fileformat: str = '.xml')
def get_xml_parse (filename: str)
def convert_xml_tag_df (tagname: str, csv_output: str = "output.csv")

'''

def validate_file_format (filename: str, fileformat: str = '.xml'):
    # Check input format
    if (filename[-4:] == fileformat):
        pass
    else:
        filename = f'{filename}{fileformat}'
    
    return (filename)

def get_xml_parse (filename: str):

    xmlparse = Xet.parse(f'xml_source/{filename}')
    return (xmlparse)

def convert_xml_tag_df (filename: str ,tagname: str, csv_output: str = "output.csv"):
    '''
    using an input (ex: Events) and a csv_output, returns a csv in the target folder (csv_target)
    '''
    # Check output format
    if (csv_output[-4:] == '.csv'):
        pass
    else:
        csv_output = f'{csv_output}.csv'

    event_data = []

    file_to_convert = validate_file_format (filename = filename, fileformat = '.xml')

    # Parsing the XML file

    # Parsing the XML file
    # xmlparse = Xet.parse(f'xml_source/{file_to_convert}')

    xmlparse = get_xml_parse (filename = file_to_convert)

    root = xmlparse.getroot()

    for i in root.find(tagname):
        # get tags and attributes under tag
        event_data.append(i.attrib) # variables with values

# convert dict to df
    event_df = pd.DataFrame.from_dict(event_data)
    # print(event_df)

    # save csv
    target_folder = 'csv_target'
    event_df.to_csv(f'{target_folder}/{csv_output}',index=False)




def convert_events_xml_tag_df (filename: str, tagname= 'SourceTextChar', csv_output= 'sourcetextchar.csv'):
    
    file_to_convert = validate_file_format (filename = filename, fileformat = '.xml')

    # Parsing the XML file

    # Parsing the XML file
    # xmlparse = Xet.parse(f'xml_source/{file_to_convert}')

    xmlparse = get_xml_parse (filename = file_to_convert)

    # xmlparse = Xet.parse(f'xml_source/{file_to_convert}')
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
    