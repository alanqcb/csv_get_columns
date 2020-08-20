# -*- coding: UTF-8 -*-
# coding: utf-8
import os
import substring
import csv
first_lines = []
files = []
lines_aux = []
linex_aux_2 = []
# Lista definitiva, armazenará um csv da maneira que deve ser lido pelo excell

## identifica cada csv na pasta atual e armazena na Lista files.
# r=root, d=directories, f = files
for r, d, f in os.walk('.'):
    for file in f:
        if '.csv' in file:
            files.append(os.path.join(r, file))
for f in files:
    ######## lê a primeira linha de cada arquivo csv e guarda na Lista first_lines. 
    ######## pode ser utf-8, utf-8-sig, utf-16, utf-16le e utf-16be
    with open(f, "r", encoding="utf-8-sig") as csvfile:
        first_lines.append(csvfile.readline())

linha_um = "gato preto;a;sabiá"
leitor = csv.DictReader(linha_um)
print(leitor)