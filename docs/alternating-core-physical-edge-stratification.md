# Alternating-core physical edge stratification and rank compiler

## Status

This note keeps AC as the sole active research focus and proves AC5md--AC5mi. It composes the physical mechanisms populated in AC5kz--AC5mc into the `rank` and `stratification` sections of the initial-state manifest. Deficit supply and credited restart occupy the first two ordinal components. First signature exposure, labelled support descent, acyclic old-signature motion, cycle-bank descent and local canonical repair are compiled into one finite physical repair rank. Payment, tickets, disturbances, recreation and funded resets remain exceptional occurrences.

The result is conditional on one fixed finite physical schema and the exact local component bounds extracted from its dictionaries. It does not prove that every actual operation satisfies one route; it returns the first edge that changes an earlier component, fails its strict decrease or lacks a live exceptional occurrence.

## Physical repair-rank components

For one fixed-schema reachable state `v`, retain:

1. `u_sig(v)`: the number of declared physical signatures not yet exposed;
2. `u_sup(v)`: the size of the current AC2 labelled-recursion object universe;
3. `r_top(v)`: the reverse-topological rank in the acyclic old-signature graph currently selected by the scheduler;
4. `r_cyc(v)`: the remaining named cycle-bank or recreation-excursion rank;
5. `r_loc(v)`: the existing canonical local repair/minimax rank.

Let their finite schema bounds be

\[
S_*,O_*,Q_*,B_*,L_*.
\]

Define the mixed-radix repair rank

\[
\boxed{
\rho_{\rm phys}(v)
=
((((u_{\rm sig})(O_*+1)+u_{\rm sup})(Q_*+1)+r_{\rm top})(B_*+1)+r_{\rm cyc})(L_*+1)+r_{\rm loc}.
}
\]

Earlier components dominate arbitrary later-component changes.

## AC5md -- first-exposure and support-descent rank components -- PROVED

A first physical signature exposure removes one address from the unexposed set, so

\[
u_{\rm sig}(v')=u_{\rm sig}(v)-1.
\]

A pure AC2 labelled recursive step replaces `U` by a strict subset excluding its centre, so

\[
u_{\rm sup}(v')<u_{\rm sup}(v).
\]

When the earlier component is fixed, each route strictly lowers `rho_phys`, regardless of changes in later bounded components. Reopening a discarded object or forgetting an exposed signature is not a progress edge and requires an exceptional ticket or reset.

### Proof

Exposure is monotone set union, hence the unexposed complement loses one member. Labelled recursion strictly shrinks the object universe. Mixed-radix dominance makes a strict decrease of the first changed component dominate all later bounded coordinates. QED.

## AC5me -- acyclic signature and cycle-bank rank components -- PROVED

On an accepted acyclic old-signature graph, assign

\[
r_{\rm top}(v)=\max\{\text{length of a directed path starting at }v\}.
\]

Every scheduled old-signature edge lowers `r_top` by at least one. A returned SCC cycle is excluded until AC5lx--AC5mc supplies payment, ticket, impossibility or a named cycle-bank descent.

For a cycle discharged by strict bounded descent, retain its exact nonnegative bank before and after values; completing the cycle lowers `r_cyc`. Source/recreation-ticket cycles are exceptional, not rank edges.

### Proof

Every edge of a DAG shortens the maximum remaining path length. The cycle compiler verifies the exact bank inequality on descent cycles and separates ticket routes. QED.

## AC5mf -- local repair component and immutable earlier components -- PROVED

A local canonical repair edge is accepted in the final repair component only when

\[
\Delta(v')=\Delta(v),
\quad
\Theta(v')=\Theta(v),
\quad
u_{\rm sig},u_{\rm sup},r_{\rm top},r_{\rm cyc}
\text{ are unchanged},
\]

and

\[
r_{\rm loc}(v')<r_{\rm loc}(v).
\]

An edge advertised as local repair while changing an earlier component is returned as a misclassification, even if the final scalar value happens to fall accidentally.

### Proof

The operation record exposes every component before and after. The route definition requires equality of all earlier components and strict local decrease. QED.

## AC5mg -- complete physical internal-edge stratification -- PROVED

Every internal nonterminal operation is accepted in exactly one ordered class.

1. **Supply:** `Delta` strictly decreases.
2. **Credited restart:** `Delta` is fixed, `Theta` strictly decreases and no unaccounted activation mass appears.
3. **First exposure:** the two earlier ordinal components are fixed and `u_sig` decreases.
4. **Support descent:** earlier components are fixed and `u_sup` decreases.
5. **Acyclic signature progress:** earlier components are fixed and `r_top` decreases.
6. **Cycle-bank descent:** earlier components are fixed and `r_cyc` decreases.
7. **Local repair:** every earlier component is fixed and `r_loc` decreases.
8. **Exceptional:** one live globally addressed payment, reuse ticket, reopening ticket, cycle ticket, disturbance, recreation ticket or funded-reset occurrence is consumed.

An edge receiving no class, two primary classes, an earlier-component increase, or an exceptional label without a live occurrence is rejected with its exact before/after vector and operation address.

### Proof

Choose the first differing ordinal/rank component in the displayed order. A progress class is accepted only when that component decreases. Exceptional edges are separated before rank comparison by their physical debit record. The fixed order makes the classes mutually exclusive. QED.

## AC5mh -- strict ordinal descent on physical progress edges -- PROVED

Define

\[
\Phi_{\rm phys}(v)
=
\omega^2\Delta(v)
+
\omega\Theta(v)
+
\rho_{\rm phys}(v).
\]

Every accepted supply, credited-restart, first-exposure, support-descent, acyclic-signature, cycle-bank or local-repair edge strictly decreases `Phi_phys`.

No finite upper bound on `Delta`, `Theta` or `rho_phys` over every future box is needed for qualitative termination. Every individual state has finite coefficients, and well-founded ordinal descent forbids an infinite progress-only trajectory.

### Proof

Supply lowers the `omega^2` coefficient; credited restart lowers the `omega` coefficient with deficit fixed; every remaining progress route lowers the mixed-radix natural coefficient with both earlier ordinal coefficients fixed. QED.

## AC5mi -- physical rank/stratification manifest compiler -- PROVED

For every operation exposed from the manifested AN seed and its descendants, the compiler:

1. reconstructs every rank component from the accepted physical ledgers;
2. checks the complete before/after component vector;
3. applies AC5mg;
4. verifies strict ordinal decrease on progress edges;
5. verifies one live globally addressed debit on exceptional edges;
6. appends accepted records to the overlap-preserving shell rank and edge-stratification tables.

The output is exactly one of:

- an accepted progress edge and its strict rank witness;
- an accepted exceptional edge and its physical debit;
- a boundary route;
- the first component reconstruction failure;
- the first mislabeled or nondecreasing edge;
- the first missing, exhausted, duplicated or relabelled exceptional occurrence.

Combined with reachable cofinality and the global exceptional source network, an accepted complete table satisfies the remaining physical hypotheses of the initial-state ordinal termination theorem.

### Proof

AC5md--AC5mf construct the physical repair components, AC5mg stratifies edges and AC5mh proves progress descent. The existing global exception compiler validates exceptional debits. Their ordered outputs populate the two manifest sections. QED.

## Deterministic audit

`scripts/verify_ac_physical_edge_stratification.py` checks 2,500 generated physical edge records. It verifies every progress component, mixed-radix strict descent, exceptional debit separation, earlier-component misclassification and missing occurrence failures.

## Main AC frontier

Only AC remains active. The next physical tasks are:

1. compute these rank components on the actual operations reached from the AN seed;
2. repair every returned nondecreasing or misclassified edge;
3. connect every exceptional debit to the integrated physical source network;
4. run fair reachable shell expansion with overlap-preserving rank extensions;
5. complete the remaining manifest sections or retain the first finite witness.

AC6 and the global no-three-in-line conjecture remain open.
