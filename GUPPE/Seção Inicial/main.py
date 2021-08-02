"""Os atributos e metodos com dois __ underlines são chamados de Dunder
   eles são assim para evitar que os programas tenham incompatibilidades de nome
   são atributos e metodos internos

   1- Caso o arquivo seja executado diretamente, o atributo __name__ será chamado de __main__
   2- Se o arquivo for importado por outro arquivo o atributo __name__ será o mesmo nome do arquivo
"""

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Ao executar o arquivo no prompt automaticamente o atributo __name__ recebe o valor __main__.
# Esse if só executa se o arquivo estiver sendo executado e não executa se ele for importado
# como parte de outro arquivo .py
if __name__ == '__main__':
    print_hi('O main.py está sendo executado diretamente')
else:
    print("Esse modulo foi importado!")

