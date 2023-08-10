from itemadapter import ItemAdapter
from varredor_de_preco.utiliti import funcao_email, interface
import openpyxl

class VarredorDePrecoPipeline:
    def open_spider(self,spider):
        self.workbook = openpyxl.Workbook()
        self.workbook['Sheet'].title = 'Lista Preço'
        self.workbook['Lista Preço'].append(['Marca','Preço'])

    def process_item(self,item,spider):
        produto = ItemAdapter(item).asdict()
        self.workbook['Lista Preço'].append([produto["Marca"],produto["Preço"]])
        return item

    def close_spider(self,spider):
        nome_tabela = ['Celulares Importados.xlsx']
        self.workbook.save(nome_tabela[0])
        destinatario = [interface()]
        funcao_email(destinatario, nome_tabela)


