# Recapture-free resource banks reduce to foreign shadow cores

The support-cleaning theorem PP3jt--PP3jx leaves three possible local support
concentrations on a two-scale endpoint bank:

```text
rich designated recapture,
foreign unary insertion shadow,
foreign binary insertion shadow.
```

The ambient-bank thinning theorem PP3afn--PP3aft removes the first alternative
before the endpoint permutation is chosen.  It produces a source-regular
`q`-subbank on which no off-diagonal replacement cell lies on any selected
credit line.  Hence the designated recapture support is empty, not merely
low-degree.

Combining this with the zero-cost permutation local lemma gives a sharper
resource-bank endpoint: either the trade has zero insertion shadow and positive
credit, or a linear set of endpoint indices carries genuinely foreign unary or
binary shadow degree.  The resulting quadratic unary and cubic binary cores
are exactly the already-localized source-star/resource-bank and
binary-star/fixed-cell-fan objects.

## 1. Joint source and recapture-free thinning

Let a full resource-disjoint credited bank have size

```text
Q=m^(21/40+o(1)).
```

Choose

```text
q=m^(kappa+o(1)),
0<kappa<1/40.
```

### Proposition PP3afu -- PROVED

The bank contains a `q`-subbank satisfying simultaneously:

1. the source-validity regularization of PP3jl--PP3jn;
2. zero designated self-recapture support;
3. at least `q` units of removal credit.

#### Proof

The source-thinning objective is `o(1)` by PP3jl--PP3jn.  The probability of
any selected credit-line self-recapture is `O(q^3/Q)=o(1)` by PP3afo--PP3afr.
Apply the joint-selection statement PP3afp.  Every retained endpoint keeps its
chosen credit incidence, so the selected removal credit is at least `q`. ∎

Write `d_1` for the maximum typed-resource degree of the residual **foreign**
unary insertion-shadow support and `d_2` for the corresponding binary support
degree.

## 2. Zero-cost endpoint without a recapture term

Let `lambda_src` be the low-support source-event resource mass after
regularization, and let `H_src` be the normalized high-support source
expectation.

### Theorem PP3afv -- PROVED

On the PP3afu subbank, if

```text
lambda_src
+d_1/q
+d_2/(q)_2
<=1/24
```

and

```text
H_src<1,
```

then there is a source-admissible endpoint derangement with

```text
I_Xi=0.
```

It therefore strictly decreases `Xi`.

#### Proof

The designated recapture family is empty by PP3afu, so the `d_rec/q` term in
PP3jv is exactly zero.  Add every foreign unary support cell and binary support
pair to the permutation local-lemma family.  The displayed local mass verifies
PP3jt, and the high-support source condition is the second hypothesis of
PP3jv.  The resulting permutation has zero residual insertion cost by PP3ju.
It also recreates none of the selected credits by PP3afq.  Positive removal
credit then gives a strict decrease through PP3kx. ∎

## 3. Persistent failure is a foreign linear support core

For an endpoint index `s`, let

```text
d_un(s)=max{d_1(s_L),d_1(s_R)},
d_bin(s)=max{d_2(s_L),d_2(s_R)}.
```

### Corollary PP3afw -- PROVED

If PP3afv cannot be applied along an infinite sequence of recapture-free banks,
then after passing to a subsequence there is a fixed `rho>0` such that at least
one of the following holds.

1. At least `rho q` endpoint indices satisfy

   ```text
   d_un(s)>=rho q.
   ```

2. At least `rho q` endpoint indices satisfy

   ```text
   d_bin(s)>=rho q^2.
   ```

3. The source or endpoint-host hypotheses of PP3afv fail.

#### Proof

When the source and host hypotheses hold, repeat the deletion argument
PP3kd--PP3kf with `d_rec=0`.  If all but `o(q)` indices have
`d_un=o(q)` and `d_bin=o(q^2)`, delete the exceptional indices and apply
PP3afv.  Negating this statement gives one of the two displayed linear cores.
∎

Unlike PP3kf, the unary degree here contains no designated recapture cells.

## 4. Pure foreign support size

Let `U_foreign` be the simple foreign unary support and `B_foreign` the simple
foreign binary support.

### Proposition PP3afx -- PROVED

Under the first alternative of PP3afw,

```text
|U_foreign|>=rho^2 q^2/4.
```

Under the second,

```text
|B_foreign|>=rho^2 q^3/8.
```

#### Proof

This is the incidence count PP3kg after setting the recapture support to the
empty family.  A unary cell uses at most two endpoint indices and a binary
event uses at most four. ∎

Thus the persistent objects are a quadratic foreign unary core or a cubic
foreign binary core.

## 5. Existing structural handoffs

### Corollary PP3afy -- PROVED

The cores in PP3afx rejoin existing conversion chains.

1. The unary core contains a linear resource-disjoint unary-cell matching.
   Choosing retained-source witnesses gives either a source-star centre or a
   credited endpoint bank through PP3wc--PP3wh and PP3yc--PP3yi.
2. The binary core gives either a quadratic endpoint-resource star or a linear
   resource-disjoint binary bank by PP3kh.
3. A quadratic binary star conditions to a fixed-cell fan, conditional Hall
   family, or residual paid/source concentration by PP3wv--PP3xc.
4. Complete choice-grid/projective-cover output is already a fixed-cell
   candidate fan by PP3afh--PP3afm.

#### Proof

Apply PP3kh to the support sizes in PP3afx, followed by the cited witness and
conditional-completion theorems. ∎

## 6. Revised resource-bank frontier

### Corollary PP3afz -- PROVED

A large resource-disjoint credited endpoint bank now has one of the following
forms.

1. A source-admissible zero-insertion permutation strictly decreases `Xi`.
2. A purely foreign quadratic unary support core.
3. A purely foreign cubic binary support core.
4. A source-preparation or endpoint-host failure.

Rich designated recapture fibres and recreation of the selected witness
incidences are no longer independent resource-bank frontiers.

The remaining paid difficulty is conversion of the foreign unary/binary cores
after they re-enter the source-star, fixed-cell-fan, conditional-Hall, or
alternating-host chains.

## 7. Finite diagnostic

The script

```text
scripts/check_recapture_free_resource_bank.py
```

checks the recapture-free local-mass criterion and reports paid completion,
foreign unary core, foreign binary core, or source/host failure.
