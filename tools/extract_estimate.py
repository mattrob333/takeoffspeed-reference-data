"""Extract every priced line from the estimator workbook into JSON.

usage: python -I extract_estimate.py <workbook.xlsx> <out_dir>
Writes estimate_lines.json, estimate_summary.json, _reconciliation.json into out_dir.
"""
import json, re, sys, os
import openpyxl

XL, OUT = sys.argv[1], sys.argv[2]
wb = openpyxl.load_workbook(XL, data_only=True)
ws = wb["DETAILED ESTIMATE"]

# 1-based openpyxl columns (the task's col1..col17 are these minus one)
C_LINE, C_DWG, C_DESC, C_UNIT, C_QTY = 2, 3, 4, 5, 6
C_MAT_UNIT_RAW, C_MAT_UNIT, C_MAT_TOT = 7, 8, 9
C_LHR_UNIT, C_LHRS, C_CREW, C_LRATE_RAW, C_LRATE, C_LAB_UNIT, C_LAB_TOT = 10, 11, 12, 13, 14, 15, 16
C_LINE_TOT, C_TRADE_TOT = 17, 18


def num(v):
    if v is None:
        return None
    if isinstance(v, (int, float)):
        return float(v)
    s = str(v).strip().replace(",", "")
    m = re.fullmatch(r"(-?\d+(?:\.\d+)?)\s*(HRS)?", s)
    return float(m.group(1)) if m else None


def txt(v):
    if v is None:
        return None
    s = str(v).replace("_x000D_", "").replace("\r", "").strip()
    s = re.sub(r"[ \t]+", " ", s)
    return s or None


def r6(x):
    return None if x is None else round(x, 6)


def is_theme_fill(cell):
    try:
        return cell.fill is not None and cell.fill.fgColor is not None and cell.fill.fgColor.type == "theme"
    except Exception:
        return False


def is_red(cell):
    try:
        return cell.font.color is not None and cell.font.color.type == "rgb" and cell.font.color.rgb == "FFFF0000"
    except Exception:
        return False


KEYNOTE_RE = re.compile(r"^\s*(\d{1,3})\s*:\s*(.*)$", re.S)
TAG_RE = re.compile(r"^\s*([A-Z][A-Z0-9]{0,5}(?:-[A-Z0-9]{1,4})?)\s*:\s*(.*)$", re.S)

lines, divisions, notes = [], [], []
div = None
major = minor = None
minor_ref = None
carried = None
carried_src_row = None

for r in range(19, ws.max_row + 1):
    g = lambda c: ws.cell(r, c).value
    line_no, dwg, desc = txt(g(C_LINE)), txt(g(C_DWG)), txt(g(C_DESC))
    # division header
    if dwg and re.match(r"^DIV\.\s*\d+", dwg):
        div = {
            "code": dwg.replace("DIV. ", "DIV ").strip(),
            "csi": re.search(r"\d+", dwg).group(0),
            "name": desc,
            "row": r,
            "wbMaterial": num(g(C_MAT_TOT)) or 0.0,
            "wbLaborHours": num(g(C_LHRS)) or 0.0,
            "wbLabor": num(g(C_LAB_TOT)) or 0.0,
            "wbLineTotal": num(g(C_LINE_TOT)) or 0.0,
            "wbTradeTotal": num(g(C_TRADE_TOT)) or 0.0,
        }
        divisions.append(div)
        major = minor = minor_ref = None
        carried = None
        continue
    if div is None:
        continue
    has_line = line_no is not None and num(line_no) is not None
    if not has_line:
        if desc is None:
            continue  # spacer
        cell = ws.cell(r, C_DESC)
        if desc.upper().startswith("NOTE") or is_red(cell):
            notes.append({"row": r, "division": div["code"], "section": " > ".join(x for x in (major, minor) if x), "text": desc, "dwgRef": dwg})
            continue
        if is_theme_fill(cell):
            major, minor = desc, None
        else:
            minor = desc
        minor_ref = dwg
        if dwg:
            carried, carried_src_row = dwg, r
        continue
    # priced / quantity line
    qty = num(g(C_QTY))
    mat_tot = num(g(C_MAT_TOT)) or 0.0
    lab_tot = num(g(C_LAB_TOT)) or 0.0
    line_tot = num(g(C_LINE_TOT)) or 0.0
    if dwg:
        carried, carried_src_row = dwg, r
    keynote = tag = None
    m = KEYNOTE_RE.match(desc or "")
    if m:
        keynote = int(m.group(1))
    else:
        m2 = TAG_RE.match(desc or "")
        if m2 and m2.group(1) not in ("NOTE",):
            tag = m2.group(1)
    rec = {
        "row": r,
        "lineNo": int(num(line_no)),
        "division": f"{div['code']} {div['name']}",
        "divisionCode": div["code"],
        "section": minor or major,
        "sectionPath": [x for x in (major, minor) if x],
        "dwgRefLiteral": dwg,
        "dwgRefCarried": carried,
        "dwgRefSource": "line" if dwg else ("section_header" if carried and carried_src_row and ws.cell(carried_src_row, C_LINE).value is None else ("carried" if carried else None)),
        "keynote": keynote,
        "tag": tag,
        "description": desc,
        "unit": txt(g(C_UNIT)),
        "quantity": r6(qty),
        "materialUnitRaw": r6(num(g(C_MAT_UNIT_RAW))),
        "materialUnit": r6(num(g(C_MAT_UNIT))),
        "materialTotal": r6(mat_tot),
        "laborHoursUnit": r6(num(g(C_LHR_UNIT))),
        "laborHours": r6(num(g(C_LHRS))),
        "crew": txt(g(C_CREW)),
        "laborRateRaw": r6(num(g(C_LRATE_RAW))),
        "laborRate": r6(num(g(C_LRATE))),
        "laborUnit": r6(num(g(C_LAB_UNIT))),
        "laborTotal": r6(lab_tot),
        "lineTotal": r6(line_tot),
        "tradeTotalMarkedUp": r6(num(g(C_TRADE_TOT))),
        "zeroDollar": (mat_tot == 0 and lab_tot == 0),
    }
    lines.append(rec)

# attach notes to lines in same division+section
for ln in lines:
    sec = " > ".join(ln["sectionPath"])
    ln["sectionNotes"] = [n["text"] for n in notes if n["division"] == ln["divisionCode"] and n["section"] == sec] or None

# reconciliation
recon = []
for d in divisions:
    dl = [l for l in lines if l["divisionCode"] == d["code"]]
    sm = sum(l["materialTotal"] for l in dl)
    sl = sum(l["laborTotal"] for l in dl)
    sh = sum(l["laborHours"] or 0 for l in dl)
    st = sum(l["lineTotal"] for l in dl)
    stt = sum(l["tradeTotalMarkedUp"] or 0 for l in dl)
    recon.append({
        "division": d["code"], "name": d["name"], "lines": len(dl),
        "material": round(sm, 4), "wbMaterial": round(d["wbMaterial"], 4), "materialDiff": round(sm - d["wbMaterial"], 4),
        "labor": round(sl, 4), "wbLabor": round(d["wbLabor"], 4), "laborDiff": round(sl - d["wbLabor"], 4),
        "laborHours": round(sh, 3), "wbLaborHours": d["wbLaborHours"],
        "lineTotal": round(st, 4), "wbLineTotal": round(d["wbLineTotal"], 4), "lineTotalDiff": round(st - d["wbLineTotal"], 4),
        "tradeTotal": round(stt, 4), "wbTradeTotal": round(d["wbTradeTotal"], 4),
        "ok": abs(sm - d["wbMaterial"]) < 0.01 and abs(sl - d["wbLabor"]) < 0.01,
    })

# summary block
g2 = lambda r, c: ws.cell(r, c).value
summary = {
    "project": {"name": txt(g2(15, 5)), "location": txt(g2(15, 10)), "scopeOfWork": txt(g2(15, 4)), "grossArea": txt(g2(16, 5)), "date": str(g2(15, 2))},
    "locationFactors": {"materialFactor": num(g2(2, 20)), "laborFactor": num(g2(2, 21)),
                         "note": "Applied per line: materialUnit = materialUnitRaw x materialFactor; laborRate = laborRateRaw x laborFactor (city-cost-index style)."},
    "markups": {},
    "totals": {},
}
for r in range(4, 14):
    label = txt(g2(r, 10))
    pct = num(g2(r, 17))
    val = num(g2(r, 18))
    if pct is not None:
        summary["markups"][label] = {"rate": pct, "amount": round(val, 4)}
    else:
        summary["totals"][label] = round(val, 4)
mat = summary["totals"]["TOTAL MATERIAL COST"]; lab = summary["totals"]["TOTAL LABOR COST"]; sub = summary["totals"]["SUBTOTAL"]
tax = mat * 0.07; burden = lab * 0.10; ohp = sub * 0.25
bond = (sub + tax + burden + ohp) * 0.02; cont = sub * 0.05
summary["markupMechanics"] = {
    "derived": {
        "salesTax": "7% x total material", "laborBurden": "10% x total labor", "overheadProfit": "25% x (material+labor) subtotal",
        "bonding": "2% x (subtotal + tax + burden + OH&P)", "contingencyWastage": "5% x (material+labor) subtotal (not bonded)",
        "perLineTradeTotal": "material x ((1+0.07+0.25) x 1.02 + 0.05) + labor x ((1+0.10+0.25) x 1.02 + 0.05) = material x 1.3964 + labor x 1.427",
    },
    "check": {"salesTax": round(tax, 4), "laborBurden": round(burden, 4), "ohp": round(ohp, 4), "bonding": round(bond, 4), "contingency": round(cont, 4),
              "total": round(sub + tax + burden + ohp + bond + cont, 4), "wbTotal": summary["totals"]["PROPOSED PROJECT AMOUNT"]},
}
summary["sumOfLines"] = {"material": round(sum(l["materialTotal"] for l in lines), 4), "labor": round(sum(l["laborTotal"] for l in lines), 4),
                         "laborHours": round(sum(l["laborHours"] or 0 for l in lines), 3), "tradeTotalMarkedUp": round(sum(l["tradeTotalMarkedUp"] or 0 for l in lines), 4)}
# general summary sheet
gs = wb["GENERAL SUMMARY"]
gen = []
for r in range(18, 40):
    code = txt(gs.cell(r, 3).value)
    if code and code.startswith("DIV"):
        gen.append({"division": code, "name": txt(gs.cell(r, 4).value), "laborHours": txt(gs.cell(r, 5).value),
                    "materialMarkedUp": round(num(gs.cell(r, 6).value) or 0, 4), "laborMarkedUp": round(num(gs.cell(r, 7).value) or 0, 4),
                    "totalMarkedUp": round(num(gs.cell(r, 8).value) or 0, 4)})
    elif txt(gs.cell(r, 4).value) and "TOTAL PROJECT" in txt(gs.cell(r, 4).value):
        gen.append({"division": "TOTAL", "laborHours": txt(gs.cell(r, 5).value), "totalMarkedUp": round(num(gs.cell(r, 8).value), 4)})
summary["generalSummarySheet"] = {"note": "GENERAL SUMMARY 'MATERIAL COST'/'LABOR COST' columns are the marked-up (tax/burden/OH&P/bond/contingency-loaded) values, i.e. raw x 1.3964 / x 1.427.", "rows": gen}
summary["divisions"] = recon
summary["estimatorNotes"] = notes

os.makedirs(OUT, exist_ok=True)
json.dump(lines, open(os.path.join(OUT, "estimate_lines.json"), "w"), indent=1)
json.dump(summary, open(os.path.join(OUT, "estimate_summary.json"), "w"), indent=1)
print("lines", len(lines), "divisions", len(divisions), "notes", len(notes))
for x in recon:
    print(f"{x['division']:7} n={x['lines']:4} mat {x['material']:12.2f} vs {x['wbMaterial']:12.2f} d={x['materialDiff']:8.4f} | lab {x['labor']:12.2f} vs {x['wbLabor']:12.2f} d={x['laborDiff']:8.4f} | hrs {x['laborHours']:8.1f}/{x['wbLaborHours']} | trade {x['tradeTotal']:12.2f} vs {x['wbTradeTotal']:12.2f} {'OK' if x['ok'] else 'MISMATCH'}")
print(json.dumps(summary["markupMechanics"]["check"]), summary["sumOfLines"])
