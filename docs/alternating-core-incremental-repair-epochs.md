# Alternating-core incremental repair epochs

## Status

This note proves AC5fp--AC5ft under the exact repair-source compatibility and occurrence-faithful source contracts from AC5fa--AC5fo. It does not construct the geometric compatibility predicate, prove AC5 or AC6, or prove the no-three-in-line conjecture.

## Setup

At one repair epoch let `R` be the selected repair incidences, `T` the live repair-source tokens, and

\[
E=\{(r,t):\operatorname{Compat}(r,t)\}
\]

an exact dictionary computed from the complete retained incidence and token addresses. Let `d:R->T` be an injective compatible assignment.

At the next epoch write

\[
R'=R^\circ\sqcup \Delta R,
\qquad
T'=T^\circ\sqcup \Delta T.
\]

Here `R^circ` and `T^circ` are exactly the records whose complete predicate inputs, physical identity, class, epoch signature and occurrence address are unchanged. New, relabelled or otherwise changed records belong to `Delta R` or `Delta T`; deleted records belong to neither next-epoch set. The compatibility predicate itself is required to be unchanged on pairs from `R^circ x T^circ`.

## AC5fp -- unchanged-pair persistence -- PROVED

For every `r in R^circ` and `t in T^circ`,

\[
\boxed{
\operatorname{Compat}'(r,t)=\operatorname{Compat}(r,t).
}
\]

Consequently the old exact dictionary may be copied without reevaluation on `R^circ x T^circ`.

### Proof

Every input used by the deterministic compatibility predicate is unchanged on the two records, and the predicate version is unchanged. Therefore its truth value is unchanged. QED.

## AC5fq -- boundary-only exact dictionary audit -- PROVED

The only next-epoch pairs requiring evaluation are

\[
\mathcal B
=
(\Delta R\times T')
\sqcup
(R^\circ\times\Delta T).
\]

The union is disjoint and has exact size

\[
\boxed{
|\mathcal B|
=|\Delta R|\,|T'|+|R^\circ|\,|\Delta T|.
}
\]

If the old dictionary is exact, the copied unchanged block is retained, and the stored next-epoch dictionary agrees with `Compat'` on every pair in `mathcal B`, then the next-epoch dictionary is exact on all of `R' x T'`.

### Proof

The product `R' x T'` is the disjoint union of the unchanged block `R^circ x T^circ` and the displayed boundary. AC5fp certifies the unchanged block; the boundary audit certifies every remaining pair. QED.

## AC5fr -- carried matching deficit bound -- PROVED

Restrict the old assignment `d` to unchanged incidences whose assigned tokens are also unchanged:

\[
M^\circ
=
\{(r,d(r)):r\in R^\circ,\ d(r)\in T^\circ\}.
\]

Let

\[
a=|\Delta R|,
\qquad
b=|\{r\in R^\circ:d(r)\notin T^\circ\}|.
\]

Then `M^circ` is a compatible matching in the next-epoch dictionary and leaves at most

\[
\boxed{a+b}
\]

next-epoch incidences unmatched.

### Proof

Restriction preserves injectivity. Every retained pair lies in the unchanged block and remains compatible by AC5fp. Exactly `|R^circ|-b` unchanged incidences remain matched, while `R'` contains `|R^circ|+a` incidences. Their difference is `a+b`. QED.

## AC5fs -- bounded reaugmentation or canonical Hall core -- PROVED

Let `u=a+b`. Exactly one of the following holds in the exact next-epoch compatibility graph:

1. a complete compatible assignment exists and can be reached from `M^circ` using at most `u` augmenting paths;
2. no complete assignment exists, the maximum matching deficit `delta` satisfies
   \[
   \boxed{1\le\delta\le u,}
   \]
   and AC5ff--AC5fj return the canonical positive-deficit Hall core, saturated old neighbourhood and missing-compatibility rectangle;
3. one purportedly unchanged record, compatibility edge or occurrence token fails the retained-field contract.

### Proof

Every augmenting path increases matching size by one. Since `M^circ` leaves at most `u` incidences unmatched, at most `u` successful augmentations can saturate `R'`. If saturation is impossible, the carried matching already has size at least `|R'|-u`, so the maximum matching deficit is at most `u`; apply AC5ff--AC5fj to the exact graph. QED.

## AC5ft -- bounded-churn recurrent repair router -- PROVED UNDER THE EPOCH CONTRACT

For a finite sequence of repair epochs, let `mathcal B_j` be the boundary pair set and let `u_j=a_j+b_j` be the carried matching disturbance at transition `j`. If every unchanged-block declaration is valid, then exact dictionaries and compatible assignments may be maintained using at most

\[
\boxed{
\sum_j |\mathcal B_j|
}
\]

new compatibility evaluations and at most

\[
\boxed{
\sum_j u_j
}
\]

augmenting paths. Matching maintenance creates no repair-source mass; actual issuance remains governed by AC5fa--AC5fc.

Every failure has a first exact form:

1. a missing or spurious boundary edge;
2. a record incorrectly declared unchanged;
3. an omitted field, stale epoch signature or relabelled address;
4. a source-conservation or repeated-debit failure;
5. a canonical Hall core of deficit at most the current disturbance `u_j`.

### Proof

Apply AC5fq and AC5fs independently at each transition and sum their exact bounds. The source ledger is untouched by merely carrying or augmenting a proposed matching; debits occur only at issuance. First-failure ordering is inherited from the deterministic boundary, source-ledger and Hall-core audits. QED.

## Corrected AC6 frontier

A recurrent restricted-menu repair process no longer requires a full compatibility recomputation after every bounded physical change. The cost is localized to the incidence-token boundary created by new or changed records, and the matching repair cost is bounded by new incidences plus disturbed old assignments. Remaining work is to prove bounded churn for the concrete alternating-core menu, construct its geometric compatibility predicate, and discharge the returned boundary, source-ledger or Hall-core witnesses.

## Finite check

`scripts/verify_ac_incremental_repair_epochs.py` generates finite exact compatibility dictionaries, mutates incidence and token records, verifies unchanged-edge persistence and boundary reconstruction, and checks the carried-matching and reaugmentation deficit bounds.