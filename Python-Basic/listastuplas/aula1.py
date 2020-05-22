idades = [12, 15, 20, 25]
idades.extend([13, 19])
print(idades)

idades_ano_que_vem = [idade+1 for idade in idades]
print(idades_ano_que_vem)
