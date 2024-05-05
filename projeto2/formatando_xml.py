import re

def format_xml(xml_string):
    # Adiciona recuo e espaços entre as tags usando expressões regulares
    formatted_xml = re.sub(r'><', '>\n<', xml_string)

    return formatted_xml

# Carrega o arquivo XML do mesmo diretório
file_path = "Financial_Sample.xml"
with open(file_path, 'r') as file:
    xml_string = file.read()

# Formata o XML
formatted_xml = format_xml(xml_string)

# Salva o XML formatado em um novo arquivo
output_file_path = "xml_formatado.xml"
with open(output_file_path, 'w') as output_file:
    output_file.write(formatted_xml)

print("XML formatado salvo como xml_formatado.xml.")
