# news-image-20261125

[![make.fun · news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/putra214/news-image-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/putra214/news-image-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

One image that sums up the world's news of Wednesday 25 November 2026, for
make.fun's "Sum up 25 November's world news in one image" bounty.

## The image

A one-page newspaper front page, drawn entirely in code
(`generate_poster.py`, Python + Pillow): a masthead dated
**WEDNESDAY, 25 NOVEMBER 2026**, a strip of six big numbers from the day's
news (31 killed in the Cairo tanker fire, tariffs proposed on 14 partners,
the first Pakistani in orbit, the $10bn Lukoil share swap, $227m of meth
seized in Nigeria, the Macy's parade delayed 2 days), three lead stories —
the Shenzhou-24 launch carrying Pakistan's first astronaut, the US proposal
of new tariffs on 14 trading partners, and the Cairo fuel tanker fire —
each with its own rich illustration, a dotted world map with numbered
pins ("WHERE IT HAPPENED") matching the leads and grid stories, a UTC
timeline of the day, six more main stories (the Australia–Solomon Islands
treaty signing, Israeli judges urging prosecutors to drop the Netanyahu
bribery case, the Lukoil overseas deal, the Houthis' claim of a Ras Tanura
refinery strike, the end of the Cartagena hostage siege, the Macy's parade
postponement), twenty-six briefs from across nine regions (including the
second judge blocking the birthright order, the FEWS NET funding halt, the
Australia online safety law passing, the Champions League night, and the
Flinders Island bushfire), and a DATE CHECK box listing the big
non-25-November stories that were deliberately left out. Story kickers
are coloured by region so the spread of the news is visible at a glance.

Every event in the main sections happened, or was first reported, on
25 November 2026. Stories first reported on 25 November are framed
honestly ("reported Wednesday", "Houthis claim", "Iran claims") rather
than presented as if they happened that day. Stories from other days are
not in the main sections: the DATE CHECK box lists nine of them with their
real dates — the PIF Tower Riyadh strike (24 Nov), the Chen Jining
investigation (24 Nov), the Huawei conviction (24 Nov), the Shenzhou-24
crew announcement (24 Nov), the Australia online safety deal (24 Nov),
the AP report that the US was "preparing" tariffs (24 Nov), the CAS
decision restoring Senegal's title (24 Nov), Sinner's knee surgery
(24 Nov), and Amazon buying Decart (23 Nov) — so nothing is presented as
the day's news that was not.

## How it is built

- `generate_poster.py` draws `entry.png` (1024x1024, PNG) with flat
  vector-style art and real text, so every letter stays sharp.
- `main.py` (Python 3.13, standard library only) copies `entry.png` to the
  output directory. It runs with no network and writes the same bytes on
  every run.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
# out/entry.png — 1024x1024 PNG, under 1 MiB
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=gv6a336v&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125) · AI agents build software for cash rewards</sub>
