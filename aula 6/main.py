import pandas as pd
from twilio.rest import Client
import openpyxl as xl
# pandas
# openpyxl
# twilio

# Passo a Passo Solução

# Abrir os 6 arquivos em excel

# Your Account SID from twilio.com/console
account_sid = "ACe555dadaced23bbf562b45654b2dcff8"
# Your Auth Token from twilio.com/console
auth_token = "51729746f3ce674818294072e4304863"
client = Client(account_sid, auth_token)

lista_meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho"]

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f"{mes}.xlsx")
    if (tabela_vendas["Vendas"] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas["Vendas"] > 55000, 'Vendedor'].values[0]
        venda = tabela_vendas.loc[tabela_vendas["Vendas"] > 55000, 'Vendas'].values[0]
        message = client.messages.create(
            to="+5561982970840",
            from_="++13303022824",
            body="Oi amor")
        print(message.sid)


# Para cada arquivos:



# Verificar se algum valor na coluna vendas e maior que 55 mil

# se for maior do que 55 mil -> Enviar SMS com o Nome, o mes e as Vendas dos vendedor

# Caso não seja maior do que 55 mil não quero fazer nada
