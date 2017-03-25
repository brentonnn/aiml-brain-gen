import aiml
import xml.dom.minidom
import os
import argparse


def main(fNameList="aiml_file_list.txt", brainFileName="brain_file.brn", stdStartup=False):

    xmll ="<aiml version=\"1.0.1\" encoding=\"UTF-8\">\n<category>\n<pattern>LOAD AIML B</pattern>\n<template>\n"

    with open(fNameList) as f:
        c = f.readlines()
        c = [x.strip() for x in c]

    for line in c:
        xmll += "<learn>" + line + "</learn>\n"

    xmll += "</template>\n</category>\n</aiml>"

    pretty_xml = xml.dom.minidom.parseString(xmll)


    with open("std-startup.xml", "w") as z:
        z.write(pretty_xml.toprettyxml())

    kernel = aiml.Kernel()
    kernel.bootstrap(learnFiles = "temp.xml", commands = "load aiml b")
    kernel.saveBrain(brainFileName)

    print("Brain file save to:" + brainFileName)

    if not stdStartup:
        os.remove('std-startup.xml')
    else:
        print("Saving 'std-startup.xml'")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='This program creates brain files for aiml bots')
    parser.add_argument('-i','--input', default='aiml_file_list.txt', help='Input file with filenames to include in brain file')
    parser.add_argument('-n','--brainfile', default='brain_file.brn', help='Name of brain file')
    parser.add_argument('-s','--stdstartup', default=False, help='Select true if you would like the raw source file saved for the brain file')
    args = parser.parse_args()

    print("Running build...")
    main(args.input, args.brainfile, args.stdstartup)
