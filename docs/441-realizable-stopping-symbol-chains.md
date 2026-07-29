# Realizable stopping-symbol chains

`docs/435` encodes nonintrinsic stopping levels by abstract prefix words.  This
chapter inserts an actual sequence of local marker kernels between a repair
prefix and its final code tag.  The resulting load is the product of the base
repair load and the symbol-kernel loads, while prefix recovery prevents any sum
over stopping classes.

## 1. Symbol-chain composition

Let stopping class `i` have a base kernel `P_i` with reverse load at most
`lambda_i`.  Its codeword is

```text
w_i=s_(i,1)...s_(i,ell_i).
```

For every symbol `s`, let `S_s` be a local marker kernel with reverse load at
most `r_s`.  Assume every intermediate target records the code prefix already
written.

### Theorem PP3cbj -- PROVED / REALIZABLE SYMBOL-CHAIN LOAD

The composed stopping kernel

```text
K_i=P_i S_(s_(i,1)) ... S_(s_(i,ell_i))
```

has reverse load at most

```text
lambda_i product_(j=1)^(ell_i) r_(s_(i,j)).
```

#### Proof

Reverse loads are submultiplicative under kernel composition.  Apply that fact
successively to the base kernel and every symbol kernel.  Prefix recording does
not increase a column sum; it only refines the target state. ∎

## 2. Prefix-free class combination

### Theorem PP3cbk -- PROVED / NO STOPPING-CLASS SUM

If the codewords `w_i` are prefix-free and the terminal target retains the whole
word, then the union of all stopping-class kernels has reverse load at most

```text
max_i lambda_i product_j r_(s_(i,j)).
```

No factor equal to the number of stopping classes appears.

#### Proof

A terminal target decodes at most one prefix-free codeword, hence receives mass
from at most one stopping class.  Its column load is therefore bounded by the
corresponding class bound from `PP3cbj`.  Taking the maximum proves the claim. ∎

This is the implementation interface missing from `docs/435`: the schedule
word may be built one short clean marker move at a time.

## 3. Failure localization along the word

Suppose symbol position `j` is expected to retain conditional mass at least
`p_(i,j)`, but the observed retained word mass is `g_i`.

### Theorem PP3cbl -- PROVED / FIRST BAD SYMBOL PREFIX

If

```text
g_i < product_j p_(i,j),
```

then some code-prefix transition has conditional retained mass less than its
promised value `p_(i,j)`.  The first such position is a concrete local marker
obstruction.

#### Proof

Write the retained word mass as the product of its conditional prefix-retention
ratios.  If every ratio were at least the promised value, their product would be
at least the promised product, contrary to the displayed inequality. ∎

Thus failed schedule realization does not invalidate the entire repair word.  It
returns one short prefix and one symbol move whose geometric safety estimate is
false.

## 4. Exact diagnostic

Run

```bash
python scripts/check_realizable_stopping_symbol_chains.py
```

The script checks the prefix code `{0,10,110,111}`, exact rational symbol-chain
loads, all fifteen nonempty unions of stopping classes, and a three-symbol word
whose retention failure localizes to its second transition.

The next theorem identifier after this chapter is `PP3cbm`.
