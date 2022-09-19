final_arquivo = False
string_vazia = ''
times=[]
lista=[]
total=0

meu_arquivo = open('resultados_jogos.txt', 'r')

while not final_arquivo: #enquanto True
    linha = meu_arquivo.readline().rstrip()#corintians:santos    
    if linha == string_vazia:
        final_arquivo = True        
    else:
        info_ex1 = linha.split(':')
        time1 = info_ex1[0]
        times.append(time1)
        gol = info_ex1[1]
        time2 = info_ex1[2]
        gol2=info_ex1[3]
        if int(gol) > int(gol2):
            lista.append(time1)
        elif int(gol2) > int(gol):
            lista.append(time2)

times = list(dict.fromkeys(times))
for i in range(len(times)):
    teste=lista.count(times[i])
    print(times[i],": ",teste," VICTORIES")


meu_arquivo.close()
