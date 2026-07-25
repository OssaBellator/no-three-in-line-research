# Dense clean-chain conditioning has exact inverse-density loss

After PP3adu--PP3aem, the only marked-centre term still named abstractly is the
source or `Xi` cost whose support does not contain the captive centre. A dense
source-clean five-chain bank controls this term without a new geometric
decomposition.

The joint marked state law factors exactly through the local five-chain. Every
ordered five-chain through the centre has the same number of block-and-cycle
completions. Hence the local chain is uniform. Restricting this uniform law to
any source-clean subfamily of density `delta` increases the expectation of
every nonnegative residual objective by at most the sharp factor `1/delta`.

The supply theorem PP3aeh--PP3aem gives `delta=N^(-o(1))` unless the existing
transition-petal branch occurs. Therefore the off-centre source and insertion
terms retain all polynomial thinning gains. Failure is a global support-ranked
threshold or one of the fixed-centre cores already produced by unary/binary
truncation.

## 1. The marked state space

Let a pool have endpoint set `V`, `|V|=N`, fix `c in V`, and choose a marked
block of size `b>=5` containing `c`. On that block choose one directed Hamilton
cycle.

Let `Omega_c` be the set of all such block-cycle states, with the uniform law.
Every state has one local five-chain

```text
r -> p -> c -> s -> t,
```

where `r,p` are the second predecessor and predecessor of `c`, and `s,t` are
the successor and second successor.

Let

```text
H_c={(r,p,s,t): r,p,s,t are distinct elements of V\{c}}.
```

Thus

```text
|H_c|=(N-1)_4.
```

### Proposition PP3aen -- PROVED

The local chain of a uniform state in `Omega_c` is uniform on `H_c`.
For every fixed `h in H_c`, the number of states with local chain `h` is

```text
binom(N-5,b-5)(b-5)!
=
(N-5)!/(N-b)!.
```

Conditional on `h`, the remaining state law is exactly the five-chain
conditional law of PP3abp and PP3adw.

#### Proof

After fixing `h`, choose the other `b-5` block indices and then choose one of
the `(b-5)!` Hamilton cycles containing the four prescribed chain arcs. The
count is independent of `h`.

Moreover

```text
(N-1)_4 binom(N-5,b-5)(b-5)!
=
binom(N-1,b-1)(b-1)!,
```

which is the total number of marked block-cycle states. Hence every state is
accounted for once and the chain marginal is uniform. The conditional
description is the construction used in PP3abp and PP3adw. ∎

## 2. Sharp restriction inequality

Let `C subseteq H_c` be any nonempty chain family and put

```text
delta=|C|/(N-1)_4.
```

For a nonnegative function `X` on `Omega_c`, write `E[X|h]` for its expectation
under the conditional completion through `h`.

### Theorem PP3aeo -- PROVED

One has

```text
(1/|C|) sum_{h in C} E[X|h]
<=
E_{Omega_c} X / delta.
```

The factor `1/delta` is best possible for arbitrary nonnegative objectives.

#### Proof

By PP3aen,

```text
E_{Omega_c}X
=
(1/|H_c|) sum_{h in H_c} E[X|h].
```

All summands are nonnegative, so the sum over `C` is at most the full sum.
Divide by `|C|=delta|H_c|`. Sharpness follows by taking an objective supported
exactly on the states whose local chain lies in `C`. ∎

This lemma requires no independence inside the clean-chain family.

## 3. Off-centre Xi insertion weight

Use the support-ranked full-pool weights `A_2,B_3,B_4`. Let
`J_h^off` be the exact conditional expected unary/binary `Xi` insertion cost
of patterns whose endpoint support does not contain `c`.

The single-cycle marked law has unmarked paid expression

```text
U_Xi
=
K [
 A_2 b/N^2
 +B_3 b/N^3
 +B_4 b^2/N^4
],
```

for one absolute fixed-rank constant `K`, by PP3zb.

### Corollary PP3aep -- PROVED

For every nonempty clean-chain family `C` of density `delta`,

```text
(1/|C|) sum_{h in C} J_h^off
<=
U_Xi/delta.
```

#### Proof

Apply PP3aeo to the nonnegative off-centre `Xi` insertion cost. Its expectation
under the unrestricted marked law is bounded by the unmarked terms in PP3zb. ∎

For the dense family supplied by PP3aej,

```text
delta>=1/(3log^4 N)=N^(-o(1)).
```

Thus clean-chain conditioning loses only a polylogarithmic factor.

## 4. Remaining source-invalid objective

Let `Y_h^off` be the conditional expected number of all source-invalid events
not already excluded by the source-clean local chain. Let

```text
U_src(c)=E_{Omega_c} Y^off
```

be the corresponding unrestricted marked expectation, using the exact source
classes and cylinder factors of PP3za.

### Corollary PP3aeq -- PROVED

For every clean-chain family `C` of density `delta`,

```text
(1/|C|) sum_{h in C} Y_h^off
<=
U_src(c)/delta.
```

Consequently, if

```text
U_src(c)=o(delta),
```

then all but `o(|C|)` clean chains have residual source-invalid expectation
`o(1)`.

#### Proof

The expectation bound is PP3aeo. Markov's inequality gives the final
statement. ∎

The hypothesis is an explicit quantitative strengthening of the ordinary
marked source-light condition; it is not a new combinatorial host assumption.

## 5. Paid completion from a dense clean bank

Let `C_Xi(h)` be the exact centre-supported cost from PP3adx and let `R_c>0`
be the centre removal credit. Define the deterministic/local rank-four
objective through the exact formula of PP3ady.

### Theorem PP3aer -- PROVED

Let `C` be a source-clean chain family of density `delta`. If

```text
(1/|C|) sum_{h in C} C_Xi(h)/R_c
+
U_Xi/(delta R_c)
+
U_src(c)/delta
<1,
```

then one chain in `C` and one conditional single-cycle completion are
source-valid and strictly decrease `Xi`.

#### Proof

Choose `h` uniformly from `C` and then choose a uniform conditional completion.
The first term is the exact averaged centre cost. Corollaries PP3aep and
PP3aeq bound the off-centre paid and source objectives. The displayed sum is
therefore an upper bound for the expectation of

```text
number of source violations + insertion cost/R_c.
```

An outcome below one has zero source violations and insertion cost below the
removal credit. Apply PP3kx. ∎

The exact support-ranked source terms may be substituted for `U_src(c)` when a
fully expanded criterion is desired.

## 6. Failure alternatives

### Corollary PP3aes -- PROVED

Assume the clean-bank branch of PP3aej, so
`delta>=1/(3log^4 N)`. If PP3aer fails, at least one of the following occurs.

1. The averaged exact centre cost is at the removal-credit scale. By
   PP3aeb--PP3aeg this yields a heavy unary arc family, rank-three path/grid
   family, or rank-four partner family.
2. The unrestricted marked residual source objective satisfies

   ```text
   U_src(c)=Omega(delta).
   ```

3. The full-pool off-centre weight satisfies

   ```text
   U_Xi=Omega(delta R_c).
   ```

   Unary/binary truncation PP3adh--PP3adt converts this into a fixed-centre
   heavy arc, rank-three path, or rank-four partner core unless the local
   pattern cost is already at its credit-normalized truncation scale.
4. A transition role-star occurs instead of the clean-bank branch, and feeds
   PP3zw--PP3aaj.

#### Proof

Negate PP3aer and use the clean-supply dichotomy PP3aej. The structural
handoffs are PP3aeb--PP3aem and PP3adh--PP3adt. ∎

Thus an arbitrary residual off-centre `Xi` table is no longer an independent
marked-centre obstruction.

## 7. Revised marked-Xi endpoint

### Corollary PP3aet -- PROVED

The marked-centre `Xi` branch reduces to payment or conversion of:

1. heavy arc/path petal banks;
2. weighted middle grids or projective covers;
3. rank-four conditional-Hall or alternating-host families;
4. transition-petal/resource banks;
5. explicit residual source thresholds after the inverse-density factor;
6. local pattern cost already comparable with removal credit.

Opaque centre cost, deterministic local-credit tables, failure of dense clean
supply, and unstructured off-centre insertion concentration are no longer
separate cases.

## 8. Finite diagnostic

The script

```text
scripts/check_clean_chain_inverse_density.py
```

enumerates all marked block-cycle states, verifies that every ordered local
five-chain has the same number of completions, restricts to a chosen clean
subfamily, and checks the sharp inverse-density inequality for a nonnegative
cycle objective.
