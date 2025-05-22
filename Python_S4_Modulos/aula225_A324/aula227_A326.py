from time import sleep
from threading import Thread
from threading import Lock


class Ingressos:
    def __init__(self, estoque: int):
        self.estoque = estoque
        self.lock = Lock()

    def comprar(self, quantidade: int):
        with self.lock:  # Usando context manager para garantir release do lock
            if self.estoque < quantidade:
                print(f'Não temos ingressos suficientes para {quantidade}.')
                return

            sleep(1)  # Simula processamento

            self.estoque -= quantidade
            print(f'Você comprou {quantidade} ingresso(s). '
                  f'Ainda temos {self.estoque} em estoque.')


if __name__ == '__main__':
    ingressos = Ingressos(10)
    threads = []

    for i in range(1, 20):
        t = Thread(target=ingressos.comprar, args=(i,))
        t.start()
        threads.append(t)

    # Espera todas as threads terminarem
    for t in threads:
        t.join()

    print(f'Estoque final: {ingressos.estoque}')

    # ingressos.comprar(1)
    # ingressos.comprar(1)
    # ingressos.comprar(1)
    # ingressos.comprar(1)
