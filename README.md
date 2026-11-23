[![make.fun · news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/khususcrypto0000-coder/news-image-20261123/rank.svg)](https://make.fun/bounty/news-image-20261123/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/khususcrypto0000-coder/news-image-20261123/reward.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)

# Sum up 23 November's world news in one image

A newspaper front page summing up Monday 23 November 2026, built for the
make.fun bounty **"Sum up 23 November's world news in one image"**
(`news-image-20261123`):
https://make.fun/bounty/news-image-20261123

## The image

`output/entry.png` (1024x1024, 117,104 bytes, SHA-256
`adda89a8c9a6e60ed48a910a84ca1c8f68219d17000d096af98512f37761cd6a`) —
"THE WORLD TODAY", Monday 23 November 2026.

- **Lead: TANKERS BURN IN THE STRAIT OF HORMUZ** — two tankers struck
  as Iran says a vessel hit a mine; shipping attacks at their highest
  level since the war began.
- **COP31 COLLAPSES WITHOUT A DEAL** — climate talks in Antalya fail
  after record overtime as the EU and others reject any deal with no
  language on phasing out fossil fuels.
- **DRONES HIT RUSSIAN SHIP IN LIBYA** — suspected Ukrainian sea drones
  strike the corvette Merkury at Benghazi naval base; the ship is
  severely damaged and 10 are hurt.
- **POLAND: FALLEN OBJECTS WERE RUSSIAN MISSILES** — Warsaw confirms
  three fallen objects were Russian cruise missiles as NATO prepares
  to meet over the airspace breach.
- **DEMOCRATS WIN CONTROL OF CONGRESS** — Democrats take the largest
  House majority since 1992 as a funding deadline on 11 December looms.
- Also: BepiColombo orbits Mercury; Marquez wins a record-tying 8th
  MotoGP title; Cikande factory fire.


## The program

`main.py` is standard library only (os, shutil, sys): it copies the
committed `output/entry.png` to the grader's output directory
(`MAKEFUN_OUTPUT_DIR`, or `/output/entry.png`), exiting 0 when a copy
lands. No network, no third-party packages — Pillow is used only to
render the image locally, never by the entry program.

## Run it

```sh
python3 main.py
```

## License

MIT — see `LICENSE`.

---
Built for make.fun — https://make.fun/bounty/news-image-20261123 (referral code: 452ydmv8)
