# secrets gera números aleatórios seguros
import secrets
import string as s
from secrets import SystemRandom as Sr

print(''.join(Sr().choices(s.ascii_letters + s.digits + s.punctuation, k=64)))
# Ao acionar a instância Sr é posssível escolher entre as opções mencionadas
# para criar uma senha aleatória de tamanho determinado por k=N.

# s.ascii_letters mostra todas letras maiúsculas e minúsculas
# s.digits mostra todos os números
# s.punctuation mostra todas as pontuações, acentos e caracteres especiais

# python -c "import string as s;from secrets import SystemRandom as Sr;
# print(''.join(Sr().choices(
#   s.ascii_letters + s.punctuation + s.digits,k=12
# )))"

# É possível executar o mesmo comando via terminal utilizando esse script.

random = secrets.SystemRandom()

# Usando o módulo secrets com secrets.System Random() é possível
# usar a aleatoriedade, diferente do random. Fato é que seed não funciona,
# pois não é possível controlar a aleatoriedade.

# print(secrets.randbelow(100))
# print(secrets.choice([10, 11, 12]))

# Funções:
# seed
#   -> Não faz nada
random.seed(10)

# random.randrange(início, fim, passo)
#   -> Gera um número inteiro aleatório dentro de um intervalo específico
r_range = random.randrange(10, 20, 2)
# print(r_range)

# random.randint(início, fim)
#   -> Gera um número inteiro aleatório dentro de um intervalo "sem passo"
r_int = random.randint(10, 20)
# print(r_int)

# random.uniform(início, fim)
#   -> Gera um número flutuante aleatório dentro de um intervalo "sem passo"
r_uniform = random.uniform(10, 20)
# print(r_uniform)

# random.shuffle(SequenciaMutável) -> Embaralha a lista original
nomes = ['Rafael', 'Maria', 'Helena', 'Joana']
# random.shuffle(nomes)
# print(nomes)

# random.sample(Iterável, k=N)
#   -> Escolhe elementos do iterável e retorna outro iterável (não repete)
novos_nomes = random.sample(nomes, k=3)
# print(nomes)
# print(novos_nomes)

# random.choices(Iterável, k=N)
#   -> Escolhe elementos do iterável e retorna outro iterável (repete valores)
novos_nomes = random.choices(nomes, k=3)
# print(nomes)
# print(novos_nomes)

# random.choice(Iterável) -> Escolhe um elemento do iterável
# print(random.choice(nomes))
