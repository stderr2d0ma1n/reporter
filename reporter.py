from docxtpl import DocxTemplate
from docxtpl import InlineImage
from docx.shared import Mm
import os
import argparse
import datetime


parser = argparse.ArgumentParser(description='Simple tool for writing pentest report for multiply same vulnerabilies.')
parser.add_argument(
    '-t', '--template', type=str,
    default=None, help='Provide template docx file'
)
parser.add_argument(
    '-d', '--dir', type=str,
    default='./', help='Provide directory with pocs'
)
parser.add_argument(
    '-o', '--output', type=str,
    default=datetime.datetime.now().strftime("%d-%m-%Y_%H:%M") + '.docx', help='Provide output file'
)
args = parser.parse_args()

tpl = DocxTemplate('template.docx')
content = {'hosts': []}
for screen in os.listdir(args.dir):
    if not screen.startswith('.'):
        host_addr = screen.split('.')[0].replace('_', '.')
        host_poc = InlineImage(tpl, image_descriptor=args.dir + '/' + screen, width=Mm(150))
        content['hosts'].append({
            'host_addr': host_addr,
            'host_poc': host_poc
        })
    else:
        continue

tpl.render(content)
tpl.save(args.output)
