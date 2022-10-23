# Convert XML into csv - Data and Metadata

target_xml = 'T03_R.xml'

# extract xml_data
print('Extracting data...')
from get_xml_data import *

# extract xml metadata
print('Extracting metadata...')

from get_xml_metadata import *

print('Extracting data and metadata extracted')
