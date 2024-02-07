from bs4 import BeautifulSoup
import glob

class PagamentosReader:

    def __init__(self):
        self.elements_found_list_to_excel = []
    def __load_xml_files(self):
        dir_xml_files = r'xml_files/*.xml'
        xml_files = glob.glob(dir_xml_files)
        return xml_files

    def read_xml_files(self):
        for xml_file in self.__load_xml_files():
            with open(xml_file, 'r') as file:
                content = file.read()
                xml_data = BeautifulSoup(content, 'xml')
                per_apur = xml_data.find('perApur')
                ver_proc = xml_data.find('verProc')
                cpf_trab = xml_data.find('cpfTrab')
                remun_per_apur = xml_data.find('remunPerApur')
                remun_loaded_data = remun_per_apur.findAll('itensRemun')
                remun_list = []
                for remun in remun_loaded_data:
                    cod_rubr = remun.find('codRubr')
                    vr_rubr = remun.find('vrRubr')
                    remun_data = {'cod_rub': cod_rubr.text, 'vr_rubr': vr_rubr.text}
                    remun_list.append(remun_data)
                final_data_to_excel = {'per_apur': per_apur.text,
                                       'ver_proc': ver_proc.text,
                                       'cpf_trab': cpf_trab.text,
                                       'dados_remun': remun_list}
                self.elements_found_list_to_excel.append(final_data_to_excel)

                return self.elements_found_list_to_excel


