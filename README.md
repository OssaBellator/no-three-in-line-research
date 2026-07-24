# No-Three-in-Line Research Notebook

A rigorous research notebook for attempts toward the classical conjecture

\[
D(n)=2n,
\]

where \(D(n)\) is the maximum number of points that can be selected from an \(n\times n\) integer grid with no three collinear.

> **Status:** This repository does **not** contain a complete proof. The conjecture remains open as of 24 July 2026. The purpose of this repository is to preserve proved lemmas, conditional reductions, failed pathways, counterexamples, computational tools, and promising next targets in a form suitable for independent checking.

## Repository map

- [`STATUS.md`](STATUS.md): concise status and honesty ledger.
- [`proofs/theorem-index.md`](proofs/theorem-index.md): theorem-by-theorem classification.
- [`docs/00-problem-and-literature.md`](docs/00-problem-and-literature.md): problem, current literature, and conventions.
- [`docs/01-saturation-and-reservoirs.md`](docs/01-saturation-and-reservoirs.md): two-per-row/column framework, clones, deficits, and secant shadows.
- [`docs/02-reverse-scale-switching.md`](docs/02-reverse-scale-switching.md): descending-scale potential and batch repair.
- [`docs/03-uniform-local-bank.md`](docs/03-uniform-local-bank.md): spread injection and explicit local-bank hypotheses.
- [`docs/04-protected-tomographic-trades.md`](docs/04-protected-tomographic-trades.md): exact line-sum-preserving trades.
- [`docs/05-subgroup-absorbers.md`](docs/05-subgroup-absorbers.md): affine terminal configurations and installed coset-cycle absorbers.
- [`docs/06-block-collateral-energy.md`](docs/06-block-collateral-energy.md): exact one-block collateral identities and block closure.
- [`docs/07-failed-wall-pathway.md`](docs/07-failed-wall-pathway.md): false wall-termination lemma and translated-block counterexample.
- [`docs/08-hyperbola-interleaver.md`](docs/08-hyperbola-interleaver.md): complementary modular hyperbolas, low-syndrome seeds, and Hamiltonian interleavers.
- [`docs/09-orbit-tanner-and-mobius-cycles.md`](docs/09-orbit-tanner-and-mobius-cycles.md): orbit codebooks, Möbius secant matchings, cycle trades, and window products.
- [`docs/10-cross-disciplinary-pathway.md`](docs/10-cross-disciplinary-pathway.md): radar, coding, tomography, and CSP interpretations.
- [`docs/11-open-bottlenecks.md`](docs/11-open-bottlenecks.md): exact remaining lemmas and proposed experiments.
- [`docs/12-failed-claims-ledger.md`](docs/12-failed-claims-ledger.md): claims that were corrected, weakened, or refuted.
- [`docs/13-carry-cycle-dispersion.md`](docs/13-carry-cycle-dispersion.md): frozen-cycle counterexample and corrected collision-aware bank theorem.
- [`docs/15-degree-constrained-hypergraph-selection.md`](docs/15-degree-constrained-hypergraph-selection.md): clone-space exact selection theorem and local triple-load endpoint.
- [`docs/16-superregular-clone-selection.md`](docs/16-superregular-clone-selection.md): six-cycle spread proof, dense superregular perfect-matching spread, and two-layer global conflict endpoint.
- [`scripts/verify_hyperbola.py`](scripts/verify_hyperbola.py): checks modular-hyperbola line bounds and displacement multiplicities for small primes.
- [`scripts/verify_absorber.py`](scripts/verify_absorber.py): checks subgroup absorber states and protected line sums.
- [`scripts/search_cycle_trades.py`](scripts/search_cycle_trades.py): extracts cross-channel syndrome graphs and Möbius cycles.
- [`scripts/verify_carry_cycle_bound.py`](scripts/verify_carry_cycle_bound.py): verifies the frozen carry cycle and two-colour anchor release.

## Research discipline

Every mathematical item is tagged as one of:

- **PROVED:** a complete proof is written in this repository.
- **PROVED UNDER HYPOTHESES:** the implication is complete, but one or more hypotheses are not known to hold in the desired construction.
- **CONDITIONAL:** a reduction or theorem schema whose premise remains open.
- **HEURISTIC:** a proposed mechanism, not a theorem.
- **REFUTED:** a tempting statement accompanied by a counterexample.

The notebook deliberately keeps failed routes. In a long open problem, knowing exactly why a route fails is often as valuable as a new lemma.

## Principal current pathway

The strongest current synthesis is:

1. Start from two complementary modular hyperbola permutations \(H_a\cup H_b\).
2. Use their line cap, bounded displacement multiplicity, and \(O(n\log n)\) triple syndrome.
3. Encode row-column-preserving changes through multiplicative orbit blocks or cycle trades.
4. Represent cross-channel bad triples as properly edge-coloured secant graphs whose colour classes are matchings.
5. Peel leaves; every residual core contains a Möbius cycle.
6. Use collision-aware full permutation banks on cycle blocks.
7. When a one-colour cycle is frozen, expand to its opposite-colour secant anchors.
8. Control the alternating closure through quantitative one-, two-, and three-cell concentration certificates.
9. Finish in a near-complete candidate host using the clone-space degree-constrained local-load theorem.
10. In dense superregular candidate hosts, use spread perfect-matching measures or the new six-cycle switching bound; the missing upgrade is a local dependency/resampling theorem.

The original one-colour **carry-cycle dispersion lemma is refuted** by an exact \(p=11\) frozen cycle. The current geometric target is an alternating two-colour carry-core lemma. The exact complete-host endpoint is proved, and dense superregular pairs now admit rank-three and all-rank spread matching distributions. Spread alone, however, does not inherit the complete-permutation lopsided dependency graph.

## Running the checks

The scripts require Python 3.10+ and only the standard library.

```bash
python scripts/verify_hyperbola.py --prime 17
python scripts/verify_absorber.py --n 30 --h 5 --m 7
python scripts/search_cycle_trades.py --prime 17 --a 1 --b 3
python scripts/verify_carry_cycle_bound.py
```

These programs are sanity checks, not proofs for arbitrary \(n\).

## Primary references

- Ghosal, Goenka, Grebennikov, Keevash, Kwan, Pham, *No-\((k+1)\)-in-line problem for \(k\ge3\)*, arXiv:2607.05255.
- Kovács, Nagy, Szabó, *Randomised algebraic constructions for the no-\((k+1)\)-in-line problem*, arXiv:2508.07632.
- Nenadov, Pham, *Spread blow-up lemma with an application to perturbed random graphs*, arXiv:2410.06132.
- Pham, Sah, Sawhney, Simkin, *A Toolkit for Robust Thresholds*, arXiv:2210.03064.
- Glock, Joos, Kim, Kühn, Lichev, *Conflict-free hypergraph matchings*, arXiv:2205.05564.
- Joos, Mubayi, Smith, *Conflict-free Hypergraph Matchings and Coverings*, arXiv:2407.18144.
- Lu, Szekely, *A new asymptotic enumeration technique: the Lovasz Local Lemma*, arXiv:0905.3983.
- Ceko, Pagani, Tijdeman, *Algorithms for linear time reconstruction by discrete tomography II*, arXiv:2010.07862.

## Contribution guidance

A useful contribution should do at least one of the following:

- verify or repair a proof tagged **PROVED**;
- produce a small counterexample to a conditional lemma;
- prove a quantified shadow/codegree bound;
- build a superregular perfect-matching resampling oracle or conflict-free exact-cover theorem;
- extend dense \(O(1/N)\)-spread to sparse algebraic hosts with \(O(1/d)\)-spread;
- classify frozen cycles and alternating anchor closures;
- connect the carry filter to additive-combinatorial structure.

See [`CONTRIBUTING.md`](CONTRIBUTING.md).