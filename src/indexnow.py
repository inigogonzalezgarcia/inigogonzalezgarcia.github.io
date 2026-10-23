"""Tell Bing (and the other IndexNow engines) which pages changed, right after the CI build.
The key is public by design: it lives in <key>.txt at the site root so the engines can verify it.
Usage: python src/indexnow.py --all            every URL in sitemap.xml
       python src/indexnow.py --since <sha>    pages (html) changed since that commit, if they are in the sitemap
       add --dry-run to print the list without sending."""
import json, pathlib, re, subprocess, sys, urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = "https://inigogonzalezgarcia.github.io"
ENDPOINT = "https://api.indexnow.org/indexnow"

def key():
    for f in ROOT.glob("*.txt"):
        if re.fullmatch(r"[0-9a-f]{32}", f.stem) and f.read_text().strip() == f.stem: return f.stem
    sys.exit("no IndexNow key file (<32 hex>.txt) at the site root")

def sitemap_urls():
    return set(re.findall(r"<loc>([^<]+)</loc>", (ROOT / "sitemap.xml").read_text()))

def changed_since(sha):
    out = subprocess.run(["git", "diff", "--name-only", f"{sha}..HEAD"], cwd=ROOT, capture_output=True, text=True, check=True).stdout.split()
    urls = set()
    for p in out:
        if not p.endswith(".html"): continue
        u = SITE + "/" + p
        urls.add(SITE + "/" if p == "index.html" else u[:-len("index.html")] if u.endswith("/index.html") else u)
    return urls

def main(argv):
    dry = "--dry-run" in argv
    sm = sitemap_urls()
    if "--all" in argv: urls = sm
    elif "--since" in argv: urls = changed_since(argv[argv.index("--since") + 1]) & sm
    else: sys.exit(__doc__)
    urls = sorted(urls)
    print(f"{len(urls)} URL(s) to submit" + (" (dry run)" if dry else ""))
    for u in urls: print(" ", u)
    if not urls or dry: return
    k = key()
    body = json.dumps({"host": SITE.split("//")[1], "key": k, "keyLocation": f"{SITE}/{k}.txt", "urlList": urls}).encode()
    req = urllib.request.Request(ENDPOINT, data=body, headers={"Content-Type": "application/json; charset=utf-8"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r: print("IndexNow:", r.status, r.reason)
    except urllib.error.HTTPError as e:
        sys.exit(f"IndexNow error {e.code}: {e.read().decode()[:300]}")

if __name__ == "__main__": main(sys.argv[1:])
