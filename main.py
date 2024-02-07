from xml_reader.pagamentos import PagamentosReader
from excel_generator.excel_generator import ExcelGenerator

if __name__ == '__main__':
    pagamentos = PagamentosReader()
    excel_generator = ExcelGenerator()
    result = pagamentos.read_xml_files()
    excel_generator.generate_excel_file(result)
