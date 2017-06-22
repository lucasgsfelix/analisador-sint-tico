#!/usr/bin/env python2.7.12
#-*- coding: utf-8 -*-
import unicodedata
import re

def A(tokens, i):
	aux = tokens[i].split('\t')
	if((aux[2]=='(')or(aux[3]=='1')or(aux[3]=='4')):
		i=B(tokens, i)
		i=Alinha(tokens,i)
		return i 
	else:
	 	i=erro(tokens, i, '||')
def Alinha(tokens, i):
	aux = tokens[i].split('\t')
	if(aux[2]=='||'):
		i=i+1
		i=B(tokens, i)
		i=Alinha(tokens, i)
		return i
	else:
		return i
def B(tokens, i):
	aux =  tokens[i].split('\t')
	if((aux[2]=='(')or(aux[3]=='1')or(aux[3]=='4')):
		i=D(tokens, i)
		i=Blinha(tokens, i)
		return i
	else:
		i=erro(tokens, i, '&&')
def Blinha(tokens, i):
	aux = tokens[i].split('\t')
	if(aux[2]=='&&'):
		i=i+1
		i=D(tokens, i)
		i=Blinha(tokens, i)
		return i 
	else:
		return i
# def C(tokens, i): comentário de bloco ctrl + shift + /
# 	aux = tokens[i].split('\t')
# 	if((aux[2]=='(')or(aux[3]=='1')or(aux[3]=='4')):
# 		i=D(tokens, i)
# 		i=Clinha(tokens, i)
# 		return i
# 	else:
# 		erro(tokens, i, '==/!=')
# def Clinha(tokens, i):
# 	aux = tokens[i].split('\t')
# 	if((aux[2]=='==')or(aux[2]=='!=')):
# 		i=i+1
# 		i=D(tokens, i)
# 		i=Clinha(tokens, i)
# 		return i
# 	else:
# 		return i
def D(tokens, i):
	aux = tokens[i].split('\t')
	if((aux[2]=='(')or(aux[3]=='1')or(aux[3]=='4')):
		i=E(tokens, i)
		i=Dlinha(tokens, i)
		return i
	else:
		i=erro(tokens, i, '</>')
def Dlinha(tokens, i):
	aux = tokens[i].split('\t')
	if((aux[2]=='>')or(aux[2]=='<')):
		i=i+1
		i=D2linha(tokens, i)
		return i
	else:
		return i
def D2linha(tokens, i):
	aux = tokens[i].split('\t')
	if(aux[2]=='='):
		i=i+1
		i=E(tokens, i)
		i=D2linha(tokens, i)
		return i
	else:
		return i
def E(tokens, i):
	aux = tokens[i].split('\t')
	if((aux[2]=='(')or(aux[3]=='1')or(aux[3]=='4')):
		i=F(tokens, i)
		i=Elinha(tokens, i)
		return i
	else:
		i=erro(tokens, i, '==/!=')
def Elinha(tokens, i):
	aux = tokens[i].split('\t')
	if((aux[2]=='==')or(aux[2]=='!=')):
		i=i+1
		i=F(tokens, i)
		i=Elinha(tokens, i)
		return i
	else:
		return i
def F(tokens, i):
	aux = tokens[i].split('\t')
	if((aux[2]=='(')or(aux[3]=='1')or(aux[3]=='4')):
		i=G(tokens, i)
		i=Flinha(tokens, i)
		return i
	else:
		i=erro(tokens, i, '+/-')
def Flinha(tokens, i):
	aux = tokens[i].split('\t')
	if((aux[2]=='+')or(aux[2]=='-')):
		i=i+1
		i=G(tokens, i)
		i=Flinha(tokens, i)
		return i
	else:
		return i
def G(tokens, i):
	aux = tokens[i].split('\t')
	if((aux[2]=='(')or(aux[3]=='1')or(aux[3]=='4')):
		i=H(tokens, i)
		i=Glinha(tokens, i)
		return i
	else:
		i=erro(tokens, i, '* /')
def Glinha(tokens, i):
	aux = tokens[i].split('\t')
	if((aux[2]=='*')or(aux[2]=='/')):
		i=i+1
		i=H(tokens, i)
		i=Glinha(tokens, i)
		return i
	else:
		return i
def H(tokens, i):
	aux = tokens[i].split('\t')
	if((aux[2]=='(')):
		i=i+1
		i=A(tokens, i)
		i=i+1
		aux = tokens[i].split('\t')
		if(aux[2]==')'):
			return i
	elif((aux[3]=='1')or(aux[3]=='4')):
		i=i+1
		return i
	else:
		i=erro(tokens, i, aux[2])
def erro(tokens, i, caractere):
	aux = tokens[i].split('\t')
	if(caractere!=''):
		print "Existe um erro na linha ", aux[0], "coluna ", aux[1], "!!! Parece que você esqueceu o caractere", caractere
	exit()
	i = linha_nova(tokens, i)
	i = recuperacao_erro(tokens, i)
	return i
def linha_nova(tokens, i): #yeld
	aux = tokens[i].split('\t')
	a = int(aux[0])
	b=0
	while(1):
		aux = tokens[i].split('\t')
		if(a+1==int(aux[0])):
			break
		else:i=i+1
	return i 
def recuperacao_erro(tokens, i):
	aux = tokens[i].split('\t')
	#{,},if, for, while, comandos, expressao, declaracao, atribuicao
	if(aux[2]=='{'): #quer dizer que posso ter um if, while ou for
		print 'oi'
	elif(aux[2]=='}'):
		print 'oioi'

def expressao(tokens, i): #expressão pode ser lógica, aritmetica ou um numeral 
	i = A(tokens, i)
	return i

def declaracao(tokens, i):
	aux = tokens[i].split('\t')
	if((aux[2]=='int')or(aux[2]=='char')or(aux[2]=='float')):
		#faço um getNextChar
		i=i+1
		i=identificadores(tokens, i)
		i=i+1
		i = declaracao_linha(tokens, i)
		return i
def identificadores(tokens, i):
	#vai na posicao dos identificadores, são os tokens[0]
	aux = tokens[i].split('\t')
	if(int(aux[3])!=1): #o caracetere que vem depois dos identificadores de identificação não é um identificador
		print 'O token que deveria vir na linha', aux[0] ,'coluna', aux[1], 'deve ser um identificador ! '
		i = erro(tokens, i, '')
	else: 
		return i

def declaracao_linha(tokens, i): #essa função vai ser responsável por verificar se existem mais tokens sendo declarados juntos
	aux = tokens[i].split('\t')
	if(aux[2]==';'): #eu olho na minha lista de separadores
		return i
	elif(aux[2]==','):
		#faço um getNextSimbol()
		i=i+1
		i = identificadores(tokens, i)
		i = declaracao_linha(tokens, i) 
		return i
	elif(aux[2]=='='):
		i=i+1
		i = declaracao_atribuicao(tokens, i)
		return i
	else:
		print 'Há um erro na linha ', aux[0], 'coluna ', aux[1], 'você pode ter esquecido um token ou colocado colocado o token errado !'
		i = erro(tokens, i, '')
		return i
def declaracao_atribuicao(tokens, i):
	aux = tokens[i].split('\t')
	if((aux[3]=='1')or(aux[3]=='4')):
		i=i+1
		aux = tokens[i].split('\t')
		if(aux[2]==';'):
			return i
		else: 
			erro(tokens, i, ";")
	elif((aux[2]=='"')):
		i=i+1
		aux = tokens[i].split('\t')
		if(aux[3]=='4'):
			i=i+1
			aux = tokens[i].split('\t')
			if(aux[2]=='"'):
				i=i+1
				aux = tokens[i].split('\t')
				if(aux[2]==';'):
					return i
				else:erro(tokens, i, ";")
			else:erro(tokens, i, "\"")
	elif((aux[2]=='\'')):
		i=i+1
		aux = tokens[i].split('\t')
		if(aux[3]=='4'):
			i=i+1
			aux = tokens[i].split('\t')
			if(aux[2]=='\''):
				i=i+1
				if(aux[2]==';'):
					return i
				else:erro(tokens, i, ";")
			else:erro(tokens, i, "\'")
	else:
		print 'Há um erro na linha ', aux[0], 'coluna ', aux[1], 'você pode ter esquecido um token ou colocado colocado o token errado !'
		i = erro(tokens, i, '')
def condicao(tokens, i):
	aux = tokens[i].split('\t')
	if(aux[2]=='if'):
		i=i+1
		aux = tokens[i].split('\t')
		if(aux[2]=='('):
			i=i+1
			i = expressao(tokens, i)
			aux = tokens[i].split('\t')
			if(aux[2]==')'):
				i=i+1
				aux = tokens[i].split('\t')
				if(aux[2]=='{'):
					i=i+1
					i = bloco(tokens, i)
					i=i+1
					aux = tokens[i].split('\t') 
					if(aux[2]=='}'):
						i = condicao_linha(tokens, i)
						return i
					else:erro(tokens, i, "}")
				else:erro(tokens, i, "{")
			else:erro(tokens, i, ")")
		else:erro(tokens, i, "(")
def condicao_linha(tokens, i):
	aux = tokens[i].split('\t')
	if(aux[2]=='else'):
		i=i+1
		aux = tokens[i].split('\t')
		if(aux[2]=='{'):
			#i=i+1
			aux = tokens[i].split('\t')
			i = bloco(tokens, i)
			i=i+1
			aux = tokens[i].split('\t')
			if(aux[2]=='}'):
				return i
			else:erro(tokens, i, "}")
		else:erro(tokens, i, "{")
	else:
		return i

def bloco(tokens, i):
	aux = tokens[i].split('\t')
	if(aux[3]=='1'):
		i = atribuicao(tokens, i)
		i = bloco(tokens, i)
		return i
	elif((aux[2]=='int')or(aux[2]=='float')or(aux[2]=='char')):
		i = declaracao(tokens, i)
		i = bloco(tokens, i)
		return i
	elif((aux[2]=='for')or(aux[2]=='while')):
		i = repeticao(tokens, i)
		i = bloco(tokens, i)
		return i
	elif(aux[2]=='if'):
		i = condicao(tokens, i)
		i = bloco(tokens, i)
		return i
	elif((aux[2]=='scanf')or(aux[2]=='printf')):
		i = comandos(tokens, i)
		i = bloco(tokens, i)
	else:
		return i
def comandos(tokens, i):
	aux = tokens[i].split('\t')
	if(aux[2]=='printf'):
		i=i+1
	elif(aux[2]=='scanf'):
		i=i+1
	else: 
		i=erro(tokens, i, 'printf/scanf')

def atribuicao(tokens, i):
	aux = tokens[i].split('\t')
	if(aux[3]=='1'): # o que quer dizer que um identificador 
		i=i+1
		aux = tokens[i].split('\t')
		if(aux[2]=='='): # está recebendo um valor
			i=i+1
			aux = tokens[i].split('\t')
			if((aux[3]=='1')or(aux[3]=='4')):#atribui
				#i = expressao(tokens, i)
				i=i+1
				aux = tokens[i].split('\t')
				if(aux[2]==';'):		
					return i 
				else:
					i=erro(tokens, i, ";")
			elif((aux[2]=='"')): # quando estou recebendo um literal x = "a"
				i=i+1
				aux = tokens[i].split('\t')
				if(aux[3]=='4'):
					i=i+1
					aux = tokens[i].split('\t')
					if((aux[2]=='"')):
						i=i+1
						aux = tokens[i].split('\t')
						if(aux[2]==';'):
							return i 
						else: 
							i=erro(tokens, i, ";")
					else:
						i=erro(tokens, i, "\"")
			elif((aux[2]=='\'')): # quando estou recebendo um literal x = "a"
				i=i+1
				aux = tokens[i].split('\t')
				if(aux[3]=='4'):
					i=i+1
					aux = tokens[i].split('\t')
					if((aux[2]=='\'')):
						i=i+1
						aux = tokens[i].split('\t')
						if(aux[2]==';'):
							return i 
						else:i=erro(tokens, i, ";")
					else:i=erro(tokens, i, "\'")
			else:
				print "Você está tentando fazer uma atribuição de um token não válido, na linha", aux[0], "coluna", aux[1]
				i = erro(tokens, i, '')
		else:i=erro(tokens, i, "=")


def andamento(tokens, i):
	aux = tokens[i].split('\t')
	if(aux[3]=='1'): # o que quer dizer que é um identificador 
		i=i+1
		i = andamento_linha(tokens, i)
		return i
	else:
		print "O token na linha", aux[0], "coluna", aux[1], " deveria ser um identificador !"
		i = erro(tokens, i, '')
		return i

def andamento_linha(tokens, i): #tenho que fazer diminuir tbm 
	#i=i+1
	aux = tokens[i].split('\t')
	if(aux[2]=='='): #i=i+1
		i=i+1
		aux = tokens[i].split('\t')
		if((aux[3]=='1')or(aux[3]=='4')): # quer dizer que é um identificador 
			i=i+1
			aux = tokens[i].split('\t')
			if((aux[2]=='+')or(aux[2]=='-')):
				i=i+1
				aux = tokens[i].split('\t')
				if((aux[3]=='1')or(aux[3]=='4')):
					return i 
				else:print "O token na linha", aux[0], "coluna", aux[1], " deveria ser um identificador !"
				i = erro(tokens, i, '')
			else:i=erro(tokens, i, "+/-")
		else:print "O token na linha", aux[0], "coluna", aux[1], " deveria ser um identificador !"
		i = erro(tokens, i, '')
	elif((aux[2]=='++')or(aux[2]=='--')): #i++
		return i
	elif(aux[2]=='-'): #i--
		i=i+1
		aux = tokens[i].split('\t')
		if(aux[2]=='-'):
			return i
	elif(aux[2]=='+'): #i--
		i=i+1
		aux = tokens[i].split('\t')
		if(aux[2]=='+'):
			return i
	else:print "O token da linha ", aux[0], "coluna", aux[1], "está incorreto!"
	i = erro(tokens, i, '')

def repeticao(tokens, i):
	#faço aqui um split
	aux = tokens[i].split('\t') 
	if(aux[2]=='while'):
		i=i+1
		aux = tokens[i].split('\t') 
		if(aux[2]=='('):
			i=i+1
			i = expressao(tokens, i)
			aux = tokens[i].split('\t')
			if(aux[2]==')'):
				i=i+1
				aux = tokens[i].split('\t')
				if(aux[2]=='{'):
					i=i+1
					i=bloco(tokens, i)
					i=i+1
					aux = tokens[i].split('\t') 
					if(aux[2]=='}'):
						return i
					else:i=erro(tokens, i, "}")
				else:i=erro(tokens, i, "{")
			else:i=erro(tokens, i, ")")
		else:i=erro(tokens, i, "(")
	elif(aux[2]=='for'):
		i=i+1
		aux = tokens[i].split('\t')
		if(aux[2]=='('):
			i=i+1
			i=atribuicao(tokens, i)
			aux = tokens[i].split('\t') 
			if(aux[2]==';'):
				i=i+1
				aux = tokens[i].split('\t') 
				i=expressao(tokens, i)
				i=i+1
				aux = tokens[i].split('\t') 
				if(aux[2]==';'):
					i=i+1
					i=andamento(tokens, i)
					i=i+1
					aux = tokens[i].split('\t')
					if(aux[2]==')'):
						i=i+1
						aux = tokens[i].split('\t') 
						if(aux[2]=='{'):
							i=i+1
							i=bloco(tokens, i)
							i=i+1
							aux = tokens[i].split('\t') 
							if(aux[2]=='}'):
								return i 
							else:i=erro(tokens, i, "}")
						else:i=erro(tokens, i, "{")
					else:i=erro(tokens, i, ")")
				else:i=erro(tokens, i, ";")
			else:i=erro(tokens, i, ";")
		else:i=erro(tokens, i, ")")

#tokens = ["(","a",")", "+","(", "a", ")", "$"]
#t = 0
#t = E(tokens, t)
#if(t==len(tokens)-1):
#	print 'SUCESSO'
#else:
#	print "ERRO"

	

