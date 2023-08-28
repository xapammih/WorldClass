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

    def get_data(self):
        return self.data_handler.__dict__

    def load_bg(self, pattern):
        return self.patterns.get(pattern).get('bg')

    def load_options(self, pattern):
        return self.patterns.get(pattern).get('options')

    def fill_blank(self, pattern):
        inputs = self.get_data()
        options = self.load_options(pattern)
        bg = self.load_bg(pattern)
        if (self.last_inputs != inputs) | (self.last_pattern != pattern):
            self.last_inputs = inputs
            self.last_pattern = pattern

            # Р—Р°РїРѕР»РЅРµРЅРёРµ Р±Р»Р°РЅРєР° Р”РѕРїРёСЃС‚СЊ
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
            for line in text_lines:
                textobj.textLine(line)
            can.drawText(textobj)

    def save_pdf(self, path, pattern='v1'):
        self.fill_blank('v1')
        output_stream = open(path, 'wb')
        self.output.write(output_stream)
        output_stream.close()