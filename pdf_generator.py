import os
import io

from PyPDF2 import PdfWriter, PdfReader
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

from patterns import PATTERNS


class PdfGenerator:

    def __init__(self, data_handler):
        self.data_handler = data_handler
        self.patterns = PATTERNS
        self.init_fonts()

        self.last_inputs = {}
        self.last_pattern = ''

    def init_fonts(self):
        font_path = r'.\data\fonts\Roboto-Regular.ttf'
        pdfmetrics.registerFont(TTFont('Roboto', font_path))
        font_path = r'.\data\fonts\RobotoMono-VariableFont_wght.ttf'
        pdfmetrics.registerFont(TTFont('RobotoMono', font_path))

    def get_data(self):

        inputs = self.data_handler.__dict__
        processed_inputs = {}

        processed_inputs.update({k: v for k, v in inputs.items() if 'step' not in k})

        steps = {}
        step_blacklist = [
            '',
            'Консультации',
            'Диагностика',
            'Лицо ап.косм',
            'Тело ап.косм',
            'Лицо инъекции',
            'Тело инъекции',
            'Лицо эстетика',
            'Тело эстетика',
            'СПА услуги'
        ]

        for i in range(3):
            step = {k: v for k, v in inputs.items() if (f'step_{i + 1}_procedure_' in k) & \
                                                       ('period' not in k) & \
                                                       (v not in step_blacklist)}
            sorted_proc_num = sorted(list(map(lambda s: int(s.split('_')[-1]), step.keys())))
            for j, n in enumerate(sorted_proc_num):
                steps.update({f'step_{i + 1}_procedure_{j + 1}': inputs.get(f'step_{i + 1}_procedure_{n}', '')})
                steps.update({f'step_{i + 1}_count_procedures_{j + 1}': inputs.get(f'step_{i + 1}_count_procedures_{n}', '')})
                steps.update({f'step_{i + 1}_procedure_period_{j + 1}': inputs.get(f'step_{i + 1}_procedure_period_{n}', '')})

        processed_inputs.update(steps)
        processed_inputs.update({k: v for k, v in inputs.items() if 'commentary' in k})

        processed_inputs = {k: v.strip() for k, v in processed_inputs.items()}
        processed_inputs.update({k: ' ' * 15 + v for k, v in processed_inputs.items() if 'commentary' in k})
        processed_inputs['step_4_commentary'] = processed_inputs['step_4_commentary'].strip()

        return processed_inputs

    def load_bg(self, pattern):
        return self.patterns.get(pattern).get('bg')

    def load_options(self, pattern):
        return self.patterns.get(pattern).get('options')

    def fill_blank(self, pattern):
        inputs = self.get_data()
        options = self.load_options(pattern)
        bg = self.load_bg(pattern)
        if (self.last_inputs != inputs) | (self.last_pattern != pattern):
            self.last_inputs = inputs.copy()
            self.last_pattern = pattern

            packet = io.BytesIO()
            can = canvas.Canvas(packet, pagesize=A4)
            for form, text in inputs.items():
                if text and form in options:
                    form_opts = options[form]
                    self.add_item_on_page(can, form_opts, text)
            can.save()
            packet.seek(0)

            data_pdf = PdfReader(packet)
            bg_pdf = PdfReader(open(os.path.join(r'.\data\bgs', bg), 'rb'))

            self.output = PdfWriter()

            page = bg_pdf.pages[0]
            page.merge_page(data_pdf.pages[0])
            self.output.add_page(page)

    def add_item_on_page(self, can, option, text):
        def split_str_by_length(s, length):
            lines = []
            stack = s
            while len(stack) > 0:
                if len(stack) <= length:
                    lines.append(stack)
                    stack = ''
                else:
                    if ' ' in stack[:length + 1]:
                        idx = stack[:length].rfind(' ')
                        lines.append(stack[:idx])
                        stack = stack[idx + 1:]
                    else:
                        idx = length
                        lines.append(stack[:idx])
                        stack = stack[idx:]
            return lines

        mode = option.get('mode', 'string')
        align = option.get('align', 'left')
        x, y = option.get('position', (0, 0))
        font = option.get('font', 'Roboto')
        fontsize = option.get('fontsize', 8)
        leading = option.get('leading', 15.45)
        max_len = option.get('max_len', 30)
        max_text_rows = option.get('max_text_rows', 2)

        if mode == 'string':
            can.setFont(font, fontsize)
            if align == 'centred':
                can.drawCentredString(x, y, text)
            elif align == 'left':
                can.drawString(x, y, text)

        elif mode == 'text':
            textobj = can.beginText(x, y)
            textobj.setFont(font, fontsize, leading)
            text_lines = split_str_by_length(text, max_len)
            for line in text_lines[:max_text_rows]:
                textobj.textLine(line)
            can.drawText(textobj)

    def save_pdf(self, path, pattern='v2'):
        self.fill_blank(pattern)
        output_stream = open(path, 'wb')
        self.output.write(output_stream)
        output_stream.close()

