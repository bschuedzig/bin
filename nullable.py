#!/usr/bin/python
import sys
import xml.etree.ElementTree as ET
from os import path


def main():

    try:
        file=sys.argv[1]
    except:
        print("Please provide .csproj file as first argument")
        sys.exit(1)

    print(file)

    if not path.exists(file):
        print("The file does not exist")
        sys.exit(1)

    tree = ET.parse(file)
    root = tree.getroot()

    nullable = root.findall("./PropertyGroup/Nullable")

    if len(nullable) == 1:

        val = nullable[0].text
        if val == "enable":
            print("Nullable entry is found & set correctly, skipping")
        else:
            print("Nullable entry is found, but not set correctly. Updating file.")
            nullable[0].text = "enable"
            tree.write(file)

    else:
        print("Nullable entry not found, adding")
        propertygroup = root.findall("./PropertyGroup")
        if len(propertygroup) == 1:
            propertygroup = propertygroup[0]
        else:
            propertygroup = ET.SubElement(root, "PropertyGroup")

        nullable = ET.SubElement(propertygroup, "Nullable")
        nullable.text = "enable"

        tree.write(file)


if __name__ == "__main__":
    main()
