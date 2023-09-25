from lotterie import TirageEuroMillion, Tirageloto

if __name__ == "__main__":

    typeTirage: [int, None] = None
    while typeTirage not in [1, 2]:
        try:
            typeTirage = int(input("Voulez vous faire des tirages Loto ou Euromillion ? \n"
                                   "1 - Pour loto \n"
                                   "2 - pour euromillion\n"
                                   "Votre Choix : "))
        except ValueError:
            print("\nVeuillez entrer un entier \n")

    if typeTirage == 1:
        Tirage = Tirageloto
    else:
        Tirage = TirageEuroMillion

    nombreTirage: [int, None] = None
    while nombreTirage is None:
        try:
            nombreTirage = int(input("Entrez le nombre de tirage que vous souhaitez : "))

        except ValueError:
            print("Veuillez entrer un entier")

    mesTirages: list = []
    for _ in range(nombreTirage):
        mesTirages.append(Tirage())

    for tirage in mesTirages:
        print(tirage)
