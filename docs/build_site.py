"""Build docs/index.html from docs/template.html + data/demo_examples.json.

    python docs/build_site.py
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
template = (ROOT / "docs/template.html").read_text(encoding="utf-8")
assert template.count("/*%%DATA%%*/") == 1, "template must hold exactly one data placeholder"
data = json.loads((ROOT / "data/demo_examples.json").read_text(encoding="utf-8"))
# "</" inside the JSON would close the <script> tag early
blob = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
(ROOT / "docs/index.html").write_text(template.replace("/*%%DATA%%*/", blob), encoding="utf-8", newline="\n")
print("wrote docs/index.html")
