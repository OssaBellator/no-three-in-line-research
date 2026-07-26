# One-controller puncture frees a captive source star

A controller-shadow source star may be centred at a point `p` that belongs to the
fixed controller infrastructure.  Earlier conversions either moved free partners
or left a controller--controller star.  The remaining captivity costs only one
controller value.

Remove `p` from its controller pool before performing the marked endpoint trade.
Every designated star entry remains in the candidate universe, because a bad
entry witnessed by a noncontroller pair containing `p` cannot itself be
controlled by `p`.  Relative to the punctured infrastructure, `p` is an ordinary
free centre.  The puncture reduces one macro domain by at most one value, while
moving `p` removes the entire star credit.

This chapter gives both the paid-potential and robust direct-allocation forms of
that observation.

## 1. Puncturing one controller value

Let the fixed controller pools be

```text
E_1,...,E_M,
|E_i|=R,
```

inside one permutation layer.  Let `p in E_a` and define

```text
E_a^- = E_a\{p},
E_i^- = E_i  for i != a.
```

Let `V^-` be the candidate-entry universe obtained by deleting only entries whose
controller is `p`.

### Proposition PP3ake -- PROVED

For every controller edge `e != p`, every candidate cell `z`, and every retained
original source `S' subseteq S\{p}` containing `e`,

```text
B_(S')^+(z;e) subseteq B_S^+(z;e).
```

Consequently every controller-aware domain loses at most the single unavailable
value `p` when passing to the punctured retained-original infrastructure.  More
precisely,

```text
H_(i,A,B)^ctrl(S)\{p}
subseteq
H_(i,A,B)^ctrl(S\{p}; E_i^-),
```

and therefore

```text
|H_(i,A,B)^ctrl(S\{p};E_i^-)|
>=
|H_(i,A,B)^ctrl(S)|-1.
```

#### Proof

The blocker-pair inclusion is PP3ajm.  Same-slot anchor witnesses can only
disappear by PP3ajn.  Thus every old safe controller other than `p` remains safe.
Only `p` itself is unavailable as a controller value. ∎

### Corollary PP3akf -- PROVED

Fix constants `gamma,xi>0`.  If an original label pair has domain size at least

```text
(gamma+xi)R,
```

then, for sufficiently large `R`, the same label pair has punctured retained-
original domain size at least

```text
(gamma+xi/2)R.
```

Every original balanced ownership and global label matching chosen at threshold
`gamma+xi` therefore remains valid at threshold `gamma+xi/2` after one
controller puncture.

#### Proof

By PP3ake the domain loses at most one value.  For large `R`, `1<=xi R/2`.
The certificate statement is the graph-inclusion argument PP3ajp. ∎

The puncture cost is `1/R=o(1)` of one macro domain.

## 2. The star credit survives the universe change

Suppose `p` is the centre of distinct chosen blocker pairs

```text
{p,s_1},...,{p,s_C},
```

for distinct bad entries `v_1,...,v_C`.

### Proposition PP3akg -- PROVED

Every designated entry `v_j` belongs to `V^-`.  Deleting `p` removes all `C`
designated incidences from the punctured controller-shadow potential.

#### Proof

Let `e_j` be the controller of `v_j`.  The pair `{p,s_j}` is a noncontroller
blocker witness, so

```text
e_j notin {p,s_j}.
```

In particular `e_j!=p`, and deleting entries controlled by `p` does not delete
`v_j`.  Since every chosen blocker pair contains `p`, removing `p` destroys its
incidence. ∎

This is the decisive asymmetry: one controller value is sacrificed, but the
entire star credit remains visible.

## 3. Paid marked conversion after puncturing

After the puncture, regard `p` as a free endpoint relative to the remaining fixed
controller infrastructure.  Choose an ambient one-layer helper set containing
`p`, disjoint from every active controller, and use a source-valid marked
single-cycle or derangement state that moves `p`.

### Theorem PP3akh -- PROVED / CONDITIONAL MARKED-HOST INTERFACE

Let `Q` be the ambient helper-layer size and let the selected marked state have
size `q`.  Under a marked law with cylinder-spread constant `K`, the selected
star-line self-recapture satisfies

```text
E I_self <= K C (q-2)/(Q-2).
```

If the expected foreign insertion shadow is smaller than

```text
C[1-K(q-2)/(Q-2)],
```

then some source-valid state strictly decreases the punctured controller-shadow
potential `Psi_(V^-)`.

Failure is one of:

1. marked source, transition, anchor, Hall, alternating, or distinguished-host
   obstruction;
2. foreign unary or binary support concentrated at the star-credit scale;
3. lack of a sufficiently large controller-disjoint helper layer.

#### Proof

Proposition PP3akg supplies removal credit at least `C` in the fixed universe
`V^-`.  Relative to that universe `p` is free and every remaining controller is
preserved.  Apply the marked source-star amortisation theorem PP3agh--PP3agn. ∎

Thus a controller-centred star has the same paid interface as a free star after
one puncture.

## 4. Robust direct-allocation endpoint

The direct route does not need star credit or a monotone potential.  Let a
source-valid punctured marked state move `p` together with `q-1` helpers, and let
`N` be its `q` final inserted points.

### Theorem PP3aki -- PROVED / CONDITIONAL INITIAL ROBUST-CERTIFICATE INTERFACE

Assume the original controller-aware graphs at threshold `gamma+xi` contain the
balanced ownership and global matching required by PP3ho.  Suppose

```text
q+q(q-1) <= xi R/4.
```

Then exactly one of the following occurs.

1. Final unary support together with the binary term `q(q-1)` fits the remaining
   margin, and direct allocation completes.
2. More than `3xi R/4` final losses are unary.  One point of `N` is a free final
   source-star centre of degree

   ```text
   C_new > 3xi R/(8q).
   ```
3. The marked source-valid punctured state cannot be prepared.
4. The initial robust controller-aware allocation certificate was absent.

#### Proof

The puncture loses at most one controller value by PP3ake.  The final binary
support loses at most `q(q-1)` values by PP3aha--PP3aig.  The displayed bound
places their combined contribution below one quarter of the reserved margin for
large `R`.  If direct allocation fails despite the inherited base certificate,
more than `3xi R/4` losses are unary.  Split them by movement/refill type and by
their causing point in `N`, giving at most `2q` classes. ∎

At the active scale `R=W^2`, every choice

```text
q -> infinity,
q=o(W)
```

satisfies `q^2=o(R)` and gives

```text
C_new=omega(W).
```

## 5. Revised captive-star endpoint

### Corollary PP3akj -- PROVED

A source-star centre inside the fixed controller infrastructure is not a separate
geometric obstruction.  Sacrificing that one controller value yields one of:

1. a free-centre paid marked conversion;
2. robust direct completion;
3. a new free super-target source star;
4. an explicit marked-host or foreign-support obstruction;
5. failure of the initial controller-aware allocation theorem.

The controller--controller partner core of PP3akc remains useful as a
controller-preserving alternative, but it is no longer the only route out of a
captive centre.

No completion of the no-three-in-line conjecture is claimed.
