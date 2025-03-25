# Todo App

En enkel Todo-applikation byggd med Flask för kursen i Applikationsutveckling och Testning.

## Installation

1. Skapa en virtuell miljö:
```bash
python -m venv venv
```

2. Aktivera den virtuella miljön:
```bash
# På Windows:
venv\Scripts\activate
# På Unix/MacOS:
source venv/bin/activate
```

3. Installera beroenden:
```bash
pip install -r requirements.txt
```

## Kör applikationen

```bash
python src/app.py
```

Besök sedan `http://localhost:5000` i din webbläsare.

## Kör tester

```bash
pytest
```

För att se kodtäckning:
```bash
pytest --cov=src
```

## Funktioner

- Lägg till nya uppgifter
- Markera uppgifter som klara/ej klara
- Ta bort uppgifter
- Enhetstester för all funktionalitet
- Responsiv design 