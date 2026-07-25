# Credited-line self-recapture diagnostic

This check accompanies
`docs/193-credited-line-self-recapture-thinning.md`.

Run:

```bash
python scripts/check_credited_line_self_recapture.py \
  experiments/credited-line-self-recapture-example.json
```

The stored abstract trace system has a full credited bank of size `Q=12` and
subbank size `q=4`.  Every credit line contains its own current diagonal cell
and a derangement matching on the other eleven indices.  Thus every trace is a
matching of size twelve, has a unique current diagonal, and has no other cell
using the credit owner's row or column.

There are `12*11=132` off-diagonal trace entries.  Every entry uses one
credit-line index and two distinct cell indices, so its probability of
surviving a uniform four-index thinning is

```text
(4)_3/(12)_3.
```

The exact average restricted self-trace count is therefore

```text
132*(4)_3/(12)_3 = 2.4.
```

A uniform derangement of a selected four-bank chooses each off-diagonal cell
with probability `1/(4-1)`, giving average recreated credit

```text
2.4/3 = 0.8.
```

The checker also enumerates every four-subbank and every derangement.  It
verifies that whenever a subbank has zero restricted self-trace entries, every
derangement has zero selected-credit recreation.

The finite instance is intentionally dense and does not yet lie in the
asymptotic `q^3/Q=o(1)` regime.  It checks the exact triple-selection and
derangement arithmetic used by the theorem.
