import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "colocar sid"
# Your Auth Token from twilio.com/console
auth_token  = "colocar token"
client = Client(account_sid, auth_token)

# Passo a passo de solução

# 1- Abrir os arquivos em Excel
lista_meses= ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mês {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}') 





message = client.messages.create(
    to="+colocar seu numero", 
    from_="colocar numero disponibilizado pelo twilio",
    body=f'No mês {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')

print(message.sid)


# 2- Para cada arquivo: Verificar se algum valor na coluna vendas naquele arquivo é maior que 55.000


# 3- Se for maior que 55.000 -> Envia um SMS com o nome, o mês e se as vendas do vendedor

# 4- Caso não seja maior que 55.000 nenhuma aplicação é feita

