'''Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu
aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.'''

expr = str(input('Digite a expressão: '))
if expr.count('(') == expr.count(')'):
    print('Sua expressão é válida!!')
else:
    print('Sua expressão não é válida')
