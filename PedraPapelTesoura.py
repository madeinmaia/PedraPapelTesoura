def exibirMenu():
    print("Bem-vindo ao Jogo de Pedra, Papel e Tesoura!")
    print("1. Jogador vs Jogador")
    print("0. Sair")

def obterEscolhaJogador(jogador):
    escolha = input(f"{jogador}, escolha Pedra, Papel ou Tesoura: ")
    while escolha not in ["Pedra", "Papel", "Tesoura"]:
        print("Escolha inválida! Tente novamente.")
        escolha = input(f"{jogador}, escolha Pedra, Papel ou Tesoura: ")
    return escolha

def determinarVencedor(escolha1, escolha2):
    if escolha1 == escolha2:
        return "empate"
    elif (escolha1 == "Pedra" and escolha2 == "Tesoura") or (escolha1 == "Tesoura" and escolha2 == "Papel") or (escolha1 == "Papel" and escolha2 == "Pedra"):
        return "jogador1"
    else:
        return "jogador2"

def exibirResultado(vencedor):
    if vencedor == "empate":
        print("Empate!")
    else:
        print(f"{vencedor} venceu!")

def jogar():
    while True:
        exibirMenu()
        escolhaMenu = input("Escolha uma opção: ")
        
        if escolhaMenu == "1":
            escolhaJogador1 = obterEscolhaJogador("Jogador 1")
            escolhaJogador2 = obterEscolhaJogador("Jogador 2")
            vencedor = determinarVencedor(escolhaJogador1, escolhaJogador2)
            exibirResultado(vencedor)
        elif escolhaMenu == "0":
            print("Obrigado por jogar!")
            break
        else:
            print("Opção inválida! Tente novamente.")


jogar()