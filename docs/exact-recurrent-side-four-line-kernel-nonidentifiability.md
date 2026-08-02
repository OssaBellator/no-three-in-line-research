# Complete line-kernel non-identifiability from the populated side-four records

**Branch:** `research/exact-recurrent-lyapunov-audit`

**Status:** exact contract-level obstruction proved. This is an obstruction to
constructing an exact recurrent row from the current manifests, not a
counterexample to the no-three-in-line conjecture.

## Complete line kernel

The installed line-energy theorem uses

\[
K(h,k)=k\binom h2+\binom k2h+\binom k3
      =\binom{h+k}{3}-\binom h3,
\]

where `h` is the number of background points on a real line and `k` is the
number of response points on that line.

The current side-four host, selector and selected-line manifests determine `k`,
but they do not contain `h`.

## Theorem ERL-S4.5 — PROVED

The populated side-four records do not determine even the selected-line
contribution to the complete coupled response kernel.

### Class `3012`

The selected line contains `k=3` response points. Two completions of the omitted
background-load coordinate give

```text
h=0 -> K(0,3)=1
h=1 -> K(1,3)=4
```

The exact difference is `3`.

### Class `3210`

The selected line contains `k=4` response points. The corresponding completions
give

```text
h=0 -> K(0,4)=4
h=1 -> K(1,4)=10
```

The exact difference is `6`.

Because every residual host belongs to one of these two classes, none of the
eleven current host/selector/selected-line records determines its complete
selected-line energy.

### Proof

The selected-line geometry checker determines `k=3` for class `3012` and `k=4`
for class `3210`. Substitute `h=0` and `h=1` into the exact installed kernel.
The resulting values differ in both classes. Since `h` is not a field of the
populated records, those records have the same declared data under both schema
completions but require different exact kernel coefficients. Therefore the
kernel is not a function of the currently populated record. ∎

## Scope of the witness

The two background-load values are schema-completion witnesses. This theorem
does **not** assert that both completions occur as globally legal states of the
construction. That stronger statement would require the missing physical
background and provenance compiler.

This distinction is important:

- the theorem proves that the present manifests are insufficient to determine an
  exact row;
- it does not prove that the full geometric construction has two realizable
  fibres;
- it does not prove a recurrent obstruction once the missing data are supplied;
- it does not alter any all-`n` proof flag.

## Consequence for the first host

For `s4-75b04c45c1c8eac2`, the selected response `3012` contributes one intrinsic
triple when `h=0`, but the exact complete selected-line contribution is four when
one background point lies on `x-y-1=0`.

Thus the intrinsic energy `1` and selector gap `3` cannot be inserted as the
complete line coefficient without first supplying the background line load and
retained incidence labels. In particular, the gap `3` is a response-only
stability margin, not a complete coupled-score margin.

## Exact next requirement

A provenance compiler must attach, for each selected line occurrence:

1. its exact background load `h`;
2. retained incidence and physical-owner labels;
3. all other response/background line interactions;
4. the installed legal operation selected for the resulting complete score;
5. exact child multiplicities and weights.

Until these fields exist, an exact compulsory weighted row cannot be inferred
from the side-four host and selector manifests alone.

## Executable audit

Run

```bash
python scripts/check_exact_recurrent_side_four_line_kernel_nonidentifiability.py \
  --geometry data/exact_recurrent_side_four_selected_line_geometry.json \
  --witness data/exact_recurrent_side_four_line_kernel_nonidentifiability.json
```

The checker evaluates the exact binomial kernel under both identities, joins the
witness to all eleven residual hosts, and rejects twelve corruption classes.
All global proof, physical-realizability, row-completeness and Lyapunov flags
remain zero.
