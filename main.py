import lxml.etree as et
import re
import pyttsx3


fname = 'Я весь внутри плачу.fb2'

with open(fname, 'rb') as f:
    data = f.read()
    
tree = et.fromstring(data)

ns = {'ns': "http://www.gribuser.ru/xml/fictionbook/2.0"}
for bin_eb in tree.xpath('//ns:binary', namespaces=ns):
    bin_eb.getparent().remove(bin_eb)
for bin_ed in tree.xpath('//ns:description', namespaces=ns):
    bin_ed.getparent().remove(bin_ed)
cleart = et.tounicode(tree)
cleart = re.sub(r'\<[^>]*\>', '', cleart)


engine = pyttsx3.init()
voice = engine.getProperty('voices')
zx={}
for i in voice:
    zx[i.name] = i.id
    
print(zx.items())

engine.setProperty('voice', zx['Microsoft Irina Desktop - Russian'])

engine.say(cleart)
engine.runAndWait()