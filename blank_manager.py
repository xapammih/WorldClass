class BlankManager:

    def __init__(self, pdf_generator, data_handler, printer):
        self.pdf_generator = pdf_generator(data_handler=data_handler)
        self.printer = printer()

    def save_pdf(self, path):
        self.pdf_generator.save_pdf(path)

    def print_pdf(self):
        self.pdf_generator.save_pdf(r'.\data\lastblank.pdf')
        self.printer.print_file(r'.\data\lastblank.pdf')

