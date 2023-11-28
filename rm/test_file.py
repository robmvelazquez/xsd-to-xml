import xml.etree.ElementTree as ET
import sys

"""
def generate_random_string(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


def generate_random_xml_data(schema_element):
    if schema_element.type_name == 'string':
        return generate_random_string(10)
    elif schema_element.type_name == 'int':
        return str(random.randint(1, 100))
    # Add more data types as needed


def generate_xml_data(schema, element):
    data = {}
    for child_element in schema.elements[element.name]:
        data[child_element.name] = generate_random_xml_data(child_element)
    return data


def generate_random_xml(schema, root_element_name, num_records):
    root = ET.Element(root_element_name)
    for _ in range(num_records):
        data = generate_xml_data(schema, schema.elements[root_element_name])
        record_element = ET.SubElement(root, root_element_name)
        for field, value in data.items():
            field_element = ET.SubElement(record_element, field)
            field_element.text = value
    return ET.ElementTree(root)
"""

xsd_file_path = 'VehicularUnknownTrackTypeGENSER.xsd'
tree = ET.parse(xsd_file_path)
xsd = tree.getroot()

abstract_file_path = 'AbstractVehicularTrackTypeGENSER.xsd'
tree = ET.parse(abstract_file_path)
abstract = tree.getroot()

output_file_path = 'output.xml'


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


# def header_and_footer(element)
#     print(f'<{element.tag.split('}')[-1]}>')


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


print_header(xsd)
first_complex_type(xsd)
print_elements_names(xsd)
first_complex_type(xsd)
