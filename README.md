# Childhood Memories — An Improv Session

A single-page slide deck for a Toastmasters variety session.

## The session

1. **Pick a paper** — each slip carries a single number. That is you for the session.
2. **Check the screen** — enter the headcount on the Pairings slide and it builds all
   three rounds. Everyone reads their partner off the table.
3. **Change every round** — your number stays put, your partner changes.

Pairings come from the round-robin circle method, so nobody draws the same partner
twice. Odd headcounts put one group of three in each round; they share an extra
minute. At 3 or 5 people a repeat is unavoidable and the page says so.

Each person shares for one minute. Every round draws a random topic, framed as
**the most memorable one** — the toy, the gift, the trouble that stuck with you —
and the goal is to tell the childhood story behind it.

**Improv tip:** use a story with *who, when, what, why*.

## Printing the slips

`pairing-slips.pdf` is ready to print: 40 numbered slips across two A4 pages, four
across and five down per sheet, with dashed cut lines. Hand them out as people
arrive and use only as many as you need — the numbers must run 1..N with no gaps.

To print a different count:

```
python3 make_slips.py 24 pairing-slips.pdf
```

It fills 20 slips per page and adds pages as needed. Needs `reportlab`.

## Running it

No build step. Open `index.html`, or:

```
npx serve .
```

## Controls

- Click anywhere, press `→` / `Space` to advance; `←` to go back
- Topic wheel draws at random from 16 topics
- Built-in one-minute speaking timer
