import xml.etree.ElementTree as ET

items_list = []

xsd_file_path = r'C:\Users\rmvelazquez\Documents\Work\XSDs\Vehicular\VehicularUnknownTrackTypeGENSER.xsd'
tree = ET.parse(xsd_file_path)
xsd = tree.getroot()

# File path of secondary abstract .xsd called by root .xsd.
abstract_file_path = r'C:\Users\rmvelazquez\Documents\Work\XSDs\Vehicular\AbstractVehicularTrackTypeGENSER.xsd'
tree = ET.parse(abstract_file_path)
abstract = tree.getroot()

output_file_path = r'C:\Users\rmvelazquez\PycharmProjects\xsd-to-xml\rm\output.xml'

