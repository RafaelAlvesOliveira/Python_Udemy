# Abstração: consiste em esconder detalhes da implementação e
# expor apenas o que é essencial, ajudando a reduzir a complexidade
# do código e deixa os programas mais organizados.
# Log
# Herança: permite que uma classe (subclasse ou classe filha) herde
# atributos e métodos de outra classe (superclasse ou classe pai)
from pathlib import Path

LOG_FILE = Path(__file__).parent / 'log.txt'


class Log:
    def _log(self, msg):
        raise NotImplementedError('Implemente o método log')

    def log_error(self, msg):
        return self._log(f'Error: {msg}')

    def log_success(self, msg):
        return self._log(f'Success: {msg}')


# O termo Mixin usado nessa classe é para orientar outros 
# desenvolvedores de que essa classe serve para adicionar
# outras funcionalidades usando herança múltipla
class LogFileMixin(Log):
    def _log(self, msg):
        msg_formatada = f'{msg} ({self.__class__.__name__})'
        print('Salvando no log: ', msg_formatada)
        with open(LOG_FILE, 'a', encoding='utf-8') as arquivo:
            arquivo.write(msg_formatada)
            arquivo.write('\n')
            # arquivo.write('\r\n')


class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')


# Se o arquivo que estiver sendo executado for o main.py
# então ele vai executar o código de log.py sem erros.
if __name__ == '__main__':
    lp = LogPrintMixin()
    lp.log_error('qualquer coisa')
    lp.log_success('Que legal')
    lf = LogFileMixin()
    lf.log_error('qualquer coisa')
    lf.log_success('Que legal')
    # print(LOG_FILE)
