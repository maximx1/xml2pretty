import sys
from xml.dom import minidom

"""
    Testable xml formatter.
"""
class XMLFormatter:
    """
        Formats an xml string to look pretty.
    """
    @staticmethod
    def beautifyXMLString(xmlString):
        return minidom.parseString(xmlString).toprettyxml()[23:]
    
"""
    Parse and command.
"""
class JeCommande:
    """
        Parses the commands coming in.
    """
    @staticmethod
    def run():
        routes = {1: JeCommande.printError, 2: JeCommande.inOnly, 3: JeCommande.inAndOut}
        routes[len(sys.argv)]()
    
    """
        For printing a usage.
    """
    @staticmethod
    def printError():
        print("Usage -> python xml2pretty [input_file.xml] [output_file.xml]")
    
    """
        For reading from file and printing to screen.
    """
    @staticmethod
    def inOnly():
        with open (sys.argv[1], "r") as inFile:
            print(XMLFormatter.beautifyXMLString(inFile.read().replace('\n', '')))
        
    """
        For reading from and writing to file.
    """
    @staticmethod
    def inAndOut():
        with open (sys.argv[1], "r") as inFile:
            with open (sys.argv[2], "w") as outFile:
                outFile.write(XMLFormatter.beautifyXMLString(inFile.read().replace('\n', '')))

# Run that shtuff            
JeCommande.run()