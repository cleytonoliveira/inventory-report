# from inventory_report.importer.csv_importer import CsvImporter
# from inventory_report.importer.json_importer import JsonImporter
# from inventory_report.importer.xml_importer import XmlImporter
from abc import ABC, abstractmethod


class Importer(ABC):
    @abstractmethod
    def import_data(self, pathfile):
        pass
