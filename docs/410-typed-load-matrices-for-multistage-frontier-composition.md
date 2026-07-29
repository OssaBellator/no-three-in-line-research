# Typed load matrices for multistage frontier composition

`docs/404` combines type-specific kernels using one maximum load and one
target-support overlap multiplicity per stage.  That scalar product can lose
substantial information when only certain source types feed certain target
types.  This chapter records the exact finite-dimensional load-matrix
calculus.  Multistage reverse load is controlled by a product of nonnegative
type matrices.

The statements are general interfaces.  They do not construct the
prime-patching stage kernels.

## 1. Block reverse-load matrices

Partition the source and target sets as

```text
X=disjoint_union_(i=1)^p X_i,
Y=disjoint_union_(j=1)^q Y_j.
```

For a row-stochastic kernel `P:X->Y`, define its block load matrix by

```text
M_P(i,j)
 =max_(y in Y_j)
   sum_(x in X_i)P(x,y).
```

### Theorem PP3bxs -- PROVED / BLOCK LOAD ENVELOPE

The ordinary reverse-column load satisfies

```text
lambda(P)
 <=max_j sum_i M_P(i,j)
 =||1^T M_P||_infinity.
```

More generally, if the incoming mass at every source in type `X_i` is bounded
by `b_i`, then the outgoing column load on every target in type `Y_j` is at
most

```text
(b^T M_P)_j.
```

#### Proof

For a target `y in Y_j`, split its column by source type:

```text
sum_x P(x,y)
 =sum_i sum_(x in X_i)P(x,y)
 <=sum_i M_P(i,j).
```

With source multipliers bounded by `b_i`, the `i`th block contributes at most
`b_i M_P(i,j)`.  Summing gives the vector form. ∎

The scalar type-overlap theorem `PP3bxb` follows by bounding the nonzero
entries of each column crudely.

## 2. Matrix composition

Let `P:X->Y` and `Q:Y->Z` use compatible partitions, and let `M_P,M_Q` be
their block load matrices.

### Theorem PP3bxt -- PROVED / ELEMENTWISE LOAD-MATRIX COMPOSITION

The composite kernel satisfies the elementwise inequality

```text
M_(PQ)<=M_P M_Q.
```

For a sequence of compatible stages `P_1,...,P_s`,

```text
lambda(P_1...P_s)
 <=||1^T M_(P_1)...M_(P_s)||_infinity.
```

#### Proof

Fix a source type `i` and target `z` in final type `k`.  Then

```text
sum_(x in X_i)(PQ)(x,z)
 =sum_j sum_(y in Y_j)
   [sum_(x in X_i)P(x,y)]Q(y,z)
 <=sum_j M_P(i,j)
   sum_(y in Y_j)Q(y,z)
 <=sum_j M_P(i,j)M_Q(j,k).
```

Maximize over `z` to obtain the elementwise inequality.  Iterate it and apply
`PP3bxs` at the final stage. ∎

This retains the full allowed type-transition pattern instead of multiplying
worst stage constants.

## 3. Type-dependent conditioning

Suppose actions are deleted from `P`, leaving row mass

```text
g(x)>=p_i>0
```

for every `x in X_i`, and normalize the retained rows.

### Theorem PP3bxu -- PROVED / DIAGONAL CONDITIONING PENALTY

Let

```text
D_p=diag(1/p_1,...,1/p_p).
```

Then the conditioned block load matrix obeys

```text
M_(P^G)<=D_p M_P.
```

Thus type-dependent retained masses enter a multistage bound as diagonal
matrices, rather than through the single worst value `min_i p_i`.

#### Proof

For `y in Y_j`,

```text
sum_(x in X_i)P^G(x,y)
 =sum_(x in X_i)P(x,y)/g(x)
 <=(1/p_i)sum_(x in X_i)P(x,y).
```

Take the maximum over `y`. ∎

## 4. Repeated typed stages and spectral closure

### Corollary PP3bxv -- PROVED / TYPE-SPECTRAL CONTRACTION

Suppose compatible level kernels

```text
P_1,P_2,...,P_n
```

share one finite type alphabet and every block load matrix is bounded
elementwise by the same square matrix `M`.  Then

```text
lambda(P_1...P_n)<=||1^T M^n||_infinity.
```

If the spectral radius satisfies

```text
rho(M)<1,
```

these loads tend to zero exponentially.

More explicitly, if a positive vector `u` and `rho<1` satisfy

```text
u^T M<=rho u^T,
```

then, after normalizing `min_i u_i=1`,

```text
lambda(P_1...P_n)
 <=(max_i u_i) rho^n.
```

#### Proof

The first statement follows from `PP3bxt` and monotonicity of products of
nonnegative matrices.  Since `1^T<=u^T` coordinatewise under the normalization,

```text
1^T M^n
 <=u^T M^n
 <=rho^n u^T.
```

Take the largest coordinate.  Perron--Frobenius theory supplies such
subeigenvectors for every `rho` strictly above the spectral radius, proving
exponential decay when `rho(M)<1`. ∎

A multitype procedure may therefore contract even when some individual type
transition has load above one, provided the complete type-transition matrix
has spectral radius below one.

## 5. Revised integration frontier

The six active branches can now export matrices rather than isolated scalar
loads:

- boundary-core and corridor types index source rows;
- target hubs and repair reservoirs index target columns;
- finite-depth Hall certificates bound individual matrix entries;
- conditioning contributes diagonal penalties;
- shell or repair stages multiply their matrices.

The remaining integration task is to construct these matrices geometrically
and prove that their finite product, or repeated spectral radius, is below
one.

## 6. Finite diagnostic

The script

```bash
python scripts/check_typed_load_matrix_composition.py
```

uses exact rational kernels to verify every block entry of a two-stage
composition, the diagonal conditioning inequality, and the repeated-stage
spectral bound.

The next theorem identifier after this chapter is `PP3bxw`.
