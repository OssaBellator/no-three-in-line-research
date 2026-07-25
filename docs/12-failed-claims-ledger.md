# Failed claims and corrections ledger

This file is intentionally blunt. It prevents future work from quietly reusing false intermediate statements.

## 1. “A dense candidate host can be pruned probabilistically until candidate-only triples are negligible.”

**Status:** REFUTED AS A GENERAL STRATEGY.

Constant-density hosts have \(\Omega(n^4\log n)\) candidate-only triples. Uniform thinning does not remove the logarithmic line energy while retaining enough density for saturation.

## 2. “Many disjoint blocker secants automatically pay for current defect destruction.”

**Status:** FALSE WITHOUT A PAYMENT MAP.

A blocker secant may only forbid a future cell. It need not be a currently overloaded line.

## 3. “Ascending scales are natural.”

**Status:** TECHNICALLY INFERIOR.

Ascending scales leave previously protected lines longer than current lines, ruining uniform interaction counts. Descending heights fixes this.

## 4. “Formal protected tomography trades give executable repair banks.”

**Status:** FALSE WITHOUT INSTALLATION.

The negative support of a formal signed trade need not be selected.

## 5. “A common translation or common affine slope can repair a fully expanded block reservoir.”

**Status:** REFUTED.

Three translated copies of the same block force corresponding-cell triples under every synchronized state.

## 6. “Wall expansion must terminate in an improving synchronized state.”

**Status:** REFUTED.

A full reservoir can be shadow-clean, have no outside anchors, and remain a synchronized local minimum.

## 7. “Bounded line occupancy and bounded pair codegree force Tanner expansion.”

**Status:** FALSE.

Cycle-like labelled constraint systems have bounded local parameters but no leaves or private repairs.

## 8. “Mutually exclusive bad literals can be ignored in a lopsided local lemma.”

**Status:** WRONG DIRECTION.

Conditioning on avoiding one mutually exclusive assignment increases the probability of another assignment of the same variable, so these events are lopsided neighbours rather than harmless non-neighbours.

## 9. “The exact one-block collateral has an unavoidable \(O(h/H)\) term.”

**Status:** IMPROVED.

When \(h\le H\), a high line meets the block at most once. The internal unanchored term is exactly zero; collateral is purely external secant shadow.

## 10. “The current notebook proves \(D(n)=2n\).”

**Status:** FALSE.

Alternating two-colour carry-core conversion and multiscale integration remain open.

## 11. “Every carry-filtered Möbius cycle improves or contains an improving orbit absorber.”

**Status:** REFUTED.

For \(p=11\), \(H_2\cup H_3\) contains the chordless red cycle with parameters \((4,5,7,6)\). Its identity state is the unique minimum among all fourteen collision-free row-column matchings of its cycle block. The shift by two has constant window product and decomposes into two order-two orbit absorbers, but its potential is larger, and each individual rectangle switch is also worse. See `docs/13-carry-cycle-dispersion.md`.

## 12. “Two affine permutation channels can give a direct all-modulus no-three seed.”

**Status:** REFUTED FOR EVERY \(N\ge5\).

Affine channels do saturate every row and column, but their lifted first differences take only the two values \(m\) and \(m-N\). Equal adjacent differences give a consecutive triple; strict alternation makes columns \(0,2,4\) collinear. See `docs/27-composite-modulus-obstructions.md`.

## 13. “The prime-field hyperbola line cap survives at composite modulus.”

**Status:** REFUTED.

For odd squarefree \(N\), the unit hyperbola \(xy\equiv1\pmod N\) has \(2^{\omega(N)}\) standard-lift points on \(y=x\). For odd prime powers \(p^k\), a suitable unit hyperbola has \(p^{\lfloor k/2\rfloor}\) points on one real anti-diagonal. Powers of two have a four-point diagonal collapse.

## 14. “A unit-group hyperbola can be treated as a full permutation channel.”

**Status:** FALSE.

It has only \(\varphi(N)\) points and occupies exactly the unit rows and columns. Adding more unit-hyperbola channels never fills a nonunit row or column.

## 15. “A toroidal no-three set may gain a real triple under standard lifting.”

**Status:** WRONG IMPLICATION UNDER THE GENUINE DEFINITION.

Every real collinear triple lies in one primitive toroidal direction fibre after reduction modulo \(N\). Hence a set protecting all such fibres cannot gain a real triple. The converse is the actual failure: a modular determinant can vanish while the integer determinant is a nonzero multiple of \(N\).

## 16. “The known 64-point digit-linear layer should admit some second permutation completion.”

**Status:** REFUTED BY AN EXACT INTEGER CERTIFICATE.

For the CMR12 layer, only `390` cells survive the two-fixed-point constraints. The admissible bipartite graph still has perfect matchings, but `122` one-fixed-point line capacities, together with row and column capacities, have an integer dual cover of cost `31718/500<64`. Hence no second permutation can avoid all mixed triples, even before its own internal triples are considered. See `docs/51-digital-64-completion-obstruction.md`.

## 17. “Saturated prime-factor pairs can satisfy the local modular-arc premise needed by the simple CRT criterion.”

**Status:** IMPOSSIBLE FOR EVERY ODD PRIME.

An affine no-three set in \(\mathbb F_p^2\) has at most \(p+2\) points by the direction count through one selected point. A saturated local pair has `2p` points, so it cannot satisfy that premise. The CRT route must retain distinct-point local slopes and their carry signatures, not only mixed collisions. See `docs/46-crt-local-arc-obstruction.md` and `docs/52-crt-slope-carry-signatures.md`.

## 18. “A carry token is permanently spent after one complete prefix rematching.”

**Status:** REFUTED FOR EVERY BLOCK SIZE \(t\ge2\).

Choose any derangement \(\sigma\) and replace a permutation layer \(f\) by \(f\circ\sigma\). This moves every old point. Applying \(\sigma^{-1}\) is also old-cell-clean and returns exactly to \(f\), restoring every occupied cell and every state-only carry token after two steps. Repeated-token control therefore needs a reintroduction charge or a time-oriented ancestry invariant; static token counting is insufficient. See `docs/130-prime-power-token-reintroduction-ledger.md`.

## 19. “A recreated selected packet triple contains a returned old edge.”

**Status:** ORIENTATION CORRECTED; NUMERICAL BOUNDS UNCHANGED.

For a selected-state reset \(M\to M'\), a triple absent from \(M\) and present in \(M'\) contains an **entering** edge of \(M'\setminus M\). The edges returned to the complementary available host are the opposite set \(M\setminus M'\). Since both sets have the same cardinality for perfect matchings, all CMR418--CMR421 counting bounds remain valid after replacing the support statement by entering-edge support and charging its size to leaving-edge churn. See `docs/141-prime-power-packet-recreation-churn-ledger.md`.
