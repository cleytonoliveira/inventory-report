from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    def import_data(pathfile):
        if pathfile.endswith('json'):
            with open(pathfile) as file:
                content = file.read()
                reporter = json.loads(content)
                return reporter
        else:
            raise ValueError('Arquivo inválido')
