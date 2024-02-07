import pandas as pd

class ExcelGenerator:
    def generate_excel_file(self, data):
        df = pd.DataFrame(data=data)
        df.to_excel('xml_files/arquivo_final.xlsx', index=False)
