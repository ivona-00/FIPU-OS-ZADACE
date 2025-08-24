from pony.orm import Database, Required, PrimaryKey, Optional, Set
from datetime import datetime

db = Database()

class Usluga(db.Entity):
    id_usluge = PrimaryKey(int, auto=True)
    naziv_usluge = Required(str)
    vrsta_usluge = Required(str)
    trajanje = Required(int)
    cijena = Required(int)
    rezervacije = Set("Rezervacija")

    def to_dict(self):
        return {
            "id_usluge": self.id_usluge,
            "naziv_usluge": self.naziv_usluge,
            "vrsta_usluge": self.vrsta_usluge,
            "trajanje": self.trajanje,
            "cijena": self.cijena
        }

class Rezervacija(db.Entity):
    id_rezervacije = PrimaryKey(int, auto=True)
    datum_termina = Required(datetime)
    vrijeme_termina = Required(datetime)
    prezime_osobe = Required(str)
    kontakt = Required(str)
    djelatnik = Required(str)
    napomena = Optional(str)
    usluga = Required(Usluga)

    def to_dict(self):
        return {
            "id_rezervacije": self.id_rezervacije,
            "datum_termina": self.datum_termina.isoformat(),
            "vrijeme_termina": self.vrijeme_termina.isoformat(),
            "prezime_osobe": self.prezime_osobe,
            "kontakt": self.kontakt,
            "djelatnik": self.djelatnik,
            "napomena": self.napomena,
            "usluga": self.usluga.to_dict()
        }