from time import sleep
from threading import Thread


def vai_demorar(texto, tempo):
    sleep(tempo)
    print(texto)


t1 = Thread(target=vai_demorar, args=('Olá mundo 1!', 10))
t1.start()
t1.join()
# Usar join() para esperar a thread principal terminar antes que o restante
# seja executado.

# Enquanto a thread estiver viva o laço não termina.
# while t1.is_alive():
#     print('Esperando a thread.')
#     sleep(2)

print('Thread acabou!')

# def vai_demorar(texto, tempo):
#     sleep(tempo)
#     print(texto)


# t1 = Thread(target=vai_demorar, args=('Olá mundo 1!', 5))
# t1.start()

# t2 = Thread(target=vai_demorar, args=('Olá mundo 2!', 1))
# t2.start()

# t3 = Thread(target=vai_demorar, args=('Olá mundo 3!', 2))
# t3.start()

# for i in range(10):
#     print(i)
#     sleep(.5)
