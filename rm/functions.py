import sys
import random


# Function to redirect print statements to XML file.
def redirect_output_to_xml(file_path):
    def decorator(func):
        def wrapper(*args, **kwargs):
            with open(file_path, 'a') as output_file:
                sys.stdout = output_file
                result = func(*args, **kwargs)
                sys.stdout = sys.__stdout__
                return result
        return wrapper
    return decorator


# Prints the xml declaration and redirects the output to the xml file.
@redirect_output_to_xml('output.xml')
def xml_declaration(element):
    with open('output.xml', 'w', encoding='UTF-8') as xml_file:
        xml_file.write('<?xml version="1.0" encoding="UTF-8"?>')


# Prints the header data and redirects the output to the xml file.
def header(element, indent=0):
    if element.tag.endswith('complexType') and 'name' in element.attrib:
        with open('output.xml', 'a') as output_file:
            sys.stdout = output_file
            print(f"<{element.attrib.get('name')}>")
            sys.stdout = sys.__stdout__

    for child in element:
        header(child, indent + 1)


# Prints the footer data and redirects the output to the xml file.
def footer(element, indent=0):
    if element.tag.endswith('complexType') and 'name' in element.attrib:
        with open('output.xml', 'a') as output_file:
            sys.stdout = output_file
            print(f"</{element.attrib.get('name')}>")
            sys.stdout = sys.__stdout__

    for child in element:
        footer(child, indent + 1)


# Prints all elements with the words 'element' and 'name' to the xml file.
def print_elements_names(element, indent=0):
    if element.tag.endswith('element') and 'name' in element.attrib:
        # Skips duplicate elements using 'mode' within the element name.
        if 'mode' not in element.attrib['name']:
            data_type = element.attrib['type']
            data_type = data_type.replace('xs:', '')
            with open('output.xml', 'a') as output_file:
                sys.stdout = output_file
                print(
                    ' ' * indent + f"<{element.attrib['name']}>" + f"{data_type}" + f"</{element.attrib['name']}>")
                sys.stdout = sys.__stdout__

    for child in element:
        print_elements_names(child, indent + 1)


# Generates a random value within a range relative to the datatype.
def generate_random_value(data_type):
    if data_type == 'long':
        return random.randint(-(2**63), 2**63 -1)
    elif data_type == 'short':
        return random.randint(-(2**15), 2**15 -1)
    elif data_type == 'boolean':
        return random.choice([True, False])
    elif data_type == 'float':
        return random.uniform(-1e6, 1e6)
    elif data_type == 'int':
        return random.randint(-(2**31), 2**31 - 1)
    elif data_type == 'bigInt':
        return random.randint(-(2**127), 2**127 -1)
    else:
        raise ValueError(f"Unknown data type: {data_type}")


def add_item(name, data_type):
    item = {"name": name, "data_type": data_type}
    item_list.append(item)


item_list = []


add_item('updateReason', 'long')
add_item('numberSupportingSourceTracks', 'long')
add_item('identitySource', 'short')
add_item('identityRationale', 'short')
add_item('exerciseSource', 'short')
add_item('strength', 'short')
add_item('strengthSource', 'short')
add_item('trackKind', 'short')
add_item('trackAuthenticity', 'short')
add_item('trackStatus', 'short')
add_item('altitudeSourceType', 'short')
add_item('positionSourceType', 'short')
add_item('trackDesignation', 'short')
add_item('crosslinkReason', 'short')
add_item('emergencySource', 'short')
add_item('specialInterest', 'boolean')
add_item('identityConflictInProgress', 'boolean')
add_item('exerciseConflictInProgress', 'boolean')
add_item('exercise', 'boolean')
add_item('isExercise', 'boolean')
add_item('identityReevaluationRequired', 'boolean')
add_item('nonRealTime', 'boolean')
add_item('lostTrack', 'boolean')
add_item('ownShip', 'boolean')
add_item('specialProcessing', 'boolean')
add_item('troubledTrack', 'boolean')
add_item('isSelfDefenseInterest', 'boolean')
add_item('identity', 'int')
add_item('identityUpdateTime', 'bigInt')
add_item('identity', 'bigInt')
add_item('creationTime', 'bigInt')
add_item('lostTime', 'bigInt')
add_item('altitudeValidTime', 'bigInt')
add_item('positionValidTime', 'bigInt')

data_dict = dict(item_list)


@redirect_output_to_xml('output.xml')
def print_list(data):
    for item in data:
        print(f"<{item['name']}>{generate_random_value(item['data_type'])}</{item['name']}>")
