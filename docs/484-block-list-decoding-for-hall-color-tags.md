# Block-list decoding for Hall-color tags

`docs/472` and `docs/478` protect Hall colors by concatenating outer color codes
with geometric inner marker words.  An inner geometric decoder may naturally
return a short list rather than one symbol.  This chapter transfers those block
lists exactly to the outer Hall-color ambiguity.

Let `C subseteq A^n` be the outer proper-color code.  After observing inner block
`j`, let `L_j subseteq A` be the exact set of outer symbols still compatible with
that block.  Define

```text
C(L_1,...,L_n)={c in C: c_j in L_j for every j}.
```

## 1. Exact block-list transfer

### Theorem PP3cgi -- PROVED / OUTER COMPATIBILITY LIST

The Hall colors compatible with all inner observations are exactly
`C(L_1,...,L_n)`.  If this set has size `L` and each tagged target has at least
`d` residual Hall actions, the reverse load is at most `L/d`.

#### Proof

A concatenated tag is compatible with the received marker blocks exactly when
its outer symbol at every coordinate belongs to the corresponding inner list.
Thus no color outside the displayed set can contribute.  Every compatible color
class contributes at most `1/d`, and summing at most `L` classes gives `L/d`. ∎

## 2. Information-set and distance bounds

### Theorem PP3cgj -- PROVED / INFORMATION-SET LIST BOUND

Suppose projection of `C` onto coordinate set `I` is injective.  Then

```text
|C(L_1,...,L_n)| <= product_(j in I) |L_j|.
```

Consequently one may minimize this product over all known information sets.  If
all blocks outside a set `B` return the correct singleton and `|B|<delta(C)`, the
outer color is unique.

#### Proof

Every compatible codeword has a distinct projection on `I`, and that projection
lies in the Cartesian product of the lists on `I`.  This proves the product
bound.  In the singleton statement, two compatible codewords could differ only
inside `B`, hence would have distance at most `|B|`, contradicting the minimum
distance. ∎

For an `[n,k]` MDS outer code, every `k`-coordinate set is an information set, so
the product of the `k` smallest block-list sizes is always a valid bound.

## 3. Finite ambiguity witness

### Theorem PP3cgk -- PROVED / BLOCK-LIST AUDIT

For finite outer and inner alphabets, the claimed list bound has a finite exact
audit.  Failure returns one outer codeword excluded by a claimed inner list, one
included word incompatible with a block, two words colliding on a claimed
information set, or one observation whose compatible-color count exceeds the
claimed reverse-load factor.

#### Proof

All codewords, coordinate projections, block lists, and compatibility tests are
finite.  Exhaustive exact checking establishes each claim, and any failed check
is already one of the listed witnesses. ∎

## 4. Stored exact fixture

The audit `scripts/check_block_list_hall_decoding.py` uses the `[4,2,3]`
Reed--Solomon code over `F_5`.  Every coordinate pair is an information set.  It
checks all `15^4=50,625` observations whose coordinate lists are singletons or
pairs.  The information-set product bound always holds, the largest actual color
list has size two, and the bound is tight in `3,025` cases.

For every true color it also checks all `2,825` observations with zero, one, or
two ambiguous blocks containing the true symbol and recovers the color uniquely.
A concrete three-block ambiguity contains two colors, showing that the distance
threshold is sharp.

## 5. Prime-patching consequence

Localized Hall transport can now consume whatever exact symbol lists the inner
geometry produces.  The outer algebraic code converts them into a certified
Hall-color list and hence a certified reverse-load multiplier, without forcing
every inner block to decode uniquely.
