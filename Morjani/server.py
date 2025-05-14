from flask import Flask, request, jsonify


app = Flask(__name__)



db = {
    "case_in_vendita": [
        {"catastale": "A123", "indirizzo": "Via Roma", "numero_civico": "10", "piano": 1, "metri": 90, "vani": 4, "prezzo": 200000, "stato": "LIBERO", "filiale_proponente": "Filiale1"},
        {"catastale": "B456", "indirizzo": "Via Milano", "numero_civico": "15", "piano": 2, "metri": 80, "vani": 3, "prezzo": 250000, "stato": "LIBERO", "filiale_proponente": "Filiale2"}
    ],
    "case_in_affitto": [
        {"catastale": "C789", "indirizzo": "Via Napoli", "numero_civico": "20", "tipo_affitto": "TOTALE", "bagno_personale": True, "prezzo_mensile": 600, "filiale_proponente": "Filiale1"}
    ]
}


@app.route('/cerca_casa_vendita', methods=['POST'])

def cerca_casa_vendita():
    filtri = request.json.get('filtri', {})
    
    risultato = [casa for casa in db["case_in_vendita"]if (casa["stato"] == filtri.get("stato", casa["stato"]) and casa["prezzo"] <= filtri.get("prezzo_max", casa["prezzo"]))]
    return jsonify(risultato)


@app.route('/cerca_casa_affitto', methods=['POST'])

def cerca_casa_affitto():
    filtri = request.json.get('filtri', {})
    risultato = [casa for casa in db["case_in_affitto"] if (casa["tipo_affitto"] == filtri.get("tipo_affitto", casa["tipo_affitto"]) and casa["prezzo_mensile"] <= filtri.get("prezzo_max", casa["prezzo_mensile"]))]
    return jsonify(risultato)


@app.route('/venduta_casa', methods=['POST'])
def venduta_casa():
    data = request.json
    catastale = data.get("catastale")
    for casa in db["case_in_vendita"]:
        if casa["catastale"] == catastale:
            if casa["stato"] == "LIBERO":
                casa["stato"] = "VENDUTA"
                return jsonify({"message": f"Casa {catastale} segnata come venduta con successo."}), 200
            else:
                return jsonify({"error": f"Casa {catastale} non è disponibile per la vendita."}), 400
    return jsonify({"error": f"Casa con catastale {catastale} non trovata."}), 404

@app.route('/affittata_casa', methods=['POST'])
def affittata_casa():
    data = request.json
    catastale = data.get("catastale")
    for casa in db["case_in_affitto"]:
        if casa["catastale"] == catastale:
            casa["stato"] = "AFFITTATA"
            return jsonify({"message": f"Casa {catastale} segnata come affittata con successo."}), 200
    return jsonify({"error": f"Casa con catastale {catastale} non trovata."}), 404


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080)
