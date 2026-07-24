# Composite-modulus track: current progress and revised bottlenecks

This is the current addendum to
[`tracks/all-n-composite-modulus.md`](all-n-composite-modulus.md). Detailed
claims are indexed in
[`proofs/composite-modulus-theorem-index.md`](../proofs/composite-modulus-theorem-index.md).

## Current state of CM1–CM6

### CM1 — nonlinear full channels and recursive saturated banks

Valuation-completed reciprocals are full nonlinear permutation channels at
every prime power. A universal row companion produces a disjoint saturated
pair with one alternating Hamiltonian cycle.

At \(N=p^k\), the pair decomposes into \(N/p\) top-digit column blocks of size
`p`. Both layers can be independently permuted inside every block, giving

\[
(p!)^{2N/p}
\]

saturated states with an exact cylinder law. Contracting the blocks recovers
the identical host at exponent \(k-1\), yielding an exact recursive multiscale
bank.

The restricted CMR43 lift replaces each full fibre permutation by the
quadratic-size conic family CMR35. It remains saturated, excludes every triple
internal to one quotient column fibre, and gives `O(1/p)` conditional
anti-concentration for every first-separating fibre by CMR46.

### CM2 — real line cap: height-sensitive but open

For odd prime powers, every line intersection reduces to simple lower
valuation roots plus one possible top Hensel-tangent cell. The coarse cap is

\[
O(\sqrt N+\log N).
\]

CMR30 sharpens the top population on a primitive line of height `H` to

\[
O\left(1+\frac{p^t}{H}\right),
\]

where \(2t\) is the discriminant valuation. Large cells must therefore be both
highly singular and supported on small primitive directions.

A constant uniform line cap remains open, but the exception is now
height-weighted. CMR38 already converts this line cap into a general
\(O(N^{3/2}\log N)\) deterministic harmonic-energy bound.

### CM3 — one- and two-layer syndrome bounds

Bounded same-channel displacement multiplicity is impossible: CMR14 gives one
exact top-digit vector repeated at least

\[
\frac{p-1}{p^2}N
\]

times. CMR15–CMR22 localize those repeats to disjoint executable blocks.

For one deterministic completed-reciprocal layer, two independent arguments
now reach quadratic order:

- CMR38–CMR39 use direction splitting to prove
  \[
  \mathcal E=O(N^{3/2}\log N),
  \qquad
  T=O(N^2\log N);
  \]
- CMR56–CMR66 reduce the same energy to exact divisor-collision cells, prove
  \[
  C(a,d)<20N/d+13\sqrt N+8k,
  \]
  and again obtain
  \[
  \mathcal E=O(N^{3/2}+N\log^3N),
  \qquad
  T=O(N^2\log N).
  \]

The second proof identifies the remaining arithmetic loss: rare nearly
singular carries create the square-root boundary.

For the complete two-layer companion host, CMR40–CMR42 give a
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

even with a no-three spread family at the base. Thus a saturated recursive
state with near-linear polylogarithmic harmonic energy exists.

### CM4 — prime-power carry calculus and recursive decoder space

The branch now contains:

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
- the restricted conic-fibre bank CMR43–CMR46;
- the complementary uniform-lift bounds CMR53–CMR54;
- exact complete and unit scalar root averages CMR47–CMR49.

The terminal state is solved uniformly at every prime, and CMR35–CMR37 give a
spread terminal base. The remaining decoder theorem is global: sum
first-separation certificate weights across quotient levels without losing the
local `O(1/p)` gain.

### CM5 — CRT local-arc route corrected

Synchronized local permutation pairs assemble to exact global saturation, and
mixed collisions retain

\[
\Delta(P_0,P_1,P_2)=uv\det(A,B).
\]

CMCRT6 proves that a saturated odd-prime local pair cannot be a modular arc, so
the simple CMCRT4 premise cannot directly assemble saturated factors.
CMCRT7 classifies the unavoidable collision/local-line projection patterns.

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
classification of noncyclic zero-divisor incidences for composite local
factors.

### CM6 — finite coverage and the digital branch

Exact saturated no-three configurations are recorded at composite side lengths

\[
4,6,8,9,10,12.
\]

The `N=12` configuration is an exact feasibility certificate verified over all
\(inom{24}{3}\) triples.

Binary digit-linear one-channel no-three permutations are verified at

\[
8,16,32,64.
\]

The direct one-bit extension of the CMR12 matrix to `128` is refuted. CMR55
also proves, by an exact integer covering certificate, that the existing
`64`-point layer has no second-permutation no-three completion at all, even
before triples internal to the proposed second layer are imposed.

The digital route must therefore search jointly for both layers or replace the
first layer. No scalable all-composite construction is known.

## Revised bottlenecks

1. **Recursive first-separation summation.** Combine CMR28–CMR29 with the
   restricted-fibre `O(1/p)` bound from CMR46 and prove a global normalized
   certificate estimate across quotient levels.
2. **Remove the square-root divisor boundary.** Sharpen CMR61 and CMR64 for the
   rare carries whose discriminant is divisible by nearly the full modulus,
   closing the gap between CMR66 and near-linear deterministic energy.
3. **Balanced small-height tangent lines.** Sum the highly singular low-height
   directions without reverting to a worst-case square-root cap.
4. **Joint digital construction.** Search for two compatible layers from the
   outset, or a different first layer and nonlinear lift to `128`.
5. **CRT slope-carry incompatibility.** Construct local saturated pairs whose
   signatures cannot simultaneously vanish except in an absorbable family.
6. **Further finite coverage.** `N=12` is solved; bounded `N=14` runs produced
   no certificate, so no claim is made there.

## Checks

```bash
python scripts/verify_prime_power_global_energy.py
python scripts/verify_prime_power_companion_global.py
python scripts/verify_prime_power_average_roots.py
python scripts/verify_prime_power_restricted_bank.py
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
