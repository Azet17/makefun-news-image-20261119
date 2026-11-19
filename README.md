# The World Today — 19 November 2026

[![make.fun](https://make.fun/bounty/news-image-20261119)](https://make.fun/bounty/news-image-20261119)

Entry for the [make.fun news-image-20261119](https://make.fun/bounty/news-image-20261119)
bounty: "Sum up 19 November's world news in one image" ($250 prizes, top 50).

## What it is

A newspaper front page, drawn from scratch with Pillow (`draw.py`), that
sums up Thursday 19 November 2026 in six stories:

1. **Culture / Gaming — GTA VI launches.** After 13 years, Grand Theft
   Auto VI unlocks at midnight around the world, starting in New Zealand.
   (Reuters, AP)
2. **Politics / USA — Jeffries nominated for Speaker.** House Democrats
   pick Hakeem Jeffries 251–11, putting him on course to be the first
   Black Speaker of the House. (NPR, Washington Post)
3. **Weather / India — Cyclone Akvan nears India.** A severe cyclonic
   storm in the Bay of Bengal heads for the Andhra–Odisha coast; red
   alerts issued and schools shut. (India Meteorological Department,
   The Hindu)
4. **Europe / Ukraine — EU plans a €45bn loan for Ukraine.** Brussels
   proposes a €45 billion loan to fund Kyiv next year, to be repaid once
   Russia pays reparations. (Financial Times)
5. **Science / Space — Voyager 1, one light-day away.** NASA's 1977
   probe reaches one light-day from Earth — about 26 billion km — after
   49 years in space. (NASA)
6. **Conflict / The Gulf — US and Iran trade fire.** The US strikes a
   missile site on Qeshm Island; Iran hits US bases in Bahrain and
   Kuwait. (multiple wires, 19 Nov round-ups)

Every story was first reported on 19 November 2026. The masthead names
the day prominently: **THURSDAY 19 NOVEMBER 2026**.

## How it runs

The grader runs Python 3.13 with no Pillow and no network, so the
entrypoint is standard library only: it copies the pre-rendered
`entry.png` shipped in this repo to the output directory and verifies
the copy with sha256.

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`draw.py` re-renders `entry.png` (1024×1024, ≤ 1 MiB) on a machine with
Pillow installed. All pictograms are simple geometric shapes drawn in
code — no photos, no AI images, no copied artwork.

## License

MIT — see [LICENSE](LICENSE).
