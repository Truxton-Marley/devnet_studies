#xmltodict is an alternative to lxml
import xmltodict

stream = open('sample.xml', 'r')

#Convert XML file to python OrderedDict
xml = xmltodict.parse(stream.read())

#Parse as needed/appropriate
for e in xml:
    print(e)

