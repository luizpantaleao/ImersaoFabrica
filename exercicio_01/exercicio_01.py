"""
    --- Exercicio 1 ---
    Crie dois arquivos Python: um deverá ser o módulo, que vai conter uma função qualquer, e o outro deve chamar essa função passando argumentos.
    - - -
    . deve ser entregue até o dia 13/09 às 14h
    . deve ser entregue pelo Git
    - - -

    Qualquer duvida pode colocar no canal de dúvidas.
"""
from modulo_01 import multiplicacao

fator1 = float(input('Digite o primeiro fator da multiplicação: '))
fator2 = float(input('Digite o segundo fator da multiplicação: '))

multiplicacao(fator1, fator2)
