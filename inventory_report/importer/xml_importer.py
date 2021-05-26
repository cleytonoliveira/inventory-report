from inventory_report.importer.importer import Importer
import xml.etree.ElementTree as ET


class XmlImporter(Importer):
    def import_data(pathfile):
        if pathfile.endswith('xml'):
            with open(pathfile) as file:
                reporter = []
                tree = ET.parse(file)
                root = tree.getroot()
                all_records = root.findall('record')
                for item in all_records:
                    inventory = {element.tag: element.text for element in item}
                    reporter.append(inventory)
                return reporter
        else:
            raise ValueError('Arquivo inválido')
