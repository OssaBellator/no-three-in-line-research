# Exact coordinated-repair support census for the one-defect p=17 state

The one-defect state isolated in PP3bdw has two individually clean permutation
layers, exactly one bad line in their union, and no valid repair that leaves
either layer fixed.  This chapter measures how shallow a genuinely two-sided
repair could be.

For an ordered pair of repaired layers `(sigma',tau')`, define the assignment
supports

```text
A_sigma={x:sigma'(x)!=sigma(x)},
A_tau={x:tau'(x)!=tau(x)}
```

and the total support

```text
h=|A_sigma|+|A_tau|.
```

The finite census below proves that `h>=8` for this state.  It does not prove
that support eight is sufficient, and it does not assert a uniform repair
bound for arbitrary side length.

## 1. The audited near-state

Use one-based permutation values

```text
sigma =
[11,7,9,16,2,10,6,1,15,4,13,14,5,12,8,3],

tau =
[6,13,10,14,5,9,4,12,16,1,11,15,8,3,2,7].
```

Both layers are individually no-three.  Their union has exactly one forbidden
triple:

```text
(1,11), (3,10), (13,5).
```

The first and third cells belong to `sigma`; the middle cell belongs to `tau`.

## 2. Exact support normal form

### Proposition PP3ben -- PROVED

Let `sigma'` be a permutation and let

```text
A={x:sigma'(x)!=sigma(x)}.
```

Then `sigma'` agrees with `sigma` outside `A`, and on `A` it is obtained by a
derangement of the old values `sigma(A)`.  Conversely every derangement of the
old values on `A` gives a permutation whose exact change support is `A`.

#### Proof

The unchanged columns use exactly the values `sigma([n]\A)`.  Since `sigma'`
is a permutation, the remaining columns must use the complementary value set,
which is `sigma(A)`.  Thus the restriction is a permutation of those old
values.  Exact support means that no column receives its old value, so the
induced permutation has no fixed point.  The converse is immediate. ∎

Therefore a complete support census may enumerate a subset and a derangement,
rather than all full permutations.

## 3. Necessary bad-line filter

### Proposition PP3beo -- PROVED

Every valid repair must change at least one of the three assignment slots

```text
sigma column 1,
sigma column 13,
tau column 3.
```

#### Proof

If all three slots remain unchanged, the unique forbidden triple remains
selected. ∎

For support sizes `a=|A_sigma|` and `b=|A_tau|`, with both layers changed, the
number of exact candidates surviving this necessary filter is

```text
N_(a,b)
=
[ C(16,a) C(16,b) - C(14,a) C(15,b) ] !a !b,
```

where `!k` is the number of derangements of `k` objects.  The subtracted term
chooses neither of the two marked `sigma` columns and not the marked `tau`
column.

## 4. Exact line-delta verification

### Proposition PP3bep -- PROVED

For a fixed support candidate, no-three validity can be decided by updating
only maximal grid lines through an old or new changed cell.

#### Proof

Every other maximal line has exactly the same selected cells as in the base
state.  For an affected line, subtract its changed old cells and add its changed
new cells.  The candidate is valid exactly when every resulting occupancy is
at most two.  By PP3bcy this is equivalent to the absence of a collinear
triple. ∎

The diagnostic uses exact integer line equations and no floating-point
geometry.

## 5. Complete two-sided census through support seven

The earlier PP3bdw proves that no repair can leave either layer fixed.  Hence a
repair has

```text
|A_sigma|>=2,
|A_tau|>=2,
```

because a nonempty exact support of a permutation cannot have size one.

### Proposition PP3beq -- VERIFIED FINITELY

The complete candidate counts after the necessary bad-line filter are:

| total support `h` | candidates checked |
|---:|---:|
| 4 | 4,845 |
| 5 | 109,550 |
| 6 | 2,459,240 |
| 7 | 44,402,358 |

The total is

```text
46,975,993
```

exact two-sided candidates.

#### Verification

For each split `h=a+b` with `a,b>=2`, the checker enumerates every `a`-column
subset, every `b`-column subset, and every derangement of the corresponding old
values.  PP3ben proves completeness and PP3beo justifies the only support
filter.  The observed counts agree with the displayed formula for `N_(a,b)`.
∎

### Theorem PP3ber -- VERIFIED FINITELY

None of the `46,975,993` candidates with total support at most seven is a
saturated no-three seed.

#### Verification

Every candidate preserves the two permutation constraints by construction.
Candidates with a same-cell collision are rejected, and every remaining
candidate is checked against all affected maximal-line occupancies by PP3bep.
No candidate has all occupancies at most two. ∎

## 6. Exact lower and finite upper bounds

### Corollary PP3bes -- PROVED / VERIFIED FINITELY

Every valid repair of the audited one-defect state changes at least eight
assignment positions:

```text
h>=8.
```

#### Proof

PP3bdw excludes every one-sided repair, regardless of support size.  PP3ber
excludes every two-sided repair with `h<=7`. ∎

### Proposition PP3bet -- VERIFIED FINITELY

A valid `p=17` seed stored in the archive suite is

```text
sigma =
[4,10,9,16,6,12,2,3,14,15,5,11,1,8,7,13],

tau =
[5,13,11,2,16,3,9,7,10,8,14,1,15,6,4,12].
```

It differs from the audited near-state in exactly `29` assignment positions.
Consequently the minimum labelled repair support `h_min` satisfies

```text
8 <= h_min <= 29.
```

#### Verification

The exact seed checker performs all `4960` determinants for the displayed
pair.  Direct comparison with the near-state gives support `29`. ∎

## 7. Revised repair frontier

### Corollary PP3beu -- PROVED / FINITE BARRIER RECORDED

The one-defect example rules out all of the following as general repair
principles:

1. changing only one permutation layer;
2. one transposition in each layer;
3. any coordinated permutation rearrangement supported on at most seven total
   assignment positions.

A successful repair or absorption theorem must permit a genuinely distributed
two-layer move.  The present census does not rule out a larger absolute
constant, a support growing slowly with `n`, or a structured global switch.

## 8. Diagnostic

Compile and run:

```bash
g++ -O3 -std=c++17 \
  scripts/check_p17_coordinated_repair_support.cpp \
  -o /tmp/check_p17_repair
/tmp/check_p17_repair \
  experiments/p17-coordinated-repair-support-example.json
```

The program verifies the base state, its unique bad triple, the known valid
upper certificate, the exact support counts, and the complete no-repair census
through total support seven.