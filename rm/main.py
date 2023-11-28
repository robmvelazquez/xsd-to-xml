import xml.etree.ElementTree as ET
import sys


xsd_file_path = 'VehicularAirTrackTypeGENSER.xsd'
output_file_path = 'output.xml'
tree = ET.parse(xsd_file_path)
root = tree.getroot()


def redirect_output_to_xml(file_path):
    def decorator(func):
        def wrapper(*args, **kwargs):
            with open(file_path, 'w') as output_file:
                sys.stdout = output_file
                result = func(*args, **kwargs)
                sys.stdout = sys.__stdout__
                return result
        return wrapper
    return decorator


@redirect_output_to_xml('output.xml')
def print_header(element):
    print(f'<?xml version="1.0" encoding="UTF-8"?>')


def first_complex_type(element, indent=0):
    if element.tag.endswith('complexType') and 'name' in element.attrib:
        with open('output.xml', 'a') as output_file:
            sys.stdout = output_file
            print(f"<{element.attrib.get('name')}>")
            sys.stdout = sys.__stdout__

    for child in element:
        first_complex_type(child, indent + 1)


def print_elements_names(element, indent=0):
    if element.tag.endswith('element') and 'name' in element.attrib:
        with open('output.xml', 'a') as output_file:
            sys.stdout = output_file
            print(' ' * indent + f"<{element.attrib['name']}>" + "placeholder" + f"</{element.attrib['name']}>")
            sys.stdout = sys.__stdout__

    for child in element:
        print_elements_names(child, indent + 1)


print_header(root)
first_complex_type(root)
print_elements_names(root)
first_complex_type(root)
