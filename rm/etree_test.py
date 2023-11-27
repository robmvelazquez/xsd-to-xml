import xml.etree.ElementTree as ET


def print_elements_names(element, indent=0):
    if element.tag.endswith('element') and 'name' in element.attrib:
        print(' ' * indent + f"Element Name: {element.attrib['name']}")

    for child in element:
        print_elements_names(child, indent + 1)

    with open(output_file_path, 'w') as output_file:
        output_file.write(root_element)


xsd_file_path = 'test.xsd'
output_file_path = 'output.xml'
tree = ET.parse(xsd_file_path)
root = tree.getroot()

print_elements_names(root)