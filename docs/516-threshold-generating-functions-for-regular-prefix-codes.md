# Threshold generating functions for regular prefix codes

`docs/510` optimizes one fixed multiplicity vector by dynamic programming on an
automaton state. A generating-function version solves every multiplicity profile
at a fixed risk threshold simultaneously and counts the realizing legal codes.

Let `Q` be a deterministic automaton with accepting set `F`, symbol survivals
`p_0,p_1<1`, and risk classes `rho_i`. For a threshold `tau`, let
`P_q^tau(z)` be a multivariate polynomial truncated at the required maximum
multiplicities.

## 1. Threshold polynomial recurrence

### Theorem PP3cka -- PROVED / REGULAR PREFIX THRESHOLD POLYNOMIAL

The exact ordered-code generating polynomial satisfies

```text
P_q^tau(z)
 = sum_(i: q in F and rho_i<=tau) z_i
   + P_(delta(q,0))^(p_0 tau)(z)
     P_(delta(q,1))^(p_1 tau)(z).
```

The first term chooses a single leaf at the current node. The product chooses a
nonempty legal code in each child, as required by a full binary prefix tree.
Because the threshold is multiplied by a number below one at every descent, the
truncated recurrence is finite.

#### Proof

A legal full prefix tree is either one accepted leaf or has two nonempty child
trees. Prefixing a child word by symbol `b` divides realized survival by `p_b`,
so the child threshold is `p_b tau`. Multiplication adds class multiplicities and
counts independent ordered child choices. Induction over the finite truncated
recursion proves the identity. ∎

## 2. Feasibility, counting, and optimum extraction

### Theorem PP3ckb -- PROVED / COEFFICIENT CERTIFICATE

For a target multiplicity vector `m`,

```text
[z^m] P_(q0)^tau(z)
```

is exactly the number of ordered legal prefix codes with maximum realized risk
at most `tau`. It is nonzero exactly when the threshold is feasible.

For `K=|m|` leaves, every full binary tree has depth at most `K-1`. Hence the
optimum belongs to the finite set

```text
rho_i / product(symbol survivals along a legal word of length <=K-1).
```

Scanning that set in increasing order gives the exact optimum and its number of
realizations.

#### Proof

Coefficient extraction records exactly the leaf-class multiset in the recurrence
of `PP3cka`. A full binary tree with `K` leaves has no root-to-leaf path longer
than `K-1`, giving the finite candidate set. ∎

## 3. Stored exact fixture

### Theorem PP3ckc -- PROVED / UNIQUE GENERATING-FUNCTION WITNESS

The audit `scripts/check_regular_prefix_code_generating_function.py` forbids
`00`, uses survivals `(3/4,2/3)`, risks `(1/32,1/16,1/8)`, and multiplicities
`(3,2,1)`. The first nonzero target coefficient occurs at

```text
243/1024,
```

where the coefficient is exactly one. The threshold `3/16` has coefficient zero,
and the memoized polynomial evaluation visits 37 product states.

## 4. Prime-patching consequence

Regular-language marker legality can now be imposed before choosing one
multiplicity profile. A single finite polynomial table supplies feasibility,
counts, and the exact minimax threshold for an entire family of repair banks.
