# Fixed-centre residual source load collapses to unary support

The clean-chain inverse-density theorem PP3aen--PP3aet leaves one explicit
residual source threshold

```text
U_src(c)=Omega(delta),
```

where `delta>=1/(3log^4 N)` is the density of the source-clean five-chain
family.  The high-support part of this threshold can be removed at a fixed
centre.

The global bounds PP3jj and PP3jk lose one full power of the pool size when one
endpoint index is prescribed.  For anchored pairs this follows by the same
multiplicative-energy argument with one factor fixed.  For inserted triples it
follows from the line-column unique-completion argument with the marked index
included among the fixed indices.  Consequently every marked high-support
source term remains polynomially small even after multiplication by
`delta^(-1)=O(log^4 N)`.

The only surviving residual source alternatives are unary:

1. a large unary degree at the captive centre; or
2. a large full-pool unary graph.

Both alternatives contain a target-size fixed-resource unary star and therefore
feed the existing witness star/resource-bank conversion PP3wc--PP3wh and
PP3yc--PP3yi.

Thus the residual source threshold in PP3aes is no longer an independent
high-support source core.

## 1. Fixed-centre anchored-pair degree

Let the pool have tied endpoint indices `V`, `|V|=N`, with distinct old columns
`x_i` and old rows `y_i`.  Fix `c in V`.  For a retained source anchor
`z=(u,v)`, two compatible inserted cells

```text
(x_i,y_j), (x_k,y_l)
```

are collinear with `z` exactly when

```text
(u-x_i)(v-y_l)=(u-x_k)(v-y_j).
```

Let `D_P(c)` be the number of distinct support-rank-four anchored-pair patterns
whose endpoint-index support contains `c`.

### Proposition PP3aeu -- PROVED

One has

```text
D_P(c)=O(m D_m N+N^2).
```

#### Proof

Pigeonhole the one of four endpoint-index roles occupied by `c`, and fix one
anchor `z`.  Consider, for example, the role `i=c`.

If `u!=x_c`, then for every choice of `l` the value

```text
n=(u-x_c)(v-y_l)
```

is fixed.  For `n!=0`, the number of pairs `(k,j)` satisfying

```text
(u-x_k)(v-y_j)=n
```

is at most `2D_m`, exactly as in PP3ji.  There is at most one choice of `l`
giving `n=0`, and its zero-product fibre has size `O(N)`.  Thus this role
contributes `O(D_m N+N)` for one nonaxis anchor.

If `u=x_c`, support rank four forces `k!=c`, hence `u-x_k!=0`.  The equality can
hold only when `v=y_j`.  There is at most one such pool row index `j`, after
which `(k,l)` have at most `O(N^2)` choices.  Only `O(1)` retained source points
lie on the old column `x_c` by saturation.

The roles in which `c` is a right index are transposed, with the only
degenerate anchors lying on the old row `y_c`.  Sum the generic bound over at
most `2m` retained anchors and the axis bound over `O(1)` anchors, then absorb
the four roles into the constant. ∎

The `N^2` axis term is harmless at the active pool scale.

## 2. Fixed-centre inserted-triple degrees

Let `D_h(c)` count compatible inserted collinear triples of endpoint-index
support rank `h` whose support contains `c`, for `h=4,5,6`.  Under a single-cycle
state, proper directed cycles are absent.

### Proposition PP3aev -- PROVED

One has

```text
D_4(c)=O(N^2),
D_5(c)=O(N^3),
D_6(c)=O(N^4).
```

#### Proof

There are only constantly many directed support structures and roles of `c`.

For support rank four, the three selected arcs form one directed path of length
three.  After fixing `c` and two further support indices, two inserted cells and
the old column or old row of the third cell are known.  The line through the
known cells is nonvertical or nonhorizontal in the required direction because
the cells are compatible.  Its intersection determines at most one final pool
index.  This gives `O(N^2)` patterns.

For support rank five, the structure is a directed two-arc path together with
one disjoint arc.  Fix `c` and three further support indices so that two cells
and one endpoint resource of the remaining cell are known.  The same
line-resource intersection determines the fifth index, giving `O(N^3)`.

For support rank six, the three arcs are vertex-disjoint.  Fix `c`, its partner
index, both indices of a second arc, and one endpoint index of the third arc.
The first two cells determine the line and the prescribed resource of the last
cell determines its remaining endpoint.  This gives `O(N^4)`.

The argument also covers the transposed roles, and the number of structures and
roles is absolute. ∎

This is the marked analogue of PP3jk with one support index prescribed.

## 3. High-support marked source load is uniformly negligible

Use the marked high-support expression from PP3xq,

```text
H_src(c)
=
K^2 D_P(c)b/N^3
+
K^3 [
 D_4(c)/N^3
 +D_5(c)b/N^4
 +D_6(c)b^2/N^5
].
```

### Corollary PP3aew -- PROVED

Uniformly in the marked centre,

```text
H_src(c)
=
O(
 mD_m b/N^2
 + b/N
 + 1/N
 + b^2/N
).
```

At

```text
N=m^(19/20+o(1)),
b=m^(kappa+o(1)),
0<kappa<19/80,
```

one has

```text
H_src(c)=m^(-Omega(1)).
```

Consequently, for every

```text
delta>=1/(3log^4 N),
```

```text
H_src(c)=o(delta).
```

#### Proof

Substitute PP3aeu--PP3aev.  The four relevant exponents are at most

```text
kappa-9/10,
kappa-19/20,
-19/20,
2kappa-19/20,
```

all strictly negative under the displayed range.  A polylogarithmic inverse-
density factor cannot remove a fixed polynomial saving. ∎

The unmarked pair/triple terms of PP3xq and the unmarked transition term of
PP3xx have the same or stronger polynomial savings.

## 4. Residual transition load vanishes on the clean chain

Every support-rank-three transition containing `c` is one of

```text
r->p->c,
p->c->s,
c->s->t
```

on the local five-chain.

### Proposition PP3aex -- PROVED

Conditioning on a source-clean five-chain makes the marked transition count
through `c` exactly zero.  The remaining transition expectation, whose patterns
avoid `c`, is

```text
O(mD_m b/N^2+b/N)=o(delta)
```

for `delta>=1/(3log^4 N)`.

#### Proof

The deterministic statement is the definition of the clean-chain family
PP3aeh.  The off-centre estimate is the unmarked term in PP3xx.  Its polynomial
decay survives the inverse-density loss. ∎

Proper directed-cycle source classes are zero under the single-cycle law, and
the remaining universal low-support terms are `O(1/b)`; choose the adaptive
filler size to make them `o(delta)`.

## 5. Exact residual unary alternative

Let `U_2` be the total full-pool support-rank-two unary forbidden-cell count,

```text
theta=U_2/N^2,
```

and let `d_U(c)` be the unary degree of the marked centre.

### Theorem PP3aey -- PROVED

For the clean-chain branch of PP3aej, after choosing the adaptive filler size so
that the universal low-support terms are `o(delta)`, the residual source
expectation satisfies

```text
U_src(c)
<=
K [
 d_U(c)/N
 + theta b
]
+o(delta).
```

Hence, for every fixed `rho>0`, if

```text
U_src(c)>=rho delta,
```

then, after reducing the constant, at least one of

```text
d_U(c)>=c_rho delta N,
```

```text
U_2>=c_rho delta N^2/b
```

holds.

#### Proof

Combine PP3yd with PP3aew and PP3aex, the unmarked estimates in PP3xq, and the
single-cycle zero classes.  If both unary terms were below a sufficiently small
constant multiple of `rho delta`, the full residual expectation would be below
`rho delta`. ∎

Thus no anchored-pair, inserted-triple, or transition degree survives as a
residual source threshold after clean-chain conditioning.

## 6. Both unary alternatives give a target resource star

### Proposition PP3aez -- PROVED

At the slab-optimal scales and for `delta>=1/(3log^4 N)`:

1. `d_U(c)>=c delta N` contains an incoming or outgoing fixed-resource unary
   star of size `Omega(delta N)`, hence a `W`-sized substar.
2. `U_2>=c delta N^2/b` contains some typed endpoint resource of unary degree

   ```text
   Omega(delta N/b),
   ```

   hence again a `W`-sized unary star.

#### Proof

For the marked alternative, split the support degree between the two typed
resources of `c`.

For the global alternative, sum unary incidences over the `2N` typed endpoint
resources and take one of at least average degree.  The exponent gaps are

```text
log_m(delta N/W)=19/40-o(1)>0,
```

and

```text
log_m(delta N/(bW))
=
19/40-kappa-o(1)>0.
```

Thus both stars contain `W=m^(19/40+o(1))` cells. ∎

Choosing one retained-source witness pair for every cell and applying
PP3we--PP3wg converts either star into a source-star centre, a resource-disjoint
credited endpoint bank, or concentrated insertion collateral.

## 7. Revised residual-source endpoint

### Corollary PP3afa -- PROVED

The residual source term in PP3aes reduces to:

1. a source-valid clean-chain completion;
2. a target-size unary forbidden-cell star feeding PP3wc--PP3wh and
   PP3yc--PP3yi;
3. the corresponding paid star/resource-bank collateral or endpoint-host
   failure;
4. failure of the adaptive unary-density hypothesis.

Fixed-centre anchored-pair degrees, rank-four through rank-six inserted-triple
degrees, and marked transition degree are no longer independent residual source
frontiers.

The remaining marked-centre work is payment or conversion of the already
extracted unary/resource, arc/path-petal, weighted-grid, conditional-Hall, and
alternating-host objects.

## 8. Finite diagnostic

The script

```text
scripts/check_fixed_centre_source_degree_saving.py
```

enumerates support-rank-four anchored pairs and support-rank-four through
support-rank-six inserted collinear triples on a finite endpoint pool.  It
reports the fixed-centre degrees, compares them with the one-power-saving
scales, evaluates the normalized marked source load, and checks the residual
unary star alternatives.
