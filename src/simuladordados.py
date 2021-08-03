from random import randint



class SimuladorDados:
    def __init__(self):
        self.name  = input('Qual é seu nome?\n')
        self.q_jogar = None

    def perguntar(self):
        self.q_jogar = input('{name} quer Jogar Dados? [yes] [no]: '.format(name=self.name))
        if self.q_jogar == 'yes':
            self.jogar()
            self.perguntar()
        elif self.q_jogar == 'no':
            print('Beleza, até mais!')
        else:
            print('Opção invalida digite [yes] ou [no]')
            self.perguntar()

    def jogar(self):
        print('Número: {numero}'.format(numero=randint(1,6)))


if __name__ == '__main__':
    simuladordados = SimuladorDados()
    simuladordados.perguntar()

