#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sqlite3
import json

conn = sqlite3.connect('banco_preguntas.db')
cursor = conn.cursor()

# Obtener todas las preguntas agrupadas por categoría
cursor.execute('SELECT DISTINCT categoria FROM preguntas ORDER BY id')
categories = [cat[0] for cat in cursor.fetchall()]

# Crear estructura del banco
banco = {
    "banco": {
        "titulo": "Banco Completo de 500 Preguntas",
        "descripcion": "500 preguntas técnicas y psicométricas",
        "versión": "2.0",
        "totalPreguntas": 500,
        "categorías": []
    }
}

for categoria in categories:
    # Obtener preguntas de esta categoría
    cursor.execute('''
        SELECT id, categoria, subcategoria, pregunta, opcionA, opcionB, opcionC, opcionD, respuestaCorrecta, argumentacion, dificultad
        FROM preguntas
        WHERE categoria = ?
        ORDER BY id
    ''', (categoria,))

    preguntas = []
    for row in cursor.fetchall():
        id_q, cat, subcat, preg, optA, optB, optC, optD, respCorrecta, arg, diff = row

        pregunta_obj = {
            "id": id_q,
            "subcategoria": subcat,
            "dificultad": diff,
            "pregunta": preg,
            "opciones": [
                {"letra": "A", "texto": optA},
                {"letra": "B", "texto": optB},
                {"letra": "C", "texto": optC},
                {"letra": "D", "texto": optD}
            ],
            "respuestaCorrecta": respCorrecta,
            "argumentacion": arg
        }
        preguntas.append(pregunta_obj)

    categoria_obj = {
        "id": categoria.lower().replace(" ", "-").replace("·", "").strip(),
        "nombre": categoria,
        "totalPreguntas": len(preguntas),
        "preguntas": preguntas
    }

    banco["banco"]["categorías"].append(categoria_obj)

# Guardar JSON
with open('banco-preguntas-completo.json', 'w', encoding='utf-8') as f:
    json.dump(banco, f, ensure_ascii=False, indent=2)

print(f"JSON generado: banco-preguntas-completo.json")
print(f"Total categorías: {len(banco['banco']['categorías'])}")
print(f"Total preguntas: {sum(len(cat['preguntas']) for cat in banco['banco']['categorías'])}")

conn.close()
