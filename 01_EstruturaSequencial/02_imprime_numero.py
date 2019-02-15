'''
lembrando que nesse caso do INPUT já estamos convertendo para int pois por defaut ele vem como string.
Aqui está sendo usado o RAW_INPUT por causa da vesão do Python (mais antiga), atualmente usaremos INPUT, beleza? 
A partir da versão 3.0 usamos INPUT
'''
x = int(raw_input("Informe um numero: "))
print "O numero informado foi:", x
