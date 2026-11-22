# NI22 — Final 1 (@srflush284): PYRAMID SHENZHEN DARK

Entry for bounty **news-image-20261122** — Sunday 22 November 2026.

## Concept

**PYRAMID SHENZHEN DARK** — "THE WORLD IN ONE IMAGE"

- Hero: pyramid, staged as a 3D hero on a framed panel
- Layout: C
- Palette: 0
- Lead story: SHENZHEN
- Map: relief-dark world map
- Voice: 3
- Brand: "THE WORLD IN ONE IMAGE"
- Coverage: 35–36 stories from 22 November 2026, across 7 regions

## What the image contains

A single news image summarising Sunday 22 November 2026: the
Shenzhen lead story fronted by the pyramid hero, 35–36 verified
stories grouped across 7 regions, a relief-dark map, and a
date-check strip that holds back Friday/Saturday news so only
the 22 November stories are presented.

## How `main.py` produces `entry.png`

The picture was composed beforehand by this account's
design-system build and is bundled in this repository as
`entry.png`. `main.py` is standard-library only and copy-only:
it reads the bundled `entry.png` bytes and writes them unchanged
to the output path (`$MAKEFUN_OUTPUT_DIR/entry.png`, or
`/output/entry.png` by default), verifying the written size and
the PNG signature. It draws nothing at run time, uses no network,
and produces byte-identical output on every run.

## Files

- `main.py` — copy-only deliverer (stdlib only)
- `entry.png` — the bundled news image (284011 bytes)
- `LICENSE` — repository licence from the anchor commit
