"""Olá, essa é minha atividade do dia 20/08 do curso de introdução a programação. 
Esse programa faz algumas perguntas básicas sobre quem está acessando ele, é um programa simples e funcional!"""
nome = str(input('Olá, qual o seu nome?'))
idade = int(input('Qual a sua idade?'))
altura = float(input('Qual a sua altura? (em metros, ex: 1.80)'))
sorte = int(input('Qual o seu número da sorte?'))
#resposta para duas perguntas que foram feitas anteriormente.
print (' Olá {}, que bom que está testando esse programa, vi que você tem o número {} como número da sorte, que legal!'.format(nome, sorte))
print (type(nome))
print (type(idade))
print (type(altura))
print (type(sorte))