#!/usr/bin/env python3
# -*- coding: utf-8 -*

from PIL import Image, ImageShow
import numpy as np

class Morfologia():

	def __init__(self, nome_imagem):
		self.nome_imagem = nome_imagem
		self.m = 0
		self.n = 0
		self.matriz = []
		self.img = []

	'''
	Abrindo o arquivo e pegando dimensões MxN
	'''
	def carregarImagem(self):
		img = Image.open(self.nome_imagem)
		self.img = img
		#Converte Imagem Object para Matriz
		self.matriz = np.asarray(img.convert('L'))
		#Dimensão M
		self.m = np.size(self.matriz, 0)
		#Dimensão N
		self.n = np.size(self.matriz, 1)
		print("Linhas: {}\nColunas: {}\n".format(self.m, self.n))
		print(self.matriz)


	'''
	Método de Erosão
	'''
	def erosao(self, matriz):
		m = np.zeros([self.m,self.n])
		m1 = np.size(m, 0)
		n1 = np.size(m, 1)
		print("Linhas: {}\nColunas: {}\n".format(m1,n1))

		#B&W
		#Ternário em Python
		m1 = self.m if self.m%2==0 else self.m-1
		n1 = self.n if self.n%2==0 else self.n-1

		binaria = self.binarizar(matriz)

		print("Matriz B&W:")
		#print(m)
		#x = Image.fromarray(m)
		#x.show()

		mascara =[[0, 0, 0],
				[0, 0, 0],
				[0, 0, 0]]

		for i in range(m1):
			for j in range(n1):
				if i != 0 and j != 0 and i != (m1-1) and j != (n1-1):
					if (binaria[i-1][j-1] == mascara[0][0] and binaria[i-1][j] == mascara[0][1] and binaria[i-1][j+1] == mascara[0][2]
						 and binaria[i][j-1] == mascara[1][0] and binaria[i][j] == mascara[1][1] and binaria[i][j+1] == mascara[1][2]
						 and binaria[i][j-1] == mascara[2][0] and binaria[i+1][j] == mascara[2][1] and binaria[i+1][j+1] == mascara[2][2]):
							m[i][j] = 0
					else:
						m[i][j] = 255
					

		#xy = Image.fromarray(m)
		#xy.show()
		return m	

	def dilatacao2(self,matriz):
		m = np.zeros([self.m,self.n])
		m1 = np.size(m, 0)
		n1 = np.size(m, 1)
		print("Linhas: {}\nColunas: {}\n".format(m1,n1))

		#B&W
		#Ternário em Python
		m1 = self.m if self.m%2==0 else self.m-1
		n1 = self.n if self.n%2==0 else self.n-1

		binaria = self.binarizar(matriz)

		print("Matriz B&W:")
		#print(m)
		#x = Image.fromarray(m)
		#x.show()

		mascara =[[0, 0, 0],
				[0, 0, 0],
				[0, 0, 0]]


		for i in range(m1):
			for j in range(n1):
				if i != 0 and j != 0 and i != (m1-1) and j != (n1-1):
					if (binaria[i-1][j-1] == mascara[0][0] or binaria[i-1][j] == mascara[0][1] or binaria[i-1][j+1] == mascara[0][2]
						 or binaria[i][j-1] == mascara[1][0] or binaria[i][j] == mascara[1][1] or binaria[i][j+1] == mascara[1][2]
						 or binaria[i][j-1] == mascara[2][0] or binaria[i+1][j] == mascara[2][1] or binaria[i+1][j+1] == mascara[2][2]):
						m[i-1][j-1]= 0
						m[i-1][j]= 0
						m[i-1][j+1]= 0
						m[i][j-1]= 0
						m[i][j]= 0
						m[i][j+1] = 0
						m[i+1][j-1]=0
						m[i+1][j]=0
						m[i+1][j+1]=0


					else:
						m[i][j] = 255

		#xy = Image.fromarray(m)
		#xy.show()
		return m		


	'''
	Dilatacion
	'''		
	def dilatacao(self, matriz):
		m = np.zeros([self.m,self.n])
		m1 = np.size(m, 0)
		n1 = np.size(m, 1)
		print("Linhas: {}\nColunas: {}\n".format(m1,n1))

		#B&W
		#Ternário em Python
		m1 = self.m if self.m%2==0 else self.m-1
		n1 = self.n if self.n%2==0 else self.n-1

		binaria = self.binarizar(matriz)

		print("Matriz B&W:")
		#print(m)
		#x = Image.fromarray(m)
		#x.show()

		mascara =[[0, 0, 0],
				[0, 0, 0],
				[0, 0, 0]]


		for i in range(m1):
			for j in range(n1):
				if i != 0 and j != 0 and i != (m1-1) and j != (n1-1):
					if (binaria[i-1][j-1] == mascara[0][0] or binaria[i-1][j] == mascara[0][1] or binaria[i-1][j+1] == mascara[0][2]
						 or binaria[i][j-1] == mascara[1][0] or binaria[i][j] == mascara[1][1] or binaria[i][j+1] == mascara[1][2]
						 or binaria[i][j-1] == mascara[2][0] or binaria[i+1][j] == mascara[2][1] or binaria[i+1][j+1] == mascara[2][2]):
							m[i][j] = 0
					else:
						m[i][j] = 255

		#xy = Image.fromarray(m)
		#xy.show()
		return m		


	def binarizar(self, matriz):
		m = np.zeros([self.m,self.n])
		m1 = np.size(m, 0)
		n1 = np.size(m, 1)
		print("Linhas: {}\nColunas: {}\n".format(m1,n1))

		#B&W
		#Ternário em Python
		m1 = self.m if self.m%2==0 else self.m-1
		n1 = self.n if self.n%2==0 else self.n-1

		for i in range(m1):
			for j in range(n1):
				if matriz[i][j] < 127:
					m[i][j] = 0
				else:
					m[i][j] = 255

		return m


	def abertura(self):
		abertura = self.erosao(self.matriz)
		abertura = self.dilatacao2(abertura)

		print(abertura)
		imagem = Image.fromarray(abertura)		
		#self.img.show()
		imagem.show()


	def fechamento(self):
		fechamento = self.dilatacao2(self.matriz)
		fechamento = self.erosao(fechamento)
		
		print(fechamento)
		imagem = Image.fromarray(fechamento)		
		#self.img.show(title="Original")
		imagem.show()
	
	def extrairContorno(self):
		erosao = self.erosao(self.matriz)

		m1 = self.m if self.m%2==0 else self.m-1
		n1 = self.n if self.n%2==0 else self.n-1

		extracao = np.zeros([self.m,self.n])

		for i in range(m1):
			for j in range(n1):
				extracao[i][j] = int(erosao[i][j] - self.matriz[i][j])
										
		imagem = Image.fromarray(extracao)		
		self.img.show()
		imagem.show()
		