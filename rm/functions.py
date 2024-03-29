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


def escape_xml(text):
    return text.replace("<", "&lt;").replace(">", "&gt;")


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
            print(f"\n<{element.attrib.get('name')}>")
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


# Generates a random value within a range relative to the datatype.
def generate_random_value(data_type):
    if data_type == 'Long':
        return random.randint(-(2**63), 2**63 -1)
    elif data_type == 'Short':
        return random.randint(-(2**15), 2**15 -1)
    elif data_type == 'Boolean':
        return random.choice([True, False])
    elif data_type == 'Float':
        return random.uniform(-1e6, 1e6)
    elif data_type == 'int':
        return random.randint(-(2**31), 2**31 - 1)
    elif data_type == 'BigInteger':
        return random.randint(-(2**127), 2**127 -1)
    elif data_type == 'String':
        alphabets = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        string_length = random.randint(1, 100)
        random_string = ""
        for _ in range(string_length):
            random_string += alphabets[random.randint(0, len(alphabets) - 1)]
        return random_string
    elif data_type == 'double':
        return random.uniform(-1e6, 1e6)
    else:
        raise ValueError(f"Unknown data type: {data_type}")


@redirect_output_to_xml('output.xml')
def print_list(data, indent=0):
    for key, value in data.items():
        if isinstance(value, dict):
            print(' ' * 4 + f"<{key}>")
            for inner_key, inner_value in value.items():
                if isinstance(inner_value, dict):
                    print(' ' * 4 + f"<{inner_key}>")
                    for innermost_key, innermost_value in inner_value.items():
                        print(' ' * 8 + f"<{innermost_key}>{generate_random_value(innermost_value)}</{innermost_key}>")
                    print(' ' * 4 + f"</{inner_key}>")
                else:
                    print(' ' * 8 + f"<{inner_key}>"f"{generate_random_value(inner_value)}"f"</{inner_key}>")
            print(' ' * 4 + f"</{key}>")

        elif isinstance(value, list):
            print(f"{' ' * 4}<{key}>")
            for item in value:
                for inner_key, inner_value in item.items():
                    if isinstance(inner_value, dict):
                        print(' ' * 8 + f"<{inner_key}>")
                        for inside_key, inside_value in inner_value.items():
                            if isinstance(inside_value, dict):
                                print(' ' * 16 + f"<{inside_key}>")
                                for outer_key, outer_value in inside_value.items():
                                    print(f"{' ' * 20}<{outer_key}>{generate_random_value(outer_value)}</{outer_key}>")
                                print(' ' * 16 + f"</{inside_key}>")
                            else:
                                print(f"{' ' * 16}<{inside_key}>{generate_random_value(inside_value)}</{inside_key}>")
                        print(' ' * 8 + f"</{inner_key}>")
            print(f"{' ' * 4}</{key}>")

        else:
            print(' ' * 4 + f"<{key}>{escape_xml(str(generate_random_value(value)))}</{key}>")
'''
for items in data["assignedTrackNumberString"]:
    print(' ' + 4 + f"<{key}")
    for dict_key, dict_value in items.items():
        print(f"{' ' * 20}<{dict_key}>{generate_random_value(dict_value)}</{dict_key}>")
'''

'''
                            if isinstance(nested_value, dict):
                                for dict_key, dict_value in nested_value.items():
                                    print(f"{' ' * 20}<{dict_key}>{generate_random_value(dict_value)}</{dict_key}>")
                                    
                                    
    for key, my_list in data.items():
        print({key})
        for item in my_list:
            print(item)
'''