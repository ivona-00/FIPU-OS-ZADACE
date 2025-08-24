from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import FileResponse
from pydantic import BaseModel
from pony.orm import db_session, desc
from datetime import datetime
from models import db, Usluga, Rezervacija
import os

app = FastAPI(title="Salon Magnolya API")

# --- Baza ---
db.bind(provider="sqlite", filename="database.sqlite", create_db=True)
db.generate_mapping(create_tables=True)

# --- Serviranje HTML na root ---
@app.get("/")
def root():
    return FileResponse(os.path.join(os.path.dirname(__file__), "index.html"))

# --- Pydantic modeli ---
class UslugaIn(BaseModel):
    naziv_usluge: str
    vrsta_usluge: str
    trajanje: int
    cijena: int

class RezervacijaIn(BaseModel):
    id_usluge: int
    prezime_osobe: str
    kontakt: str
    datum_termina: str
    vrijeme_termina: str
    djelatnik: str
    napomena: str | None = None

# --- API endpoints ---
# USLUGE
@app.get("/usluge")
@db_session
def get_usluge():
    return [u.to_dict() for u in Usluga.select()]

@app.post("/usluge")
@db_session
def create_usluga(data: UslugaIn):
    u = Usluga(
        naziv_usluge=data.naziv_usluge,
        vrsta_usluge=data.vrsta_usluge,
        trajanje=data.trajanje,
        cijena=data.cijena
    )
    return u.to_dict()

@app.delete("/usluge/{id_usluge}")
@db_session
def delete_usluga(id_usluge: int):
    u = Usluga.get(id_usluge=id_usluge)
    if not u:
        raise HTTPException(status_code=404, detail="Usluga ne postoji")
    u.delete()
    return {"status": "ok", "message": f"Usluga {id_usluge} obrisana"}

@app.delete("/usluge")
@db_session
def delete_all_usluge():
    Usluga.select().delete(bulk=True)
    return {"status": "ok", "message": "Sve usluge obrisane"}

# REZERVACIJE
@app.get("/rezervacije")
@db_session
def get_rezervacije():
    return [r.to_dict() for r in Rezervacija.select()]

# GET rezervacije sortirano po datumima
@app.get("/rezervacije/sortirane")
@db_session
def get_rezervacije_sortirano(descending: bool = Query(False, description="True = silazno, False = uzlazno")):
    q = Rezervacija.select()
    if descending:
        q = q.order_by(lambda r: desc(r.datum_termina))
    else:
        q = q.order_by(Rezervacija.datum_termina)
    return [r.to_dict() for r in q]

@app.post("/rezervacije")
@db_session
def create_rezervacija(data: RezervacijaIn):
    usluga = Usluga.get(id_usluge=data.id_usluge)
    if not usluga:
        raise HTTPException(status_code=404, detail="Usluga ne postoji")
    rez = Rezervacija(
        datum_termina=datetime.fromisoformat(data.datum_termina),
        vrijeme_termina=datetime.fromisoformat(data.datum_termina + "T" + data.vrijeme_termina),
        prezime_osobe=data.prezime_osobe,
        kontakt=data.kontakt,
        djelatnik=data.djelatnik,
        napomena=data.napomena,
        usluga=usluga
    )
    return rez.to_dict()

@app.delete("/rezervacije/{id_rezervacije}")
@db_session
def delete_rezervacija(id_rezervacije: int):
    r = Rezervacija.get(id_rezervacije=id_rezervacije)
    if not r:
        raise HTTPException(status_code=404, detail="Rezervacija ne postoji")
    r.delete()
    return {"status": "ok", "message": f"Rezervacija {id_rezervacije} obrisana"}

@app.delete("/rezervacije")
@db_session
def delete_all_rezervacije():
    Rezervacija.select().delete(bulk=True)
    return {"status": "ok", "message": "Sve rezervacije obrisane"}
