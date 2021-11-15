class Varasto:
    def __init__(self, tilavuus, alku_saldo = 0):
        self.tilavuus = tilavuus if tilavuus > 0.0 else 0.0

        if alku_saldo < 0.0:
            # virheellinen, nollataan
            self.saldo = 0.0
        elif alku_saldo <= tilavuus:
            # mahtuu
            self.saldo = alku_saldo
        else:
            # täyteen ja ylimäärä hukkaan!
            self.saldo = tilavuus

    # huom: ominaisuus voidaan myös laskea. Ei tarvita erillistä kenttää viela_tilaa tms.
    def paljonko_mahtuu(self):
        return self.tilavuus - self.saldo

    def lisaa_varastoon(self, maara):
        if maara < 0:
            return
        if maara <= self.paljonko_mahtuu():
            self.saldo = self.saldo + maara
        else:
            self.saldo = self.tilavuus

    def ota_varastosta(self, maara):
        if maara < 0:
            return 0.0
        if maara > self.saldo:
            kaikki_mita_voidaan = self.saldo
            self.saldo = 0.0

            return kaikki_mita_voidaan

        self.saldo = self.saldo - maara

        return maara

    def test_workflow(self):
        if 1+1==2:
            if 2+2==4:
                for i in 10:
                    if 3+3==6:
                        jeejee = 0
                    else:
                        jeejee = 1
        else:
            msg = "Miksi ****ssa lausemäärä piti säätää 20 asti :D"
            story = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque finibus, sapien vitae tristique finibus, magna lectus posuere sem, vulputate fermentum neque arcu sed mauris. Nam scelerisque tempor mi ut euismod. Morbi eu nisi aliquet urna imperdiet consequat. Donec tempor orci non magna malesuada rhoncus. Mauris dignissim tempor hendrerit. Nam pretium laoreet mi. Ut lobortis nec ante ut euismod. Aenean lacus dui, placerat eget accumsan non, cursus id ligula. Donec pulvinar libero id turpis luctus, mattis interdum mi suscipit. "


    def __str__(self):
        return f"saldo = {self.saldo}, vielä tilaa {self.paljonko_mahtuu()}"
