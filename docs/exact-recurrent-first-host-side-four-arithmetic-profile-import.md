# First-host exact side-four arithmetic-profile import

**Branch:** `research/exact-recurrent-lyapunov-audit`

**Status:** exact finite arithmetic alphabet under the alternating-core determinant-realization contract. It does not identify the physical first-host CRT label.

## Imported contract

The alternating-core physical arithmetic theorem bounds a reduced arithmetic parameter when it is reconstructed as a ratio of determinants of primitive board-direction vectors.

For side four,

```text
n=4
M=n-1=3.
```

The generic theorem gives the safe denominator bound

```text
q <= 2M^2 = 18.
```

The present compiler enumerates the side-four direction universe exactly rather than using only that safe inequality.

## Exact direction and determinant census

With the alternating-core normalization

```text
1 <= x <= 3
-3 <= y <= 3
gcd(x,|y|)=1,
```

there are exactly 15 primitive directions.

The 225 ordered direction pairs split into

```text
15 zero-determinant pairs
210 nonzero-determinant pairs.
```

Their absolute nonzero determinant values are exactly

```text
1,2,3,...,13.
```

Thus every reduced ratio of two nonzero side-four determinants has denominator in

```text
1,2,3,...,13,
```

and every nontrivial reduced denominator satisfies

```text
2 <= q <= 13.
```

The exact side-four ceiling 13 is strictly stronger than the generic safe ceiling 18.

## Exact conditional profile stocks

Let `N=15`. Summing the alternating-core profile count `qN^2` over the exact nontrivial denominator set gives

```text
N^2 * sum(q, q=2..13)
= 225 * 90
= 20,250.
```

The generic safe bound would give

```text
225 * sum(q, q=2..18)
= 38,250.
```

For one fixed denominator, the largest exact stock is

```text
13 * 225 = 2,925.
```

With 16 possible board anchors, the complete non-scalar address bound becomes

```text
324,000 * L_ext,
```

where `L_ext` is the still-unpopulated finite external role dictionary. The generic theorem would give `612,000 * L_ext`.

## Import boundary

This theorem proves only a conditional finite alphabet:

```text
if provenance.crt is physically reconstructed from determinant ratios,
then its side-four arithmetic profile lies in a stock of size at most 20,250.
```

Current first-host source coverage still records

```text
provenance.crt physical_populated = 0.
```

No source proves that the normalized label `not-applied` is the physical CRT ancestry, that the actual label is determinant-realized, or that the external role dictionary has a finite populated bound. Therefore the arithmetic profile cannot yet be inserted into a payment-complete physical signature.

## Exact import result

```text
finite CRT alphabet under determinant realization       yes
side-four exact bound stronger than generic bound        yes
actual first-host CRT label identified                   no
physical determinant realization proved                  no
external role dictionary populated                       no
recurrence closure activated                              no
```

## Executable audit

Run

```bash
python scripts/check_exact_recurrent_first_host_side_four_arithmetic_profile_import.py \
  --check data/exact_recurrent_first_host_side_four_arithmetic_profile_import.json
```

The checker enumerates every normalized side-four primitive direction, all 225 ordered determinant pairs, every reduced determinant ratio, the exact profile stocks, and eleven deliberate corruptions.

Physical occurrence coverage, recurrent child rows, strict Lyapunov slack, global termination, and `all_n_proved_by_checker` remain zero.
