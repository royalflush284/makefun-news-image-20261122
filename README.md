# THE TELEGRAPH ROOM — NI22 Wave 7 · Final 1 (@srflush284)

Bounty: `news-image-20261122` (make.fun) · Final 1

## Gelombang 7 — bangun baru dari pool segar 22 November 2026
Halaman koran satu gambar "THE TELEGRAPH ROOM — Wired Sunday, In Print":
hitam/merah klasik di atas gading, Layout A (3 lead: Ukraina, Iran, COP31),
36 cerita (15 kartu + 21 brief) dari pool terverifikasi Minggu 22 November 2026
(bedah Top 1 G7 §4). Perbaikan kritis vs G6: semua font dikali ±1,45
(headline lead 74, mini 60, deck 43, brief 35 pada W=3900) supaya headline kartu
terbaca pada 300px; DATE CHECK berisi 9 buangan bernama + bertanggal (19-21 Nov);
peta dotted kontras tinggi berpin bernomor = nomor kartu + legenda dua klausa.

## Entry
- Dimensi: **1024 × 1024 px** (lolos gate server)
- Ukuran: **233.203 byte**
- sha256: **a1330ff6f6bdd42ba6e6beff284dfdce2f660a70fead37ac057a7a57a10a0118**
- Pemenang duel: **varian B (40/40)** — layout alternatif (1 lead lebar + 2 lead),
  palet sama, terang
- `main.py` — carrier stdlib-only: verifikasi signature PNG + dimensi IHDR,
  MENOLAK gambar yang melanggar gate 1024×1024, salin byte-for-byte ke
  `MAKEFUN_OUTPUT_DIR` (fallback /output), verifikasi salinan identik.
- Margin: **13/13 LOLOS** (`margin_check.py --fresh ni22-fresh-g7.txt`)
- Isi: 15 kartu + 21 brief = **36 cerita**, 7 region, strip angka hari ini
  (186/161/35%/$120bn/720/9/50), strip region, timeline UTC 6 slot, tag
  sumber + kepastian di 15/15 kartu, peta dunia titik-titik berpin,
  panel ALSO ON bernomor 16-36, dan kotak DATE CHECK.

## Catatan repo
Repo GitHub akun ini (royalflush284) masih berisi commit lama G1 — itu urusan
koordinator saat push; paket di sini (compose.py, entry.png, main.py, README.md)
adalah paket G7 yang baru dan berdiri sendiri.
