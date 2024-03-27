from lxml import etree
agent = etree.XML(
    '<agent type="secret"><prenom>James</prenom><nom>Bond</nom></agent>')
agent.attrib
dict((e.tag,e.text)for e in agent.iterchildren())
matricule = etree.SubElement(agent,"matricule")
matricule.text = "007"
etree.indent(agent)
print(etree.tostring(agent,pretty_print = True).decode())