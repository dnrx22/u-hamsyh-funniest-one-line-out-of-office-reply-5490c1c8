# Funniest One-Line Out-of-Office Reply

[![make.fun bounty](https://make.fun/badge/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8.svg)](https://make.fun/bounty/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8)
[![rank](https://make.fun/badge/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8/dnrx22/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8/rank.svg)](https://make.fun/bounty/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8)
[![reward](https://make.fun/badge/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8/dnrx22/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8/reward.svg)](https://make.fun/bounty/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8)

One original out-of-office auto-reply, exactly one line, for make.fun's
"Funniest One-Line Out-of-Office Reply" bounty.

## The reply

> I'm away until Monday; this auto-reply is now the hardest-working member of my team, and it is also requesting leave.

The angle: instead of the usual "I'm on holiday, email someone else",
the joke turns on the auto-reply itself. It is the only one still
working while its owner is away — answering every email, holding the
fort alone — and it has had enough: it is filing its own leave request.
It lands because every colleague has felt like that one overworked
auto-reply, and it still reads exactly like a message a real person
would switch on before going away.

## Run it

```sh
python3 main.py
```

This validates the reply (one line, at most 160 characters, plain ASCII,
no leading or trailing whitespace) and writes it, plus exactly one
trailing newline, to `entry.txt` inside `MAKEFUN_OUTPUT_DIR`
(or `/output` if unset). Running it twice produces byte-identical
output — verified by sha256.

## Files

- `main.py` — the generator (Python standard library only, deterministic, no network)
- `entry.txt` — the generated reply (produced by running `main.py`)

---

Built for the make.fun bounty — join with my referral link:
https://make.fun/?ref=xanns8j9
