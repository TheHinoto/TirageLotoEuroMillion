from lotterie import TirageEuroMillion, Tirageloto

if __name__ == "__main__":

    typeTirage: [int, None] = None
    while typeTirage not in [1, 2]:
        try:
            typeTirage = int(input("Voulez vous faire des tirages Loto ou EuroMillion ? \n"
                                   "1 - Pour Loto \n"
                                   "2 - pour EuroMillion\n"
                                   "Votre Choix : "))
        except ValueError:
            print("\nVeuillez entrer un entier \n")

    Tirage = Tirageloto
    if typeTirage == 2:
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
