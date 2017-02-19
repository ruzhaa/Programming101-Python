import json
import xml.etree.ElementTree as ET


class Jsonable:
    def to_json(self):
        return json.dumps({'dict': self.__dict__,\
          'class_name': self.__class__.__name__}, indent=4)

    @classmethod
    def from_json(cls, json_string):
        cls_dict = json.loads(json_string)
        cls_name = eval(cls_dict['class_name'])
        args = cls_dict['dict']
        if cls == cls_name:
            return cls_name(**args)
        else:
            ValueError


class XMLable:
    def to_xml(self):
        root = ET.Element(self.__class__.__name__)
        for prop in self.__dict__:
            b = ET.SubElement(root, prop)
            ET.SubElement(b, self.__dict__[prop])
        return ET.tostring(root)

    @classmethod
    def from_xml(cls, xml_string):
        print(ET.XML(xml_string))
        root = ET.fromstring(xml_string)
        cls_dict = {}
        for elem in root:
            for child in elem.getchildren():
                cls_dict[elem.tag] = child.tag
        return eval(root.tag)(**cls_dict)


class Panda(Jsonable, XMLable):
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name


class Person(Jsonable, XMLable):
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name

person = Person(name='Rado')
# print(Panda.from_json(person.to_json()))

# p = Panda(name='ivo')
# # print(p.to_json())
# # print(p.to_xml())
# json_string = p.to_json()
# xml_string = p.to_xml()

# p1 = Panda.from_json(json_string)
# p2 = Panda.from_xml(xml_string)
# print(p == p1)
