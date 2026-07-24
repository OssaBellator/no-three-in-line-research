# Random-pool fixed-core sparsification

PP3cm makes the same-pool local load small on almost every random matching pool.
PP3cr compresses an opposite fixed layer into distinct forbidden cell and pair
patterns.  This chapter combines the two statements before the pools are chosen.
The remaining fixed-core preparation condition becomes one normalized global
pattern density.

## 1. Global interval pattern counts

Let `P` be a perfect matching of `m` source points and let `F` be a disjoint
fixed no-three-in-line source set.  Assume `m=Kr`, and fix disjoint width-two new
intervals `I_1,...,I_K`.

For interval `I_i`, form the complete candidate support of all `m` edges of `P`
and define the PP3cr pattern families against `F`:

- `C_i`: candidate cells lying on a secant through two points of `F`;
- `H_i`: same-edge movement/refill candidate pairs whose line meets `F`;
- `A_i`: all other feasible candidate pairs whose line meets `F`.

Put

\[
 \boxed{
 \Sigma(P,F;I_1,\ldots,I_K)
 =
 \frac{2\sum_i|C_i|+\sum_i|H_i|}{Km}
 +
 \frac{4\sum_i|A_i|}{K m(m-1)}.
 }
\]

This is a support-pattern density, not a triple count.  A cell or pair is counted
once even if its line supports several source certificates.

## 2. Expected fixed-core loss after equipartition

Randomly permute `P` and split it into ordered `r`-edge pools
`E_1,...,E_K`, assigning interval `I_i` to `E_i`.  Let

\[
 L_i
 =
 \frac{2|C_i(E_i)|}{r}
 +
 \frac{|H_i(E_i)|}{r}
 +
 \frac{4|A_i(E_i)|}{r(r-1)},
\]

where the pattern families are restricted to the edges of `E_i`.

### Proposition PP3ct -- PROVED

The average fixed-core pattern loss satisfies

\[
 \boxed{
 \mathbb E\frac1K\sum_iL_i
 =
 \Sigma(P,F;I_1,\ldots,I_K).
 }
\]

#### Proof

A cell or same-edge pair is controlled by one source edge.  That edge lies in a
specified pool with probability `r/m`.  Therefore

\[
 \mathbb E|C_i(E_i)|=|C_i|\frac rm,
 \qquad
 \mathbb E|H_i(E_i)|=|H_i|\frac rm.
\]

An ordinary pair is controlled by two distinct source edges, which both lie in a
specified pool with probability `(r)_2/(m)_2`.  Hence

\[
 \mathbb E|A_i(E_i)|=|A_i|\frac{(r)_2}{(m)_2}.
\]

Substitute these identities into `L_i`, average over `i`, and cancel the falling
factorials. ∎

## 3. Simultaneous local and fixed-core cleaning

Let `Lambda_i` be the canonical same-pool load from PP3ca for pool `E_i` and
interval `I_i`.  PP3cm gives

\[
 \mathbb E\frac1K\sum_i\Lambda_i\le\lambda(m,r),
\]

where `lambda(m,r)=O(r^2/m+r/m)` is explicit in PP3cl.

### Theorem PP3cu -- PROVED

For any thresholds `eta,zeta>0`, there is an equipartition for which at least

\[
 \boxed{
 \left(
 1-rac{\lambda(m,r)}{\eta}
  -\frac{\Sigma(P,F;I_1,\ldots,I_K)}{\zeta}
 \right)K
 }
\]

pools satisfy both

\[
 \Lambda_i\le\eta
 \qquad\text{and}\qquad
 L_i\le\zeta.
\]

Every such pool has a full-bank state subfamily that is simultaneously
same-pool local clean and fixed-core clean, with density at least

\[
 \boxed{
 \frac{1-\eta}{36}-\zeta.
 }
\]

#### Proof

For a random equipartition, Markov's inequality bounds the expected number of
pools with `Lambda_i>eta` by `K lambda(m,r)/eta`.  Proposition PP3ct bounds the
expected number with `L_i>zeta` by `K Sigma/zeta`.  Therefore some equipartition
has at most the sum of those two numbers of bad pools.

For a good pool, PP3ca supplies at least `(1-eta) binom(r,4)` clean canonical
states.  Viewed inside the full bank, this is density at least `(1-eta)/36`.
Apply PP3cr with loss at most `zeta` to obtain the stated simultaneous density.
∎

### Corollary PP3cv -- PROVED

If

\[
 r=o(\sqrt m)
\]

and

\[
 \Sigma(P,F;I_1,\ldots,I_K)=o(1),
\]

then an equipartition exists in which all but `o(K)` pools have simultaneous
same-pool and fixed-core clean density

\[
 \frac1{36}-o(1).
\]

#### Proof

Take `eta=sqrt(lambda(m,r))` and `zeta=sqrt(Sigma)`.  Both tend to zero, and the
exceptional fractions in PP3cu also tend to zero. ∎

At the prime-gap scale `r=m^0.475`, the local term is already
`lambda=O(m^-0.05)`.  Thus only the global fixed-core pattern density `Sigma`
remains in this step.

## 4. Coarse universal bounds and why they are insufficient

For every interval,

\[
 |C_i|\le4m,
 \qquad
 |H_i|\le4m,
 \qquad
 |A_i|\le8m(m-1).
\]

These bounds make `Sigma=O(1)`, not `o(1)`.  Consequently PP3cv is not a
universal consequence of saturation and no-three alone.  A successful source or
trade preparation must save a vanishing fraction of the candidate support
patterns, or use the more flexible directional endpoint PP3cp when many cells
are blocked but alternatives remain.

## 5. Revised fixed-core bottleneck

The matching-first constant-width route now has the following exact split.

- **Universal:** disjoint pool packing and same-pool clean density are supplied by
  PP3cm.
- **One scalar hypothesis:** opposite-layer cleaning follows from
  `Sigma=o(1)` by PP3cv.
- **Fallback:** if `Sigma` is large because many cells are blocked but most edges
  retain directional alternatives, use PP3cp and solve the remaining pair
  patterns inside that domain.
- **Concentrated failure:** small sets of repeatedly forced edges or pair patterns
  are explicit targets for protected rectangle, cycle, or tomographic trades.

After PP3cv, only cross-pool patch patterns remain for PP3ci or PP3bl.