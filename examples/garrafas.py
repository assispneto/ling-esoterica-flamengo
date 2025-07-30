import time
def main():
   garrafas = int(99)

   while garrafas > 0:
      print("{} garrafas de cerveja na parede do Maracanã".format(garrafas))
      time.sleep(1)
      print("{} garrafas de cerveja. Pegue uma e passe ao redor".format(garrafas))
      time.sleep(1)
      garrafas -= 1
      print("{} garrafas de cerveja sobraram".format(garrafas))
      time.sleep(1)

   print("Não tem mais garrafas de cerveja no Maracanã")
if __name__ == "__main__":
    main()
