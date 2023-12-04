import xml.etree.ElementTree as ET

data = {
    "identityUpdateTime": "BigInteger",
    "identity": "int",
    "identitySource": "Short",
    "identityConfidencePercent": "Float",
    "identityRationale": "Short",
    "isSpecialInterest": "Boolean",
    "isIdentityConflictInProgress": "Boolean",
    "isExerciseConflictInProgress": "Boolean",
    "isExercise": "Boolean",
    "exerciseSource": "Short",
    "isIdentityReevaluationRequired": "Boolean",
    "strength": "Short",
    "strengthSource": "Short",
    "classification": {
        "updateTime": "BigInteger",
        "specificTypeSource": "Short",
        "specificType": "int",
        "specificTypeModifier": "Short",
        "nationalitySource": "Short",
        "nationalityAlliance": "int",
        "category": "int",
        "categorySource": "Short",
        "isCategoryConflictInProgress": "Boolean",
        "platformActivity": "int",
        "platformActivitySource": "Short",
        "platformActivityAmplification": "int",
        "platformSource": "Short",
        "platform": "int"
    },
    "tdmVersion": "String",
    "updateReason": "Long",
    "creationTime": "BigInteger",
    "isNonRealTime": "Boolean",
    "trackKey": {
        "index": "int",
        "useCount": "int",
        "trackType": "int"
    },
    "trackKind": "Short",
    "trackAuthenticity": "Short",
    "trackStatus": "Short",
    "isLostTrack": "Boolean",
    "lostTime": "BigInteger",
    "groundSpeed": "Float",
    "course": "Float",
    "altitudeValidTime": "BigInteger",
    "positionValidTime": "BigInteger",
    "isOwnShip": "Boolean",
    "isSpecialProcessing": "Boolean",
    "isTroubledTrack": "Boolean",
    "numberSupportingSourceTracks": "Long",
    "trackNumberList": [
        {
            "sourceTrackKey": {
                "index": "int",
                "useCount": "int",
                "trackType": "int"
            },
            "assignedTrackNumber": {
                "trackNumber": "Long",
                "trackNumberIdentifier": "Short",
                "assignedTrackNumberString": {
                    "trackNumberString": "String",
                    "trackNumberStringOtherIdentifier": "String"
                },
                "resourceKey": {
                    "unitNumber": "Long",
                    "resourceType": "int",
                    "resourceInstance": "int"
                }
            }
        },
    ],
    "altitudeSourceType": "Short",
    "positionSourceType": "Short",
    "isSelfDefenseInterest": "Boolean",
    "masterSystemTrackKey": {
        "index": "int",
        "useCount": "int",
        "trackType": "int"
    },
    "trackDesignation": "Short",
    "crosslinkSystemTrackKey": {
        "index": "int",
        "useCount": "int",
        "trackType": "int"
    },
    "crosslinkReason": "Short",
    "emergencySource": "Short",
    "ecefCovariance": {
        "covType": "Short",
        "posVelRandUnc": {
            "xx": "double",
            "xy": "double",
            "xz": "double",
            "xxdot": "double",
            "xydot": "double",
            "xzdot": "double",
            "yy": "double",
            "yz": "double",
            "yxdot": "double",
            "yydot": "double",
            "yzdot": "double",
            "zz": "double",
            "zxdot": "double",
            "zydot": "double",
            "zzdot": "double",
            "xdotxdot": "double",
            "xdotydot": "double",
            "xdotzdot": "double",
            "ydotydot": "double",
            "ydotzdot": "double",
            "zdotzdot": "double"
        },
        "posVelBiasUnc": {
            "xx": "double",
            "xy": "double",
            "xz": "double",
            "xxdot": "double",
            "xydot": "double",
            "xzdot": "double",
            "yy": "double",
            "yz": "double",
            "yxdot": "double",
            "yydot": "double",
            "yzdot": "double",
            "zz": "double",
            "zxdot": "double",
            "zydot": "double",
            "zzdot": "double",
            "xdotxdot": "double",
            "xdotydot": "double",
            "xdotzdot": "double",
            "ydotydot": "double",
            "ydotzdot": "double",
            "zdotzdot": "double"
        },
        "dataType": "Short"
    },
    "ecefX": "Float",
    "ecefY": "Float",
    "ecefZ": "Float",
    "ecefIsECEFReliable": "Boolean",
    "ecefItsVelocityECEFX": "Float",
    "ecefItsVelocityECEFY": "Float",
    "ecefItsVelocityECEFZ": "Float",
    "ecefIsECEFVelocityReliable": "Boolean",
    "isPUJU": "Boolean",
    "isCooperatingUnit": "Boolean",
    "isCommandAndControl": "Boolean",
    "isIntelSpecialProcessing": "Boolean"
}

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

