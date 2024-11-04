from varasto import Varasto


def init():
    mehua = Varasto(100.0)
    olutta = Varasto(100.0, 20.2)
    print("Luonnin jälkeen:")
    print(f"Mehuvarasto: {mehua}")
    print(f"Olutvarasto: {olutta}")
    return mehua, olutta


def olut_getters(varasto):
    print("Olut getterit:")
    print(f"saldo = {varasto.saldo}")
    print(f"tilavuus = {varasto.tilavuus}")
    print(f"paljonko_mahtuu = {varasto.paljonko_mahtuu()}")


def mehu_setters(varasto):
    print("Mehu setterit:")
    print("Lisätään 50.7")
    varasto.lisaa_varastoon(50.7)
    print(f"Mehuvarasto: {varasto}")
    print("Otetaan 3.14")
    varasto.ota_varastosta(3.14)
    print(f"Mehuvarasto: {varasto}")


def virheelliset():
    print("Virhetilanteita:")
    print("Varasto(-100.0);")
    huono = Varasto(-100.0)
    print(huono)

    print("Varasto(100.0, -50.7)")
    huono = Varasto(100.0, -50.7)
    print(huono)


def suuri_lisays(varasto):
    print(f"{varasto} ennen suurta lisäystä")
    print("Lisätään 1000.0")
    varasto.lisaa_varastoon(1000.0)
    print(f"{varasto} lisäyksen jälkeen")


def negatiivinen_lisays(varasto):
    print(f"{varasto} ennen negatiivista lisäystä")
    print("Lisätään -666.0")
    varasto.lisaa_varastoon(-666.0)
    print(f"{varasto} lisäyksen jälkeen")


def suuri_poisto(varasto):
    print(f"{varasto} ennen suurta poistoa")
    print("Otetaan 1000.0")
    saatiin = varasto.ota_varastosta(1000.0)
    print(f"saatiin {saatiin}")
    print(f"{varasto} poiston jälkeen")


def negatiivinen_poisto(varasto):
    print(f"{varasto} ennen negatiivista poistoa")
    print("Otetaan -32.9")
    saatiin = varasto.ota_varastosta(-32.9)
    print(f"saatiin {saatiin}")
    print(f"{varasto} poiston jälkeen")


def main():
    mehua, olutta = init()
    olut_getters(olutta)
    mehu_setters(mehua)
    virheelliset()
    suuri_lisays(olutta)
    negatiivinen_lisays(mehua)
    suuri_poisto(olutta)
    negatiivinen_poisto(mehua)


if __name__ == "__main__":
    main()
