import xml.etree.ElementTree as ET

items_list = []


item_list = [
    ("updateReason", "long"),
    ("numberSupportingSourceTracks", "long"),
    ("identitySource", "short"),
    ("identityRationale", "short"),
    ("exerciseSource", "short"),
    ("strength", "short"),
    ("strengthSource", "short"),
    ("trackKind", "short"),
    ("trackAuthenticity", "short"),
    ("trackStatus", "short"),
    ("altitudeSourceType", "short"),
    ("positionSourceType", "short"),
    ("trackDesignation", "short"),
    ("crosslinkReason", "short"),
    ("emergencySource", "short"),
    ("specialInterest", "boolean"),
    ("identityConflictInProgress", "boolean"),
    ("exerciseConflictInProgress", "boolean"),
    ("exercise", "boolean"),
    ("isExercise", "boolean"),
    ("identityReevaluationRequired", "boolean"),
    ("nonRealTime", "boolean"),
    ("lostTrack", "boolean"),
    ("ownShip", "boolean"),
    ("specialProcessing", "boolean"),
    ("troubledTrack", "boolean"),
    ("isSelfDefenseInterest", "boolean"),
    ("identity", "int"),
    ("identityUpdateTime", "bigInt"),
    ("identity", "bigInt"),
    ("creationTime", "bigInt"),
    ("lostTime", "bigInt"),
    ("altitudeValidTime", "bigInt"),
    ("positionValidTime", "bigInt")
]
data_dict = dict(item_list)


root = ET.Element('items')
element_tree = ET.ElementTree(root)

xsd_file_path = r'C:\Users\rmvelazquez\Documents\Work\XSDs\Vehicular\VehicularUnknownTrackTypeGENSER.xsd'
tree = ET.parse(xsd_file_path)
xsd = tree.getroot()

# File path of secondary abstract .xsd called by root .xsd.
abstract_file_path = r'C:\Users\rmvelazquez\Documents\Work\XSDs\Vehicular\AbstractVehicularTrackTypeGENSER.xsd'
tree = ET.parse(abstract_file_path)
abstract = tree.getroot()

output_file_path = r'C:\Users\rmvelazquez\PycharmProjects\xsd-to-xml\rm\output.xml'

