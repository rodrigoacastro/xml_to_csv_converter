from xml.etree import cElementTree as ET
xmlstr = """
<root>
  <page>
    <title>Chapter 1</title>
      <content>Welcome to Chapter 1</content>
    </page>
    <page>
     <title>Chapter 2</title>
     <content>Welcome to Chapter 2</content>
    </page>
    </root>
 """
root = ET.fromstring(xmlstr)
for page in list(root):
  print(page)
  title = page.find('title').text
  content = page.find('content').text
  print('title: %s; content: %s' % (title, content))
