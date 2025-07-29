def main():
    garrafas = int(99)

    while garrafas > 0:
        print("{} garrafas de cerveja na parede do Maracanã".format(garrafas))
        print("{} garrafas de cerveja. Pegue uma e passe ao redor".format(garrafas))
        garrafas -= 1
        print("{} garrafas de cerveja sobraram".format(garrafas))

    print("Não tem mais garrafas de cerveja no Maracanã")
if __name__ == "__main__":
    main()
