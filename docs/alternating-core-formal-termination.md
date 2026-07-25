# Formal termination interfaces for the alternating core

This note separates the finite-state parts of AC4--AC6 from the geometric
content still required in AC1--AC3.  It does **not** prove that every failed
bank has an AC2 output, or that the proposed carry mass cannot be recycled.
It proves that once those two facts are supplied with the stated interfaces,
termination and the reverse-scale assembly are formal consequences.

## AC4a -- bounded monotone closure terminates

An active closure record is a tuple

\[
(\mathcal S,\Phi,\Xi,\mathcal L),
\]

where \(\mathcal S\) is the two-colour row-column state, \(\Phi\) is its
triple potential, \(\mathcal L\) is the set of exposed carry labels, and
\(\Xi\) is an integer.  Fix an integer \(B\).  A closure transition is
**certified** when exactly one of the following is recorded:

1. an improving row-column-preserving state, after which the closure attempt
   stops;
2. a bounded-denominator chamber accepted by the BDA interface;
3. a subgroup-coset or order-two state accepted by the rational inverse
   interface;
4. a nonterminal re-extraction with
   \[
   0\leq \Xi<\Xi'\leq B.
   \]

### Lemma AC4a -- PROVED

Every sequence of certified closure transitions starting with value
\(\Xi_0\) has at most

\[
B-\Xi_0
\]

nonterminal transitions.  Consequently a procedure which supplies a
certified transition whenever it is nonterminal reaches one of outcomes
1--3 after at most \(B-\Xi_0+1\) calls to its transition oracle.

### Proof

Every nonterminal transition strictly increases an integer in
\(\{\Xi_0,\Xi_0+1,\ldots,B\}\).  There can be at most \(B-\Xi_0\) such
increases.  If the procedure is called once more, the returned transition
cannot be nonterminal and is therefore one of outcomes 1--3. \(\square\)

This elementary lemma fixes the exact obligation on AC3: a qualitative
claim that "new complexity is exposed" is not enough.  AC3 must return the
new integer value, prove the common bound \(B=p^{O(1)}\), and show that no
transition class leaves \(\Xi\) unchanged.

## Mandatory \(p=11\) transition

The existing verifier `scripts/verify_carry_cycle_bound.py` proves that the
one-colour \(p=11\), \(a=2\), \(b=3\) cycle is frozen in its entire
one-colour matching space, while the displayed opposite-colour anchor
permutation changes the full potential from \(16\) to \(6\).

Thus the frozen one-colour state is not an admissible terminal outcome of a
certified AC4 transition system.  Any implementation of the transition
oracle must include the opposite-colour release before it may report a
structured exception.  This is a regression condition, not an asymptotic
heuristic.

## AC5a -- reverse-scale induction

Let

\[
H_0>H_1>\cdots>H_m
\]

be the finitely many dyadic height scales.  Say that scale \(H_i\) is
settled when no bad line in its height band remains.  Suppose the repair
procedure at scale \(H_i\) has the following properties:

1. it preserves every already settled band \(H_0,\ldots,H_{i-1}\);
2. it creates bad lines only in bands \(H_j\) with \(j>i\);
3. while \(H_i\) is not settled, it returns a certified batch for which the
   nonnegative integer \(\Psi_{H_i}\) strictly decreases.

### Lemma AC5a -- PROVED

Descending processing settles all height bands after finitely many repair
batches.  More precisely, after scale \(H_i\) is entered it uses at most the
value of \(\Psi_{H_i}\) at entry many batches.

### Proof

At scale \(H_i\), property 3 decreases a nonnegative integer by at least one,
so the scale terminates in at most its entry value.  Properties 1 and 2 show
that this work cannot unsettle an earlier band.  Induction on \(i\) settles
all finitely many bands. \(\square\)

The fixed-fraction drift requested in AC5 implies property 3 whenever the
paid incidence is positive: an integer potential which decreases by a
strictly positive real amount decreases by at least one.

## AC6a -- conditional prime-minus-one assembly

### Lemma AC6a -- PROVED UNDER HYPOTHESES

Assume, for every sufficiently large odd prime \(p\):

1. the H4 seed supplies two permutation layers on the
   \((p-1)\times(p-1)\) grid;
2. every frozen local core encountered at a height scale has a certified
   AC4 transition;
3. every such transition satisfies the three reverse-scale hypotheses of
   AC5a; and
4. every BDA or rational-inverse delegation returns a
   row-column-preserving state through the same reverse-scale interface.

Then there is a set of \(2(p-1)\) grid points, two in every row and column,
with no collinear triple.

### Proof

The seed is saturated and decomposed into two permutation layers, so every
allowed transition preserves exactly two points in each row and column.
Apply AC4a whenever a local bank freezes and use the delegated interfaces
in outcomes 2 and 3.  The resulting batch satisfies AC5a by assumptions
3--4.  Descending scale induction therefore removes every bad line.  The
final saturated state has zero triple potential and hence no collinear
triple. \(\square\)

## Remaining nonformal obligations

The lemmas above deliberately leave the following items open:

- AC1's certificate concentration with multiplicity;
- AC2's constant-fraction paid re-extraction;
- AC3's explicit bounded integer potential and no-recycling proof;
- verification that every BDA and rational-inverse return state obeys the
  AC5 scale contract.

Those are precisely the places where arithmetic or geometric input is
still needed; none can be replaced by finiteness alone.
