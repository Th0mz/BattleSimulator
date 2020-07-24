# Tomas de Araujo Tavares          Numero: 95680

# ----------------------- : Posicao : ----------------------- #
# Construtores: 
def cria_posicao(x, y):
    """- Construtor:
           A funcao recebe dois argumentos (x, y) que correspondem as 
         coordenadas x e y de uma posicao e devolve essa mesma posicao
         
         - Esta funcao levata um erro se algum dos argumentos for invalido"""
    # Verificar se os argumentos sao validos
    if type(x) is int and type(y) is int and \
       x >= 0 and y >= 0:
        # Guardar a posicao como um dicionario com 2 chaves 
        # "x" e "y" que cada um correspode a uma coordenada    
        return {"x": x, 
                "y": y}    
    else:
        raise ValueError("cria_posicao: argumentos invalidos") 

    
def cria_copia_posicao(posicao):
    """- Construtor:
           A funcao recebe um argumento posicao que corresponde a uma posicao
                     e devolve uma copia dessa posicao
                     
            - Esta funcao levata um erro se algum dos argumentos for invalido"""
    
    return cria_posicao(posicao["x"], posicao["y"])
    

# Seletores:
def obter_pos_x(posicao):
    """- Seletor:
             A funcao recebe como argumento uma posicao e devolve a sua
                                componente x"""

    return posicao["x"]

def obter_pos_y(posicao):
    """- Seletor:
             A funcao recebe como argumento uma posicao e devolve a sua
                                componente y"""

    return posicao["y"]


    
# Reconhecedores
def eh_posicao(posicao):
    """- Reconhecedor:
            E uma funcao que recebe um argumento e verifica se esse argumento
            e ou nao uma posicao valida devolvento:
                  True: se o argumento for uma posicao valida
                  False: se o argumento for uma posicao invalida"""


    # Verifica se e igual a representacao interna 
    # verifica tambem se os valores de x e y existem e sao inteiros nao negativos
    if type(posicao) is dict and len(posicao) == 2 and \
        "x" in posicao and "y" in posicao:
            posicao_x, posicao_y = obter_pos_x(posicao), obter_pos_y(posicao)
            
            # Verifica as se as caracteristicas da posicao sao validas (x e y)
            return type(posicao_x) is int and type(posicao_y) is int and \
                   posicao_x >= 0 or posicao_y >= 0
    else:
        return False
    
    

# Testes
def posicoes_iguais(posicao1, posicao2):
    """- Teste: 
            E uma funcao que recebe como argumento duas posicoes e compara-as
            e devolve (posicao1["x"] = x1 posicao2["x"] = x2 ...):
                    True: se as posicoes forem iguais (x1 == x2 e y1 == y2)
                    False: se as posicoes forem diferentes (x1 != x2 ou y1 != y2)"""

    # Verificar se a cordenada x de cada um e igual e o mesmo para a coordenada y
    return obter_pos_x(posicao1) == obter_pos_x(posicao2) and \
           obter_pos_y(posicao1) == obter_pos_y(posicao2)
    
    

# Transformadores
def posicao_para_str(posicao):
    """- Transformador: 
             A funcao recebe como argumento uma posicao e devolve uma 
              cadeia de caracteres com a posicao na forma "(x, y)" 
                    onde x e y sao as coordenadas da posicao"""

    return str( (obter_pos_x(posicao), obter_pos_y(posicao)) )



# Funcoes de Alto Nivel
def obter_posicoes_adjacentes(posicao):
    """ Recebe uma posicao como argumento e devolve um tuplo com 
     todas as posicoes adjecentes a essa posicao por ordem de leitura"""

    x = obter_pos_x(posicao)
    y = obter_pos_y(posicao)
    posicoes_adjacentes = ()
    formula = ((0, -1), (-1, 0), (1, 0), (0, 1))
    for tuplo in formula:
        # Verifixcar se as posicoes adjecentes nao tem coordenadas 
        # negativas para que nao de erro ao criar_posicao
        if x + tuplo[0] >= 0 and y + tuplo[1] >= 0:
            posicoes_adjacentes += (cria_posicao(x + tuplo[0], y + tuplo[1]), )
    return posicoes_adjacentes


# ----------------------- : Unidade : ----------------------- #
# Construtores
def cria_unidade(posicao, vida, forca, exercito):
    """- Construtor:
            Recebe quatro argumentos que correspondem:
                - Posicao: a posicao que a unidade ocupa no labirinto   [tipo int nao negativa]
                - Vida: corresponde aos pontos de vida da unidade (se for 0 unidade morre)   [tipo int nao negativa]
                - Forca: corresponde ao poder do exercito (dano que dao a unidades de outros exercitos)   [tipo int nao negativa]
                - Exercito: identifica a que exercito pertence essa unidade   [tipo str nao vazia]
                
            - Esta funcao levata um erro se algum dos argumentos for invalido"""

    # Verificar validade dos argumentos
    if eh_posicao(posicao) and \
       type(vida) is int and type(forca) is int and \
       type(exercito) is str and \
       vida > 0 and forca > 0 and exercito != "":
            # Representacao interna, dicionario com 4 chaves
            # "posicao", "vida", "forca" e "exercito" 
            return {"posicao": posicao,
                    "vida": vida,
                    "forca": forca,
                    "exercito": exercito}
    else:
        raise ValueError("cria_unidade: argumentos invalidos")
    



def cria_copia_unidade(unidade):
    """- Construtor:
            Recebe como argumento uma unidade e faz uma copia de dessa unidade"""

    posicao = cria_copia_posicao(unidade["posicao"])
    return cria_unidade(posicao, unidade["vida"], unidade["forca"], unidade["exercito"])




# Seletores
def obter_posicao(unidade):
    """- Seletores:
            A funcao recebe como argumento uma unidade e devolve a sua posicao"""

    return unidade["posicao"]

def obter_exercito(unidade):
    """- Seletores:
            A funcao recebe como argumento uma unidade e devolve o exercito a que 
                                        pertence"""
    return unidade["exercito"]

def obter_forca(unidade):
    """- Seletores:
            A funcao recebe como argumento uma unidade e devolve a forca do exercito"""

    return unidade["forca"]

def obter_vida(unidade):
    """- Seletores:
            A funcao recebe como argumento uma unidade e devolve a vida do exercito"""

    return unidade["vida"]



# Modificadores
def muda_posicao(unidade, posicao):
    """- Modificador:
            Recebe como argumento uma unidade e uma posicao e altera a posicao da unidade
        para a posicao passada como argumento devolvento a unidade com a posicao atualizada
                                    de forma destrutiva"""
    
    unidade["posicao"] = posicao
    return unidade


def remove_vida(unidade, forca):
    """- Modificador:
            Recebe como argumento uma unidade uma quantidade de vida e devolve a unidade
                com a a sua vida diminuida pelo valor passado como argumento vida"""

    # Remover a vida atual a forca passada como argumento de forma destrutiva
    unidade["vida"] = obter_vida(unidade) - forca
    return unidade


# Reconhecedores
def eh_unidade(unidade):
    """- Reconhecedor:
            E uma funcao que recebe um argumento e verifica se esse argumento
            e ou nao uma unidade valida devolvento:
                  True: se o argumento for uma unidade valida
                  False: se o argumento for uma unidade invalida"""

    # Verificar representacao interna
    if type(unidade) is dict and \
       len(unidade) == 4 and \
       "posicao" in unidade and "vida" in unidade and \
       "forca" in unidade and "exercito" in unidade:
            vida = obter_vida(unidade)
            exercito = obter_exercito(unidade)
            forca = obter_forca(unidade)
            posicao = obter_posicao(unidade)
            
            # Verificar se respeita as caracteristicas da unidade (posicao, vida , forca e exercito)
            return type(vida) and type(forca) is int and \
                   type(exercito) is str and vida > 0 and \
                   forca > 0 and exercito != "" and eh_posicao(posicao)
    else:
        return False

 

# Testes
def unidades_iguais(unidade1, unidade2):
    """- Teste:
            Recebe como argumentos duas unidades e testa se elas sao
            iguais, devolvendo:
                    True: Se unidade1 for igual a unidade2
                    False: Se unidade2 nao for igual a unidade2"""
    
    # Verificar se posicao, vida , forca e exercito de cada unidade sao iguais so 
    #           assim as unidades sao consideradas iguais
    return obter_posicao(unidade1) == obter_posicao(unidade2) and \
           obter_vida(unidade1) == obter_vida(unidade2) and \
           obter_forca(unidade1) == obter_forca(unidade2) and \
           obter_exercito(unidade1) == obter_exercito(unidade2)

# Transformadores
def unidade_para_char(unidade):
    """- Transformador:
            Recebe como argumento uma unidade e devolve a inicial do nome
                         do seu exercito em maiuscula"""
    
    exercito = obter_exercito(unidade)
    # Obter o primeiro caracter do nome do exercito e por em maiuscula se ainda nao estiver
    inicial = exercito[0].upper()
    return inicial

def unidade_para_str(unidade):
    """- Transformador:
            Recebe como argumento uma unidade e devolve uma string que esta
              na forma PrimeiroCaracterExercito[Vida, Ataque]@[Posicao]"""
    
    vida = obter_vida(unidade)
    ataque = obter_forca(unidade)
    vida_ataque = str([vida, ataque])
    posicao = posicao_para_str(obter_posicao(unidade))

    return unidade_para_char(unidade) + vida_ataque + "@" + posicao

# Funcoes de alto nivel
def unidade_ataca(unidade, unidade_atacada):
    """ Esta funcao faz com que a unidade ataque a unidade_atacada, ou seja
        e removida a vida da unidade_atacada a forca da unidade, recebendo
               estas duas unidades nos pelos argumentos da funcao"""


    remove_vida(unidade_atacada, obter_forca(unidade))
    return obter_vida(unidade_atacada) <= 0


def ordenar_unidades(unidades):
    """ Recebe como argumento um tuplo com unidades e retorna um tuplo com
                 as mesmas unidades so que ordenadas de acordo a 
                         ordem de leitura do mapa"""
    
    return tuple(sorted(list(unidades), key = lambda unidade: [obter_pos_y(obter_posicao(unidade)), obter_pos_x(obter_posicao(unidade))]))

# ----------------------- : Mapa : ----------------------- #
# Construtores
def cria_mapa(tamanho, paredes, exercito1, exercito2):
    """- Construtor:
            Esta funcao recebe 4 argumentos:
                - tamanho: e um tuplo com dois valores inteiros positivos que representa
                    as dimencoes do mapa onde a primeira coordenada(tamanho[0]) e a largura
                    do mapa e a segunda coordenada(tamanho[1]) e a altura do mapa
                - Paredes: e um tuplo com zero ou mais elementos que correspondem a posicoes
                    dentro dos limites do mapa e correspondem a paredes dentro do mapa
                - Exercitos: correspondem a tuplos com pelo menos 1 elemento que corresponde
                    a uma unidade valida
                    
                - Esta funcao levata um erro se algum dos argumentos for invalido"""

    # Testar se todos os argumentos sao tuplos
    if type(tamanho) is not tuple or type(paredes) is not tuple or \
       type(exercito1) is not tuple or type(exercito2) is not tuple:
            raise ValueError("cria_mapa: argumentos invalidos")

    # Testar se o argumento tamanho e valido
    if len(tamanho) > 2 or type(tamanho[0]) is not int or \
    type(tamanho[1]) is not int or tamanho[0] < 3 or tamanho[1] < 3:
        raise ValueError("cria_mapa: argumentos invalidos")

    largura, altura = tamanho[0], tamanho[1]
    
    # Testar se o cada parede e uma parede valida
    for parede in paredes:
        if not eh_posicao(parede) or 0 in [obter_pos_x(parede), obter_pos_y(parede)] or \
           obter_pos_x(parede) >= largura - 1 or obter_pos_y(parede) >= altura - 1:
            raise ValueError("cria_mapa: argumentos invalidos")

    # Testar se o argumento exercito1 e exercito2 e agrumento valido
    if len(exercito1) < 1 or len(exercito2) < 1:
        raise ValueError("cria_mapa: argumentos invalidos")
    
    # Verificar se cada unidade do exercito e uma unidade ou nao para cada exercito
    for unidade in exercito1:
        if not eh_unidade(unidade):
            raise ValueError("cria_mapa: argumentos invalidos")
    
    for unidade in exercito2:
        if not eh_unidade(unidade):
            raise ValueError("cria_mapa: argumentos invalidos")

    else:
        return {"tamanho": tamanho,
                "paredes": paredes,
                "exercito1": exercito1,
                "exercito2": exercito2}

def cria_copia_mapa(mapa):
    """- Construtor:
        A funcao recebe um argumento mapa que corresponde a um mapa
                 e devolve uma copia desse mapa
                     
        - Esta funcao levata um erro se algum dos argumentos for invalido"""

    tamanho = mapa["tamanho"]
    paredes = mapa["paredes"]
        
    exercito1 = ()
    # Fazer uma copia de todas as unidades do exercito1
    for unidade in mapa["exercito1"]:
        exercito1 += (cria_copia_unidade(unidade), )

    exercito2 = ()
    # Fazer uma copia de todas as unidades do exercito2
    for unidade in mapa["exercito2"]:
        exercito2 += (cria_copia_unidade(unidade), )
        
    return cria_mapa(tamanho, paredes, exercito1, exercito2)

# Seletores
def obter_tamanho(mapa):
    """ - Seletor: 
            Recebe como argumento um mapa e devolve o tamanho do
                            mapa em um tuplo"""

    return mapa["tamanho"]

def obter_nome_exercitos(mapa):
    """ - Seletor: 
            Recebe como argumento um mapa e devolve um tuplo com duas cadeias de 
                    caracteres correspondentes ao nome dos exercitos"""

    nome_exercito1 = obter_exercito(mapa["exercito1"][0])
    nome_exercito2 = obter_exercito(mapa["exercito2"][0])    

    return tuple(sorted([nome_exercito1, nome_exercito2]))

def obter_unidades_exercito(mapa, exercito):
    """ - Seletor:
            Recebe como argumentos um mapa e um o nome de um exercito
        e devolve um tuplo com todas as unidades com esse nome de exercito"""

    unidades = obter_todas_unidades(mapa)
    unidades_exercito = ()
    # Veirificar para todas as unidades do mapa se pertencem ao exercito
    for unidade in unidades:
        exercito_unidade = obter_exercito(unidade)
        if exercito_unidade == exercito:
            unidades_exercito += (unidade, )

    return unidades_exercito
    
def obter_todas_unidades(mapa):
    """ - Seletor:
            Recebe como argumento um mapa e devolve um tuplo com
                   todas as unidades que estao no mapa"""
        
    return ordenar_unidades(mapa["exercito1"] + mapa["exercito2"]) 

def obter_unidade(mapa, posicao):
    """ - Seletor:
            Recebe como argumento um mapa e uma posicao e devolve a
           unidade que se encontra na posicao passada como argumento"""

    todas_unidades = obter_todas_unidades(mapa)
    # Ver se alguma posicao do mapa tema mesma posicao passada como argumento
    for unidade in todas_unidades:
        if posicoes_iguais(posicao, unidade["posicao"]):
            return unidade
    return None

# Modificadores
def eliminar_unidade(mapa, unidade):
    """ - Modificador:
            Recebe como argumentos um mapa e uma unidade e devolve
                 o mapa sem a unidade passada como argumento"""
    
    # Verificar a que exercito pertence a unidade e remove-la desse exercito
    if unidade in mapa["exercito1"]:
        mapa["exercito1"] = list(mapa["exercito1"])
        mapa["exercito1"].remove(unidade)
        mapa["exercito1"] = tuple(mapa["exercito1"]) 
    elif unidade in mapa["exercito2"]:
        mapa["exercito2"] = list(mapa["exercito2"])
        mapa["exercito2"].remove(unidade)
        mapa["exercito2"] = tuple(mapa["exercito2"])
    
    return mapa

def mover_unidade(mapa, unidade, posicao):
    """ - Modificador: 
            Recebe como argumentos um mapa uma unidade e uma posicao e retorna
                    o mapa com a posicao da unidade atualizada"""
        
    todas_unidades = obter_todas_unidades(mapa)
    for unidade_ in todas_unidades:
        if unidades_iguais(unidade, unidade_):
            muda_posicao(unidade_, posicao)
            return mapa


# Reconhecedores
def eh_posicao_unidade(mapa, posicao):
    """ - Reconhecedor:
            Recebe como argumentos um mapa e uma posicao e devolve:
                - True: se essa posicao for ocupada por uma unidade
                - False: se essa posicao nao for ocupada por uma unidade"""

    # Ir buscar a unidade que esta nessa posicao se nao exitir funcao obter_unidade
    # retorna None
    unidade = obter_unidade(mapa, posicao)
    return unidade != None

def eh_posicao_corredor(mapa, posicao):
    """ - Reconhecedor: 
            Recebe como argumentos o uma e uma posicao e verifica se essa posicao 
                corresponde a um corredor(nao e ocupado por uma parede)"""
    
    # Testar se a posicao esta dentro do mapa
    tamanho = obter_tamanho(mapa)
    if obter_pos_x(posicao) >= tamanho[0]  or obter_pos_y(posicao) >= tamanho[1]:
        return False
    else:
        # Verificar se nao e uma parede que ja testa se a posicao e posicao valida ou seja coordendas maior que zero
        return not eh_posicao_parede(mapa, posicao) 


def eh_posicao_parede(mapa, posicao):
    """ - Reconhecedor: 
            Recebe como argumentos o uma e uma posicao e verifica se essa posicao 
                            corresponde a uma parede"""
    
    tamanho_mapa = obter_tamanho(mapa)
    num_colunas, num_linhas = tamanho_mapa[0],  tamanho_mapa[1] 
    posicao_x, posicao_y = obter_pos_x(posicao), obter_pos_y(posicao) 

    # Verificar se a posicao se encontra nas paredes que limitam o mapa
    posicao_na_fornteira = 0 in [posicao_x, posicao_y] or posicao_x == num_colunas - 1 or posicao_y == num_linhas - 1
    return (posicao_na_fornteira or posicao in mapa["paredes"]) and eh_posicao(posicao)

# Testes
def mapas_iguais(mapa1, mapa2):
    """ - Teste: 
            Recebe como argumento dois mapas e verifica se eles sao iguais e devolve:
                - True: Se os mapas forem iguais
                - False: Se os mapas forem diferentes"""

    # Verificar se cada caracteristica do mapa1 e igal a mesma caracteristica do mapa2
    # onde as caracteristicas sao o tamanho dos mapas a posicao das paredes e as unidades de cada exercito
    return mapa1["tamanho"] == mapa2["tamanho"] and \
           mapa1["paredes"] == mapa2["paredes"] and \
           mapa1["exercito1"] == mapa2["exercito1"] and \
           mapa1["exercito2"] == mapa2["exercito2"]

# Transformadores

def mapa_para_str(mapa):
    """ - Transformador: 
            Recebe como argumento um mapa e devolve uma string que representa esse mapa
                que representa graficamente o mapa onde pode ter estes elementos:

                - # - Representa uma parede
                - . - Representa um corredor sem unidade
                - "unidade_para_char(unidade)" - que representa uma unidade de um certo exercito """

    linhas_extermidades = ""
    mapa_string = ""
    
    tamanho_mapa = obter_tamanho(mapa)
    num_colunas, num_linhas = tamanho_mapa[0],  tamanho_mapa[1]
    # Inicializar linhas_extermidades que repesentam a primira e a ultima linhas
    for x in range(num_colunas):
        linhas_extermidades += "#"
    
    # Adicionar a primeira linha ao mapa final
    mapa_string += linhas_extermidades + "\n"
    # Inicializar o resto do mapa tendo em conta paredes e unidades
    for y in range(1, num_linhas - 1):
        linha = "#"
        for x in range(1, num_colunas - 1):
            posicao = cria_posicao(x, y)
            if eh_posicao_parede(mapa, posicao):
                # Adicionar uma parede
                linha += "#"
            elif eh_posicao_unidade(mapa, posicao):
                # Adicionar a inicial em maisculo do exercito da unidade
                unidade = obter_unidade(mapa, posicao)
                linha += unidade_para_char(unidade)
            else:
                # Adicionar um corredor
                linha += "."

        mapa_string += (linha + "#\n")
    return mapa_string + linhas_extermidades

# Funcoes alto nivel
def obter_inimigos_adjacentes(mapa, unidade):
    """ Recebe como argumentos o mapa e uma unidade do mapa e devolve um tuplo com todas as 
                unidades adjecentes a unidade passada como argumento da funcao"""

    posicoes_adjecentes = obter_posicoes_adjacentes(obter_posicao(unidade))
    exercitos = obter_nome_exercitos(mapa)
    
    # Verificar qual e o nome do exercito inimigo
    if obter_exercito(unidade) == exercitos[0]:
        nome_enimigo = exercitos[1]
    else:
         nome_enimigo = exercitos[0]

    exercito_enimigo = obter_unidades_exercito(mapa, nome_enimigo)
    unidades_adjecentes = ()
    for posicao in posicoes_adjecentes:
        # Verificar se esta alguma unidade inimiga nas posicoes adjecentes a unidade passada como argumento
        if eh_posicao_unidade(mapa, posicao) and obter_unidade(mapa, posicao) in exercito_enimigo:
            unidades_adjecentes += (obter_unidade(mapa, posicao), )
        
    return ordenar_unidades(unidades_adjecentes) 


def obter_movimento(mapa, unit):
    ''' Funcao de alto nivel - Devolve a posicao seguinte da unidade argumento
                               de acordo com as regras de movimento das unidades no labirinto.'''

    ######################
    # Funcoes auxiliares #
    ######################
    def pos_to_tuple(pos):
        return obter_pos_x(pos), obter_pos_y(pos)

    def tuple_to_pos(tup):
        return cria_posicao(tup[0], tup[1])

    def tira_repetidos(tup_posicoes):
        conj_tuplos = set(tuple(map(pos_to_tuple, tup_posicoes)))
        return tuple(map(tuple_to_pos, conj_tuplos))

    def obter_objetivos(source):
        enemy_side = tuple(filter(lambda u: u != obter_exercito(
            source), obter_nome_exercitos(mapa)))[0]
        target_units = obter_unidades_exercito(mapa, enemy_side)
        tup_com_repetidos = \
            tuple(adj
                  for other_unit in target_units
                  for adj in obter_posicoes_adjacentes(obter_posicao(other_unit))
                  if eh_posicao_corredor(mapa, adj) and not eh_posicao_unidade(mapa, adj))
        return tira_repetidos(tup_com_repetidos)

    def backtrack(target):
        result = ()
        while target is not None:
            result = (target,) + result
            target, _ = visited[target]
        return result

    ####################
    # Funcao principal #
    ####################
    # Nao mexer se ja esta' adjacente a inimigo
    if obter_inimigos_adjacentes(mapa, unit):
        return obter_posicao(unit)

    visited = {}
    # posicao a explorar, posicao anterior e distancia
    to_explore = [(pos_to_tuple(obter_posicao(unit)), None, 0)]
    # registro do numero de passos minimo ate primeira posicao objetivo
    min_dist = None
    # estrutura que guarda todas as posicoes objetivo a igual minima distancia
    min_dist_targets = []

    targets = tuple(pos_to_tuple(obj) for obj in obter_objetivos(unit))

    while to_explore:  # enquanto nao esteja vazio
        pos, previous, dist = to_explore.pop(0)

        if pos not in visited:  # posicao foi ja explorada?
            # registro no conjunto de exploracao
            visited[pos] = (previous, dist)
            if pos in targets:  # se a posicao atual eh uma dos objetivos
                # se eh primeiro objetivo  ou se esta a  distancia minima
                if min_dist is None or dist == min_dist:
                    # acrescentor 'a lista de posicoes minimas
                    min_dist = dist
                    min_dist_targets.append(pos)
            else:  # nao 'e objetivo, acrescento adjacentes
                for adj in obter_posicoes_adjacentes(tuple_to_pos(pos)):
                    if eh_posicao_corredor(mapa, adj) and not eh_posicao_unidade(mapa, adj):
                        to_explore.append((pos_to_tuple(adj), pos, dist + 1))

        # Parar se estou a visitar posicoes mais distantes que o minimo,
        # ou se ja encontrei todos os objetivos
        if (min_dist is not None and dist > min_dist) or len(min_dist_targets) == len(targets):
            break

    # se encontrei pelo menos uma posicao objetivo,
    # escolhe a de ordem de leitura menor e devolve o primeiro movimento
    if len(min_dist_targets) > 0:
        # primeiro dos objetivos em ordem de leitura
        tar = sorted(min_dist_targets, key=lambda x: (x[1], x[0]))[0]
        path = backtrack(tar)
        return tuple_to_pos(path[1])

    # Caso nenhuma posicao seja alcancavel
    return obter_posicao(unit)



def calcula_pontos(mapa, exercito):
    """ Recebe dois arugmentos um mapa e um nome de um exercito e devolve 
          a pontuacao desse exercito que e igual a soma dos pontos de 
                        vida de todas as unidades"""      
    
    unidades_exercito = obter_unidades_exercito(mapa, exercito)
    pontos = 0
    # Para cada unidade do exercito adicionar aos pontos os pontos de vida dessa unidade
    for unidade in unidades_exercito:
        pontos += obter_vida(unidade)
    
    return pontos

def simula_turno(mapa):
    """ Esta funcao recebe como argumento um mapa e devolve o mapa modificado
         que corresponde ao mapa apos um turno de batalha completo ou seja 
            cada unidade se desloca uma unidade e ataca uma unidade do 
            exercitp enimigo se se encontrar nas suas refondesas"""

    unidades = obter_todas_unidades(mapa)
    for unidade in unidades:
        if obter_vida(unidade) > 0:  
            # Deslocar unidade
            mover_unidade(mapa, unidade, obter_movimento(mapa, unidade))
            # Atacar
            unidades_adjecentes = obter_inimigos_adjacentes(mapa, unidade)
        
            if unidades_adjecentes != ():
                inimigo = unidades_adjecentes[0]
                # Se a vida da unidade for menor ou igual a 0 remove a unidade do mapa
                if  unidade_ataca(unidade, inimigo):
                    if len(obter_unidades_exercito(mapa, obter_exercito(inimigo))) == 1 :
                        eliminar_unidade(mapa, inimigo)
                        return mapa
                    eliminar_unidade(mapa, inimigo)

        
    return mapa 

def simula_batalha(documento, modo_verboso):
    """ Esta funcao recebe como argumentos um documento de texto que contem as informasoes sobre
         o mapa (dimensao, paredes, exercitos) e simula uma batalha ate que um exercito ganhe ou 
       haja um empate (mapa antes do turno == mapa depois do turno) e da escreve o mapa e os pontos
          de cada unidade no terminal dependento do segundo argumento, se for True escreve todos 
              os turnos no terminal se for falso, so escreve o primeiro e o ultimo turnos
        esta funcao devolve ou o nome do exercito vencedor ou EMPATE quando os exertitos empatam"""

    def pontos_para_str(mapa, exercitos):
        """ Recebe como argumentos duas o mapa e um tuplo com o nome dos exercitos
            que estao a batalhar e escreve no terminal o mapa atual seguido dos pontos
                            de cada exercito formatados na forma 
                   [ exercito1:PontosExercito1 exercito2:PontosExercito2 ]"""
        print(mapa_para_str(mapa))
        exercito1 = exercitos[0] + ":" + str(calcula_pontos(mapa, exercitos[0]))
        exercito2 = exercitos[1] + ":" + str(calcula_pontos(mapa, exercitos[1]))
        print("[ " + exercito1 + " " + exercito2 + " ]") 

    # Abrir o ficheiro e ler as suas linhas
    documento_texto = open(documento, mode = "r")
    lista_linhas = documento_texto.readlines()
    documento_texto.close()
    
    # Trasformar cada linha de uma string para o tipo que ela representa
    for indice in range(len(lista_linhas)):
        lista_linhas[indice] = eval(lista_linhas[indice])

    # Setup dos dados guardados no ficheiro de texto
    dimensao = lista_linhas[0]
    paredes = tuple(cria_posicao(parede[0], parede[1]) for parede in lista_linhas[3])

    exercito1 = tuple(cria_unidade(cria_posicao(posicao[0], posicao[1]), lista_linhas[1][1], lista_linhas[1][2], lista_linhas[1][0]) \
    for posicao in lista_linhas[4])
    exercito2 = tuple(cria_unidade(cria_posicao(posicao[0], posicao[1]), lista_linhas[2][1], lista_linhas[2][2], lista_linhas[2][0]) \
    for posicao in lista_linhas[5])


    mapa = cria_mapa(dimensao, paredes, exercito1, exercito2)
    fim_jogo = False
    nome_exercitos = obter_nome_exercitos(mapa)
    # Print mapa inicial
    pontos_para_str(mapa, nome_exercitos)
    while not fim_jogo:
        mapa_inicial = cria_copia_mapa(mapa)
        mapa = simula_turno(mapa)

        if modo_verboso:
            pontos_para_str(mapa, nome_exercitos)

        if obter_unidades_exercito(mapa, nome_exercitos[0]) == ():
            if not modo_verboso:
                pontos_para_str(mapa, nome_exercitos)
            return nome_exercitos[1] 
        elif obter_unidades_exercito(mapa, nome_exercitos[1]) == ():
            if not modo_verboso:
                pontos_para_str(mapa, nome_exercitos)
            return nome_exercitos[0]

        if mapas_iguais(mapa_inicial, mapa):
            if not modo_verboso:
                pontos_para_str(mapa, nome_exercitos)
            return "EMPATE"