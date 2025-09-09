from exercicio02 import status

alunos = [5, 8.5, 6, 6.2, 2]
for nota_aluno in alunos:
    resultado = status(nota_aluno)
    print (f"{nota_aluno} --> {resultado}")