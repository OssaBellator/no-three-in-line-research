# Two-sided Schur potentials for localized Hall congestion

`docs/389` gives a one-sided diagonal scaling of the source overlap Gram matrix.
This chapter factors the same spectral constant through the source-target
incidence operator and permits independent positive potentials on sources and
targets. The result is an exact two-sided Schur variational principle.

The statements are general. No uniform source or target potential is constructed
for the prime-patching transport graph.

## 1. Incidence factorization

For a nonempty source subset `U`, let `Y=N(U)`, let every target have positive
capacity `v(y)`, and write

```text
D(x)=sum_(y in N(x)) v(y).
```

Define the normalized incidence matrix

```text
B(x,y)=sqrt(v(y)/D(x))  if y in N(x),
       =0                otherwise.
```

Then the normalized overlap Gram matrix from `PP3bun` is

```text
H_U=B B^T,
```

so its Perron eigenvalue `lambda(U)` equals `||B||_2^2`.

For positive functions `a:U->(0,infinity)` and `b:Y->(0,infinity)`, define

```text
P(a,b)
 = max_(x in U)
   [sum_(y in N(x)) v(y)b(y)]/[D(x)a(x)],

Q(a,b)
 = max_(y in Y)
   [sum_(x in U:y in N(x)) a(x)]/b(y).
```

### Theorem PP3bvs -- PROVED / TWO-SIDED SCHUR HALL CRITERION

For every positive pair `(a,b)`,

```text
lambda(U) <= P(a,b) Q(a,b).
```

Consequently

```text
v(N(U)) >= S_1(U)/[P(a,b)Q(a,b)]
```

and

```text
w(U)/v(N(U))
 <= P(a,b)Q(a,b) w(U)/S_1(U).
```

#### Proof

Apply the weighted Schur test to `B` with source weights

```text
p(x)=sqrt(D(x))a(x)
```

and target weights

```text
q(y)=sqrt(v(y))b(y).
```

The two Schur sums are exactly

```text
sum_y B(x,y)q(y)/p(x)
 = [sum_y v(y)b(y)]/[D(x)a(x)],
```

and

```text
sum_x B(x,y)p(x)/q(y)
 = [sum_x a(x)]/b(y),
```

with the sums restricted to incidences. Hence `||B||_2^2<=P Q`. Insert this into
`PP3bun`. ∎

## 2. Exact variational form

### Theorem PP3bvt -- PROVED / EXACT SOURCE-TARGET POTENTIAL OPTIMUM

The spectral congestion constant satisfies

```text
lambda(U)=inf_(a>0,b>0) P(a,b)Q(a,b).
```

#### Proof

The upper bound is `PP3bvs`. For the reverse inequality, choose nonnegative left
and right singular vectors `p,q` for the largest singular value `sigma=||B||_2`:

```text
Bq=sigma p,
B^T p=sigma q.
```

On every active irreducible component these vectors are positive. Setting

```text
a(x)=p(x)/sqrt(D(x)),
b(y)=q(y)/sqrt(v(y))
```

gives `P=Q=sigma`, hence `P Q=lambda(U)`. Reducible or zero-coordinate cases are
obtained componentwise or by a positive epsilon perturbation and a limit. ∎

Thus the localized-Hall spectral problem is exactly the least product of a
source-normalized outgoing-capacity factor and a target-normalized incoming-
source factor.

## 3. Concrete potential choices

Two choices recover useful congestion statistics without square roots.

1. With `a(x)=b(y)=1`, one has `P=1` and

   ```text
   Q=max_y n_U(y),
   ```

   the maximum target multiplicity.

2. With `a(x)=1` and `b(y)=n_U(y)`, one has `Q=1` and

   ```text
   P=max_x
     [sum_(y in N(x)) v(y)n_U(y)]/D(x),
   ```

   the maximum capacity-weighted average target multiplicity from `PP3bve`.

The two-sided principle permits intermediate choices that downweight congested
targets while compensating on sources.

### Corollary PP3bvu -- PROVED / TWO-SIDED INVERSE-SUPPORT ENVELOPE

Suppose a flaw with `s` compatible sources obeys

```text
D(x)>=a_0 s w(x)
```

for every source. If every nonempty subset `U` admits positive potentials with

```text
P(a_U,b_U)Q(a_U,b_U)<=C_0,
```

then

```text
gamma<=C_0/(a_0 s).
```

#### Proof

The capacity hypothesis gives `S_1(U)>=a_0 s w(U)`. Apply `PP3bvs` and maximize
over all source subsets. ∎

The Hall frontier can now be split between the two sides of the incidence graph:
prove outgoing capacity density on sources and construct potentials that balance
incoming target reuse. This is more flexible than bounding raw maximum target
multiplicity or an unscaled overlap row sum.

The next theorem identifier after this chapter is `PP3bvv`.
