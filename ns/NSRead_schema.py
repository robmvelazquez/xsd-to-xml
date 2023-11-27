#pip install xmlschema


import xml.etree.ElementTree as ET
import xmlschema
import random
import string

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

def main():
    print("ok0")
    xsd_file_path = 'VehicularAirTrackTypeGENSERTest.xsd'  # Replace with your XSD file path
    num_records = 1  # Adjust the number of records as needed
    output_file_path = 'output.xml'  # Replace with your desired output file path
    print("ok1")
    schema = xmlschema.XMLSchema(xsd_file_path)

    for xsd_component in schema.iter_globals():
        xsd_component


#    root_element_name = schema.root_element.name
    print("ok2")
    xml_tree = generate_random_xml(schema, root_element_name, num_records)
    print("ok3")
    with open(output_file_path, 'wb') as output_file:
        xml_tree.write(output_file)

if __name__ == "__main__":
    main()

#Replace 'your_schema.xsd' with the path to your XSD file and adjust the num_records variable based on how many random XML records you want.
#The script will generate random XML data based on the XSD schema and write it to the specified output file.
