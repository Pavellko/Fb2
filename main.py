import lxml.etree as et
import re

fname = 'Я весь внутри плачу.fb2'

with open(fname, 'rb') as f:
    data = f.read()
    
tree = et.fromstring(data)

ns = {'ns': "http://www.gribuser.ru/xml/fictionbook/2.0"}

for bin_eb in tree.xpath('//ns:binary', namespaces=ns):
    bin_eb.getparent().remove(bin_eb)
for bin_ed in tree.xpath('//ns:description', namespaces=ns):
    bin_ed.getparent().remove(bin_ed)
global cleart, cleart2
cleart = et.tounicode(tree)
cleart = re.sub(r'\<[^>]*\>', '', cleart)

print(cleart)