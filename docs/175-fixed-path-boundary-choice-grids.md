# Fixed-path boundary choice grids

PP3aaw--PP3aay reduce transition path-bank failure to a core supported at the
captive centre `c`, or at a fixed pair `{u,c}` in the fixed-predecessor star case.
These fixed cores have an exact local-choice representation.

After a source-valid path

```text
u -> p -> c
```

is fixed, a single-cycle permutation has exactly one remaining incoming arc at
`u` and one remaining outgoing arc at `c`:

```text
x -> u,
c -> y.
```

The pair `(x,y)` is compatible exactly when it does not close a proper directed
cycle. Every compatible pair extends to the same number of Hamilton cycles. Hence
one-centre concentration is a unary boundary-choice problem, and two-centre
concentration is an exact two-resource choice grid with a single-cycle residual
law.

## 1. Exact boundary choices around a fixed path

Let `V` have size `N>=6`, and fix distinct indices `u,p,c`. Put

```text
R=V\{u,p,c}.
```

For `x,y in R`, prescribe

```text
x->u->p->c->y.
```

### Proposition PP3aaz -- PROVED

1. If `x=y`, the prescribed arcs contain the proper directed cycle

   ```text
   x->u->p->c->x,
   ```

   so no single-cycle permutation on `V` contains them.
2. If `x!=y`, the prescribed arcs form one directed path on five vertices and are
   contained in exactly

   ```text
   (N-5)!
   ```

   single-cycle permutations.

#### Proof

The first statement is immediate. For `x!=y`, contract the four-arc path to one
ordered block. There are `N-4` cyclic objects, hence `(N-5)!` directed cyclic
orders. ∎

Thus the compatible boundary-state set is

```text
S_boundary={(x,y) in R x R : x!=y}.
```

## 2. One-centre successor choice

For a path state whose only fixed-core concentration is at `c`, condition first on
the successor choice

```text
c->y,
y in R.
```

### Proposition PP3aba -- PROVED

Every successor choice `y in R` is contained with the fixed path in exactly

```text
(N-4)!
```

single-cycle permutations. Conditional on `y`, every compatible set of `r`
additional arcs has probability at most an absolute constant times `N^-r`, unless
it closes a proper directed cycle.

#### Proof

The three prescribed arcs form the path `u->p->c->y`. Contract it to one block,
leaving `N-3` cyclic objects and `(N-4)!` cyclic orders. Additional compatible arcs
are counted by further contractions. ∎

Let `a(y)` be the exact unary source or paid core cost created by choosing `c->y`,
and let `J_y` be the expected residual cost after this choice.

### Corollary PP3abb -- PROVED

A strict source-valid completion exists whenever the average over `y in R` of

```text
source residual first moment
+ (a(y)+J_y)/R_*
```

is below one.

Under diffuse residual terms, failure forces

```text
sum_{y in R} a(y) >= (1-o(1)) R_* |R|.
```

Thus a one-centre path-bank core is a linear weighted successor-choice star at
`c`, not a new high-rank obstruction.

## 3. Two-centre boundary grid

In the fixed-predecessor path-star case, the unresolved fixed core may depend on
both boundary choices `x->u` and `c->y`. Let

```text
mu(x,y)
```

be the exact local insertion weight or blocker multiplicity of the compatible
boundary state `(x,y)`.

Classify every remaining source-invalid pattern by the number `r` of additional
random arcs required after the four boundary/path arcs are fixed, and write its
total weight as `S_(x,y),r`.

### Theorem PP3abc -- PROVED

If

```text
(1/|S_boundary|) sum_{x!=y} [
  sum_{r=0}^3 K^r S_(x,y),r/N^r
  + (mu(x,y)+E[C_(x,y)])/R_*
] < 1,
```

then one compatible boundary pair and one conditional single-cycle completion are
source-admissible and have insertion cost below removal credit.

#### Proof

Choose `(x,y)` uniformly from the compatible boundary states and then choose a
uniform single-cycle completion containing the five-vertex path. Proposition
PP3aaz and contraction counting give the fixed-rank cylinder estimates. Average
the nonnegative source-violation count plus normalized paid cost. ∎

This is the single-cycle analogue of PP3ze.

## 4. Weighted failure and projective covering

Put

```text
W_boundary=sum_{x!=y} mu(x,y).
```

### Corollary PP3abd -- PROVED

Under diffuse support-ranked residual source and insertion terms, failure of
PP3abc forces

```text
W_boundary >= (1-o(1))R_* |S_boundary|.
```

Since

```text
|S_boundary|=(N-3)(N-4),
```

this is a quadratic weighted boundary core at the fixed-pair credit scale.

Whenever one retained source anchor or controller candidate witnesses boundary
states by collinearity, its state set is a partial matching between the incoming
and outgoing boundary choices, except for the already isolated axis degeneracies.
Therefore the weighted failure re-enters the projective-cover and resource-bank
reductions PP3zh and PP3aam--PP3aat.

## 5. Revised fixed-core endpoint

### Corollary PP3abe -- PROVED

The fixed-core alternatives of PP3aay reduce to:

1. a linear weighted unary boundary-choice star at the captive centre;
2. a quadratic weighted two-boundary choice grid at the fixed pair `{u,c}`;
3. a candidate- or source-anchor projective matching cover of that grid;
4. support-ranked residual source or insertion concentration;
5. paid completion under PP3abb or PP3abc.

Thus one-centre and two-centre path-bank concentration do not create new abstract
core types. They rejoin the existing conditional-star, paid-grid, and projective
resource-bank interfaces.
