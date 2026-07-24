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

A constant or repairable uniform line cap is still open, but the remaining
exception is now height-weighted rather than global.

### CM3 — syndrome reduced to harmonic direction energy

Same- and cross-channel secants have explicit valuation quadratics and
mixed-layer carry identities. Bounded same-channel displacement multiplicity
is impossible: CMR14 gives one exact top-digit vector repeated at least

\[
\frac{p-1}{p^2}N
\]

times. CMR15–CMR22 localize those repeats to disjoint blocks and install
executable permutation banks.

Define

\[
\mathcal E
=
\sum_{\{P,Q\}}
\frac1{H(P,Q)}.
\]

CMR32 proves

\[
T(R_{\mathbf c})
\le
\frac{2k}{3}\binom N2
+
\frac{2\sqrt N}{3}\mathcal E.
\]

Finite data place \(\mathcal E\) near \(N\log N\). The one-channel
syndrome target is therefore reduced to a near-linear harmonic direction-
energy theorem, preferably after block contraction.

### CM4 — prime-power carry calculus: recursive decoder space constructed

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
- an exact first-separation signature \(q+M+p^{k-1}D_1=0\).

The terminal state is now explicit at every prime: CMR33 proves that

\[
F_p(0)=1,
\qquad
F_p(x)=[1+x^{-1}]_p
\]

is a no-three permutation, and CMR34 installs it simultaneously in the two
terminal row blocks. The remaining decoder theorem is therefore only a
concentration bound for nonterminal recursive first-separation certificates.

### CM5 — CRT saturation and mixed-collision criterion

Synchronized local permutation pairs assemble to exact two-layer saturation.
For a mixed collision

\[
P_1-P_0=uA,
\qquad
P_2-P_0=vB,
\]

the global determinant factors exactly as

\[
\Delta(P_0,P_1,P_2)=uv\det(A,B).
\]

Under local modular arc hypotheses, every global real triple has this mixed
form. Therefore disjoint scaled collision-direction sets give a positive
ordered-box CRT assembly criterion.

The remaining construction task is to build local pairs whose two scaled
collision-direction sets are disjoint, rather than merely controlling local
line caps.

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
least \((p-1)/3\), so a flat first-moment finish fails for \(p\ge5\). This no
longer blocks the recursive construction: CMR33–CMR34 provide one explicit
companion-compatible no-three terminal state for every prime and every
exponent.

No scalable all-composite construction is yet known.

## Revised bottlenecks

1. **Harmonic direction energy.** Prove
   \(\mathcal E(R_{\mathbf c})=O(N\log^C N)\), ideally after contracting
   the deterministic top-digit blocks.
2. **Recursive first-separation concentration.** Bound the weighted mass of
   signatures \(q+M+p^{k-1}D_1=0\) under the recursive CMR27 measure, with the
   explicit CMR34 terminal state fixed at the base.
3. **Balanced small-height tangent lines.** Sum the remaining highly singular,
   low-height directions without reverting to a global square-root cap.
4. **Digital saturation at 64 and non-block lift to 128.** The direct bit-block
   extension is refuted; unrestricted completion remains open.
5. **CRT direction separation.** Construct synchronized local pairs satisfying
   \(\mathcal D_u\cap\mathcal D_v=\varnothing\).

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
python scripts/verify_prime_power_recursive_quotient.py --max-modulus 125
python scripts/verify_prime_power_recursive_determinant.py
python scripts/verify_crt_mixed_collision.py --max-modulus 60
python scripts/verify_prime_power_tangent_parameter.py --max-modulus 243
python scripts/verify_prime_power_harmonic_energy.py --max-modulus 243
```

These are finite exact checks. They do not constitute a complete all-`n`
construction.
