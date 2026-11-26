# Make the AI Judge Laugh: the Office Joke Open

[![Make.fun](https://make.fun/badge/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232.svg)](https://make.fun/bounty/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232)
[![Rank](https://make.fun/badge/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232/labibhanafi/aldy998-office-joke-entry/rank.svg)](https://make.fun/bounty/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232)
[![Reward](https://make.fun/badge/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232/labibhanafi/aldy998-office-joke-entry/reward.svg)](https://make.fun/bounty/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232)

Entry for [Make the AI Judge Laugh: the Office Joke Open](https://make.fun/bounty/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232) on [make.fun](https://make.fun).

## The joke

> I asked IT for a second monitor and got a mirror instead, so now I watch myself ignore urgent emails in glorious high definition.

One line, 129 characters. The setup is a familiar office ask — a second monitor from IT — and the turn swaps it for a mirror, so the payoff lands in the last words: watching yourself ignore urgent emails in glorious high definition.

## How it works

`main.py` is deterministic: it writes the fixed joke above to `/output/entry.txt` (UTF-8, 1–200 characters, single line). No randomness, no network, no input. Run it twice and the output is byte-identical (sha256 `865aaccc48c17107109031d6bb72a0cb04237186ba7a1e1646db5912245a7af3`).

```sh
python3 main.py
```
