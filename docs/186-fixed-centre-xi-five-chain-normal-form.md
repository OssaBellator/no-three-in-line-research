# Fixed-centre Xi five-chain normal form

The marked-filler reductions leave “centre-core” insertion cost as a named
residual term after averaging across arc, path, or transition petals. For the
dynamic excess potential this term is not a new support class. A single directed
cycle has a unique five-index neighbourhood

```text
r -> p -> c -> s -> t
```

around the captive centre. Rank-two unary and rank-three binary `Xi` cost through
`c` is deterministic on this chain. Rank-four binary cost through `c` consists
of the two centre arcs paired with compatible remote cycle arcs.

Choosing the remaining block indices uniformly and then a uniform conditional
single cycle gives exact probabilities for those partner arcs. The centre-core
term therefore has a closed formula. Failure is local cost already at the
removal-credit scale, a boundary or remote rank-four partner fibre at its exact
credit-normalized scale, or residual source/off-centre cost. There is no
additional unstructured `Xi` centre-core table.

## 1. The deterministic local centre cost

Let a controller pool have `N` tied endpoint indices. Fix distinct indices

```text
h=(r,p,c,s,t)
```

and the directed chain

```text
r -> p -> c -> s -> t.
```

Use the rank-two unary weights `a(i,j)` of PP3abf and the rank-three path weights
of PP3abn. Define

```text
L_23(h)
=
a(p,c)+a(c,s)
+beta_L(r,p)+beta_M(p,s)+beta_R(s,t).
```

### Proposition PP3adu -- PROVED

Every selected rank-two unary or rank-three binary `Xi` pattern whose endpoint
support contains `c` contributes exactly one summand to `L_23(h)`, and no other
rank-two or rank-three `Xi` pattern containing `c` can occur.

#### Proof

The cycle selects exactly the incoming arc `p->c` and outgoing arc `c->s`, giving
the two unary terms by PP3abf. By PP3abn--PP3abo, every rank-three binary pattern
through `c` is one of the three adjacent pairs

```text
r->p, p->c;
p->c, c->s;
c->s, s->t.
```

Their weights are the three displayed beta terms. ∎

Rank-one unary patterns and rank-two binary transpositions are absent from every
single-cycle state by PP3yx--PP3zb.

## 2. Rank-four partner classes around the chain

Use the rank-four weights of PP3abv:

```text
gamma_in(p;u,v)
```

for the pattern `p->c, u->v`, and

```text
gamma_out(s;u,v)
```

for `c->s, u->v`.

Let

```text
U=V\{r,p,c,s,t}.
```

The two rank-four patterns already forced by the chain have total weight

```text
D_4(h)
=
gamma_in(p;s,t)+gamma_out(s;r,p).
```

Define the boundary-extension mass

```text
E_1(h)
=
sum_{u in U} [
 gamma_in(p;t,u)+gamma_in(p;u,r)
 +gamma_out(s;t,u)+gamma_out(s;u,r)
].
```

Define the fully remote mass

```text
E_0(h)
=
sum_{u,v in U, u!=v} [
 gamma_in(p;u,v)+gamma_out(s;u,v)
].
```

### Proposition PP3adv -- PROVED

Apart from the two deterministic partner patterns in `D_4(h)`, every
rank-four pattern through `c` compatible with a cycle containing `h` belongs
to exactly one of the following classes.

1. A boundary extension `t->u` or `u->r`, counted in `E_1(h)`.
2. A directed arc `u->v` wholly inside `U`, counted in `E_0(h)`.

#### Proof

The fixed chain already uses the tails `r,p,c,s` and the heads `p,c,s,t`.
An additional compatible arc meeting the chain can therefore only leave the
free tail `t` or enter the free head `r`. The arc `t->r` closes the five-chain
as a proper directed cycle and cannot occur in a larger single cycle. Thus the
only one-new-index arcs are `t->u` and `u->r`. Every other compatible additional
arc has both endpoints outside the chain. The incoming and outgoing centre
roles are disjoint pattern classes by PP3abv. ∎

## 3. Exact joint block-and-cycle probabilities

Assume

```text
7<=b<=N.
```

Choose a uniform `(b-5)`-subset of `U`, adjoin the five chain indices, and then
choose a uniform directed Hamilton cycle on the selected block conditioned on
containing the four arcs of `h`.

### Proposition PP3adw -- PROVED

Every selected block has exactly

```text
(b-5)!
```

conditional single-cycle states. Moreover:

1. each prescribed boundary extension `t->u` or `u->r` occurs with probability

   ```text
   1/(N-5);
   ```

2. each prescribed fully remote arc `u->v` occurs with probability

   ```text
   (b-6)/((N-5)(N-6)).
   ```

Consequently the exact expected rank-four `Xi` cost through `c` is

```text
C_4(h)
=
D_4(h)
+E_1(h)/(N-5)
+(b-6)E_0(h)/((N-5)(N-6)).
```

#### Proof

The state count is PP3abp. A boundary extension requires one specified outside
index, selected with probability `(b-5)/(N-5)`, and then one additional
compatible arc under the five-chain conditional law, with probability
`1/(b-5)`. Their product is `1/(N-5)`.

A fully remote arc requires two specified outside indices, selected with
probability `(b-5)_2/(N-5)_2`, followed by the same one-arc conditional
probability `1/(b-5)`. Cancelling gives

```text
(b-6)/((N-5)(N-6)).
```

Linearity of expectation and PP3adv give the cost identity. ∎

## 4. Exact centre-Xi normal form

Put

```text
C_Xi(h)=L_23(h)+C_4(h).
```

### Theorem PP3adx -- PROVED

`C_Xi(h)` is the exact expected insertion cost of every unary or binary `Xi`
pattern whose endpoint-index support contains `c`, under the joint random
block and conditional single-cycle law through `h`.

#### Proof

PP3adu accounts for all possible rank-two unary and rank-three binary patterns
through `c`. PP3adw accounts for all rank-four binary patterns through `c`.
The lower cyclic support classes vanish identically, and unary/binary endpoint
patterns have support rank at most two/four respectively. The classes are
disjoint, so their costs add. ∎

Thus the previously named `J_h^core` term may be replaced by the displayed
formula whenever the centre neighbourhood is fixed.

## 5. Unified paid five-chain criterion

Let `S_h,u`, `0<=u<=3`, be the remaining source-invalid count or nonnegative
weight requiring `u` additional compatible arcs after the chain is fixed. Let

```text
J_h^off
```

be the exact expected `Xi` insertion cost of patterns whose endpoint support
does not contain `c`. Let `R_c>0` be the exact removal credit obtained by moving
the centre.

### Theorem PP3ady -- PROVED

If

```text
sum_{u=0}^3 S_h,u/(b-5)_u
+
[C_Xi(h)+J_h^off]/R_c
<1,
```

then one conditional single-cycle completion is source-valid and strictly
decreases `Xi`.

#### Proof

Use the exact conditional cylinder law PP3abp for the source terms, Theorem
PP3adx for the centre-supported insertion cost, and linearity for the off-centre
cost. An outcome below one has zero source-invalid count and insertion cost
below `R_c`. Apply PP3kx. ∎

## 6. Quantitative failure alternatives

Write

```text
D(h)=L_23(h)+D_4(h).
```

Let `rho_h` be the normalized source and off-centre objective:

```text
rho_h
=
sum_{u=0}^3 S_h,u/(b-5)_u
+
J_h^off/R_c.
```

### Corollary PP3adz -- PROVED

Fix `tau in (0,1)`. Suppose

```text
rho_h<=1-tau
```

and

```text
D(h)<=tau R_c/4.
```

If the paid criterion PP3ady fails, then at least one of

```text
E_1(h)
>=
(3tau/8) R_c (N-5),
```

```text
E_0(h)
>=
(3tau/8) R_c (N-5)(N-6)/(b-6)
```

holds.

#### Proof

If both displayed lower bounds fail, then the boundary and fully remote
rank-four expectations are each below `3tau R_c/8`. Together with
`D(h)<=tau R_c/4`, the total centre cost is below `tau R_c`. Adding
`rho_h<=1-tau` makes the PP3ady objective strictly below one, a contradiction.
∎

The first alternative is a fixed-centre boundary partner fibre at scale
`R_c N`. The second is a fixed-centre remote partner fibre at scale
`R_c N^2/b`. Both feed the rank-four fibre/support/Hall chain
PP3abv--PP3acn.

If either the residual bound or the deterministic local bound fails, the
obstruction is explicitly residual source/off-centre concentration or local
arc/path/cross-pair cost already at the centre's removal-credit scale.

## 7. Revised marked-centre endpoint

### Corollary PP3aea -- PROVED

For a source-clean five-index neighbourhood around a captive centre, unary and
binary `Xi` insertion cost through the centre reduces to:

1. the exact paid criterion PP3ady;
2. deterministic rank-two/rank-three/local-cross-pair cost at the removal-credit
   scale;
3. a boundary rank-four partner fibre of weight `Omega(R_c N)`;
4. a remote rank-four partner fibre of weight `Omega(R_c N^2/b)`;
5. residual source or off-centre paid concentration.

Therefore an unspecified `Xi` centre-core term is no longer an independent
frontier. Its rank-four alternatives rejoin the conditioned partner-support,
robust Hall, weighted-grid, and alternating-host chains already in the ledger.

## 8. Finite diagnostic

The script

```text
scripts/check_fixed_centre_xi_five_chain.py
```

enumerates small joint block-and-cycle instances containing a prescribed
five-chain. It checks the `(b-5)!` state count on every selected block, the exact
boundary and remote arc probabilities, the formula for `C_4(h)`, and the paid
versus boundary-fibre versus remote-fibre alternatives. The stored example
realizes the boundary-fibre branch.
