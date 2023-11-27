import xml.etree.ElementTree as ET
import xmlschema


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


def main():
    xsd_file_path = 'test.xsd'  # Replace with XSD file path
    output_file_path = 'output.xml'  # Replace with desired output file path

    schema = xmlschema.XMLSchema(xsd_file_path)

    root_elements = [name for name, element in schema.elements.items() if element.is_global()]
    if root_elements:
        root_element = root_elements[0]
        print(f'The root element of the schema is: {root_element}')
    else:
        print("No global elements found in the schema.")

    with open(output_file_path, 'w') as output_file:
        output_file.write(root_element)

if __name__ == "__main__":
    main()


#Replace 'your_schema.xsd' with the path to your XSD file and adjust the num_records variable based on how many random XML records you want. 
#The script will generate random XML data based on the XSD schema and write it to the specified output file.
