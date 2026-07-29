# Schur-complement elimination for type loads

`docs/416` replaces scalar load bounds by positive potentials for a nonnegative
type matrix. Large type systems often contain a transient collection that can
be solved internally before returning to a smaller core. This chapter gives an
exact elimination theorem: transient types contribute a nonnegative resolvent
correction to the core load matrix.

The statements are general. They do not identify the transient/core split for
the prime-patching type graph.

## 1. Block type matrix

Partition the types into transient types `X` and core types `Y`, and write the
nonnegative load matrix as

```text
M = [ A  B ]
    [ C  D ].
```

Assume

```text
rho(A)<1.
```

Then the nonnegative resolvent exists:

```text
R_A=(I-A)^(-1)=sum_(t>=0) A^t.
```

Define the effective core matrix

```text
S=D+C R_A B.
```

The correction sums every excursion that leaves the core, spends any number of
steps among transient types, and returns to the core.

### Theorem PP3bze -- PROVED / EXACT TYPE SCHUR ELIMINATION

Under `rho(A)<1`, one has

```text
rho(M)<1
```

if and only if

```text
rho(S)<1.
```

#### Proof

Use the positive-supersolution characterization from `PP3bym`.

Suppose first that `rho(M)<1`. Choose positive vectors `x,y` with

```text
Ax+By<x,
Cx+Dy<y.
```

The first inequality gives

```text
x>R_A B y.
```

Therefore

```text
Sy=Dy+C R_A B y<Dy+Cx<y,
```

so `rho(S)<1`.

Conversely, suppose `rho(S)<1`. Choose `y>0` with `Sy<y`. Since `rho(A)<1`,
choose `u>0` with `Au<u`. Put

```text
x=R_A B y+epsilon u.
```

Then

```text
Ax+By=R_A B y+epsilon Au<x.
```

Also

```text
Cx+Dy=Sy+epsilon Cu<y
```

for sufficiently small `epsilon>0`. Thus `[x;y]` is a positive strict
supersolution for `M`, proving `rho(M)<1`. ∎

## 2. Resolvent interpretation

### Corollary PP3bzf -- PROVED / TRANSIENT-EXCURSION LOAD SUM

The block

```text
C R_A B
 =sum_(t>=0) C A^t B
```

is the total load of all core-to-transient-to-core excursions. If positive
potentials `a_X,a_Y` satisfy

```text
A a_X<=q_X a_X,
B a_Y<=b a_X,
C a_X<=c a_Y,
D a_Y<=d a_Y
```

with `q_X<1`, then

```text
S a_Y<=(d+bc/(1-q_X))a_Y.
```

Hence the full type system contracts whenever

```text
d+bc/(1-q_X)<1.
```

#### Proof

From `A a_X<=q_X a_X`, the resolvent bound in `docs/416` gives

```text
R_A B a_Y<=b a_X/(1-q_X).
```

Apply `C`, add the direct core load `D a_Y`, and use the remaining potential
bounds. Then apply `PP3bze`. ∎

This is a scalar interface for a potentially large transient subsystem.

## 3. Certified finite truncation

### Theorem PP3bzg -- PROVED / FINITE EXCURSION TRUNCATION RESERVE

Under the hypotheses of `PP3bzf`, define the depth-`T` effective matrix

```text
S_T=D+sum_(t=0)^(T-1) C A^t B.
```

The omitted tail obeys

```text
(S-S_T)a_Y
 <=bc q_X^T/(1-q_X) a_Y.
```

Therefore a rational audit of `S_T` with potential margin `eta>0` remains valid
for the full Schur complement whenever

```text
bc q_X^T/(1-q_X)<eta.
```

#### Proof

The omitted series is

```text
sum_(t>=T) C A^t B.
```

Apply the potential inequalities successively to bound its action on `a_Y` by

```text
bc sum_(t>=T) q_X^t a_Y.
```

Evaluate the geometric tail. ∎

## 4. Revised integration frontier

A large typed repair system may now be reduced in three exact steps:

1. identify a transient block with a positive contraction potential;
2. sum its excursions into the effective core matrix `S`;
3. certify the much smaller core by a positive supersolution.

Finite excursion enumeration is sufficient when the geometric tail fits inside
the remaining potential margin.

## 5. Exact diagnostic

Run

```bash
python scripts/check_type_schur_elimination.py
```

The checker uses exact rational matrices to verify the block resolvent, the
Schur complement, the supersolution equivalence, and a finite truncation reserve.

The next theorem identifier after this chapter is `PP3bzh`.
