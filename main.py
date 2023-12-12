import sympy as sp

def calcular_derivada():
    variavel = sp.symbols('x')

    # Solicita ao usuário inserir a expressão da função
    expressao = input("Insira a expressão da função em termos de 'x': ")

    try:
        # Utiliza a função exp do SymPy para representar a constante de Euler
        funcao = sp.sympify(expressao, locals={'exp': sp.exp, 'Pow': sp.Pow})

        # Calcula a derivada em relação a 'x'
        derivada_calculada = sp.diff(funcao, variavel)

        # Exibe a expressão original e a derivada
        print("Expressão original:", funcao)
        print("Derivada:", derivada_calculada)

    except sp.SympifyError:
        print("Erro ao calcular a derivada. Certifique-se de fornecer uma expressão válida.")

if __name__ == "__main__":
    calcular_derivada()

