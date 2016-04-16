import xml.etree.ElementTree as etree
new_feed = etree.Element('{http://www.w3.org/2005/Atom}feed', attrib={'{http://www.w3.org/XML/1998/namespace}lang': 'en'})
sub = etree.SubElement(new_feed, 'sample')
new_feed.attrib['testAttribute'] = 'myvalue'
sub_sub = etree.SubElement(sub, 'thechild')
print(etree.tostring(new_feed)) 
