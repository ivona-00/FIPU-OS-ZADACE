Magnolya je aplikacija koja omogucava vođenje rezervacija u beauty salonu

Glavna ideja je omogućiti korisniku upravljanje rezervacijama i uslugama unutar njihovog salona. Brisanje, sortiranje, dodavanje i pregled rezervacija omogucuje efikasnost rada u salonu i preglednost. Mnogo salona jos uvijek se oslanja na rokovnike, a ovo bi im omogucilo brze rezerviranje .

Upute za pokretanje u powershellu 
-prebaci se u folder gdje se nalazi app.py i dockerfile (root folder web servisa) koristeci cd naredbu, u mojem slucaju to je: cd "C:\Users\iwona\OneDrive\Radna povrsina\IS\magnolya_salon"
-buildaj koristeci build naredbu, -t zastavicu da se pronade folder magnolya_salon i . za direktorij gdje je dockerfile
    ->build -t  magnolya_salon .
    -t zastavica da se pronade folder magnolya_salon tag 
    -. za direktorij gdje je dockerfile
-Pokretanje applikacije koristeci run i zastavice
    ->docker run -d -p 8000:8000 --name salon-app magnolya_salon
    -d: radi u pozadini
    -p 8000:8000: mapiranje porta 8000 iz containera na lokalni port 8000.
    --name salon-app : naziv containera
    -magnolya_salon: naziv Docker image-a koji se koristi.
-Ucitaj na browseru
    -samo zaljepi http://127.0.0.1:8000 za frontend
    -Za swagger interface : http://127.0.0.1:8000/docs
