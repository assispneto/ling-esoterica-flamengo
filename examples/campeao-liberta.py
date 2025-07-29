def main():
    print("Digite o número de vezes que o Falmengo foi campeão da Libertadores:")
    campeao = int(input())

    if campeao == 3:
        print("Você acertou!! O Falmengo foi campeão da Libertadores 3 vezes")

    if campeao !=3:
        print("Você errou!! O Falmengo não foi campeão da Libertadores {}".format(campeao))

if __name__ == "__main__":
    main()