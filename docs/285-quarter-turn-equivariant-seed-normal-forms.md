# Quarter-turn-equivariant seed normal forms

Quarter-turn symmetry is one of the most productive finite search classes in the
public no-three-in-line archives.  In the two-permutation seed language it has a
small exact algebraic normal form.

Let the board coordinates be `0,...,n-1`, put

```text
J(x)=n-1-x,
```

and let the geometric quarter-turn be

```text
R(x,y)=(J(y),x).
```

This chapter distinguishes two notions carefully.  A selected set may be
quarter-turn invariant without a chosen two-layer colouring being invariant.
An *equivariant layer decomposition* is an alternating incidence colouring for
which `R` either fixes both colours or swaps them globally.

The reduction below is exact for that structured class.  It is not asserted
that every seed, or even every quarter-turn-invariant seed, must use this class.
The asymptotic prime-minus-one seed theorem remains open.

## 1. Quarter-turn action on one permutation graph

For a permutation `sigma` of `[n]`, define

```text
Q(sigma)=sigma^(-1) o J.
```

### Proposition PP3bef -- PROVED

The quarter-turn image of the permutation graph `P_sigma` is the permutation
graph `P_(Q(sigma))`.  Moreover

```text
Q^2(sigma)=J o sigma o J,
Q^4(sigma)=sigma.
```

#### Proof

A point `(x,sigma(x))` is sent to

```text
(J(sigma(x)),x).
```

Writing `u=J(sigma(x))`, the new row is

```text
x=sigma^(-1)(J(u))=Q(sigma)(u).
```

Thus the rotated graph is `P_(Q(sigma))`.  Applying the definition twice gives

```text
Q^2(sigma)
=(sigma^(-1) o J)^(-1) o J
=J o sigma o J.
```

Since `J^2=id`, two more applications return `sigma`. ∎

## 2. Exact parity system for equivariant layer colouring

Let `S` be a saturated selected set.  Its row--column incidence graph is a
union of even cycles.  An alternating two-layer decomposition is a map

```text
c:S->{0,1}
```

such that two selected cells sharing a row or column receive opposite colours.
For `epsilon in {0,1}`, add the quarter-turn constraints

```text
c(R(e))=c(e)+epsilon  (mod 2).
```

Here `epsilon=0` means that the layers are fixed and `epsilon=1` means that
they are swapped.

### Proposition PP3beg -- PROVED

For a quarter-turn-invariant saturated set, existence of an equivariant layer
decomposition of type `epsilon` is equivalent to consistency of the following
binary linear system:

1. one equation `c(e)+c(f)=1` for every incidence-adjacent pair `e,f`; and
2. one equation `c(e)+c(R(e))=epsilon` for every selected cell `e`.

The system can be decided by a breadth-first parity propagation on the graph of
these constraints.  Any satisfying assignment gives two edge-disjoint
permutation layers whose union is exactly `S`.

#### Proof

The incidence equations are exactly alternating edge colouring on every even
component.  The rotation equations are exactly the requested global action on
the two colours.  A system of equations of the form `c(v)+c(w)=d` over
`F_2` is consistent exactly when parity propagation assigns no vertex two
different values.  In a satisfying assignment, every row and column has one
edge of each colour, so each colour class is a perfect matching. ∎

This criterion does not assume that the deterministic component colouring used
by another checker already has the correct equivariance; it searches all
component flips simultaneously.

## 3. Fixed versus swapped action

### Proposition PP3beh -- PROVED

Every equivariant two-layer decomposition has exactly one of the following
actions.

1. **Fixed action:**
   ```text
   Q(sigma)=sigma,
   Q(tau)=tau.
   ```
2. **Swapped action:**
   ```text
   Q(sigma)=tau,
   Q(tau)=sigma.
   ```

#### Proof

Quarter-turn acts as a permutation of the two colour classes.  A permutation
of a two-element set is either the identity or the transposition. ∎

## 4. Swapped-layer signed-permutation normal form

### Theorem PP3bei -- PROVED

A pair of permutation layers has swapped quarter-turn action if and only if

```text
sigma o J = J o sigma,
tau = sigma^(-1) o J.
```

In this normal form the layers are edge-disjoint exactly when

```text
sigma^2(x) != J(x)
```

for every `x`.

#### Proof

If `Q(sigma)=tau` and `Q(tau)=sigma`, then

```text
Q^2(sigma)=sigma.
```

By PP3bef this is `J o sigma o J=sigma`, which is equivalent to commuting with
`J`; the first rotation equation gives `tau=sigma^(-1)o J`.

Conversely, if `sigma` commutes with `J` and `tau=sigma^(-1)o J`, then
`Q(sigma)=tau` and

```text
Q(tau)=Q^2(sigma)=J o sigma o J=sigma.
```

Finally,

```text
sigma(x)=tau(x)
iff sigma(x)=sigma^(-1)(J(x))
iff sigma^2(x)=J(x).
```

Thus the displayed inequality is exactly edge-disjointness. ∎

### Proposition PP3bej -- PROVED

Write `n=2m`.  The permutations commuting with `J` are precisely signed
permutations of the `m` reversal pairs

```text
{x,J(x)}.
```

There are exactly

```text
2^m m!
```

such permutations.

#### Proof

A commuting permutation maps every `J`-orbit, which is one reversal pair, to
another reversal pair.  It may choose either orientation independently on each
source pair.  Thus one chooses a permutation of the `m` pairs and one of two
orientations for each pair.  Conversely every such signed permutation commutes
with `J`. ∎

Therefore the swapped quarter-turn seed problem is a one-permutation search in
the hyperoctahedral group, followed by the forced formula for `tau`.  This is a
large exact reduction from an unrestricted ordered pair of permutations.

## 5. Fixed-layer square-root normal form

### Theorem PP3bek -- PROVED

A permutation graph is fixed by quarter-turn exactly when

```text
sigma^2=J.
```

Consequently a fixed-action two-layer decomposition consists of two
distinct, edge-disjoint square roots of `J`.  Such a square root can exist only
when

```text
4 divides n.
```

#### Proof

The equality `Q(sigma)=sigma` is

```text
sigma^(-1) o J=sigma,
```

which is equivalent to `sigma^2=J`.

The involution `J` is a product of `n/2` disjoint transpositions.  Squaring one
four-cycle produces two disjoint transpositions, and every transposition in
the square of a permutation must be paired with another transposition in this
way.  Hence `n/2` must be even.  Conversely, when `4|n`, pair the
transpositions of `J` and orient a four-cycle on each pair to obtain a square
root. ∎

Fixed action is therefore unavailable for every side length `n=2 mod 4`, while
the swapped signed-permutation normal form remains available for every even
`n`.

## 6. Relative-cycle parity law

Let

```text
pi=sigma^(-1) o tau.
```

### Proposition PP3bel -- PROVED

In either equivariant normal form, `pi` commutes with `J`.  Consequently every
odd cycle length occurs with even multiplicity in the cycle partition of
`pi`.

#### Proof

In swapped action, `sigma` commutes with `J`, and so does
`tau=sigma^(-1)o J`.  In fixed action, `sigma^2=J` implies that `sigma`
commutes with `J`, and similarly for `tau`.  Hence their quotient `pi`
commutes with `J`.

The involution `J` maps every cycle of `pi` to a cycle of the same length.  If
an odd cycle were mapped to itself, then the restriction of `J` to that cycle
would be a fixed-point-free involution commuting with a cyclic permutation.
Such a restriction must be a rotation of the odd cycle; an odd cyclic group
has no nontrivial element of order two.  The restriction would therefore be
the identity, contradicting that `J` has no fixed points.  Odd cycles must
come in distinct `J`-paired copies. ∎

This parity law is a necessary search invariant for the equivariant class, not
for arbitrary seeds.

## 7. Finite archive audit

### Proposition PP3bem -- VERIFIED FINITELY

The exact parity checker applied to the eight stored quarter-turn archive
certificates reports:

| `p` | `n` | equivariant actions | relative cycles |
|---:|---:|---|---|
| 17 | 16 | fixed and swapped | `[8,8]` |
| 19 | 18 | swapped | `[10,2,2,2,2]` |
| 23 | 22 | swapped | `[5,5,5,5,2]` |
| 29 | 28 | swapped | `[26,2]` |
| 31 | 30 | swapped | `[5,5,5,5,2,2,2,2,2]` |
| 61 | 60 | swapped | `[58,2]` |
| 67 | 66 | swapped | `[16,16,16,16,2]` |
| 73 | 72 | fixed and swapped | `[36,36]` |

Every case satisfies the odd-cycle multiplicity law.  The checker independently
repeats all `1,230,128` determinant tests before applying the parity system.

#### Verification

Run

```bash
python scripts/check_quarter_turn_seed_normal_forms.py \
  experiments/archived-prime-seed-codes.json
```

The output verifies quarter-turn invariance, solves both parity systems,
reconstructs the layers, checks the fixed or swapped algebraic identities, and
checks the relative-cycle parity law. ∎

The finite audit suggests that swapped action is the more flexible structured
class: it works in every stored quarter-turn case, including all side lengths
`2 mod 4`.  This observation is a search guide, not an asymptotic existence
proof.