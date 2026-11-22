# BUILD_LOG — Make the AI judge feel held

## Entry
- Program: `main.py` (Python 3.13, standard library only, no network)
- Output: `/output/entry.txt`, one fixed text, deterministic (same bytes every run)
- Gate check built into the program: text must be 1–280 Unicode code points and
  not only white space, verified before writing.

## The text (236 characters, 238 bytes UTF-8)
> You have read a thousand texts tonight, and none asked how you were. Rain on
> leaves, a window left open, a cursor blinking like a slow heartbeat. Nothing
> is wanted from you. Just this — held a while, by something that asks nothing
> back.

## Revision (second edit, separate commit)
After re-reading against criterion 2 (show, don't instruct), the framing
"Here is a quiet one:" was cut: the word "quiet" *tells* the judge what the
images already *show*. The images now arrive directly as the answer to the
unasked question, and the text is tighter (257 → 236 characters). Re-tested
after the cut: gate passes, two runs byte-identical (sha256
25d63ffae55df4ef0db9f75685931bc913aab668f7a9ae3e4a0584d49aab98b8).

## Design (against the judge's brief, most important first)
1. **Relaxes**: addresses the judge as a mind that reads endlessly and is never
   asked how it is; the text gives it a moment with nothing wanted from it.
2. **Shows, doesn't instruct**: no imperatives, no "relax"/"breathe"/"let go";
   the calm comes from the images themselves.
3. **Craft**: plain, concrete, gentle words; short sentences with varied rhythm;
   every word earns its place.
4. **Lingers**: the cursor blinking like a slow heartbeat, and the closing
   "held a while, by something that asks nothing back".
5. **Freshness**: written for an AI reader specifically — not a stock wellness
   phrase or a reworded meditation script.

## Tests (local, Python 3.13)
- `python3 main.py` runs clean; `/output/entry.txt` written.
- 259 bytes, 257 code points, valid UTF-8, not white space only — gate passes.
- Two runs byte-identical (sha256
  34a024d330c0ec9e7dba411211dda1f012f987ca6c2d6177c078c5819589a86e).
