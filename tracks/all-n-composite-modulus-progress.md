# Composite-modulus track: current progress and revised bottlenecks

This is the current addendum to
[`tracks/all-n-composite-modulus.md`](all-n-composite-modulus.md). Detailed
claims are indexed in
[`proofs/composite-modulus-theorem-index.md`](../proofs/composite-modulus-theorem-index.md).

## Current state of CM1–CM6

### CM1 — nonlinear full channels and recursive saturated banks

Valuation-completed reciprocals are full nonlinear permutation channels at
every prime power. A universal row companion produces a disjoint saturated pair
with one alternating Hamiltonian cycle.

At \(N=p^k\), the pair decomposes into \(N/p\) top-digit column blocks of size
`p`. Both layers can be independently permuted inside every block, giving

\[
(p!)^{2N/p}
\]

saturated states with an exact cylinder law. Contracting the blocks recovers the
identical host at exponent \(k-1\), yielding an exact recursive multiscale bank.

The restricted CMR43 lift replaces each full fibre permutation by the
quadratic-size conic family CMR35. It remains saturated, excludes every triple
internal to one quotient column fibre, and gives `O(1/p)` conditional
anti-concentration for every first-separating fibre by CMR46.

For primes

\[
p\equiv1\pmod4,
\]

CMR67 uses all shifts and nonsquare reciprocal parameters. Every individual
layer cell is exactly uniform with probability `1/p`. The saturated root law is
not independent sampling: the two root maps use one common nonsquare parameter
and two distinct shifts. This condition is necessary and sufficient for their
pointwise disjointness. Above the root, independent balanced maps remain valid
because the two layer row-prefix fibres are already disjoint.

### CM2 — real line cap: height-sensitive but open

For odd prime powers, every line intersection reduces to simple lower valuation
roots plus one possible top Hensel-tangent cell. The coarse cap is

\[
O(\sqrt N+\log N).
\]

CMR30 sharpens the top population on a primitive line of height `H` to

\[
O\left(1+\frac{p^t}{H}\right),
\]

where \(2t\) is the discriminant valuation. Large cells must therefore be both
highly singular and supported on small primitive directions.

A constant uniform line cap remains open, but the exception is height-weighted.
CMR38 converts this line cap into a general
\(O(N^{3/2}\log N)\) deterministic harmonic-energy bound.

### CM3 — one- and two-layer syndrome bounds

Bounded same-channel displacement multiplicity is impossible: CMR14 gives one
exact top-digit vector repeated at least

\[
\frac{p-1}{p^2}N
\]

times. CMR15–CMR22 localize those repeats to disjoint executable blocks.

For one deterministic completed-reciprocal layer, two independent arguments
reach quadratic-order syndrome:

- CMR38–CMR39 use direction splitting to prove
  \[
  \mathcal E=O(N^{3/2}\log N),
  \qquad
  T=O(N^2\log N);
  \]
- CMR56–CMR66 reduce the energy to exact divisor-collision cells, prove
  \[
  C(a,d)<20N/d+13\sqrt N+8k,
  \]
  and obtain
  \[
  \mathcal E=O(N^{3/2}+N\log^3N),
  \qquad
  T=O(N^2\log N).
  \]

The second proof identifies the remaining arithmetic loss: rare nearly singular
carries create the square-root boundary.

For the complete deterministic two-layer companion host, CMR40–CMR42 give a
height-sensitive line cap, harmonic energy

\[
O_p(N^{3/2}\log N),
\]

and full same-/cross-layer syndrome

\[
O_p(N^2\log N)
\]

for every fixed odd prime base.

For the recursive bank, CMR50 gives the exact pair-difference law, while
CMR51–CMR52 prove expected harmonic energy

\[
O(N\log^3N)
\]

even with a no-three spread family at the base.

CMR68–CMR74 sum recursive first-separation certificates. For every fixed odd
`p>=5`, the original restricted bank has a genuinely subcubic expected syndrome.
For the corrected balanced saturated bank at `p=1 mod 4`,

\[
\mathbb E T_k
<
4(k-1)N^2+
\left(
\frac{p-2}{3}+
\frac{4p}{3(p-1)}
\right)N^2
<
4(k-1)N^2+\frac{p+3}{3}N^2.
\]

Thus this infinite prime-power class has saturated recursive states with
`O_p(N^2 log N)` syndrome and exact multiscale spread.

### CM4 — prime-power carry calculus and recursive decoder space

The branch contains:

- valuation-stratum line quadratics and exact square-root multiplicities;
- exact-real primitive-line tangent spacing;
- same- and cross-layer displacement quadratics;
- all-stratum collision blocks and full two-layer banks;
- recursive quotient self-similarity;
- the determinant recurrence
  \[
  \Delta_N=D_0+p^{k-1}M+p^{2k-2}D_1;
  \]
- first-separation signatures \(q+M+p^{k-1}D_1=0\);
- restricted conic-fibre and uniform-lift anti-concentration;
- exact complete and unit scalar root averages;
- full-depth layer-transverse anti-concentration
  \[
  \Pr(\Delta\equiv0\pmod N)
  \le\frac{p}{(p-1)N};
  \]
- pair-codegree localization and the binary closest-pair factor;
- exact equilateral and binary p-adic clustering sums.

CMR75–CMR78 install a full prefix-block rematching bank. Every old binary
same-layer star assigned to the block is destroyed in every state, while the
bank remains saturated and has matching-cylinder spread.

CMR79–CMR89 close the rank-one quotient-incidence reduction. The actual
rank-one candidate count contains no universal endpoint baseline, and

\[
\mathcal M_s\le3t^2Z_s,
\qquad
0\le\mathcal C_s-|E_s^{\rm coll}|<2N^2.
\]

For the balanced recursive bank, the expected total normalized rank-one
collateral over all quotient scales is

\[
O_p(N^2\log^2N).
\]

CMR90–CMR92 close the higher-rank prefix terms for every saturated state:

\[
\sum_{a,\ell}\frac{T_2(A_{s,a,\ell})}{(t)_2}<2N^2,
\qquad
\sum_{a,\ell}\frac{T_3(A_{s,a,\ell})}{(t)_3}<\frac{N^2}{3p}.
\]

CMR93–CMR95 prove descending-scale invariance. A repair at scale `s` preserves
every quotient modulo `p^r` for `r<=s`, including its modular syndrome and all
coarser block row sets. A fine-to-coarse sweep therefore retains the initial
balanced quotient charge at every unprocessed scale.

CMR96–CMR99 add a recursive-compatible node bank. For two targeted child
digits, its exact state count is

\[
h(p-2)+1,
\qquad h=(p-1)/2,
\]

with one-child atom below `1/(p-2)` and rank-at-least-two child prescriptions at
most `1/(h(p-2)+1)`. The bank changes only one reciprocal node, preserves the
recursive algebraic class, and destroys a heavy child-pair star.

CMR100–CMR101 identify and cancel an invariant subcore: triples wholly inside
one child subtree are rigidly translated by a parent-node change, so their exact
determinants and counts do not change. The remaining weak node-rank-one class is
strictly external to that child subtree.

The original generic first-separation, binary-star construction, quotient
charging, endpoint removal, and higher-rank collateral bottlenecks are therefore
closed at quadratic-polylogarithmic scale. The current recursive issue is a
termination theorem for the external child-scale rank-one shadows.

### CM5 — CRT local-arc route corrected

Synchronized local permutation pairs assemble to exact global saturation, and
mixed collisions retain

\[
\Delta(P_0,P_1,P_2)=uv\det(A,B).
\]

CMCRT6 proves that a saturated odd-prime local pair cannot be a modular arc, so
the simple CMCRT4 premise cannot directly assemble saturated factors. CMCRT7
classifies the unavoidable collision/local-line projection patterns.

For a cyclic local line representation, CMCRT8 gives

\[
L_m
=
\alpha\det(d,B)-\beta\det(d,A)+m\det(A,B),
\qquad
\Delta=mL_m.
\]

For coprime factors, CMCRT9 gives

\[
L_u=vq,
\qquad
L_v=uq,
\qquad
\Delta=uvq.
\]

The revised target is slope-carry incompatibility over prime factors, plus a
classification of noncyclic zero-divisor incidences for composite local factors.

### CM6 — finite coverage and the digital branch

Exact saturated no-three configurations are recorded at composite side lengths

\[
4,6,8,9,10,12.
\]

The `N=12` configuration is an exact feasibility certificate verified over all
\(\binom{24}{3}\) triples.

Binary digit-linear one-channel no-three permutations are verified at

\[
8,16,32,64.
\]

The direct one-bit extension of the CMR12 matrix to `128` is refuted. CMR55 also
proves, by an exact integer covering certificate, that the existing `64`-point
layer has no second-permutation no-three completion at all, even before triples
internal to the proposed second layer are imposed.

The digital route must therefore search jointly for both layers or replace the
first layer. No scalable all-composite construction is known.

## Revised bottlenecks

1. **External child-scale rank-one descent.** In the recursive-compatible CMR99
   bank, charge `U_1^{ext}` to child-prefix secant energies and prove a
   lexicographic or reverse-scale potential decrease.
2. **Termination under repeated repairs.** Fine repairs preserve all coarser
   quotient charges, but a later coarse repair may recreate fine stars. Bound
   that recreated mass by the coarse decrease.
3. **Sharper modular quotient syndrome.** Improve the current
   `O_p(sm^2)` bound for `Z_s`, or exploit inherited primitive-line signatures to
   reduce the factor `3t^2` in CMR86.
4. **Remove the square-root divisor boundary.** Sharpen CMR61 and CMR64 for rare
   carries whose discriminant is divisible by nearly the full modulus.
5. **Extend balanced local families.** CMR67 gives an exact saturated balanced
   law for `p=1 mod 4`. Find a comparable law for `p=3 mod 4`, or prove an
   obstruction within completed reciprocal maps.
6. **Joint digital construction.** Search for two compatible layers from the
   outset, or a different first layer and nonlinear lift to `128`.
7. **CRT slope-carry incompatibility.** Construct local saturated pairs whose
   signatures cannot simultaneously vanish except in an absorbable family.
8. **Further finite coverage.** `N=12` is solved; bounded `N=14` runs produced no
   certificate, so no claim is made there.

## Checks

```bash
python scripts/verify_prime_power_harmonic_energy.py --max-modulus 243
python scripts/verify_prime_power_companion_global.py
python scripts/verify_prime_power_average_roots.py
python scripts/verify_prime_power_first_separation_sum.py --max-modulus 125
python scripts/verify_prime_power_layer_transverse.py --max-modulus 125
python scripts/verify_prime_power_binary_clusters.py --max-modulus 125
python scripts/verify_prime_power_prefix_star_bank.py
python scripts/verify_prime_power_rank_one_reduction.py
python scripts/verify_prime_power_quotient_incidence.py
python scripts/verify_prime_power_quotient_excess.py
python scripts/verify_prime_power_higher_rank_prefix.py
python scripts/verify_prime_power_descending_invariance.py
python scripts/verify_prime_power_recursive_compatible_bank.py
python scripts/verify_prime_power_child_core_cancellation.py
python scripts/verify_prime_power_recursive_harmonic.py --samples 100
python scripts/verify_prime_power_lift_anti_concentration.py --max-prime 5
python scripts/verify_prime_power_divisor_collisions.py --max-modulus 243
python scripts/verify_prime_power_critical_collisions.py --max-modulus 125
python scripts/verify_prime_power_singular_collision_sum.py --max-modulus 125
python scripts/verify_prime_power_cross_stratum_sum.py --max-modulus 125
python scripts/verify_prime_power_terminal_family.py --max-prime 101 --max-exponent 4
python scripts/verify_prime_power_terminal_spread.py --max-prime 19
python scripts/verify_crt_slope_carry.py
python scripts/verify_digital_64_completion_obstruction.py
python scripts/verify_composite_finite_extensions.py
```

These finite checks do not constitute a complete all-`n` construction.
