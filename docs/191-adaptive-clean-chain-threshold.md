# Adaptive clean-chain conditioning closes vanishing residual objectives

The clean-chain supply theorem PP3aeh--PP3aem used the fixed threshold

```text
q=N/log N
```

to obtain a clean family of density at least `1/(3log^4 N)`. The inverse-
density theorem PP3aen--PP3aet then required the unrestricted residual objective
to be `o(1/log^4 N)`.

That loss is unnecessary. Choose the outer-choice threshold from the residual
objective itself. If the unrestricted nonnegative residual expectation is
`epsilon=o(1)`, take a threshold proportion at least `epsilon^(1/8)`. The clean
family then has density `Omega(epsilon^(1/2))`, while conditioning costs the
reciprocal density. The conditioned residual objective is therefore
`O(epsilon^(1/2))=o(1)`.

The threshold also dominates the sparse middle transition relation. Hence the
only alternative is the already-localized near-complete predecessor or
successor transition role-star.

This removes an explicit polylogarithmic residual-source threshold from the
marked-centre frontier.

## 1. Adaptive threshold

Retain the transition relations and threshold sets of PP3aeh:

```text
L_c={(r,p): r->p->c is source-invalid},
M_c={(p,s): p->c->s is source-invalid},
F_c={(s,t): c->s->t is source-invalid},
```

and

```text
P_q={p: |A_L(p)|>=q},
S_q={s: |A_F(s)|>=q}.
```

Let `X` be any nonnegative residual objective on the unrestricted marked
block-cycle state space `Omega_c`, and put

```text
epsilon=E_{Omega_c} X.
```

Assume `0<=epsilon<=1`. Define

```text
alpha
=
max{
 epsilon^(1/8),
 sqrt(2(|M_c|+N))/N,
 4/N
},
```

and

```text
q=ceil(alpha N).
```

### Proposition PP3afb -- PROVED

Suppose `alpha=o(1)`. Then `q=o(N)`, `q>=4`, and for all sufficiently large
`N`, `q<=N-2`. Moreover

```text
q^2>=2(|M_c|+N).
```

#### Proof

The first statements follow immediately from the definition and
`alpha=o(1)`. Since `q>=alpha N`, the final inequality follows from the second
term in the maximum. ∎

At the slab-optimal scale, `|M_c|=m^(1+o(1))` and
`N=m^(19/20+o(1))`, so `(|M_c|+N)/N^2=o(1)`. Thus `alpha=o(1)` whenever
`epsilon=o(1)`.

## 2. Adaptive clean-bank or role-star dichotomy

Let `C_c` be the source-clean ordered five-chain family through `c`.

### Theorem PP3afc -- PROVED

For the adaptive threshold above and all sufficiently large `N`, at least one of
the following holds.

1. **Adaptive clean bank:**

   ```text
   |C_c|>=q^4/16.
   ```

2. **Predecessor role-star:** fewer than `q` middle indices have at least `q`
   safe predecessors, and every other middle index has at least

   ```text
   N-q-1
   ```

   forbidden predecessors.

3. **Successor role-star:** the transposed statement holds.

#### Proof

Apply PP3aei. Proposition PP3afb rules out its middle-saturation alternative.
If neither role-star occurs, PP3aeh gives

```text
|C_c|
>=
(q^2-|M_c|-N)(q-1)(q-2).
```

The first factor is at least `q^2/2`. For `q>=4`, the final product is at least
`q^2/4`. Hence `|C_c|>=q^4/8`; the displayed weaker bound follows. ∎

Because `q=o(N)`, either star alternative is near-complete outside `o(N)`
exceptional middle indices and feeds PP3zw--PP3aaj.

## 3. Density and inverse-density balance

Put

```text
delta=|C_c|/(N-1)_4
```

in the clean-bank branch.

### Corollary PP3afd -- PROVED

In the adaptive clean-bank branch,

```text
delta>=alpha^4/32>=sqrt(epsilon)/32.
```

Consequently

```text
(1/|C_c|) sum_{h in C_c} E[X|h]
<=
epsilon/delta
<=
32 sqrt(epsilon).
```

#### Proof

Theorem PP3afc and `(N-1)_4<=N^4` give

```text
delta>=q^4/(16N^4)>=alpha^4/16.
```

The displayed weaker constant allows all finite rounding conventions. Since
`alpha>=epsilon^(1/8)`, the density lower bound follows. Apply the sharp
inverse-density inequality PP3aeo. ∎

Thus every unrestricted residual objective tending to zero remains `o(1)`
after conditioning on an adaptively chosen source-clean five-chain bank.

## 4. Joint source and off-centre paid objective

Use

```text
X
=
Y^off + J^off/R_c,
```

where `Y^off` is the residual source-invalid count and `J^off` is off-centre
`Xi` insertion cost. Put

```text
epsilon_c
=
U_src(c)+U_Xi/R_c.
```

### Theorem PP3afe -- PROVED

Assume `epsilon_c=o(1)` and the slab-optimal middle-relation bound. Then one of
the following holds.

1. A source-clean five-chain family has conditioned average residual objective

   ```text
   O(sqrt(epsilon_c))=o(1).
   ```

2. A near-complete predecessor or successor transition role-star occurs and
   feeds the credited transition-petal chain PP3zw--PP3aaj.

#### Proof

Apply PP3afc--PP3afd to the displayed nonnegative joint objective. ∎

This theorem does not assume independence between source and paid residual
terms or inside the clean-chain family.

## 5. Removing the explicit residual-source threshold

The fixed-centre degree-saving theorem PP3aeu--PP3afa gives the residual source
alternative:

- either the unrestricted source objective is `o(1)`;
- or a marked or global unary forbidden-cell star of target size occurs.

The full-pool `Xi` truncation theorems PP3adh--PP3adt give the paid analogue:

- either the unrestricted off-centre paid objective is `o(R_c)` at its displayed
  truncation scale;
- or a fixed-centre heavy unary arc, rank-three path, or rank-four partner core
  occurs.

### Corollary PP3aff -- PROVED

After the preceding source and `Xi` truncations, the adaptive theorem
PP3afe supplies a source-clean bank with vanishing conditioned residual
objective unless one of the already-listed unary, arc/path-petal,
rank-four-partner, or transition-petal cores occurs.

Hence the condition

```text
U_src(c)=o(delta)
```

from PP3aeq is no longer a separate hypothesis: the clean density may be chosen
adaptively from the unrestricted residual objective.

#### Proof

If both unrestricted residual pieces vanish, apply PP3afe. If either does not,
apply PP3aeu--PP3afa or PP3adh--PP3adt before conditioning. ∎

## 6. Revised marked-centre endpoint

### Corollary PP3afg -- PROVED

The marked-centre branch now reduces to payment or conversion of:

1. a unary source-star or credited resource bank;
2. a unary `Xi` arc-petal or rank-three path-petal bank;
3. a weighted middle grid or candidate-rich projective cover;
4. a rank-four conditional-Hall or alternating-host family;
5. a credited transition-petal/resource bank;
6. deterministic local pattern cost already comparable with removal credit;
7. endpoint-host failure.

Failure of dense clean-chain supply, an opaque inverse-density source threshold,
and diffuse off-centre residual concentration are no longer independent cases.

## 7. Finite diagnostic

The script

```text
scripts/check_adaptive_clean_chain_threshold.py
```

computes the adaptive threshold, enumerates all source-clean five-chains,
verifies the `q^4/16` lower bound, and checks the inverse-density estimate
`32sqrt(epsilon)`. It also reports the predecessor or successor role-star
branch when one thresholded outer-choice set is too small.
