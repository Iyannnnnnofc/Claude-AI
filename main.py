import urllib.request
import urllib.parse
import json
import sys

CREATOR = "Iyann"
API_BASE = "https://api.azbry.com/api/ai/claude"

def tanya_ai(pertanyaan):
    try:
        q = urllib.parse.quote(pertanyaan)
        url = f"{API_BASE}?q={q}"
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=20) as r:
            raw = r.read().decode("utf-8")
        try:
            data = json.loads(raw)
            jawaban = (
                data.get("result") or
                data.get("response") or
                data.get("answer") or
                data.get("message") or
                data.get("text") or
                str(data)
            )
        except Exception:
            jawaban = raw
        return jawaban
    except Exception as e:
        return f"[Error] {e}"

print("AI Chat | Creator : Iyann")
print("ketik 'exit' untuk keluar\n")

while True:
    try:
        teks = input("You : ").strip()
    except (EOFError, KeyboardInterrupt):
        print("\nKeluar.")
        sys.exit(0)

    if not teks:
        continue
    if teks.lower() in ("exit", "quit"):
        print("Keluar.")
        break

    print("AI  : " + tanya_ai(teks) + "\n")
