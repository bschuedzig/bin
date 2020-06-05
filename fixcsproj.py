#!/usr/bin/python
import sys
import glob
import os
import xml.etree.ElementTree as ET
from os import path

def ensureProperty(root, key, val):

    path = "./PropertyGroup/" + key
    found = root.findall(path)

    if len(found) == 1:
        found[0].text = val

    else:
        propertygroup = root.findall("./PropertyGroup")
        if len(propertygroup) == 1:
            propertygroup = propertygroup[0]
        else:
            propertygroup = ET.SubElement(root, "PropertyGroup")

        found = ET.SubElement(propertygroup, key)
        found.text = val

def processFile(file):

    print "Updating " + file
    tree = ET.parse(file)
    root = tree.getroot()

    ensureProperty(tree, "Nullable", "enable")
    ensureProperty(tree, "RestorePackagesWithLockFile", "true")

    tree.write(file)

def main():

    print "Starting"

    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(".csproj"):
                processFile(os.path.join(root, file))

if __name__ == "__main__":
    main()
