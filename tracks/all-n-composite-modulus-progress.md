# Composite-modulus track: current progress and revised bottlenecks

This is the current addendum to
[`tracks/all-n-composite-modulus.md`](all-n-composite-modulus.md). The detailed
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
the identical companion host at exponent \(k-1\). Iterating this gives an
exact recursive multiscale bank.

The alternative CMR43 lift replaces each full fibre permutation by the
quadratic-size conic family CMR35. It remains saturated, removes every
monochromatic triple internal to one fibre, and gives `O(1/p)` conditional
anti-concentration for every other triple at that lift level.

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

where \(2t\) is the discriminant valuation. Large cells must therefore be
both highly singular and supported on small primitive directions.

A constant or repairable uniform line cap for the deterministic completed
reciprocal remains open, but the exception is now height-weighted rather than
global.

### CM3 — deterministic syndrome improved to quadratic order

Same- and cross-channel secants have explicit valuation quadratics and
mixed-layer carry identities. Bounded same-channel displacement multiplicity
is impossible: CMR14 gives one exact top-digit vector repeated at least

\[
\frac{p-1}{p^2}N
\]

times. CMR15–CMR22 localize those repeats to disjoint blocks and install
executable permutation banks.

For the deterministic completed reciprocal, CMR45 converts harmonic energy to
divisor-collision counts. CMR47–CMR54 classify and sum those collisions:
regular same-stratum cells have `O(N/d)` mass; the singular same-stratum cell
has `O(M/d+sqrt(M))` mass; and each cross-stratum gap has an explicit quadratic
whose summed roots obey the same type of estimate. The resulting unconditional
bound is

\[
\mathcal E(R_{\mathbf c})
=
O(N^{3/2}+N\log^3N).
\]

Combining it with CMR32 gives the improved one-channel syndrome

\[
T(R_{\mathbf c})=O(N^2\log N),
\]

replacing the previous `O(N^(5/2)+N^2 log N)` estimate.

For the recursive bank, CMR38 gives the exact pair-difference law of a uniform
recursive p-adic permutation, and CMR39–CMR40 prove

\[
\mathbb E\mathcal E=O(N\log^3N)
\]

even with the no-three terminal spread family at the base. Thus a saturated
recursive state with near-linear polylogarithmic harmonic energy exists.

### CM4 — prime-power carry calculus and local anti-concentration

The branch now contains:

- valuation-stratum line quadratics;
- exact odd-prime square-root multiplicities;
- exact-real primitive-parameter tangent spacing;
- same- and cross-layer displacement quadratics;
- mixed-layer determinant carries;
- all-stratum collision blocks and full two-layer banks;
- exact recursive quotient self-similarity;
- the determinant recurrence
  \[
  \Delta_N=D_0+p^{k-1}M+p^{2k-2}D_1;
  \]
- an exact first-separation signature \(q+M+p^{k-1}D_1=0\);
- the affine-in-one-digit identity CMR41;
- one-step anti-concentration CMR42;
- the conic-family fibre lift CMR43, which removes the only weak
  three-in-one-fibre case.

The terminal state is solved uniformly at every prime. CMR35–CMR37 also give a
spread terminal base with one-cell probability `O(1/p)` and rank-two
probability `O(1/p^2)`.

The remaining decoder theorem is global: sum first-separation certificate
weights across quotient levels without losing the local `O(1/p)` gain.

### CM5 — CRT local-arc route corrected

Synchronized local permutation pairs still assemble to exact global
saturation, and mixed collisions retain the factorization

\[
\Delta(P_0,P_1,P_2)=uv\det(A,B).
\]

However, CMCRT6–CMCRT7 prove that the local modular-arc hypothesis in CMCRT4 is
impossible for every saturated odd-prime local pair: an affine no-three set in
\(\mathbb F_p^2\) has at most \(p+2\) points, whereas a saturated pair has
`2p`.

CMCRT8 instead applies to a cyclic local line representation and gives the
slope-carry signature

\[
L_m
=
\alpha\det(d,B)-\beta\det(d,A)+m\det(A,B),
\qquad
\Delta=mL_m.
\]

For coprime factors with such representations, CMCRT9 gives

\[
L_u=vq,
\qquad
L_v=uq,
\qquad
\Delta=uvq.
\]

The revised CRT target is slope-carry incompatibility over prime factors,
together with a separate classification of noncyclic zero-divisor incidences
inside composite local factors.

### CM6 — finite coverage and digital branch

Exact saturated no-three configurations are recorded at composite side lengths

\[
4,6,8,9,10,12.
\]

The new `N=12` configuration is an exact integer-feasibility certificate and
is verified over all \(\binom{24}{3}\) triples.

Binary digit-linear one-channel no-three permutations are verified at

\[
8,16,32,64.
\]

The direct one-bit extension of the CMR12 matrix to `128` is refuted. CMR44 now
also proves, by an exact integer covering certificate, that the existing
`64`-point CMR12 layer has no second-permutation no-three completion at all.
The certificate already contradicts the mixed-triple constraints, without
using triples internal to the proposed second layer.

Thus the digital route must search for a joint two-layer construction from the
outset or replace the first layer; completing the current CMR12 layer is closed
negatively.

No scalable all-composite construction is yet known.

## Revised bottlenecks

1. **Recursive first-separation summation.** Combine CMR28–CMR29 with the
   conic-fibre `O(1/p)` bound from CMR43 and prove a global normalized
   certificate estimate across all quotient levels.
2. **Remove the square-root collision boundary.** Sharpen CMR50 and CMR53 on
   the rare carries whose discriminant is divisible by nearly the full
   modulus. This is the remaining gap between the deterministic
   `O(N^(3/2)+N log^3 N)` energy and a near-linear bound.
3. **Balanced small-height tangent lines.** Sum the remaining highly singular,
   low-height deterministic directions without reverting to a global
   square-root cap.
4. **Joint digital construction.** Search for two compatible layers at `64`, or
   a different first layer and a nonlinear non-block lift to `128`; the CMR12
   completion subproblem is finished negatively.
5. **CRT slope-carry incompatibility.** Build local saturated pairs for which
   the two signatures `L_u,L_v` cannot simultaneously vanish except in an
   explicitly absorbable family.
6. **Further finite coverage.** The exact feasibility model solves `N=12`; no
   certificate at `N=14` was obtained in the bounded runs, so no claim is made
   there.

## Checks

```bash
python scripts/verify_prime_power_tangent_digital.py --max-modulus 125
python scripts/verify_prime_power_displacement_obstruction.py --max-modulus 343
python scripts/verify_prime_power_top_digit_blocks.py --max-modulus 125
python scripts/verify_prime_power_companion_blocks.py --max-modulus 125
python scripts/verify_prime_power_block_collateral.py
python scripts/verify_prime_power_all_stratum_bank.py --max-modulus 125
python scripts/verify_prime_power_terminal_mass.py --max-prime 13
python scripts/verify_prime_power_terminal_configurations.py
python scripts/verify_prime_power_terminal_family.py --max-prime 101 --max-exponent 4
python scripts/verify_prime_power_terminal_spread.py --max-prime 19
python scripts/verify_prime_power_recursive_quotient.py --max-modulus 125
python scripts/verify_prime_power_recursive_determinant.py
python scripts/verify_prime_power_recursive_harmonic.py --samples 100
python scripts/verify_prime_power_lift_anti_concentration.py --max-prime 5
python scripts/verify_prime_power_divisor_collisions.py --max-modulus 243
python scripts/verify_prime_power_critical_collisions.py --max-modulus 125
python scripts/verify_prime_power_singular_collision_sum.py --max-modulus 125
python scripts/verify_prime_power_cross_stratum_sum.py --max-modulus 125
python scripts/verify_crt_mixed_collision.py --max-modulus 60
python scripts/verify_crt_slope_carry.py
python scripts/verify_prime_power_tangent_parameter.py --max-modulus 243
python scripts/verify_prime_power_harmonic_energy.py --max-modulus 243
python scripts/verify_digital_64_completion_obstruction.py
python scripts/verify_composite_finite_extensions.py
```

These are finite exact checks. They do not constitute a complete all-`n`
construction.
