# Fixed-centre local-credit concentration splits into seven existing roles

The five-chain normal form PP3adu--PP3aea writes the deterministic local `Xi`
cost around a captive centre as

```text
D(h)
=
a(p,c)+a(c,s)
+beta_L(r,p)+beta_M(p,s)+beta_R(s,t)
+gamma_in(p;s,t)+gamma_out(s;r,p)
```

for a source-clean chain

```text
h=(r,p,c,s,t).
```

Thus “local cost at the removal-credit scale” is a seven-role weighted
pigeonhole problem. If a dense family of clean chains is expensive, one fixed
role is expensive on many chains. Exact extension multiplicities then force a
large family of distinct heavy arcs, paths, or disjoint-arc patterns in one of
the already-localized fixed-centre geometries.

This chapter removes an unspecified deterministic local-credit core as an
independent marked-`Xi` frontier.

## 1. Seven-role heavy assignment

Fix `lambda>0`. For every chain `h=(r,p,c,s,t)` define its seven local role
weights

```text
w_1(h)=a(p,c),
w_2(h)=a(c,s),
w_3(h)=beta_L(r,p),
w_4(h)=beta_M(p,s),
w_5(h)=beta_R(s,t),
w_6(h)=gamma_in(p;s,t),
w_7(h)=gamma_out(s;r,p).
```

### Proposition PP3aeb -- PROVED

If `D(h)>=lambda`, then at least one role satisfies

```text
w_j(h)>=lambda/7.
```

For every family `H` of such chains, there is one fixed role `j` for which at
least `|H|/7` chains satisfy the displayed inequality.

#### Proof

The seven weights are nonnegative and sum to `D(h)`. The first statement is
the pigeonhole principle. Assign one qualifying role to every chain and
pigeonhole the seven assignments. ∎

## 2. Exact extension multiplicities

For one fixed local object, count the number of ordered five-chains through `c`
that can contain it in its displayed role.

### Proposition PP3aec -- PROVED

The extension multiplicities are at most:

```text
incoming unary arc p->c:
(N-2)(N-3)(N-4);

outgoing unary arc c->s:
(N-2)(N-3)(N-4);

left rank-three path r->p->c:
(N-3)(N-4);

middle rank-three path p->c->s:
(N-3)(N-4);

right rank-three path c->s->t:
(N-3)(N-4);

incoming rank-four cross-pair
(p->c, s->t):
N-4;

outgoing rank-four cross-pair
(c->s, r->p):
N-4.
```

#### Proof

For an incoming unary arc, after fixing `p`, choose the three remaining
noncentre chain indices `r,s,t` in order, avoiding all previously chosen
indices. This gives `(N-2)(N-3)(N-4)` choices. The outgoing case is symmetric.

After fixing any displayed rank-three path, two ordered noncentre indices
remain, giving `(N-3)(N-4)` choices.

After fixing either displayed rank-four cross-pair, exactly one outer chain
index remains, giving `N-4` choices. ∎

The counts are upper bounds for an arbitrary source-clean subfamily and exact
for the complete family of all ordered five-chains through `c`.

## 3. Distinct heavy local objects

Let `H` be any family of source-clean five-chains satisfying `D(h)>=lambda`.
Let `H_j` be the role class returned by PP3aeb.

### Theorem PP3aed -- PROVED

At least one of the following holds.

1. There are at least

   ```text
   |H|/[7(N-2)(N-3)(N-4)]
   ```

   distinct incoming or outgoing centre arcs of weight at least `lambda/7`.

2. There are at least

   ```text
   |H|/[7(N-3)(N-4)]
   ```

   distinct left, middle, or right rank-three paths of weight at least
   `lambda/7`.

3. There are at least

   ```text
   |H|/[7(N-4)]
   ```

   distinct incoming or outgoing rank-four cross-pairs of weight at least
   `lambda/7`.

#### Proof

Choose the fixed heavy role from PP3aeb. Divide `|H_j|>=|H|/7` by the
corresponding maximum extension multiplicity in PP3aec. Distinct chains
projecting to the same local object are counted at most that many times. ∎

## 4. Dense-chain scale

Suppose

```text
|H|>=eta (N-1)(N-2)(N-3)(N-4)
```

for some fixed or `N^{-o(1)}` value `eta>0`.

### Corollary PP3aee -- PROVED

The three alternatives in PP3aed have respective sizes

```text
Omega(eta N),
Omega(eta N^2),
Omega(eta N^3).
```

Their total local weights are respectively

```text
Omega(eta lambda N),
Omega(eta lambda N^2),
Omega(eta lambda N^3).
```

#### Proof

Substitute the dense-chain lower bound into PP3aed and use that every retained
object has weight at least `lambda/7`. ∎

At the slab-optimal scales, even with `eta=m^{-o(1)}`, the unary family contains
a `W`-sized arc-petal bank, while the rank-three and rank-four support degrees
are stronger than the `Omega(N^2/b)` and `Omega(N^3/b^2)` cores returned by the
full-pool truncation theorem.

## 5. Handoff to the existing fixed-centre chains

### Corollary PP3aef -- PROVED

Each alternative of PP3aee is an existing object.

1. Heavy unary arcs feed PP3ada--PP3adg.
2. Heavy left or right rank-three paths feed the outer path-petal theorem
   PP3act--PP3acz.
3. Heavy middle paths feed the paid two-resource grid PP3aco--PP3acs.
4. Heavy rank-four cross-pairs are fixed-centre partner-fibre support and feed
   PP3abv--PP3acn.

Consequently dense deterministic local-credit failure creates no new geometry.

#### Proof

The role definitions are exactly the weight definitions in the cited theorem
chains. The support lower bounds of PP3aee meet or exceed their stated input
scales. ∎

## 6. Revised local-credit endpoint

### Corollary PP3aeg -- PROVED

For a captive centre with a dense source-clean five-chain family, deterministic
local `Xi` cost at scale `lambda` reduces to:

1. a chain with `D(h)<lambda`, followed by the exact paid criterion PP3ady;
2. a target-size heavy unary arc-petal bank;
3. a dense heavy rank-three outer path family or middle choice grid;
4. a dense fixed-centre rank-four partner family;
5. failure of source-clean chain density.

Therefore local-credit concentration is no longer an unspecified marked-centre
core. It rejoins the arc/path-petal, paid-grid, rank-four Hall/support, or source
transition frontiers.

## 7. Finite diagnostic

The script

```text
scripts/check_fixed_centre_local_credit_roles.py
```

enumerates ordered five-chains through one centre, applies the seven-role
assignment, verifies the extension-multiplicity bounds, and extracts the
distinct heavy local objects in the dominant role. The stored example puts all
local cost in the middle rank-three role and returns the complete fixed-centre
middle choice grid.
