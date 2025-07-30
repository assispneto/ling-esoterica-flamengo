def main():
    print("Digite o número de vezes que o Flamengo foi campeao da Libertadores: ")
    campeao = int(input())

    if campeao == 3:
        print("Voce acertou!! O Falmengo foi campeão da Libertadores 3 vezes")

        if campeao != 3:
            print("Voce errou!! O Falmengo nao foi campeão da Libertadores {}".format(campeao))

if __name__ == "__main__":
    main()