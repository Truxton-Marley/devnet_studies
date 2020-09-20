#Element Tree is for quick tasks, not for robustness
#For robustness, use lxml
import xml.etree.ElementTree as ET

#Open the XML file into variable 'stream'
stream = open('sample.xml', 'r')

#Parse into an Element Tree object
xml = ET.parse(stream)

#Get the root element
root = xml.getroot()

#Loop through the child elements of the root Element
#Get to know you're XML to properly loop through!
for e in root:
    print(ET.tostring(e))
    print("_-_-_-_-_-_-_-_-")

    #Get an attribute named "ID"
    print(e.get("ID"))