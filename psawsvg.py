#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os, sys, envoy
import xml.etree.ElementTree as ET

#namespace definition:
SVG_NS = "http://www.w3.org/2000/svg"

#filename is first argument:
filename = sys.argv[1]


def parse_xml():
    tree = ET.parse(filename)

    root = tree.getroot()

    for layer in tree.iter(tag='g'):
     print layer

    for child_of_root in root:
     for grandchild in child_of_root:
      try:
       print child_of_root.tag
       break
      except AttributeError:
        print 'no label'
    #for node in tree.findall('.//{%s}g' % SVG_NS):
    #    print 'n=', node


parse_xml()

#Check input file for layers:

#def check_for_layer(line):


#for line in fileinput.input():
# check_for_layers(line)



#for layer in layers:
# (size, ID, husleje, rooms, Postnummer, apturl) = parseRow(row)

#list layers with names (and existing params if available):

#check input file for exsisting PSAW attribs:

#ask for psaw params:

#speed:

#power:

#passes:

#assistair:

