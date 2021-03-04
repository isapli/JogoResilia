def argumento ():
    print ('''
    Olá sobrevivente, 
    você acaba de entrar no jogo === APOCALIPSE ZUMBI [¬º-°]¬ ===

    Preste atenção pois essas informações serão essenciais para sua sobrevivência.
    Você cursa biologia na Universidade Federal Brasileira (UFB) e está em reta final 
    no curso. Infelizmente pra você, hoje também é o último dia da civilização 
    como conhecemos e sua permanência nesse mundo depende unicamente da sua 
    capacidade de tomar decisões acertadas.
    Todos os acontecimentos se passam num breve período dentro de um dia, no 
    perímetro da UFB num ano até então desconhecido. 
    ==================================================
    Escolha com sabedoria e bem-vinda ao fim do mundo!
    ==================================================
    ''')

def instrucoes ():
    print ('''
    ===============
    . INSTRUÇÕES: .
    ===============

    Cada situação apresentada possui somente 2 escolhas, cada escolha leva a uma consequência
    diferente e não há como voltar atrás. As escolhas sempre serão apresentadas em números 1 (um) 
    ou 2 (dois), qualquer número fora dessas duas opções não serão aceitas.
    Este jogo possui mais de um final, dependendo de qual caminho você escolher.
    Boa sorte!
    [¬º-°]¬
    ''')

def pergunta_1 ():
    print(f'''
    Bem-vinda ao jogo {nome}, neste momento você está sentada no restaurante universitário da UFB,
    almoçando e conversando com seus amigos. O prédio do restaurante universitário, popularmente
    conhecido como bandejão, é um grande galpão com o pé direito alto, preenchido por diversas
    mesas compridas, daquelas com bancos embutidos que comportam 40 pessoas cada. A entrada se dá
    pela lateral e o edifício simula um sobrado por conta do terreno íngrime, onde os alunos entram 
    pelo que seria o primeiro andar, atravessam uma grande sacada onde formam filas e descem ordenadamente
    por uma rampa para receberem as comidas em bandejas, vindas de panelões industriais gigantescos.
    O bandejão alimenta em torno de 10 mil pessoas por dia, contando café-da-manhã, almoço e jantar.
    Esse dia em especial está absurdamente quente, o ápice do verão brasileiro, todos almoçando
    na habitual algazarra interminável, por isso a confusão inicialmente se camuflou no ambiente caótico.
    Seu amigo Caique estava acabando de contar sobre o treino de percussão quando logo a sua frente 
    você e Cíntia, sua outra amiga, viram duas pessoas caírem emboladas da sacada direto para a mesa logo 
    abaixo, uma queda de 4 metros que soou como uma batida de carro, seguida de alguns segundos de silêncio
    absoluto.
    Imediatamente todas as pessoas próximas se levantam, parte curiosidade e parte preocupação. Ao fundo 
    vocês conseguem ouvir o som de mais de uma sirene tocando. 
    Gabriela, sua outra amiga, puxa a manga da sua camiseta e aponta pela imensa janela de vidro. Mesmo de
    dentro do restaurante vocês conseguem ver a enorme nuvem de fumaça preta.
    - É pra lá que fica o laboratório de química. - comenta Gabriela. - Se o fogo for lá, é melhor a gente 
    sair rápido daqui.
    Ao mesmo tempo você ouve a gritaria das pessoas próximas do corpo pedindo ajuda pra tirar um possível
    sobrevivente.
    O que você faz? 
    1. Fica e ajuda as pessoas acidentadas;
    2. Segue o conselho da Gabriela e sai do restaurante o mais rápido possível.
    ''')
    
    escolha_a = int(input("Digite o número da sua escolha de movimento:\n- "))

    if escolha_a == 1:
        print('''
        Contrariando sua percepção de perigo, você fica pra tentar tirar o rapaz que sobreviveu à queda.
        Uma estudante de fisioterapia te chama pra você ajudar a tirar os pedaços de madeira de cima do corpo.
        Tentando arranjar uma posição melhor, você se aproxima. O rapaz, mergulhado em sangue, acorda 
        subitamente e rosnando (sim, rosnando) agarra sua perna, tirando um bom pedaço do quadríceps, 
        o músculo frontal da coxa.
        Você grita de dor enquanto o sangue jorra da perna, e a última coisa que vê é o rapaz, dado como 
        morto, se levantar, os olhos branco leitosos como alguém com catarata, agarrar o pescoço da estudante 
        de fisioterapia e mastigá-lo com tanta facilidade que parecia feito de papel.
        Depois disso você desmaia e morre.

        =========================================================
        FIM DE JOGO PRA VOCÊ, MORTE POR HEMORRAGIA SEVERA [¬º-°]¬
        =========================================================
        ''')
    
    elif escolha_a == 2:
        pergunta_2 ()
    
    else:
        print('''Você digitou um número fora das nossas opções de jogada, por favor, recomece
        o jogo e se atente às regras [¬º-°]¬''')

def pergunta_2 ():
    print('''
    Quando vocês colocam o pé pra fora do bandejão, percebem o completo caos que reina na universidade.
    Mais de um foco de incêndio ergue nuvens pretas de fumaça densa e uma correria generalizada se espalhou
    pelo campus. 
    Você, Cíntia, Gabriela e Caique correm em direção ao ponto de ônibus no bolsão do estacionamento. Na correria
    desabalada esbarram com Paulo, o outro colega de sala da biologia que também viu os acontecimentos no
    restaurante.
    - O que foi aquilo? Vocês viram o ataque? - ele pergunta, sem fôlego.
    - Eles caindo da sacada? Vimos.
    - Não, não. O ataque. O cara que caiu, que tava morto no chão levantou o atacou a mina no pescoço! No 
    pescoço cara, igual bicho.
    - Como assim? - Gabriela questiona. - Ele não tava morto? Como assim atacou?
    - Eu não sei. Não sei. É melhor a gente sair daqui agora. Sério, lá dentro tá um caos. Vamos pegar o ônibus
    que vai pra moradia, tá saindo um agora.
    Você olha pela janela de vidro mas não consegue ver nenhum ataque, só uma correria infernal lá dentro.
    Você correm pro ponto de ônibus bem na hora que o motorista está dando partida. O ônibus está quase lotado mas
    vocês conseguem ver lugares no fundo.
    - Dá tempo {nome}, vamo correr.
    O que você faz? 
    1. Corre com seus colegas pra pegar o õnibus e sair da universidade;
    2. Desiste do ônibus e prefere tentar outra alternativa.

    ''')
    escolha_b = int(input("Digite o número da sua escolha de movimento:\n- "))

    if escolha_b == 1:
        print ('''
        - Vamo {nome}, corre!
        Você corre meio sem fôlego e consegue subir no ônibus junto com seus colegas, vocês se dirigem pro
        fundo e se largam nos bancos, cansados.
        Um burburinho alto se espalha pelo õnibus, o motorista não pára no próximo ponto e segue direto,
        pegando a avenida em alta velocidade. Vocês conseguem ver um rastro de sangue no chão e ouvem um estouro.
        - Acho que o laboratório de química explodiu. Lembra daqueles tanques de oxigênio gigantes que ficam
        no pátio?
        Você não responde porque está prestando atenção ao seu entorno e também não vê o acidente que se segue.
        O motorista de ônibus, aterrorizado e com pressa de sair daquele pandemônio, estava andando a mais de 
        150 km por hora, por isso foi incapaz de desviar do carro que entrou na pista pela contramão.
        Você batem um de frente pro outro, os três carros que vinham logo atrás, também em alta velocidade,
        batem na traseira formando um acidente gigantesco e provocando um foco de incêndio bem no meio da
        avenida principal.
        Você morre na batida, seus amigos, presos aos escombros, morrem intoxicados pela fumaça sem conseguirem
        sair.
        ============================================================
        FIM DE JOGO PRA VOCÊ, MORTE POR ACIDENTE DE TRÂNSITO [¬º-°]¬
        ============================================================
        ''')
    
    elif escolha_b == 2:
        pergunta_3 ()
    
    else:
        print('''Você digitou um número fora das nossas opções de jogada, por favor, recomece
        o jogo e se atente às regras [¬º-°]¬''')


def pergunta_3 ():
    print('''
    Você tem um pressentimento ruim quando vê o ônibus e desiste de entrar.
    Gabriela, Cíntia e Paulo, supersticiosos, ficam com você.
    Vocês vêem Caique e alguns colegas subirem no ônibus e alguns minutos depois ouvem a explosão de um dos 
    tanques de oxigênio do departamento de química.
    - Acho que é melhor a gente se afastar da química. - comenta Paulo.
    - Você veio de carro, Cíntia?
    - Vim, mas deixei lá no bolsão da biologia.
    - O da frente?
    Cíntia ri sem humor. - Não, o de trás, o último do fundo.
    - Puta que pariu. Ok. Vamos lá, é melhor que tentar voltar a pé.
    Ao fundo vocês ouvem uma batida e uma nova explosão, mas dessa vez vinda de outra direção. Vocês ainda não
    sabem mas nenhum colega dentro do ônibus sobreviveu.
    Seu grupo passa correndo pela praça principal, que virou um cenário semelhante a uma pequena zona de
    guerra, ou um filme de terror. As barracas todas viradas, comidas espalhadas pelo chão e alguns corpos 
    caídos, parecendo mortos.
    - O que aconteceu aqui? Será que foi um ataque?
    - Quem atacaria a UFB? - {nome} questiona quando sem querer tropeça e cai no chão.
    Você rala os joelhos e as mãos, tentando aparar a queda. - Nossa, doeu pra caralho. Que isso aqui? - você
    pergunta, cutucando com a ponta da perna o objeto no qual tropeçou.
    - Hm. Acho que é uma perna. - Gabriela responde, num tom quase prosaico, mas que não esconde o nervosismo. 
    - {nome}, tem um cara amarrado aqui.
    - Amarrado? 
    - É, olha.
    Você se levanta do chão, evitando cuidadosamente o pedaço de perna e dá a volta nas lonas da barraca. Há um
    rapaz com o tronco amarrado a um poste de energia. 
    - {nome}, não é melhor desamarrar ele?
    - Mano, por que alguém amarraria um cara no meio da praça? Ele deve ser um dos terroristas ou sei lá. Deixa
    ele aí.
    Gabriela parece incerta ainda. - Eu acho que é melhor soltar, senão ele não vai conseguir sobreviver, se isso
    aqui pegar fogo.
    - Mas e se ele te atacar, Gabi? {nome}, o que você acha?
    O que você faz? 
    1. Desamarra o rapaz;
    2. Ignora e continua seguindo para o Instituto de Biologia.
    ''')
    escolha_c = int(input("Digite o número da sua escolha de movimento:\n- "))

    if escolha_c == 1:
        print ('''
        Sob os protestos de Cíntia, você se aproxima do homem. Ele não parece respirar.
        - Eu acho que ele morreu, gente. Vou tentar soltar as mãos.
        Você dá a volta no poste pra tentar desamarrá-lo, mas pra sua surpresa não havia nada que o prendesse
        ao poste. - Ué, ele tá solto. Acho que só desmaiou.
        O homem, aparentemente desmaiado, acorda de súbito e abre os olhos. Estão branco leitosos como os olhos
        de uma pessoa cega. Em choque, vocês o vêem farejar o ar como um cachorro e num movimento rápido e
        preciso, ele agarra sua mão e te puxa num tranco.
        Você até ouve seus amigos gritarem, mas pra você já é tarde.
        ====================================================
        FIM DE JOGO PRA VOCÊ, MORTE POR ATAQUE ZUMBI [¬º-°]¬
        ====================================================
        ''')
    
    elif escolha_c == 2:
        pergunta_4 ()
    
    else:
        print('''Você digitou um número fora das nossas opções de jogada, por favor, recomece
        o jogo e se atente às regras [¬º-°]¬''')

def pergunta_4 ():
    print('''
    - Ele vai conseguir se soltar, Gabi. Fica tranquila.
    Mas as palavras parecem esvaziadas de significado. A UFB está mergulhada na desordem, mas vocês continuam 
    seguindo para o Instituto.
    É com alívio que vocês avistam a ponta do prédio verde do Instituto de Biologia. 
    - Olha, - Cíntia fala. - A chave tá no laboratório, vamo entrar pelo fundo que é mais tranquilo.
    Vocês dão a volta pelo prédio, passando pelos laboratório de fisiologia vegetal, animal e comorbidades.
    - Agora a gente tá provisoriamente no prédio da genética, até conseguirem finalizar o reparo na fiação. É
    por aqui, entra aí.
    Quando Cíntia passa o cartão no leitor e a tranca abre, ela empurra vocês pra dentro.  Quase dá pra ouvir 
    o suspiro de alívio do grupo.
    - Tá silencioso aqui. - voc~e comenta.
    - É, falem baixo. Transformaram o Laboratório de Doenças Tropicais em um NB-3 e fizeram o de nível 4 no 
    subsolo pra estudar as variantes latinas do coronavírus. Agora quase ninguém pode entrar. - Cíntia respondia 
    enquanto os guiava pelos muitos corredores do Departamento de Genética.
    - Não sabia que tinham trazido a genética viral pra cá. Não era no Hospital das Clínicas?
    - Até era, mas os protocolos de segurança não tavam sendo seguidos. E nível 4 né, um B.O. enorme.

    * nota: laboratórios que trabalham com organismos e agentes biológicos são divididos em quatro níveis de
    biossegurança (NB), definidos pelo Centro de Controle e Prevenção de Doenças (CDC), designados em ordem
    crescente pelo grau de proteção proporcionado: NB-1, NB-2, NB-3 e NB-4. Os níveis mais baixos começam com 
    precauções mínimas por conta do baixo risco de biossegurança. A medida que o risco aumenta, a medida de
    segurança também aumenta. O nível 4 é o último, laboratórios NB-4 tratam de qualquer agente que cause
    doenças com risco de vida, sem tratamento disponível e com alto potencial de infecção transmitida por
    aerossol, ou agentes que apresentam risco desconhecido (como o Ebola, por exemplo).

    - Achei que não podia instalar NB-4 em Universidades. Sempre achei que devia ser isolado.
    - Devia, mas o Gonçolo pode tudo aqui dentro. Shhh. - Cíntia estancou, de repente. - É ele. Entra aqui.

    Agora vocês estão num quartinho pequeno que serve de despensa pra material de limpeza.
    Você sussurra pra sua amiga: - Que foi?
    - É o Gonçolo. Ele tá aqui, nossa, se ele ver vocês aqui dentro ele come meu fígado.     
    Vocês vêem 3 sombras passando pelos corredores. Dá pra entreouvir a conversa, principalmente porque eles
    estavam gritando. Você vê seus amigos encolhidos na sombra e aguça os ouvidos.
    - ... quero saber quem foi o responsável por essa merda. 
    (...)
    - Não tô nem aí, por mim pode morrer.
    (...)
    (...)
    - É o Gonçolo que tá gritando desse jeito. - Paulo sussurra. - Quem são os outros dois?
    - Devem ser o Pepas e o Minosse, eles não trabalham todos juntos?
    - Shhh. Tão voltando.
    Vocês vêem as 3 sombras retornarem da onde vieram, mas pela altura da voz, dessa vez eles estavam conversando
    ali mesmo no corredor, bem em frente ao quartinho de despensa
    (...)
    - Você perdeu a cabeça, Gonçolo? O prédio inteiro tá infectado, isso aqui tinha que estar lacrado.
    - Eu não vou lacrar enquanto não conseguir a amostra. Senão tudo isso vai ter sido em vão. 
    Uma terceira voz se pronuncia.
    - Vocês tem certeza que vazou? 
    - Certeza. Os guardas já relataram quatro ataques, e isso é o que eles sabem.
    - Mas pode ser um ataque qualquer.
    - Eles tinham os olhos leitosos. É a cepa que escapou. Hoje nós recebemos o aviso de falha na segurança.
    Por isso eu adiantei o negócio.
    Uma pausa.
    - Com certeza foi o Vinícius quem deixou o frasco cair. Lembra quando ele quebrou a centrífuga?
    - Agora já foi. Não adianta mais. Vamos esperar o helicóptero. Ele está vindo do HC, chega aqui em 20 minutos,
    mais ou menos. Enquanto isso vamos isolar o que der e lacrar o prédio. Se precisar taca fogo em tudo,
    estamos ricos mesmo.
    * nota: HC é a abreviação popular para Hospital das Clínicas.

    Do armário vocês ouvem um trio de passos se afastar. 
    Mesmo na penumbra você pode ver os rostos assustados dos seus colegas, ninguém se pronuncia por alguns
    instantes. 
    Paulo quebra o silêncio com um sussurro: - Vocês acham que é verdade?
    - Que eles iam vender uma cepa de um vírus doido e deixaram escapar e agora virou um caos? Conhecendo
    esses três, eu não duvido. São todos mercenários. Lembra das aulas?
    - A gente precisa sair daqui, eles vão lacrar o laboratório, vamo pegar a chave e sair.
    Cíntia abre a porta e espia o corredor, está tudo limpo. Vocês se esgueiram pelo corredor até a sala dos
    alunos, sua amiga pega a bolsa, tira a chave e a carteira de dentro e vocês saem silenciosamente. 
    - Pra onde eles foram?
    - Eu não sei. Onde é a saída? 
    - A lateral é à esquerda, a principal à direita, mas 
    ''')
    escolha_d = int(input("Digite o número da sua escolha de movimento:\n- "))

    if escolha_d == 1:
        print (''' escrever a situação de morte 4
        ============================
        FIM DE JOGO PRA VOCÊ [¬º-°]¬
        ============================
        ''')
    
    elif escolha_d == 2:
        pergunta_5 ()
    
    else:
        print('''Você digitou um número fora das nossas opções de jogada, por favor, recomece
        o jogo e se atente às regras [¬º-°]¬''')

def pergunta_5 ():
    print(''' ''')
    escolha_e = int(input("Digite o número da sua escolha de movimento:\n- "))

    if escolha_e == 1:
        print (''' escrever a situação de morte 5
        ============================
        FIM DE JOGO PRA VOCÊ [¬º-°]¬
        ============================
        ''')
    
    elif escolha_e == 2:
        pergunta_6 ()
    
    else:
        print('''Você digitou um número fora das nossas opções de jogada, por favor, recomece
        o jogo e se atente às regras [¬º-°]¬''')

def pergunta_6 ():
    print(''' ''')
    escolha_f = int(input("Digite o número da sua escolha de movimento:\n- "))

    if escolha_f == 1:
        print (''' escrever a situação de morte 6
        ============================
        FIM DE JOGO PRA VOCÊ [¬º-°]¬
        ============================
        ''')
    
    elif escolha_f == 2:
        print (''' PARABÉNS, VOCÊ GANHOU O JOGO ''')
    
    else:
        print('''Você digitou um número fora das nossas opções de jogada, por favor, recomece
        o jogo e se atente às regras [¬º-°]¬''')

#

print ('''
====================================
.     APOCALIPSE ZUMBI [¬º-°]¬     .
====================================
Um jogo rápido de tomada de decisões
''')

# APRESENTAÇÃO
argumento ()
instrucoes ()

# NOME DO JOGADOR
nome = input("Qual seu nome?\n- ")

# JOGO
pergunta_1 ()