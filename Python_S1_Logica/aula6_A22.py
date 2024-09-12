# conversão de tipos, coerção
# type convertion, typecasting, coercion
# é o ato de converter um tipo em outro
# tipos imutáveis e primitivos
# str, int, float, bool
print(1 + 1)
# print('1' + 1) TypeError: Não é possível concatenar uma string com um inteiro
print('1', type('1'))  # Informa o tipo do dado
print(int('1'), type(int('1')))
print(int('1') + 1)  # Foi feita a coerção da string '1' para o número 1
print(float('1') + 1)
print(type(float('1') + 1))
print(bool(' '))
print(str('11') + 'b')  # O valor númerico foi convertido para string, e
# foi concatenado com a letra 'b'.
print('a' + 'b')
