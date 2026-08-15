# Exact background-completion witness for the first residual host

**Branch:** `research/exact-recurrent-lyapunov-audit`

**Status:** complete-score selector non-identifiability proved from an exact
affine completion. Global realizability and legal repair remain open.

## Host

```text
upstream ID  s4-75b04c45c1c8eac2
deletions    {02,20}
responses    3012, 3210
intrinsic selector  3012
intrinsic scores    1, 4
intrinsic gap       3
```

The selected response `3012` has its unique intrinsic triple on
`x-y-1=0`. The competitor `3210` has its four response points on `x+y-3=0`.

## Theorem ERL-S4.6 — PROVED

The populated first-host record does not determine a unique minimizer of the
complete geometric triple score.

### Empty background

With no background points, exact enumeration gives

```text
score(3012)=1
score(3210)=4
minimizer face={3012}
```

### One-point completion

Add the integer point

```text
b=(4,3).
```

It lies on `x-y-1=0` and does not lie on `x+y-3=0`. Exact enumeration of all
collinear triples in response union background that contain at least one
response point gives

```text
score_b(3012)=4
score_b(3210)=4
minimizer face={3012,3210}.
```

The response `3012` acquires exactly three new triples, consuming its intrinsic
gap `3`. The response `3210` acquires none. Thus the unique intrinsic selector
becomes an exact tie.

### Proof

The checker constructs each response as four integer points and enumerates every
three-subset after adjoining the declared background. It tests collinearity by
the exact determinant identity. The empty and one-point score tables are the
values displayed above. Since the current populated host record omits the
background field, both are completions of the same recorded host/selector data,
but their minimizer faces differ. ∎

## What this proves

The canonical selector in the upstream manifest is a deterministic selector for
intrinsic response energy. It is not, by itself, a complete coupled-score
selector. The exact intrinsic gap is usable only after every response-dependent
background perturbation is bounded below that gap.

For this host, one omitted background point can reach the threshold exactly.
Therefore an exact recurrent row cannot safely hard-code `3012` as a unique
complete-score selector from the current record alone.

## What this does not prove

The point `(4,3)` is an affine schema witness. This chapter does not assert that
this background occurs in every or any globally legal prime-power construction
state. It does not establish a globally realized selector switch, a recurrent
cycle, a failed Lyapunov inequality, or a counterexample to the conjecture.

The next physical compiler must determine whether this completion is realizable,
forbidden, already paid, or assigned to a different owner/interface class.

## Executable audit

Run

```bash
python scripts/check_exact_recurrent_first_host_selector_background_witness.py \
  --witness data/exact_recurrent_first_host_selector_background_witness.json
```

The checker reconstructs both score tables, verifies the exact line incidences
and gap consumption, and rejects twelve corruption classes. Every global
realizability, legal-transition, recurrent-row, Lyapunov and all-`n` flag remains
zero.
