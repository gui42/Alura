from acesso_cep import BuscaEndereco

cep = input("CEP: ")
obj_cep = BuscaEndereco(cep)
bairro, cidade, uf, logradouro = obj_cep.acessa_via_cep()
print(logradouro, bairro, cidade, uf)
