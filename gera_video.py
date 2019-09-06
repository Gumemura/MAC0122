# -*- coding: utf-8 -*-
#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO 
# NÃO ALTERE OS NOMES DAS FUNÇÕES
# NÃO APAGUE OS DOCSTRINGS
#------------------------------------------------------------------

'''

    Nome: Guilherme Umemura
    NUSP: 9353592

    Ao preencher esse cabeçalho com o meu nome e o meu número USP,
    declaro que todas as partes originais desse exercício programa (EP)
    foram desenvolvidas e implementadas por mim e que portanto não 
    constituem desonestidade acadêmica ou plágio.
    Declaro também que sou responsável por todas as cópias desse
    programa e que não distribui ou facilitei a sua distribuição.
    Estou ciente que os casos de plágio e desonestidade acadêmica
    serão tratados segundo os critérios divulgados na página da 
    disciplina.
    Entendo que EPs sem assinatura devem receber nota zero e, ainda
    assim, poderão ser punidos por desonestidade acadêmica.

    Abaixo descreva qualquer ajuda que você recebeu para fazer este
    EP.  Inclua qualquer ajuda recebida por pessoas (inclusive
    monitores e colegas). Com exceção de material de MAC0110, caso
    você tenha utilizado alguma informação, trecho de código,...
    indique esse fato abaixo para que o seu programa não seja
    considerado plágio ou irregular.

    Exemplo:

        A monitora me explicou que eu devia utilizar a função int() quando
        fazemos leitura de números inteiros.

        A minha função quicksort() foi baseada na descrição encontrada na 
        página https://www.ime.usp.br/~pf/algoritmos/aulas/quick.html.

    Descrição de ajuda ou indicação de fonte:

'''

from numpymagem import NumPymagem
from numpymutil import mostre_video
from numpymutil import salve_video
import random

# Escreva aqui outras constantes que desejar
ALTURA  = 120
LARGURA = 160
BLACK = 0
WHITE = 250

#-------------------------------------------------------------------------- 

def main():
    ''' (None) -> None
    Escreva o seu programa que cria o vídeo como descrito no enunciado.
    
    O código abaixo serve para ilustrar como usar a função mostre_video()
    que recebe uma lista com NumPymagens e as mostra em um vídeo na tela
    do seu computador usando PyGame. Por isso lembre-se de seguir as 
    instruções para instalar PyGame no seu computador.

    Remova ou altere o código para gerar o seu próprio vídeo. Não se esqueça
    de criar funções para facilitar o entendimento do seu vídeo.

    Você pode (mas não precisa!) salvar o seu vídeo em um formato mp4, para
    mostrar sua obra no fórum da disciplina. Para isso, antes de salvar, 
    você deve instalar o software ffmpeg que você pode baixar de 
    https://ffmpeg.org/download.html. 
    '''
    
    video = []
    preto = NumPymagem(ALTURA, LARGURA, WHITE)
    branco = NumPymagem(ALTURA, LARGURA, WHITE)
    cor = BLACK

    raio = 5
    centrox = random.randint(raio + 1,ALTURA - raio - 1)
    centroy = random.randint(raio + 1,LARGURA - raio - 1)
    velocidadeX = random.uniform(0.7, 2.5)
    velocidadeY = random.uniform(0.7, 2.5)

    aumentaX = True
    aumentaY = True

    for i in range(120): #Faz surgir a bolinha
        cor = (cor - 1.5)%WHITE
        bola = NumPymagem(ALTURA, LARGURA, WHITE)
        bola.pinte_disco(centrox, centroy, raio, cor)
        video.append(bola)

    for i in range(600): #Move a bolinha
        bola.pinte_disco(centrox, centroy, raio, BLACK)
        video.append(bola)
        bola = NumPymagem(ALTURA, LARGURA, WHITE)

        if((ALTURA - centrox <= raio) or centrox <= raio):
            if(aumentaX == True):
                aumentaX = False
            else:
                aumentaX = True
        if((LARGURA - centroy <= raio) or centroy <= raio):
            if(aumentaY == True):
                aumentaY = False
            else:
                aumentaY = True
        if(aumentaX):
            centrox += velocidadeX
        else:
            centrox -= velocidadeX

        if(aumentaY):
            centroy += velocidadeY
        else:
            centroy -= velocidadeY

    #Faz a bolinha dar flash antes de explodir
    for i in range(30):
        bola.pinte_disco(centrox, centroy, raio, BLACK)
        bola = NumPymagem(ALTURA, LARGURA, WHITE)
        video.append(bola)
    for i in range(10):
        bola.pinte_disco(centrox, centroy, raio, 200)
        bola = NumPymagem(ALTURA, LARGURA, WHITE)
        video.append(bola)
    for i in range(30):
        bola.pinte_disco(centrox, centroy, raio, BLACK)
        bola = NumPymagem(ALTURA, LARGURA, WHITE)
        video.append(bola)
    for i in range(10):
        bola.pinte_disco(centrox, centroy, raio, 200)
        bola = NumPymagem(ALTURA, LARGURA, WHITE)
        video.append(bola)
    for i in range(30):
        bola.pinte_disco(centrox, centroy, raio, BLACK)
        bola = NumPymagem(ALTURA, LARGURA, WHITE)
        video.append(bola)
    for i in range(10):
        bola.pinte_disco(centrox, centroy, raio, 200)
        bola = NumPymagem(ALTURA, LARGURA, WHITE)
        video.append(bola)
    for i in range(15):
        bola.pinte_disco(centrox, centroy, raio, BLACK)
        bola = NumPymagem(ALTURA, LARGURA, WHITE)
        video.append(bola)
    for i in range(10):
        bola.pinte_disco(centrox, centroy, raio, 200)
        bola = NumPymagem(ALTURA, LARGURA, WHITE)
        video.append(bola)
    for i in range(15):
        bola.pinte_disco(centrox, centroy, raio, BLACK)
        bola = NumPymagem(ALTURA, LARGURA, WHITE)
        video.append(bola)
    for i in range(10):
        bola.pinte_disco(centrox, centroy, raio, 200)
        bola = NumPymagem(ALTURA, LARGURA, WHITE)
        video.append(bola)
    for i in range(15):
        bola.pinte_disco(centrox, centroy, raio, BLACK)
        bola = NumPymagem(ALTURA, LARGURA, WHITE)
        video.append(bola)
    for i in range(10):
        bola.pinte_disco(centrox, centroy, raio, 200)
        bola = NumPymagem(ALTURA, LARGURA, WHITE)
        video.append(bola)
    for i in range(5):
        bola.pinte_disco(centrox, centroy, raio, BLACK)
        bola = NumPymagem(ALTURA, LARGURA, WHITE)
        video.append(bola)
    for i in range(10):
        bola.pinte_disco(centrox, centroy, raio, 200)
        bola = NumPymagem(ALTURA, LARGURA, WHITE)
        video.append(bola)
    for i in range(5):
        bola.pinte_disco(centrox, centroy, raio, BLACK)
        bola = NumPymagem(ALTURA, LARGURA, WHITE)
        video.append(bola)
    for i in range(10):
        bola.pinte_disco(centrox, centroy, raio, 200)
        bola = NumPymagem(ALTURA, LARGURA, WHITE)
        video.append(bola)
    for i in range(5):
        bola.pinte_disco(centrox, centroy, raio, BLACK)
        bola = NumPymagem(ALTURA, LARGURA, WHITE)
        video.append(bola)
    for i in range(10):
        bola.pinte_disco(centrox, centroy, raio, 200)
        bola = NumPymagem(ALTURA, LARGURA, WHITE)
        video.append(bola)
    for i in range(5):
        bola.pinte_disco(centrox, centroy, raio, BLACK)
        bola = NumPymagem(ALTURA, LARGURA, WHITE)
        video.append(bola)
    for i in range(10):
        bola.pinte_disco(centrox, centroy, raio, 200)
        bola = NumPymagem(ALTURA, LARGURA, WHITE)
        video.append(bola)

    for i in range(120): #Explode a bolinha
        bola.pinte_disco(centrox, centroy, raio, cor)
        raio += 2
        cor = random.randint(40, 250)
        bola = NumPymagem(ALTURA, LARGURA, WHITE)
        video.append(bola)

    for i in range(60): #Descanso entre animacoes
        descanso = NumPymagem(ALTURA, LARGURA, WHITE)
        video.append(descanso)

    cArma = 0
    for i in range(120): #Surgimento do canhão
        arma = NumPymagem(ALTURA, LARGURA, WHITE)
        arma.pinte_retangulo(ALTURA//2 - 4, 0, ALTURA//2 + 4, cArma, BLACK)
        arma.pinte_disco(ALTURA//2 - 15, cArma - 30, 20, 50)
        if(cArma < 40):
            cArma += 1
        video.append(arma)

    cProjetil = cArma
    rExplosao = 0
    for i in range(180): #Recuo do disparo
        arma.pinte_retangulo(ALTURA//2 - 4, 0, ALTURA//2 + 4, cArma, BLACK)
        arma.pinte_disco(ALTURA//2 - 15, cArma - 30, 20, 50)
        if(cArma > 25):
            cArma -= 10

        #Trajetoria do projetil
        arma.pinte_retangulo(ALTURA//2 - 3, cProjetil, ALTURA//2 + 3, cProjetil + 10, BLACK)
        cProjetil += 6

        #Explosao
        if(cProjetil >= LARGURA):
            arma.pinte_disco(ALTURA//2 , LARGURA, rExplosao, cor)
            rExplosao += 2
            cor = random.randint(40, 250)


        arma = NumPymagem(ALTURA, LARGURA, WHITE)
        video.append(arma)

    for i in range(60): #Descanso entre animacoes
        descanso = NumPymagem(ALTURA, LARGURA, WHITE)
        video.append(descanso)

    lChao = 0
    altBola = ALTURA + 10
    limite = 30
    limiteSobe = 60
    velocidade = 4

    cai = True

    bolaPong = NumPymagem(ALTURA, LARGURA, WHITE)
    for i in range(120): #Chão do bola pong
        bolaPong = NumPymagem(ALTURA, LARGURA, WHITE)
        bolaPong.pinte_retangulo(0, 0, 20, lChao, BLACK)
        if(lChao < LARGURA + 50):
            lChao += 2

        video.append(bolaPong)

    for i in range(180):
        bolaPong.pinte_retangulo(0, 0, 20, LARGURA + 5, BLACK)
        bolaPong.pinte_disco(altBola, LARGURA//2, 10, BLACK)

        if(cai):
            if(altBola >= 30):
                altBola -= velocidade
                bolaPong = NumPymagem(ALTURA, LARGURA, WHITE)
            else:
                limiteSobe -= 5
                cai = False
        else:
            if(altBola <= limiteSobe):
                altBola += velocidade
                bolaPong = NumPymagem(ALTURA, LARGURA, WHITE)
            else:
                cai = True

        if(limite <= 0):
            velocidade = 0

        video.append(bolaPong)

    exploxaoFinal = NumPymagem(ALTURA, LARGURA, WHITE)
    raioExp = 1

    for i in range(60):
        exploxaoFinal.pinte_retangulo(0, 0, 20, LARGURA + 5, BLACK)
        exploxaoFinal.pinte_disco(30, LARGURA//2, 10, BLACK)

        exploxaoFinal.pinte_disco(30, LARGURA//2, raioExp, cor)
        raioExp += 2
        cor = random.randint(40, 255)

        exploxaoFinal = NumPymagem(ALTURA, LARGURA, WHITE)
        video.append(exploxaoFinal)

    mostre = True
    if mostre:
        mostre_video(video)

    salve = False
    if salve:
        print("Salvando vídeo")
        salve_video(video)

#-------------------------------------------------------------------------- 
#
# ESCREVA OUTRAS FUNÇÕES E CLASSES QUE DESEJAR
#
#-------------------------------------------------------------------------- 


#-------------------------------------------------------------------------- 
if __name__ == '__main__':
    main()