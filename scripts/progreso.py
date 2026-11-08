#!/usr/bin/env python3
"""Lee METAS.md, calcula los % ponderados y genera ESTADO.md.

Uso: python3 scripts/progreso.py   (desde la carpeta centro-de-mandos)
Sin dependencias externas.
"""
import re
import sys
from datetime import date
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
METAS = RAIZ / "METAS.md"
ESTADO = RAIZ / "ESTADO.md"

CABECERA = re.compile(
    r"^##\s*(M\d+)\s*·\s*(.+?)\s*·\s*peso\s*(\d+(?:[.,]\d+)?)\s*·\s*"
    r"(\d{4}-\d{2}-\d{2})\s*→\s*(\d{4}-\d{2}-\d{2})"
)


def num(txt):
    txt = txt.strip().replace("€", "").replace("kg", "").replace(",", ".").strip()
    if txt in ("", "?"):
        return None
    try:
        return float(txt)
    except ValueError:
        return None


def barra(p, ancho=10):
    llenos = round(p * ancho)
    return "▓" * llenos + "░" * (ancho - llenos)


def etiqueta(p):
    pct = round(p * 100)
    return f"hecho {pct} %" if pct < 50 else f"faltan {100 - pct} %"


def leer_metas(texto):
    metas, actual = [], None
    for linea in texto.splitlines():
        m = CABECERA.match(linea)
        if m:
            actual = {
                "id": m.group(1), "nombre": m.group(2), "peso": float(m.group(3).replace(",", ".")),
                "inicio": date.fromisoformat(m.group(4)), "fin": date.fromisoformat(m.group(5)),
                "subs": [],
            }
            metas.append(actual)
            continue
        if actual is None or not linea.startswith("|"):
            continue
        celdas = [c.strip() for c in linea.strip().strip("|").split("|")]
        if len(celdas) < 5 or celdas[0].lower() == "submeta" or set(celdas[0]) <= set("-: "):
            continue
        actual["subs"].append({
            "nombre": celdas[0], "peso": num(celdas[1]) or 1,
            "inicio": num(celdas[2]), "actual": num(celdas[3]), "objetivo": num(celdas[4]),
        })
    return metas


def calcular(meta, hoy):
    suma, pesos, faltan = 0.0, 0.0, []
    for s in meta["subs"]:
        i, a, o = s["inicio"], s["actual"], s["objetivo"]
        if None in (i, a, o) or o == i:
            faltan.append(s["nombre"])
            s["p"] = None
            continue
        p = max(0.0, min(1.0, (a - i) / (o - i)))
        s["p"] = p
        suma += p * s["peso"]
        pesos += s["peso"]
    meta["p"] = suma / pesos if pesos else None
    meta["faltan"] = faltan
    total = (meta["fin"] - meta["inicio"]).days
    pasado = (hoy - meta["inicio"]).days
    meta["esperado"] = max(0.0, min(1.0, pasado / total)) if total > 0 else 1.0
    meta["dias"] = max(0, (meta["fin"] - hoy).days)
    if meta["p"] is None:
        meta["sem"] = "⚪"
    else:
        dif = (meta["esperado"] - meta["p"]) * 100
        meta["sem"] = "🟢" if dif <= 0 else ("🟡" if dif <= 10 else "🔴")


def main():
    if not METAS.exists():
        sys.exit("No encuentro METAS.md")
    hoy = date.today()
    metas = leer_metas(METAS.read_text(encoding="utf-8"))
    for m in metas:
        calcular(m, hoy)

    validas = [m for m in metas if m["p"] is not None]
    global_p = (sum(m["p"] * m["peso"] for m in validas) / sum(m["peso"] for m in validas)) if validas else None

    out = [f"# ESTADO · {hoy.isoformat()}", "", "_Generado por scripts/progreso.py — no editar a mano._", ""]
    if global_p is not None:
        out += [f"**Global:** {barra(global_p)} {etiqueta(global_p)}", ""]
    out += ["| Meta | Progreso | Esperado hoy | Ritmo | Días restantes |", "|---|---|---|---|---|"]
    for m in metas:
        prog = f"{barra(m['p'])} {etiqueta(m['p'])}" if m["p"] is not None else "sin datos"
        out.append(f"| {m['id']} {m['nombre']} | {prog} | {round(m['esperado'] * 100)} % | {m['sem']} | {m['dias']} |")
    out.append("")
    for m in metas:
        out.append(f"## {m['id']} · {m['nombre']}")
        for s in m["subs"]:
            if s["p"] is None:
                out.append(f"- {s['nombre']}: ? (falta dato)")
            else:
                out.append(f"- {s['nombre']}: {barra(s['p'])} {etiqueta(s['p'])} (ahora {s['actual']:g} · meta {s['objetivo']:g})")
        out.append("")
    pendientes = [f"{m['id']} · {n}" for m in metas for n in m["faltan"]]
    if pendientes:
        out += ["## Datos que faltan", *[f"- {p}" for p in pendientes], ""]

    ESTADO.write_text("\n".join(out), encoding="utf-8")
    print("\n".join(out))


if __name__ == "__main__":
    main()
