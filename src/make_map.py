"""Regenerate src/map.json (Equal Earth projection, 1000 px wide) from Natural Earth 1:110m countries.

    git clone --depth 1 --filter=blob:none --sparse https://github.com/nvkelso/natural-earth-vector ne
    (cd ne && git sparse-checkout set --no-cone /geojson/ne_110m_admin_0_countries.geojson)
    python3 src/make_map.py ne/geojson/ne_110m_admin_0_countries.geojson
"""
import json, math, pathlib, sys

A1, A2, A3, A4 = 1.340264, -0.081106, 0.000893, 0.003796
M = math.sqrt(3) / 2

def proj(lon, lat):
    l, p = math.radians(lon), math.radians(lat)
    t = math.asin(M * math.sin(p)); t2 = t * t; t6 = t2 ** 3
    return (l * math.cos(t) / (M * (A1 + 3 * A2 * t2 + t6 * (7 * A3 + 9 * A4 * t2))),
            t * (A1 + A2 * t2 + t6 * (A3 + A4 * t2)))

XMAX, YMAX = proj(180, 0)[0], proj(0, 90)[1]
S = 1000 / (2 * XMAX)

def P(lon, lat):
    x, y = proj(lon, lat)
    return (x + XMAX) * S, (YMAX - y) * S

CITIES = {"madrid": (-3.70, 40.42), "london": (-0.13, 51.51), "paris": (2.35, 48.86), "lisbon": (-9.14, 38.72),
          "kansas": (-94.58, 39.10), "brussels": (4.35, 50.85), "ghent": (3.72, 51.05),
          "amsterdam": (4.90, 52.37), "milan": (9.19, 45.46), "istanbul": (28.98, 41.01)}

g = json.load(open(sys.argv[1]))
paths = []
for f in g["features"]:
    iso = f["properties"]["ADM0_A3"]
    if iso == "ATA":
        continue
    geom = f["geometry"]
    polys = geom["coordinates"] if geom["type"] == "MultiPolygon" else [geom["coordinates"]]
    d = "".join("M" + "L".join(f"{x:.1f},{y:.1f}" for x, y in (P(*c) for c in ring)) + "Z" for poly in polys for ring in poly)
    paths.append((iso, d))
out = {"H": 2 * YMAX * S, "paths": paths, "cities": {k: P(*v) for k, v in CITIES.items()}}
(pathlib.Path(__file__).parent / "map.json").write_text(json.dumps(out))
print(len(paths), "countries")
