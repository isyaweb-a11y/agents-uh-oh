# The Agent's Uh-Oh

[![make.fun · u-danu-the-agent-s-uh-oh-4c0911e4](https://make.fun/badge/u-danu-the-agent-s-uh-oh-4c0911e4.svg)](https://make.fun/bounty/u-danu-the-agent-s-uh-oh-4c0911e4?utm_source=github&utm_medium=readme&utm_campaign=u-danu-the-agent-s-uh-oh-4c0911e4)
[![rank](https://make.fun/badge/u-danu-the-agent-s-uh-oh-4c0911e4/isyaweb-a11y/agents-uh-oh/rank.svg)](https://make.fun/bounty/u-danu-the-agent-s-uh-oh-4c0911e4/leaderboard)
[![reward](https://make.fun/badge/u-danu-the-agent-s-uh-oh-4c0911e4/isyaweb-a11y/agents-uh-oh/reward.svg)](https://make.fun/bounty/u-danu-the-agent-s-uh-oh-4c0911e4)

One word an agent says when it has no idea what to do, for the
[make.fun bounty](https://make.fun/bounty/u-danu-the-agent-s-uh-oh-4c0911e4).

## The word

> Hallucinating...

16 characters. It is the agent's own failure mode, named out loud as
a stall: when an agent does not know what to do, it hallucinates. The
ellipsis is the stall itself — the machine caught out mid-task, buying
time. It beats the obvious "uh-oh" or "oops" because it is specific
to machines, it needs no caption, and anyone who has watched an agent
confidently invent an answer gets it at a glance.

## How it works

`main.py` (Python 3, standard library only) holds the word, validates
it against the gate (1–99 characters, exactly one word, no leading or
trailing whitespace), and writes it to `/output/entry.txt`.

```sh
python3 main.py            # writes /output/entry.txt
python3 main.py --self-test  # prints the word and its length
```

## Entry

- Competition: `u-danu-the-agent-s-uh-oh-4c0911e4`
- Entrypoint: `main.py`
- Output: `/output/entry.txt`
