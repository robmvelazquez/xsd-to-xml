import elementpath
import xmlschema
import json
import xml.etree.ElementTree as ET

def print_element_names(element):
    print(element.attrib('name') )

    'element')

print("ok")
sch = 'VehicularAirTrackTypeGENSERTest.xsd'
# schema = xmlschema.XMLSchema(sch)

tree = ET.parse(sch)
root = tree.getroot()
print_element_names(root)



root = ET.Element('root')
person = ET.SubElement(root, 'person')
name = ET.SubElement(person, 'name')
age = ET.SubElement(person, 'age')
name.text = 'John Doe'
age.text = '30'
tree = ET.ElementTree(root)
tree.write('person.xml')
# data=schema.to_dict('my_data.xml')
## from xml.etree.ElementTree import ElementTree as ET
# for xsd_component in schema.iter_components():
#    print(xsd_component)

print("ok")