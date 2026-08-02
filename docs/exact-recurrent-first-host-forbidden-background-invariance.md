# Canonical forbidden-background selector invariance

**Branch:** `research/exact-recurrent-lyapunov-audit`

**Status:** complete conditional classification of a 32-background local class.

The first host forbids the four diagonal cells and target cell `01`. This chapter
classifies every background contained in

```text
F={00,01,11,22,33}.
```

It does not assert that every physical occurrence has background contained in
`F`. It proves what follows if that local background condition is established.

## ERL-S4.11 — common-offset identity

For every subset `B` of `F` and every candidate response

```text
3012, 3210, 2031, 2310, 3201,
```

the complete new-triple score is its intrinsic score plus the same common offset

```text
c(B)=1[{00,01} subset B]+1[{01,11} subset B].
```

Thus

```text
score(2031)=score(2310)=score(3201)=c(B)
score(3012)=c(B)+1
score(3210)=c(B)+4.
```

### Proof

Enumerate the ten unordered pairs from `F`. Only the vertical pair `{00,01}` and
horizontal pair `{01,11}` have a line passing through a point of each candidate
response. Each such pair contributes exactly one rank-one triple to every
response. Every other background pair contributes zero, and no point of `F`
lies on a candidate response secant, so there is no rank-two contribution.
The intrinsic scores are `0,0,0,1,4` as displayed. ∎

## Exact census

Across all 32 subsets:

```text
common offset 0: 20 backgrounds
common offset 1:  8 backgrounds
common offset 2:  4 backgrounds
```

The selector order is preserved on all 32 backgrounds. The exact minimizer face
is always

```text
{2031,2310,3201}.
```

The reopened responses may have score one or two rather than zero, but they
remain jointly optimal within the five-response menu.

## Relation to the singleton fragility theorem

The singleton witnesses `(-1,4)` and `(4,-1)` lie outside `F`. They show that the
reopening menu is not robust for arbitrary padded backgrounds. The present result
shows that the canonical forbidden-cell class is safe for selector ordering.

Together the two results isolate the next physical question precisely:

```text
Does every realizable first-host background have the same 31-coordinate score
signature as some subset of F, or can exterior secant incidences occur?
```

That question cannot be answered from the normalized host manifest because its
background field is unpopulated.

## Executable audit

Run

```bash
python scripts/check_exact_recurrent_first_host_forbidden_background_invariance.py \
  --check data/exact_recurrent_first_host_forbidden_background_invariance.json
```

The checker directly enumerates all 32 backgrounds and all five response scores,
verifies the common-offset formula and minimizer face, and rejects eleven
corruption classes.

Physical background containment in `F`, deletion causes, legal reopening,
recurrent children, strict Lyapunov descent and the all-`n` conclusion remain
unproved.
