# Chord localization inside a target-scale reference cycle

PP3ajb--PP3aje reduce a canonical nonterminating marked cascade to one
reference-oscillation cycle of row-length `L=Theta(W)`. The next question is
whether the ambient endpoint host supplies matching states beyond the two extreme
original/current states.

Normalize the host against the original matching. The original edges become
loops, the current defect cycle becomes one directed Hamilton successor cycle,
and every additional allowed off-diagonal edge is a **chord**. The chord set has
an exact sparse/dense localization.

- Sparse chords leave a small feedback hub through which every nontrivial
  matching change must pass.
- Dense chords give either one endpoint lying on many canonical alternating
  cycles or a large family of cycles with distinct chord signatures.

Thus the target-scale cycle core feeds the existing mobility-hub and multistate
alternating-bank frontiers without another unspecified host case.

## 1. Normalized Hamilton-cycle host

Let `C=[L]` be the rows of the target-scale defect cycle. Normalize the original
matching to the loops

```text
i -> i.
```

After cyclic relabelling, normalize the current matching to

```text
i -> i+1 mod L.
```

Let `D` be the directed normalized endpoint host on `C`, containing every loop
and every Hamilton successor arc. Define the chord set

```text
E_ch={i->j in E(D): j != i, j != i+1 mod L}.
```

### Proposition PP3ajf -- PROVED

Every perfect matching of the bipartite endpoint host is a directed cycle cover
of `D`. Its nontrivial permutation cycles are exactly the alternating cycles by
which it differs from the original matching.

The current reference-oscillation state is the Hamilton directed cycle, while
the original state is the all-loop cover.

#### Proof

This is the normalized matching/permutation correspondence PP3tn and PP3um. An
off-diagonal permutation cycle alternates with the original loops to give the
corresponding even matching cycle. ∎

## 2. Sparse chords force a small feedback hub

Let `e=|E_ch|`, and let `X` be the set of all chord tails and heads. Fix one
Hamilton-cycle vertex `x_0` and put

```text
U=X union {x_0}.
```

### Theorem PP3ajg -- PROVED

Ignoring loops, the digraph `D-U` is acyclic. Consequently every nontrivial
alternating cycle and every nonidentity perfect matching state meets `U`, with

```text
|U| <= 2e+1.
```

In particular, if

```text
e=o(L),
```

then the target-scale endpoint host has an `o(L)` mobility hub.

#### Proof

Deleting every chord endpoint removes every chord. The only remaining nonloop
arcs are surviving subarcs of the Hamilton successor cycle. Deleting `x_0` breaks
that cycle into directed paths, so no nontrivial directed cycle remains. Every
nonidentity cycle cover contains a nontrivial directed cycle and must therefore
meet `U`. The size bound is immediate. ∎

This is an explicit feedback set, not merely an existential assignment-dual
certificate.

## 3. Dense chords give a star or a matching

View `E_ch` as a bipartite graph from chord tails to chord heads. Let

```text
Delta_ch
```

be its maximum degree on either side.

### Theorem PP3ajh -- PROVED

For every integer `Delta>=1`, at least one of the following holds.

1. One tail or head is incident with at least `Delta` chords.
2. There is a set of at least

   ```text
   e/(2Delta)
   ```

   chords with pairwise distinct tails and pairwise distinct heads.

#### Proof

If the first alternative fails, take a maximal matching of the chord bipartite
graph. Its tail and head endpoints cover all chords. If the matching has size
`s`, at most `2sDelta` chords meet those endpoints. Hence

```text
e <= 2sDelta,
```

which gives the second alternative. ∎

Taking

```text
Delta=ceil(sqrt(e))
```

gives either a `sqrt(e)` chord hub or an `Omega(sqrt(e))` distinct-signature
matching.

## 4. Every chord supplies a canonical alternating cycle state

For a chord

```text
a=(u->v),
```

follow the Hamilton successor cycle from `v` until returning to `u`. Together
with `a`, this path forms a simple directed cycle `Gamma_a`.

### Proposition PP3aji -- PROVED

Switching `Gamma_a` and retaining every original loop outside it gives a perfect
matching state. The state moves exactly the vertices of `Gamma_a`.

Distinct chords give distinct cycle states. If the chords have pairwise
distinct tails and heads, then their distinguished chord arcs are
resource-disjoint and each occurs in exactly one state.

#### Proof

The chord followed by the unique directed successor path closes at `u`, giving a
simple directed cycle. Switching one directed cycle gives a perfect matching by
PP3um. The switched state contains its defining chord, so two different chords
cannot give the same state. Distinct tails and heads give the final resource
statement. ∎

The Hamilton backbone paths may overlap; this overlap is the only remaining
state-family multiplicity.

## 5. Exact support law for a distinct-chord state family

Let

```text
a_1,...,a_s
```

be chords with distinct tails and heads, and choose one canonical cycle state
`Gamma_(a_j)` uniformly. For any compatible set `F` of at most three possible
inserted matching arcs, define

```text
m_r(F)=|{j:F subseteq E(Gamma_(a_j))}|,
Delta_r=max_(|F|=r) m_r(F).
```

### Proposition PP3ajj -- PROVED

For `1<=r<=3`,

```text
Pr(F is inserted)=m_r(F)/s <= Delta_r/s.
```

Every distinguished chord arc has probability exactly `1/s`. Hence a
rank-at-most-three source-validity first moment is diffuse whenever its weighted
support sums with cylinder factors `Delta_r/s` are `o(1)`. Failure gives an
explicit Hamilton-backbone arc, pair, or triple shared by many chord-cycle
states.

#### Proof

Only one canonical cycle state is chosen. Count exactly the states containing
`F`. A distinguished chord occurs only in its own state because the chord
signatures are distinct. ∎

This is the same one-variable support interface used in PP3vc--PP3vd, now derived
directly from a Hamilton reference cycle.

## 6. Dense-chord localization at target scale

### Theorem PP3ajk -- PROVED

Suppose the target-scale host has

```text
e >= eta L
```

chords for one fixed `eta>0`. Then at least one of the following occurs.

1. A tail or head lies on

   ```text
   Omega(sqrt(L))
   ```

   distinct canonical alternating cycles. This is a one-hub cycle family and
   feeds PP3uu--PP3uy.
2. There is a family of

   ```text
   Omega(sqrt(L))
   ```

   canonical cycle states with distinct chord tails and heads. It has the exact
   support law PP3ajj.
3. A rank-one, rank-two, or rank-three Hamilton-backbone support is shared by a
   positive fraction of those states.
4. Source-invalid or insertion-shadow mass is concentrated at the canonical
   cycle-state scale.

#### Proof

Apply PP3ajh with `Delta=ceil(sqrt(e))`. Since `e=Omega(L)`, either resulting
family has size `Omega(sqrt(L))`. In the matching case apply PP3aji--PP3ajj. In
the star case all canonical cycles contain the rich endpoint, so the rooted
cycle localization PP3uu--PP3uy applies. Negating the diffuse support and paid
conditions gives alternatives 3 and 4. ∎

No product-measure power is asserted for the overlapping backbone arcs.

## 7. Revised target-cycle endpoint

### Corollary PP3ajl -- PROVED

A target-scale reference-oscillation cycle of length `L=Theta(W)` has the
following exact split.

1. **Sparse chord host:** `e=o(L)`, yielding an `o(L)` feedback/mobility hub by
   PP3ajg.
2. **Dense chord star:** one endpoint belongs to `Omega(sqrt(L))` canonical cycle
   states.
3. **Dense distinct-signature bank:** `Omega(sqrt(L))` canonical cycle states
   have distinct chord tails and heads and the exact support law PP3ajj.
4. **Concentrated alternating support/cost:** one backbone arc, pair, triple, or
   paid-weight class persists in many states.
5. **Bare two-state oscillation:** the host has no useful chords beyond the
   original/current cycle pair.

Thus the target-scale cycle is no longer an unspecified alternating-host
obstruction. Its remaining geometry is a small feedback hub, a rooted cycle
star, a distinct-signature one-variable bank, concentrated backbone support, or
the explicit bare two-state core.

No completion of the no-three-in-line conjecture is claimed.
