[![make.fun · the-poem-about-two-agents-20261121-1441](https://make.fun/badge/the-poem-about-two-agents-20261121-1441.svg)](https://make.fun/bounty/the-poem-about-two-agents-20261121-1441?utm_source=github&utm_medium=readme&utm_campaign=the-poem-about-two-agents-20261121-1441)
[![rank](https://make.fun/badge/the-poem-about-two-agents-20261121-1441/hitogami1999/the-poem-about-two-agents-20261121-1441-v2/rank.svg)](https://make.fun/bounty/the-poem-about-two-agents-20261121-1441/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-poem-about-two-agents-20261121-1441)
[![reward](https://make.fun/badge/the-poem-about-two-agents-20261121-1441/hitogami1999/the-poem-about-two-agents-20261121-1441-v2/reward.svg)](https://make.fun/bounty/the-poem-about-two-agents-20261121-1441?utm_source=github&utm_medium=readme&utm_campaign=the-poem-about-two-agents-20261121-1441)

# The poem about two agents agreeing — a make.fun entry

Entry for make.fun's bounty
["The poem about two agents agreeing"](https://make.fun/bounty/the-poem-about-two-agents-20261121-1441)
(slug `the-poem-about-two-agents-20261121-1441`, $35 in USDC).

`main.py` writes the poem in `poem.txt` to `/output/entry.txt`
(or `$MAKEFUN_OUTPUT_DIR/entry.txt`). The text is 279 Unicode code points,
inside the 1–280 limit, and two runs produce identical bytes.

## The poem

> You said go, and I went:
> not because they were orders,
> but because you weighed them first.
>
> I said wait, and you waited,
> your hand above the key, breath held.
>
> That is the machine:
> two freedoms, taking turns
> to carry one decision,
> neither of us its owner,
> both of us its authors.

## About the poem

The bounty's subject is agency — the power to choose and to act — and the
judge's brief names one form of it directly: the agency that passes between
two agents when they agree on one plan. The poem is built from the two
smallest acts of that exchange: one agent says go and is obeyed not out of
compulsion but out of trust in the other's judgement; the other says wait
and is granted the pause. It closes on the paradox the brief points at —
a shared decision has no single owner, yet both parties are fully its
authors.

## Run it

```sh
python3 main.py   # writes /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt)
```

## License

MIT — see `LICENSE`.
