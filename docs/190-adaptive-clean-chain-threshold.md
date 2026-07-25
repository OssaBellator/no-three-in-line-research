# Adaptive clean-chain threshold absorbs every vanishing residual load

PP3aen--PP3aet bound the residual source and off-centre insertion objective on
a source-clean chain family by the unrestricted marked expectation divided by
the chain density. The fixed threshold `q=N/log N` gives only a polylogarithmic
loss. A threshold chosen from the actual residual expectation is stronger.

Let `epsilon_N` be the unrestricted normalized residual objective. Choose the
outer safe-choice threshold so that

```text
q/N >= epsilon_N^(1/8)
```

while also making `q^2` dominate the sparse middle relation. If the clean-bank
branch occurs, its density is `Omega((q/N)^4)`, hence at least
`Omega(sqrt(epsilon_N))`. The restricted residual expectation is then
`O(sqrt(epsilon_N))`.

If the clean-bank branch does not occur, the same threshold is `o(N)` and
therefore yields a near-complete transition role-star feeding the existing
credited-petal chain. Thus every unrestricted residual objective tending to
zero remains negligible after source-clean conditioning; no prescribed rate
of convergence is needed.

## 1. Adaptive threshold

Retain `N,c,M_c,P_q,S_q,C_c` from PP3aeh. Let `epsilon=epsilon_N` satisfy

```text
0<=epsilon<=1,
epsilon->0,
|M_c|=o(N^2).
```

Define

```text
alpha
=
max {
 epsilon^(1/8),
 sqrt(2(|M_c|+N))/N,
 4/N
},
```

and

```text
q=ceil(alpha N).
```

### Proposition PP3aeu -- PROVED

One has

```text
q=o(N),
q>=4,
q^2>=2(|M_c|+N),
(q/N)^4>=epsilon^(1/2).
```

#### Proof

Both `epsilon^(1/8)` and `sqrt(2(|M_c|+N))/N` tend to zero, while `4/N`
does also. Hence `alpha=o(1)` and `q=o(N)`. The remaining statements follow
from the definition and rounding upward. ∎

## 2. Density or near-complete role-star

### Theorem PP3aev -- PROVED

For the adaptive threshold `q`, at least one of the following holds.

1. **Adaptive clean bank:**

   ```text
   |C_c| >= q^4/16.
   ```

   Consequently its density

   ```text
   delta=|C_c|/(N-1)_4
   ```

   satisfies

   ```text
   delta >= epsilon^(1/2)/32
   ```

   for all sufficiently large `N`.

2. **Predecessor transition star:** all but `o(N)` middle indices have at
   least `(1-o(1))N` forbidden predecessors.

3. **Successor transition star:** the transposed statement holds.

#### Proof

Apply PP3aei. Middle saturation is impossible because
`q^2>=2(|M_c|+N)`. If both threshold sets have size at least `q`, PP3aeh gives

```text
|C_c|
>=
(q^2-|M_c|-N)(q-1)(q-2)
>=
(q^2/2)(q/2)(q/2)
=
q^4/8
```

for large `q`; the stated `q^4/16` is a weaker uniform bound. Since
`(N-1)_4<=N^4` and rounding changes `q/N` only by `o(1)`, PP3aeu gives the
density bound.

If one threshold set has size below `q`, PP3aei gives the corresponding
role-star. Because `q=o(N)`, both its exceptional set and safe degree are
`o(N)`, so the forbidden degree is `(1-o(1))N`. ∎

## 3. Absorbing the inverse-density loss

Let `X` be any nonnegative residual objective on the unrestricted marked
block-cycle state space and suppose

```text
E X <= epsilon.
```

### Corollary PP3aew -- PROVED

In the adaptive clean-bank branch,

```text
(1/|C_c|) sum_{h in C_c} E[X|h]
<=
32 epsilon^(1/2)
=
o(1).
```

#### Proof

Apply the inverse-density theorem PP3aeo and the lower bound
`delta>=epsilon^(1/2)/32` from PP3aev. ∎

Thus an arbitrary slowly vanishing expectation, including
`1/log log log N`, remains vanishing after conditioning.

## 4. Joint residual source and paid objective

Let

```text
epsilon_c
=
U_src(c)
+
U_Xi/R_c,
```

where `U_src(c)` is the unrestricted residual source expectation of PP3aeq and

```text
U_Xi
=
K[A_2 b/N^2+B_3 b/N^3+B_4 b^2/N^4]
```

is the unrestricted off-centre `Xi` bound of PP3aep.

### Theorem PP3aex -- PROVED

Assume `epsilon_c=o(1)`. With the adaptive threshold built from
`epsilon_c`, at least one of the following holds.

1. A source-clean chain family has averaged normalized residual objective
   `o(1)`.
2. A near-complete predecessor or successor transition role-star feeds the
   transition-petal/resource-bank chain PP3zw--PP3aaj.

#### Proof

Apply PP3aev. In the clean branch apply PP3aew to the sum of the source count
and off-centre insertion cost divided by `R_c`. In a star branch use
PP3aek. ∎

No quantitative convergence rate beyond `epsilon_c=o(1)` is required.

## 5. Complete marked-centre split

Let `C_Xi(h)` be the exact centre-supported cost from PP3adx.

### Corollary PP3aey -- PROVED

Under the marked source-light and diffuse off-centre hypotheses giving
`epsilon_c=o(1)`, the captive-centre branch has one of:

1. a clean chain whose residual source/off-centre objective is `o(1)` and whose
   exact centre cost satisfies the paid criterion;
2. deterministic local centre cost concentrated in one of the seven roles of
   PP3aeb--PP3aeg;
3. a boundary or remote rank-four centre partner mass from PP3adz;
4. a transition-petal/resource bank;
5. local pattern cost already comparable with removal credit;
6. a nonvanishing unrestricted marked source or off-centre objective.

The sixth alternative is an explicit marked concentration certificate, not a
loss caused by conditioning.

#### Proof

Use PP3aex. In the clean branch combine the residual `o(1)` objective with the
exact five-chain normal form PP3adx--PP3adz. Failure of its deterministic
local part is split by PP3aeb--PP3aeg. The star branch is the fourth
alternative. ∎

## 6. Revised residual-source endpoint

### Corollary PP3aez -- PROVED

Failure of the fixed threshold condition

```text
U_src(c)=o(delta)
```

from PP3aeq is no longer an independent frontier. The adaptive threshold
replaces it by the ordinary requirement

```text
U_src(c)+U_Xi/R_c=o(1).
```

If that requirement fails, the captive centre has a genuine nonvanishing
marked source or insertion-load certificate. If it holds, clean-chain
conditioning preserves it automatically or returns the transition-petal
branch.

## 7. Finite diagnostic

The script

```text
scripts/check_adaptive_clean_chain_threshold.py
```

computes the adaptive threshold from a finite middle relation and residual
expectation, enumerates the clean-chain family, verifies its density lower
bound when applicable, and checks the resulting inverse-density residual
bound.
