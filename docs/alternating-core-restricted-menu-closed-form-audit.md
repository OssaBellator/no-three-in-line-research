# Closed-form restricted-menu AC5 audit

**Branch:** `research/alternating-core-chain`

AC5ap--AC5at import the deterministic GC1--GC3 partner, pool and pair-shadow inventories.  The remaining
quantitative input is scattered among an absolute partner-blocker budget, paid pool depletion, declared
new blockers and the AC5q--AC5t new-assignment formulas.  This note combines those quantities into one
closed-form audit for a concrete restricted menu.

The conclusion is deliberately conditional on a complete menu inventory.  It does not prove that the
resulting numerical inequality holds for every pivot, BDA, RI, target or petal menu.

## Restricted-menu data

Fix a target batch `B` of size `t` and an initial common partner pool `P_0` of size `p`.  Paid depletion
leaves a common retained pool `P subseteq P_0` of size

`p_* = p-c`.

For each target `b`, assume `b notin Q_b` and declare:

- a physical blocker support `Q_b`;
- a finite exact non-axis dangerous-line set `L_b`;
- an exact residual partner set `J_b subseteq P_0`;
- an exact retained-partner new-blocker set `N_b subseteq P` created by declared state changes.

Put

`D_b = |P_0 intersect Q_b| + 2|Q_b| + 2|L_b| + |J_b|`,

`Delta = max_b (D_b+|N_b|)`.

Every inadmissible retained partner is assumed to lie in the union represented by these four rows.
For one line band `J`, let `ell_J` bound the number of board cells on one line, let

`m_J=(ell_J-2)_+`,

let `Theta_(J,0)` be the initial pair-shadow cap, and let `A_j` be the cumulative number of assignments
which become genuinely newly possible through installation step `j`.

## AC5au -- absolute retained-degree bound -- PROVED

Every target has retained admissible degree at least

`d_Gamma(b) >= p_* - D_b - |N_b| >= p_* - Delta`.

### Proof

GC1c--GC1e show that the initial physical, exact-line and residual blockers exclude at most `D_b`
partners in the whole initial pool.  Restriction to `P` cannot create an additional initial blocker.
The declared set `N_b` contains every new blocker on a retained partner.  Taking the union gives the
first inequality, and the definition of `Delta` gives the second. QED.

No density normalization is used here; this is an absolute count after the actual paid depletion.

## AC5av -- explicit sequential spread constant -- PROVED

Assume

`sigma = p_* - Delta - t > 0`

and put

`kappa = p_*/sigma`.

Sequentially expose the `t` targets in the fixed canonical order and choose uniformly from the unused
admissible retained partners.  This defines a distribution on injections covering all targets, and every
compatible set of `r` prescribed assignments has probability at most

`(kappa/p_*)^r = sigma^(-r)`.

### Proof

Before any choice, AC5au leaves at least `p_*-Delta` admissible partners.  At every exposure fewer than
`t` partners have already been used, so at least

`p_*-Delta-t=sigma`

choices remain.  Condition successively on the previous choices.  Every prescribed compatible choice
has conditional probability at most `1/sigma`; multiplication gives the cylinder bound. QED.

The loss is intentionally one unit conservative at the final exposure so that the formula has no
endpoint exception.

## AC5aw -- closed-form intermediate band inventory -- PROVED UNDER THE AC5o EVENT CONTRACT

At installation step `j`, define

`Lambda_J(j)=Theta_(J,0)+3m_J A_j`

and

`Gamma_J(j) = 8 kappa^2 n Lambda_J(j)/p_*^2
              + 4 kappa^2 ell_J t/p_*
              + 8 kappa^3 ell_J t^2/p_*`.

Then every unchanged anchor has pair-shadow at most `Lambda_J(j)`, and the expected number of newly
created band-`J` triples under the AC5av injection law is at most `Gamma_J(j)`.

### Proof

AC5q gives the pair-shadow bound because each newly possible assignment contributes at most two new
cells and hence at most `3m_J` anchored pairs.  AC5r converts the cap into anchored two-assignment
inventory at most `8n Lambda_J(j)`.  AC5o supplies the remaining nonanchored rank-two and rank-three
inventories.  Multiply those inventories by the `kappa/p_*` cylinder bounds of AC5av exactly as in
AC5s. QED.

## AC5ax -- one-line multistep drift certificate -- PROVED UNDER THE COMPLETE INVENTORY HYPOTHESES

Use AC5aw with the current band at the final step and with the protected band at every intermediate
step.  If

`Gamma_cur(final) + t sum_j Gamma_high(j) < t`,

then one complete installation path preserves every settled higher band at every intermediate state,
creates at most `t-1` final current-band triples and strictly decreases `Psi_H`.

### Proof

AC5aw supplies a complete current/protected event expectation for the same injection distribution.
Insert those bounds into the augmented-badness criterion AC5p.  The strict inequality leaves one state
with no protected-band event at any step and fewer than `t` final current-band events.  AC5b--AC5f then
give strict reverse-scale descent. QED.

Thus a concrete menu now needs only the displayed finite parameters; no qualitative pool-stability or
pair-shadow field remains.

## AC5ay -- failed spread denominator returns a heavy exact obstruction -- PROVED

If `sigma<=0`, choose a target `b_*` attaining `Delta`.  Then

`|P_0 intersect Q_(b_*)| + 2|Q_(b_*)| + 2|L_(b_*)| + |J_(b_*)| + |N_(b_*)| + t >= p_*`.

Consequently at least one of the six displayed weighted terms is at least `p_*/6`.  The failed
restricted menu therefore returns one of:

1. many current partners already in physical blocker support;
2. a large physical blocker support;
3. many exact dangerous non-axis lines;
4. one large global residual predicate;
5. many declared state-change blockers on retained partners;
6. a target batch too large for the retained pool.

### Proof

The condition `sigma<=0` is `Delta+t>=p_*`.  Expand `Delta=D_(b_*)+|N_(b_*)|` using the exact definition
of `D_(b_*)`.  The six nonnegative terms have sum at least `p_*`, so one is at least one sixth of the
sum. QED.

The weighted alternatives preserve the exact incidence coefficients.  For example, the second or
third alternative implies `|Q_(b_*)|>=p_*/12` or `|L_(b_*)|>=p_*/12`, respectively.

## Updated AC5 frontier

For every restricted menu satisfying the complete blocker/new-cell event contract, the GC1--GC3 and
spread parts now reduce to one explicit scalar slack `sigma` and the AC5aw formulas.  A nonpositive
slack is not discarded: AC5ay returns a physical-support, line, residual-context, new-blocker or
batch-size overload.  With positive slack, the remaining task is to verify the AC5ax inequality or its
reverse-flow/min-cost analogue using menu-specific values of `c,Delta,A_j,Theta_(J,0)` and `ell_J`.

## Finite check

`scripts/verify_ac_restricted_menu_audit.py` exhausts small retained-pool admissibility graphs, evaluates
the sequential injection distribution and checks every compatible rank-one through rank-three cylinder
against `sigma^(-r)`.  It also audits the pair-shadow substitution, drift formula and six-way overload
alternative over a finite parameter grid.
