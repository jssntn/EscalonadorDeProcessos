import menu
import copy
from operator import itemgetter
from live_layout import generate_layout



def round_robin(processos_raw, quantum, sobrecarga):
    # verifica se tem processos na lista
    if processos_raw == 0:
        print("É necessário adicionar ao menos um processo para iniciar a simulação")
        return menu.main_menu(processos_raw, quantum, sobrecarga)
    else:
        # ordena os processos pelo tempo de chegada
        processos = sorted(processos_raw, key=itemgetter('tempo_de_chegada'))
        # cria copia da lista de processos
        processos_local = copy.deepcopy(processos)


        is_processing = True
        # define time_counter como o tempo de chegada menos -1 (processos está ordenado por tempo de chegada)
        time_counter = processos[0]['tempo_de_chegada']-1

        while is_processing:
            # parar o processo caso não redefina a variavel is_processing 
            is_processing = False

            for index, processo in enumerate(processos):
                is_ready = False
                while not is_ready:
                    is_ready = True
                    # verifica se o processo acabou
                    if processos_local[index]['tempo_de_execucao'] > 0:
                        # como o processo não acabou, coloca para "processar" e adiciona o novo tempo de inicio na lista de inicios
                        is_processing = True
                        processo['inicio'].append(time_counter)

                        # verifica se o processo vai acabar
                        if processos_local[index]['tempo_de_execucao'] <= quantum:
                            # soma o tempo de execução no tempo e acaba o processo
                            time_counter += processos_local[index]['tempo_de_execucao']
                            processos_local[index]['tempo_de_execucao'] = 0

                        # se o processo não for acabar
                        else:
                            # soma o quantum e sobrecarga no tempo e diminui o tempo de execução do processo
                            time_counter += quantum + sobrecarga
                            processos_local[index]['tempo_de_execucao'] -= quantum

                        # adiciona o novo tempo final na lista de finais
                        processo['final'].append(time_counter)

                    # ainda no while not is_ready, verifica se o proximo (fazendo a volta na lista) acabou de chegar ou não chegou ainda
                    if processos[(index + 1) % len(processos)]['tempo_de_chegada'] >= time_counter:
                        if processos_local[index]['tempo_de_execucao'] != 0:
                            #se o proximo acabou de chegar ou não chegou ainda e o atual não acabou define is_ready como false e continua processando o atual
                            is_ready = False

        # layout tá vazio
        layout = []
        # para cada processo da lista
        for index, processo in enumerate(processos_raw):
            # adiciona "vazio" para a lista de layout ter o mesmo tamanho de processos e os indices serem alcançaveis
            layout.append("")
            # para cada "inicio" de processo
            for i, inicio in enumerate(processo['inicio']):
                # verifica se é a primeira iteração
                if i == 0:
                    #adiciona no layout o tempo até o processo chegar e depois adiciona o tempo de espera (inicio - tempo de chegada + 1)
                    layout[index] += "◌" * processo['tempo_de_chegada']
                    layout[index] += "□" * (inicio - processo['tempo_de_chegada']+1)

                else:
                    # se não for a primeira, adiciona no layout o tempo de espera
                    layout[index] += "□" * (inicio - processo['final'][i - 1])

                if inicio != processo['inicio'][-1]:
                    # se não for a ultima iteração, coloca no layout a execução (final - inicio - sobrecarga) e a sobrecarga
                    layout[index] += "■" * (processo['final'][i] - inicio - sobrecarga)
                    layout[index] += "◪" * sobrecarga
                else:
                    # se for a ultima iteração, coloca no layout só a execução
                    layout[index] += "■" * (processo['final'][i] - inicio)
                    ''' 
                    print("■" * (processo['final'][i] - inicio), end='') 
                    '''

            # define a lista de inicios e finais como vazio para não rodar de novo
            processo['inicio'] = []
            processo['final'] = []

        generate_layout([], layout, time_counter)
        return menu.main_menu(processos_raw, quantum, sobrecarga)












