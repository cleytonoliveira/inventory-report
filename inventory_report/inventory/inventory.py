import csv
import json
import xml.etree.ElementTree as ET
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


def reporter_csv(file):
    reporter = []
    reporter_csv = csv.DictReader(file)
    for row in reporter_csv:
        reporter.append(row)
    return reporter


def reporter_json(file):
    content = file.read()
    reporter = json.loads(content)
    return reporter


def reporter_xml(file):
    reporter = []
    tree = ET.parse(file)
    root = tree.getroot()
    all_records = root.findall('record')
    for item in all_records:
        inventory = {element.tag: element.text for element in item}
        reporter.append(inventory)
    return reporter


class Inventory:
    @classmethod
    def import_data(self, pathfile, type_report):
        with open(pathfile) as file:
            if pathfile.endswith('csv'):
                reporter = reporter_csv(file)

            elif pathfile.endswith('json'):
                reporter = reporter_json(file)

            else:
                reporter = reporter_xml(file)

            if type_report == 'simples':
                return SimpleReport.generate(reporter)
            else:
                return CompleteReport.generate(reporter)
