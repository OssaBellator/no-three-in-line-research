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

### CM2 — real line cap: narrowed but open

For odd prime powers, every line intersection reduces to simple lower
valuation roots plus one possible top Hensel-tangent cell. The coarse cap is

\[
O(\sqrt N+\log N).
\]

CMR11 proves that tangent roots lie in one or two spaced residue classes, and
an unbalanced Euclidean slope shortens the feasible coordinate interval by
the coefficient ratio. Large cells must therefore be both `p`-adically
singular and slope-balanced.

A constant or repairable uniform line cap is still open.

### CM3 — displacement and syndrome: obstruction localized and banked

Same- and cross-channel secants have explicit valuation quadratics and
mixed-layer carry identities. The current one-channel triple bound is

\[
O(N^{5/2}+N^2\log N).
\]

CMR14 proves that bounded same-channel displacement multiplicity is impossible
for completed reciprocals: one exact top-digit vector repeats at least

\[
\frac{p-1}{p^2}N
\]

times. CMR15–CMR22 localize those repeats to disjoint `p`-point blocks and
install executable one- and two-layer permutation banks with exact normalized
certificate expectations.

Thus the prime-field bounded-codegree target is refuted, but its
structured-collision replacement is constructed.

### CM4 — prime-power carry calculus: recursive decoder space constructed

The branch now contains:

- valuation-stratum line quadratics;
- exact odd-prime square-root multiplicities;
- exact-real tangent spacing;
- same- and cross-layer displacement quadratics;
- mixed-layer determinant carries;
- all-stratum collision blocks and full two-layer banks;
- exact recursive quotient self-similarity;
- the determinant recurrence
  \[
  \Delta_N=D_0+p^{k-1}M+p^{2k-2}D_1;
  \]
- an exact first-separation signature \(q+M+p^{k-1}D_1=0\).

The remaining decoder theorem is a concentration bound for these recursive
first-separation certificates.

### CM5 — CRT assembly: open

Real triples always project to modular triples, but naive coordinatewise CRT
products contain mixed-projection triples. No ordered-box assembly theorem yet
handles cases where different point pairs collapse in different factors.

### CM6 — finite coverage and digital progress

Exact saturated no-three configurations are recorded at composite side lengths

\[
4,6,8,9,10.
\]

Binary digit-linear one-channel no-three permutations are verified at

\[
8,16,32,64.
\]

The `64`-point matrix has no direct one-bit block extension to `128`.

The unrestricted uniform terminal block has expected internal triple mass at
least \((p-1)/3\), so a flat first-moment finish fails for \(p\ge5\). Exact
companion-offset terminal no-three states are nevertheless verified for every
odd prime through `31`, and the exponent-\(2\) check proves the same local state
works at all higher powers of that prime.

No scalable all-prime terminal family or all-composite construction is known.

## Revised bottlenecks

1. **Recursive first-separation concentration.** Bound the weighted mass of
   signatures \(q+M+p^{k-1}D_1=0\) under the recursive CMR27 measure, charging
   each triple at its first nonzero quotient carry.
2. **Balanced tangent-cell theorem.** Bound exact real populations when the
   discriminant is highly divisible and the line coefficients are comparable.
3. **Terminal family for all primes.** Replace the finite CMR24 table by an
   algebraic or probabilistic family with usable spread.
4. **Digital saturation at 64.** Pair the CMR12 permutation with a second
   disjoint layer without creating a real triple.
5. **Non-block digital lift to 128.** Allow changes throughout the old block or
   triangular nonlinear Boolean terms; direct one-bit extension is refuted.
6. **Mixed-projection CRT signature.** Record which pair collapses in each
   local factor and force a small determinant or absorbable pattern.

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
python scripts/verify_prime_power_recursive_quotient.py --max-modulus 125
python scripts/verify_prime_power_recursive_determinant.py
```

These are finite exact checks. They do not constitute a complete all-`n`
construction.
