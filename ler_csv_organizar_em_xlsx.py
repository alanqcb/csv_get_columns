# -*- coding: UTF-8 -*-
# coding: utf-8
######## Python 3.7.9
import os
import substring
import csv
import json
def find_str(s, char):
    index = 0
    if char in s:
        c = char[0]
        for ch in s:
            if ch == c:
                if s[index:index+len(char)] == char:
                    return index
            index += 1
    return -1
path = '.'
multiplos_cabecalhos = []
first_lines = []
files = []
for r, d, f in os.walk(path):
    for file in f:
        if '.csv' in file:
            if "out.csv" not in file:
                files.append(os.path.join(r, file))
f = ""
for f in files:
    with open(f, "r", encoding="utf-8-sig") as csvfile:
        first_lines.append(csvfile.readline())
def cada_linha_em_csv(linha_csv):
    linha_tmp = ""
    linha_definitiva = []
    indice_colons = []
    linha_tmp = linha_csv
    while (find_str(linha_tmp,';') != -1):
        indice_colons.append(find_str(linha_tmp,';')+1)
        linha_definitiva.append(linha_tmp[:indice_colons[-1]-1])
        linha_tmp=linha_tmp[indice_colons[-1]:]
        if(find_str(linha_tmp,';') == -1):
            linha_definitiva.append(linha_tmp[:])
    return (linha_definitiva )
for linha_a_linha in first_lines:
    multiplos_cabecalhos.append(cada_linha_em_csv(linha_a_linha))
try:
    os.mkdir(".\\output")
    pass
except OSError as error:
    print (error)    
print("vai ser salvo no diretorio output")
print(files) 
print(multiplos_cabecalhos)
files_final = []
mc_aux = ""
for mc in multiplos_cabecalhos:
    mc_aux = mc_aux + str(mc)[1:-1] + ';';
mc_aux=mc_aux[:-1]
i1 = 0
for fi in files:
    for mc in multiplos_cabecalhos[i1]:
        files_final.append(fi[2:-4] +';' + str(mc) + ';')
    i1+=1
print("fim")
i=0
with open("output\\out.csv", "w", encoding="utf-8-sig") as f:

    for item in files_final:
        if (i==0):
            f.write("tabela; colunas;\r")    
            i+=1
        f.write(item+"\r")
