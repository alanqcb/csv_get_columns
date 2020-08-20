# -*- coding: UTF-8 -*-
# coding: utf-8
######## Python 3.7.9
import os
import substring
import csv
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
## definido para ler somente os arquivos da mesma pasta
path = '.'
multiplos_cabecalhos = []
## duas Listas auxiliares
first_lines = []
files = []
# Lista definitiva, armazenará um csv da maneira que deve ser lido pelo excell
## identifica cada csv na pasta atual e armazena na Lista files.
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.csv' in file:
            files.append(os.path.join(r, file))
files.pop()
for f in files:
    ######## lê a primeira linha de cada arquivo csv e guarda na Lista first_lines. 
    ######## pode ser utf-8, utf-8-sig, utf-16, utf-16le e utf-16be
    with open(f, "r", encoding="utf-8-sig") as csvfile:
        first_lines.append(csvfile.readline())
### agora escrevemos um novo csv de maneira organizada, no formato
### base;          diretorio;        tabela;       colunas;
### nome_da_pasta; nome_do_diretorio; nome_do_csv; first_line_dividida_por_ponto_virgula.
# primeira tarefa é tornar a lista first_line em array bidimensional.
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
            linha_definitiva.append(linha_tmp[:]+ "\r\n")
    return (linha_definitiva + list("\r\n"))
############
## coloca todas as listas em uma lista
for linha_a_linha in first_lines:
    multiplos_cabecalhos.append(cada_linha_em_csv(linha_a_linha))
## escreve a lista de listas em um csv


print("vai ser salvo no diretório anterior")
with open("output\\out.csv", "w", encoding="utf-8-sig") as f:
    writer = csv.writer(f)
    writer.writerows(multiplos_cabecalhos)
print("fim")
## esse input serve para colocar breakpoint e debugar os valores das variaveis
input()
