from varredor_de_preco.email_model import Email
import PySimpleGUI as sg

def interface():
    sg.theme('Topanga')
    return sg.popup_get_text('Digite o E-mail, que irá receber o relatório', title='Email')

def funcao_email(destinatario, nome_tabela):
    send = Email('E-mail do rementente','Senha que permite a comunicação com python')
    mensagem = 'Segue o relatório de preços dos celulares importados.'
    send.defenior_conteudo(email_remetente='E-mail do rementente', lista_de_contatos=destinatario,
                           topico='Relatório Celulares Importados', conteudo_email=mensagem)
    send.anexar_arquivo(nome_tabela)
    send.enviar_email(intervalo_em_segundos=30)
    print('E-mail enviado com sucesso!')


