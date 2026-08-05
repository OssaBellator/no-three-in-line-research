# Threshold rigidity at every equality multiple

This chapter extends the minimum-batch rigidity from `docs/683` and the all-window
obstruction from `docs/696`. It rules out non-minimum equality multiples within
the same four-by-four source, hidden identity matrix, and legal permutation-layer
alphabet.

## PP3dfp — A dual pair of nonnegative separators

For a primitive permutation layer `L`, retain the separator `Phi` from the earlier
threshold chapters and introduce

```text
Psi =
[ 1 0 0  0 ]
[ 1 1 0  0 ]
[ 0 0 0 -1 ]
[ 0 0 0  0 ].
```

Across all eighteen legal permutation layers,

```text
Phi(L) in {0,1,2},
Psi(L) in {0,1}.
```

Both functionals are therefore nonnegative on every legal primitive layer. For
the source matrix `S` and identity layer `I`,

```text
Phi(S)=-3,  Phi(I)=-2,
Psi(S)= 3,  Psi(I)= 2.
```

Consider any equality-scale decomposition

```text
4h I + sum_j L_j = t S,
```

where `h` is the number of hidden `4I` matrices and every `L_j` is a legal
primitive layer. Applying the two separators gives

```text
sum_j Phi(L_j) = 8h-3t >= 0,
sum_j Psi(L_j) = 3t-8h >= 0.
```

Hence both sides vanish and

```text
8h=3t.
```

## PP3dfq — Exact scale and alphabet rigidity

Coprimality of three and eight forces

```text
t=8K,
h=3K
```

for an integer `K>=1`. Equality in both separator inequalities also forces every
legal primitive layer to lie in the common zero set of `Phi` and `Psi`.

That common zero set consists of exactly five permutations:

```text
(0,2,3,1),
(1,2,0,3),
(1,3,2,0),
(2,1,3,0),
(2,3,0,1).
```

Thus no positive-score legal primitive type can enter at a larger equality scale.
Non-minimum equality mixtures do not enlarge the usable primitive alphabet.

## PP3dfr — Unique multiplicities at every multiple

The five common-zero permutation matrices have rank five. Rows

```text
0,1,2,5,6
```

form a unimodular five-by-five minor, so their multiplicities are uniquely
determined over the integers by the aggregate equality matrix.

At scale `K`, the unique solution is

```text
4K copies of each of the five common-zero types.
```

Consequently every equality multiple has exactly the scaled primitive aggregate
from the minimum batch:

```text
12K hidden identity layers,
20K legal layers,
identity density 3/8.
```

This conclusion does not assume that the mixture was assembled by concatenating
minimum batches; it follows directly from the two separators and the unimodular
minor. The all-width rolling obstruction of `docs/696` therefore applies to every
equality multiple in this alphabet.

The audit is `scripts/check_threshold_all_equality_multiples_703.py`.

## Evidence boundary

The theorem is exact for the current source matrix, hidden identity matrix, and
legal four-by-four permutation alphabet. It does not exclude an enlarged
primitive alphabet or a genuinely unexposed non-rolling geometric operation. The
threshold row remains unpromoted and the all-`n` theorem remains open.
