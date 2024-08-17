import menu
import copy
from operator import itemgetter
from live_layout import generate_layout


def sjf(processos_raw, quantum, sobrecarga):
    # verifica se tem processos na lista
    if processos_raw == 0:
        print("É necessário adicionar ao menos um processo para iniciar a simulação")
        return menu.main_menu(processos_raw, quantum, sobrecarga)
    else:
        # ordena os processos pelo tempo de chegada e pelo tempo de execucao
        processos = sorted(processos_raw, key=itemgetter('tempo_de_chegada','tempo_de_execucao'))
        # cria copia independente da lista de processos
        processos_local = copy.deepcopy(processos)

        numero_de_processos_processados = 0
        # define time_counter como o tempo de chegada (processos está ordenado por tempo de chegada)
        time_counter = processos[0]['tempo_de_chegada']

        # enquanto não processar todos os procesos, continua
        while numero_de_processos_processados < len(processos):
            
            processo_escolhido = None

            # se não for o primeiro (pois sabemos que o primeiro está na ordem certa), verificamos
            if numero_de_processos_processados != 0:
                # cria lista de processos disponiveis
                processos_disponiveis = []

                for index, processo in enumerate(processos):
                    # verifica se o processo já chegou e não foi executado ainda
                    if processo['tempo_de_chegada'] <= time_counter and processos_local[index]['tempo_de_execucao'] != 0:
                        processos_disponiveis.append(processo)

                if processos_disponiveis:
                    # se tiver processos disponiveis, ordena os processos disponiveis por tempo de execução e pega o primeiro
                    processos_disponiveis.sort(key=itemgetter('tempo_de_execucao'))
                    processo_escolhido = processos_disponiveis[0]
            else:
                processo_escolhido = processos[0]

            if processo_escolhido != None:
                # se algum processo estiver sido escolhido, pega o index desse processo na lista de processos  
                processo_escolhido_index = processos.index(processo_escolhido)
            
                # coloca para "processar" e adiciona o  tempo de inicio na lista de inicios
                numero_de_processos_processados += 1
                processos[processo_escolhido_index]['inicio'].append(time_counter)
            
                # soma o tempo de execução com o tempo atual e zera o tempo de execução
                time_counter += processos_local[processo_escolhido_index]['tempo_de_execucao']
                processos_local[processo_escolhido_index]['tempo_de_execucao'] = 0

                # adiciona o tempo final na lista de finais
                processos[processo_escolhido_index]['final'].append(time_counter)
            else:
                # se nenhum processo tiver sido escolhido, quer dizer que não chegou processo, então o tempo pula para o proximo tempo de chegada (pois a lista está ordenada)
                time_counter = processos[numero_de_processos_processados]['tempo_de_chegada']

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
                    layout[index] += "□" * (inicio - processo['tempo_de_chegada'])

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

