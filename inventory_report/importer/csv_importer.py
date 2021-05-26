from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    def import_data(pathfile):
        if pathfile.endswith('csv'):
            reporter = []
            with open(pathfile) as file:
                reporter_csv = csv.DictReader(file)
                for row in reporter_csv:
                    reporter.append(row)
                return reporter
        else:
            raise ValueError('Arquivo inválido')
