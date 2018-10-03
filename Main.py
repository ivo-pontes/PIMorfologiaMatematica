#!/usr/bin/env python3
# -*- coding: utf-8 -*

from Morfologia import Morfologia

if __name__ == '__main__':
	print("Processamento de Imagens.")

	op = -1

	while op != 0:
		menuStr = "\n-------Menu-------\nMorfologia Matemática:\n1 - Abertura\n2 - Fechamento\n3 - Extrair Contorno\n"

		op = input(menuStr)
		op = int(op)

		morfologia = Morfologia("img/elefante.png")
		morfologia.carregarImagem()

		if op == 0:
			pass
		elif op == 1:
			abertura = morfologia.abertura()
		elif op == 2:
			fechamento = morfologia.fechamento()
		elif op == 3:
			x = morfologia.extrairContorno()


	print("Fim execução!!")
