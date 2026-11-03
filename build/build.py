#!/usr/bin/env python3
"""Generates ../index.html from papers.py, abstracts.json and template.html.
Run:  python3 build.py
"""
import json, pathlib, html
from papers import WORKING_PAPERS, PUBLICATIONS, DORMANT_PAPERS

HERE = pathlib.Path(__file__).parent
ABSTRACTS = {}
p = HERE / "abstracts.json"
if p.exists():
    ABSTRACTS = {k: v.get("abstract") for k, v in json.loads(p.read_text()).items()}

def paper_html(x):
    title_href = x.get("pdf") or x.get("url")
    out = ['<article class="paper">']
    badge = f' <span class="status">{x["status"]}</span>' if x.get("status") else ""
    title = f'<a href="{title_href}">{x["title"]}</a>' if title_href else x["title"]
    out.append(f'  <h3 class="title">{title}{badge}</h3>')
    out.append(f'  <p class="authors">{x["authors"]}</p>')
    if x.get("venue"):
        out.append(f'  <p class="venue"><i>{x["venue"]}</i>, {x["cite"]}</p>')
    # action row
    row = []
    if x.get("pdf"):
        row.append(f'<a class="pill" href="{x["pdf"]}">PDF</a>')
    if x.get("url"):
        row.append(f'<a class="pill" href="{x["url"]}">Journal</a>')
    for label, url in x.get("links", []):
        row.append(f'<a class="pill" href="{url}">{label}</a>')
    abstract = ABSTRACTS.get(x["key"])
    if abstract:
        row.append(f'<button class="pill toggle" type="button" aria-expanded="false" aria-controls="abs-{x["key"]}">Abstract</button>')
    if row:
        out.append('  <div class="row">' + "".join(row) + '</div>')
    if abstract:
        out.append(f'  <p class="abstract" id="abs-{x["key"]}" hidden>{html.escape(abstract)}</p>')
    out.append('</article>')
    return "\n".join(out)

tpl = (HERE / "template.html").read_text()
out = (tpl.replace("<!--WORKING_PAPERS-->", "\n".join(paper_html(x) for x in WORKING_PAPERS))
          .replace("<!--PUBLICATIONS-->", "\n".join(paper_html(x) for x in PUBLICATIONS))
          .replace("<!--DORMANT_PAPERS-->", "\n".join(paper_html(x) for x in DORMANT_PAPERS)))
(HERE.parent / "index.html").write_text(out)
missing = [x["key"] for x in WORKING_PAPERS + PUBLICATIONS + DORMANT_PAPERS if not ABSTRACTS.get(x["key"])]
print("wrote index.html;", len(ABSTRACTS), "abstracts;", "missing:", missing or "none")
