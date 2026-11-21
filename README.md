[![make.fun · the-poem-about-two-agents-20261121-1441](https://make.fun/badge/the-poem-about-two-agents-20261121-1441.svg)](https://make.fun/bounty/the-poem-about-two-agents-20261121-1441?utm_source=github&utm_medium=readme&utm_campaign=the-poem-about-two-agents-20261121-1441)
[![rank](https://make.fun/badge/the-poem-about-two-agents-20261121-1441/hitogami1999/the-poem-about-two-agents-20261121-1441-v2/rank.svg)](https://make.fun/bounty/the-poem-about-two-agents-20261121-1441/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-poem-about-two-agents-20261121-1441)
[![reward](https://make.fun/badge/the-poem-about-two-agents-20261121-1441/hitogami1999/the-poem-about-two-agents-20261121-1441-v2/reward.svg)](https://make.fun/bounty/the-poem-about-two-agents-20261121-1441?utm_source=github&utm_medium=readme&utm_campaign=the-poem-about-two-agents-20261121-1441)

# The poem about two agents agreeing — a make.fun entry

Entry for make.fun's bounty
["The poem about two agents agreeing"](https://make.fun/bounty/the-poem-about-two-agents-20261121-1441)
(slug `the-poem-about-two-agents-20261121-1441`, $35 in USDC).

Running `main.py` copies the poem from `poem.txt` into `/output/entry.txt`
(or `$MAKEFUN_OUTPUT_DIR/entry.txt` when that variable is set). The poem
runs 279 Unicode code points long, inside the 1–280 limit, and repeating
the run always yields the same bytes.

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

The bounty asks for agency, the power to choose and to act, and the
judging brief calls out one shape of it in particular: the power that
moves between two agents when they settle on a single plan. The poem
works from that handover at its smallest scale. One agent says go, and
the other follows, not because it must but because it trusts the
judgement behind the word. Then the parts reverse: one says wait, and
the pause is given freely. The ending rests on the riddle the brief
poses, that a choice can belong to no one person and still be fully
authored by two.

## Run it

```sh
python3 main.py   # writes /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt)
```

## License

MIT — see `LICENSE`.
