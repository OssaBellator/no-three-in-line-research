# Adaptive sub-square-root sizing for marked source-star cascades

The bounded-depth path theorem PP3aib--PP3aig reduces final binary shadow to the
cumulative surviving size `S` of the cascade.  The natural boundary is

```text
S^2=R.
```

At the slab-optimal parameters this boundary is exactly the target patch width:

```text
R=m^(19/20+o(1)),
W=sqrt(R)=m^(19/40+o(1)).
```

A marked source-star move does not need a polynomially large subbank.  The marked
host preparation permits every sufficiently slowly growing size below the
established upper scales.  Therefore a planned cascade of any depth `d=o(W)` can
choose a common marked subbank size `q->infinity` with

```text
dq=o(W).
```

The final binary support is then `o(R)`.  More importantly, if final unary shadow
still destroys a controller-domain margin, PP3aie gives a source star of degree

```text
Omega(R/(dq))=omega(W).
```

Thus every failed stage still returns more than target width.  Cumulative state
growth and star extraction are simultaneously compatible throughout every
sub-`W` cascade depth.

## 1. The square-root domain scale

Put

```text
W_R=sqrt(R).
```

At the active slab scale, `W_R=W` up to `m^(o(1))` factors.

### Proposition PP3aih -- PROVED

Let `d=d_R` satisfy

```text
1<=d=o(W_R).
```

There is an integer sequence `q=q_R` such that

```text
q->infinity,
dq=o(W_R),
q^3/R=o(1),
```

and `q` lies below every previously imposed polynomial marked-subbank upper
scale.

One explicit asymptotic choice before taking the minimum with earlier upper
scales is

```text
q=floor(sqrt(W_R/d)).
```

#### Proof

Since `d=o(W_R)`, the ratio `W_R/d` tends to infinity, so `q->infinity`.  Also

```text
dq/W_R <= sqrt(d/W_R)=o(1).
```

Because `q<=sqrt(W_R)=R^(1/4)`,

```text
q^3/R <= R^(3/4)/R=R^(-1/4)=o(1).
```

Taking the minimum with any finite family of divergent admissible upper scales
preserves divergence after slowing the choice further if necessary. ∎

The last condition is stronger than the self-recapture requirement used in
PP3afp and PP3agb.

## 2. Cumulative final support

Consider at most `d` source-valid controller-preserving marked trades, each
inserting at most `q` points.  Let `S` be the number of genuinely new points that
survive in the final source.

### Corollary PP3aii -- PROVED

With the choice of PP3aih,

```text
S<=dq=o(W_R)
```

and hence

```text
S^2=o(R).
```

All final binary insertion shadow is absorbed by every fixed positive
controller-domain margin.

#### Proof

The final new set is contained in the union of the inserted sets, so `S<=dq`.
Square and use `W_R^2=R`.  Apply PP3aic or PP3ahd. ∎

No cancellation or independence is needed for this binary conclusion.

## 3. Every failed final margin gives a super-target star

Fix `xi>0`.  Suppose final binary support fits the margin but final unary support
destroys one domain margin.  PP3aie produces a final source-star centre of
degree greater than `xi R/(2S)`.

### Theorem PP3aij -- PROVED

Under PP3aii, every failed final unary margin yields a source star of degree

```text
C > xi R/(2S)=omega(W_R).
```

In particular the star contains a target-size substar of size

```text
W=m^(19/40+o(1)).
```

#### Proof

Since `S=o(W_R)` and `R=W_R^2`,

```text
R/S=W_R(W_R/S)=omega(W_R).
```

Multiply by the fixed constant `xi/2`.  The target width agrees with `W_R` up to
subpolynomial factors, so a target substar exists. ∎

This is stronger than merely preserving a positive-density star: the margin
failure automatically supplies the exact prime-patching width.

## 4. Compatibility with marked self-recapture

Let the ambient matching layer for each newly created star centre have size

```text
Q_a=Omega(R).
```

The marked source-star theorem gives selected-line self-recapture at most

```text
K C(q-2)/(Q_a-2).
```

### Proposition PP3aik -- PROVED / CONDITIONAL ON MARKED HOST PREPARATION

With the common subbank size of PP3aih and `K=1+o(1)`, every one of the at most
`d` marked moves satisfies

```text
E I_self/C=o(1).
```

Moreover the union-bound scale for selecting all `d` subbanks obeys

```text
d q^3/R=o(W_R)*o(1/W_R)=o(1)
```

after choosing `q` one additional slowly varying factor below the explicit
PP3aih value.

#### Proof

Since `q=o(W_R)` and `Q_a=Omega(W_R^2)`, one has `q/Q_a=o(1)`.  For simultaneous
selection, PP3aih gives freedom to replace `q` by any slower divergent sequence.
Choose it so that `dq^3/R=o(1)` in addition to `dq/W_R=o(1)`; this is possible
because `d=o(W_R)` and the admissible ratio `W_R/d` diverges.  Apply PP3agk at
each marked centre and sum the failure probabilities. ∎

The theorem does not assert independence between generations.  Sequential
conditioning and the tower property suffice once every post-trade marked host
satisfies the same prepared bounds.

## 5. Direct cascade interface

### Theorem PP3ail -- PROVED / CONDITIONAL DIRECT-CASCADE INTERFACE

Fix a planned depth `d=o(W)` and choose `q` as above.  Suppose a sequence of at
most `d` source-valid controller-preserving marked source-star moves can be
selected and the final retained-original base domains have fixed margin.
Then exactly one of the following occurs.

1. Final unary support fits the margin; final binary support is `o(R)` and the
   patch completes directly.
2. Final unary support destroys a margin and produces another source star of
   size `omega(W)`.
3. A marked source, transition, anchor, conditional-Hall, alternating-host, or
   distinguished endpoint-host obstruction prevents the next move.
4. The nonshadow base-domain margin or global allocation criterion fails.

Intermediate `Xi` multiplicity, intermediate lack of removal credit, and
cumulative binary support are absent from this list.

#### Proof

Use PP3aii to absorb final binary support and PP3aij for failed unary margin.
Path independence PP3aib removes all transient shadow.  The remaining failures
are precisely the hypotheses needed to select the path and invoke final
allocation. ∎

## 6. Scale consequence

### Corollary PP3aim -- PROVED

At the slab scale, a marked cascade may have any depth

```text
d=m^(delta+o(1)),
delta<19/40,
```

provided the marked subbank size is chosen slowly enough that

```text
dq=m^(delta+o(1))q=o(m^(19/40)).
```

Every final binary term remains domain-negligible, and every failed final unary
margin yields at least `m^(19/40+o(1))` distinct source-star incidences.

#### Proof

Here `d=o(W)`.  Apply PP3aih--PP3aij. ∎

For a fixed polynomial depth exponent, a polylogarithmic marked subbank is more
than sufficient whenever the marked host preparation allows it.

## 7. Revised cascade frontier

### Corollary PP3ain -- PROVED

Cumulative state growth is no longer an independent obstruction for every
planned cascade of depth `o(W)`.  Adaptive subbank sizing keeps the final new set
strictly below the square-root domain scale and preserves a target-size star at
every failed unary endpoint.

The remaining cascade work is:

1. proving that a required sequence of marked source-valid hosts exists;
2. controlling base source, transition, anchor, conditional-Hall, and
   alternating-host failures along the sequence;
3. proving termination, or otherwise bounding the number of generations by
   `o(W)`;
4. treating branches with no robust final allocation;
5. handling a genuinely final unary star that cannot be moved through the
   prepared marked infrastructure.

No termination theorem is claimed.  The new result shows that state-size and
self-recapture budgets do not prevent such a theorem below the natural target
width.

## 8. Finite diagnostic

The script

```text
scripts/check_adaptive_cascade_budget.py
```

computes the explicit subbank size, cumulative final-size bound, binary-domain
ratio, marked self-recapture scale, and guaranteed final-star lower bound for a
finite parameter instance.