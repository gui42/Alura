import re
email = []
email.append("Meu numero é 99582144")
email.append("fale comigo em 9940-5070")
email.append("9951-2813 é meu numero")
email.append("99940-5070 é meu novo celular")
email.append("1234-0000 , 12345-0123, e 0000-0000")
lista = []

padrao = "[0-9]{4,5}[-]*[0-9]{4}"
for x in range(0,len(email)):
    lista.append(re.findall(padrao, email[x]))
    print(re.search(padrao, email[x]).group())
