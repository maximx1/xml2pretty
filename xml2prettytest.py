import unittest
from xml2pretty import XMLFormatter

class TestXMLFormatter(unittest.TestCase):
    def setUp(self):
        self.HTMLBefore = "<!DOCTYPE html><html><head><title>Sample html</title></head><body><p><div/></p></body></html>"
        self.HTMLAfter = "<!DOCTYPE html>\n<html>\n\t<head>\n\t\t<title>Sample html</title>\n\t</head>\n\t<body>\n\t\t<p>\n\t\t\t<div/>\n\t\t</p>\n\t</body>\n</html>\n"
        self.XMLBefore = "<root><tag1 a='blah'><tag2 /></tag1></root>"
        self.XMLAfter = "<root>\n\t<tag1 a=\"blah\">\n\t\t<tag2/>\n\t</tag1>\n</root>\n"
        
    def test_testBeautifyHTML(self):
        self.assertEqual(XMLFormatter.beautifyXMLString(self.HTMLBefore), self.HTMLAfter)
        
    def test_testBeautifyXML(self):
        self.assertEqual(XMLFormatter.beautifyXMLString(self.XMLBefore), self.XMLAfter)
        
if __name__ == '__main__':
    unittest.main()
