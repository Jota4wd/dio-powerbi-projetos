import mysql.connector
import xml.etree.ElementTree as ET

# Configurações de conexão
config = {
    'user': 'adm',
    'password': 'senhadenovedigitos',
    'host': 'mariadb-171343-0.cloudclusters.net',
    'port': 10001,
    'ip address: 209.209.40.83'
    'database': 'financial_sample',
    'ssl_ca': 'ca.pem'  # Certificado CA, se necessário
}

# Conectar ao banco de dados
conn = mysql.connector.connect(**config)
cursor = conn.cursor()

# Nome do arquivo XML
xml_file = "financial_sample.xml"

# Analisa o XML
tree = ET.parse(xml_file)
root = tree.getroot()

# Inserção das transações
for transaction in root.findall('transactions/transaction'):
    transaction_id = int(transaction.find('transaction_id').text)
    customer_id = int(transaction.find('customer_id').text)
    transaction_date = transaction.find('transaction_date').text
    total_amount = float(transaction.find('total_amount').text)

    # Verifica se os valores estão vazios ou nulos e substitui por None
    if not transaction_date:
        transaction_date = None

    # Insere os dados no banco de dados
    qry_insert = """
        INSERT INTO Transactions (transaction_id, customer_id, transaction_date, total_amount)
        VALUES (%s, %s, %s, %s)
    """
    cursor.execute(qry_insert, (transaction_id, customer_id, transaction_date, total_amount))

# Commit e fecha a conexão
conn.commit()

# Verificar se o comando de inserção foi bem-sucedido
if cursor.rowcount > 0:
    print("Inserção bem-sucedida!")
else:
    print("Nenhum registro inserido.")

cursor.close()
conn.close()
