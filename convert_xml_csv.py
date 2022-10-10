# Convert XML into csv

# Importing the required libraries
import xml.etree.ElementTree as Xet
import pandas as pd

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
xmlparse = Xet.parse(f'xml_source/{file_to_convert}')
print(xmlparse)

root = xmlparse.getroot()
# events = xmlparse.getroot('Events')

# for i in root.findall('Events'):
#     print(i)

print(root)

root_elements = []

for i in root:
    print(i)
    root_elements.append(i)

#     Time = i.find("Time").text
#     TT = i.find('TT').text
#     Win = i.find('Win').text
#     WinR = i.find('WinR').text
#     WinU = i.find('WinU').text
#     WinD = i.find('WinD').text
#     Xl = i.find('Xl').text
#     Yl = i.find('Yl').text
#     Xr = i.find('Xr').text
#     Yr = i.find('Yr').text
#     pl = i.find('pl').text
#     pr = i.find('pr').text
#     Cursor = i.find('Cursor').text
#     CursorR = i.find('CursorR').text
#     CursorU = i.find('CursorU').text
#     CursorD = i.find('CursorD').text

# root_elements.('root_elements.csv')
print (root_elements) # test

#     rows.append({"Time": Time,
#                 "TT": TT,
#                 "Win": Win,
#                 "WinR": WinR,
#                 "WinU": WinU,
#                 "WinD": WinD,
#                 "WinR": WinR,
#                 "Xl": Xl,
#                 "Yl": Yl,
#                 "Xr": Xr,
#                 "Yr": Yr,
#                 "pl": pl,
#                 "pr": pl,
#                 "Cursor": Cursor,
#                 "CursorR": CursorR,
#                 "CursorU": CursorU,
#                 "CursorD": CursorD         
#                 })

# df = pd.DataFrame(rows, columns=cols)

# print(df)


# for i in root:
#     name = i.find("name").text
#     phone = i.find("phone").text
#     email = i.find("email").text
#     date = i.find("date").text
#     country = i.find("country").text
  
#     rows.append({"name": name,
#                  "phone": phone,
#                  "email": email,
#                  "date": date,
#                  "country": country})
  
# df = pd.DataFrame(rows, columns=cols)
  
# Writing dataframe to csv
# df.to_csv('output.csv')