#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sistema para gerar dados pessoais para testes no desenvolvimento de ferramentas
@author: Deney Araujo - deneyaraujo@gmail.com
Curumim [v. 0.1]
"""
import pandas as pd
import random
import datetime
import argparse

def setOptions():
    option = argparse.ArgumentParser(description = '''Curumim [v. 0.1]''')
    option.add_argument('-n','--number',      nargs='?', required=True, help='*Quantidade de registros a ser gerada')
    option.add_argument('-o','--output',     nargs='?', required=True, help='*Nome do arquivo de saída')   
    return option.parse_args()

def cpf():                                                        
    cpf = [random.randint(0, 9) for x in range(9)]                              
    for _ in range(2):                                                          
        val = sum([(len(cpf) + 1 - i) * v for i, v in enumerate(cpf)]) % 11      
        cpf.append(11 - val if val > 1 else 0)                                  
    return '%s%s%s.%s%s%s.%s%s%s-%s%s' % tuple(cpf)

setup = setOptions()
n = setup.number
output = setup.output

quantidadeRegistros = int(n)
outPut = output
dataNames = pd.read_csv('NomesBrasileiros_sexo.txt', encoding='utf-8', dtype=str, header=None)
dataSurNames = pd.read_csv('SobrenomesBrasileiros.txt', encoding='utf-8', dtype=str, header=None)
dataNamesFem = pd.read_csv('NomesFemininos.txt', encoding='utf-8', dtype=str, header=None)

opcoes =['simple','double','triple'] #weights
start=1

with open(outPut, 'w') as save:
    save.write('Identificador\tNome\tNome da Mae\tNascimento\tSexo\tCPF\n')
    for i in range(quantidadeRegistros):
        x = random.choices(opcoes, weights=[0.05,0.8,0.15], k=1)
        nome = random.choice(dataNames[0])
        sobrenome = random.choice(dataSurNames[0])
        nascimento = datetime.date(random.randint(1900,2019), random.randint(1,12),random.randint(1,28)).strftime("%d-%m-%Y")
        if 'simple' in x:
            save.write(f'ID_{str(start).zfill(9)}\t'+nome.rsplit('-',1)[0]+' '+sobrenome+
                           '\t'+random.choice(dataNamesFem[0])+' '+random.choice(dataSurNames[0])+' '+sobrenome+
                           '\t'+str(nascimento)+
                           '\t'+nome.rsplit('-',1)[1]+
                           '\t'+cpf()+'\n')
        elif 'double' in x:
            save.write(f'ID_{str(start).zfill(9)}\t'+nome.rsplit('-',1)[0]+' '+sobrenome+' '+random.choice(dataSurNames[0])+
                           '\t'+random.choice(dataNamesFem[0])+
                           ' '+random.choice(dataSurNames[0])+' '+sobrenome+
                           '\t'+str(nascimento)+
                           '\t'+nome.rsplit('-',1)[1]+
                           '\t'+cpf()+'\n')
        else:
            save.write(f'ID_{str(start).zfill(9)}\t'+nome.rsplit('-',1)[0]+' '+random.choice(dataSurNames[0])+' '+sobrenome+' '+random.choice(dataSurNames[0])+
                           '\t'+random.choice(dataNamesFem[0])+' '+random.choice(dataSurNames[0])+
                           ' '+random.choice(dataSurNames[0])+' '+sobrenome+
                           '\t'+str(nascimento)+
                           '\t'+nome.rsplit('-',1)[1]+
                           '\t'+cpf()+'\n')
        start+=1
