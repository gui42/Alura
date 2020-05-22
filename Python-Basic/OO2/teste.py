import random
from modelo import Filme
from modelo import Serie
from modelo import Playlist

filme = Filme("avengers - end game", 2019, 182)
for x in range(0,random.randint(0, 10)):
    filme.dar_like()

serie = Serie("Friends", 1999, 9)
for x in range(0, random.randint(0,10)):
    serie.dar_like()

filme2 = Filme("todo mundo em panico", 2000, 93)
for x in range(0, random.randint(0,10)):
    filme2.dar_like()

serie2 = Serie("Bojack", 2015, 6)
for x in range(0, random.randint(0,10)):
    serie2.dar_like()

series = [filme, serie, serie2, filme2]

playlist_fim_de_semana = Playlist("fim de semana", series)

for item in playlist_fim_de_semana:
    print(item)

print(f"Tamanho da playlist: {len(playlist_fim_de_semana)}")

print(serie2 in playlist_fim_de_semana)