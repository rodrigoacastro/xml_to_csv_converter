# all functions

# index
'''
def convert_xml_tag_df (tagname: str, csv_output: str = "output.csv")

'''


def convert_xml_tag_df (tagname: str, csv_output: str = "output.csv"):
    '''
    using an input (ex: Events) and a csv_output, returns a csv in the target folder (csv_target)
    '''
    # Check output format
    if (csv_output[-4:] == '.csv'):
        pass
    else:
        csv_output = f'{csv_output}.csv'

    event_data = []

    for i in root.find(tagname):
        # get tags and attributes under tag
        event_data.append(i.attrib) # variables with values

# convert dict to df
    event_df = pd.DataFrame.from_dict(event_data)
    # print(event_df)

    # save csv
    target_folder = 'csv_target'
    event_df.to_csv(f'{target_folder}/{csv_output}',index=False)

