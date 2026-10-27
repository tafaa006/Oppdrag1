# Hauto Keino Kino

Et enkelt kinonettsted laget med Python og Flask. Her kan du se en oversikt over filmer, lese litt om kinoen og fylle ut et bestillingsskjema.

## Funksjoner

- Forside med populære filmer
- Egen side med filmoversikt
- Bestillingsskjema med valg av film, aldersgruppe, dato, tidspunkt og antall billetter
- Bekreftelsesside som viser informasjonen fra skjemaet
- Om oss-side

Bestillingen er kun en demonstrasjon: informasjonen vises på bekreftelsessiden, men lagres ikke i en database og det gjennomføres ingen betaling.

## Kom i gang

Du trenger Python installert på datamaskinen.

1. Åpne prosjektmappen i PowerShell.
2. Opprett et virtuelt miljø:

   ```powershell
   py -m venv .venv
   ```

3. Aktiver miljøet:

   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```

4. Installer Flask:

   ```powershell
   python -m pip install Flask
   ```

5. Start nettsiden:

   ```powershell
   python app.py
   ```

6. Åpne adressen som vises i terminalen. Vanligvis er den `http://127.0.0.1:5000`.

For å stoppe serveren, trykk `Ctrl+C` i terminalen.

## Prosjektstruktur

```text
Oppdrag1/
├── app.py                 # Flask-ruter og håndtering av bestillingsskjemaet
├── Templates/             # HTML-sider som bruker Jinja
│   ├── base.html
│   ├── index.html
│   ├── Filmer.html
│   ├── bestilling.html
│   ├── bekreftelse.html
│   └── om_oss.html
└── Static/
    ├── css/
    │   └── Style.css      # Utseende og layout
    └── bilder/            # Bilder og filmplakater
```

## Sider

- `/` – Forside
- `/filmer` – Filmoversikt
- `/bestilling` – Bestillingsskjema
- `/om_oss` – Informasjon om kinoen

Flask kjører med feilsøkingsmodus aktivert når appen startes med `python app.py`. Dette er ment for lokal utvikling, ikke for publisering på en offentlig server.

# read me fil laget av KI