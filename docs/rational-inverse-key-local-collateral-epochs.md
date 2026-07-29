# Rational-inverse key-local collateral epochs

## Status

This note proves RI5gw--RI5gz under the exact typed collateral and incremental-epoch contracts through RI5gv. It does not construct the arithmetic key dictionary, prove RI6, or prove the no-three-in-line conjecture.

## Setup

Let `kappa_R:R'->K` and `kappa_T:T'->K` be complete coarse collateral keys built from the retained owner/charge class, arithmetic profile, repair class and occurrence type. Assume

\[
\operatorname{Compat}'(r,t)\Longrightarrow \kappa_R(r)=\kappa_T(t).
\]

A changed key makes the complete record changed; it may not remain in the unchanged block. Write `R'=R^circ sqcup Delta R` and `T'=T^circ sqcup Delta T`, and use subscripts `k` for key fibres.

## RI5gw -- exact cross-key exclusion -- PROVED UNDER THE KEY CONTRACT

Every cross-key pair is a certified nonedge. Hence the next exact compatibility graph is the disjoint union of its within-key graphs:

\[
E'=\bigsqcup_{k\in K} E'_k.
\]

A missing key, changed key, or compatibility edge joining unequal keys is returned as a first typed-address failure.

## RI5gx -- key-local changed boundary -- PROVED

Only the pairs

\[
\mathcal B_k=(\Delta R_k\times T'_k)\sqcup(R_k^\circ\times\Delta T_k)
\]

require fresh evaluation. The complete audited boundary is the disjoint union over keys and has exact size

\[
\boxed{
|\mathcal B^{\kappa}|=
\sum_k\bigl(|\Delta R_k||T'_k|+|R_k^\circ||\Delta T_k|\bigr).
}
\]

Copying the exact unchanged within-key blocks and exactly evaluating these pairs reconstructs the complete next dictionary. Cross-key pairs need no predicate evaluation because RI5gw certifies them false.

## RI5gy -- bounded key-fibre audit -- PROVED

Put

\[
L_T=\max_k|T'_k|,
\qquad
L_R=\max_k|R_k^\circ|,
\qquad
a=|\Delta R|,
\qquad c=|\Delta T|.
\]

Then

\[
\boxed{|\mathcal B^{\kappa}|\le aL_T+cL_R.}
\]

Thus bounded typed fibres turn compatibility maintenance into a linear function of changed records rather than the total incidence-token product.

## RI5gz -- physical edit churn and reaugmentation -- PROVED

Let `e=|T\setminus T^circ|` be the number of old collateral tokens deleted, changed or relabelled. Because the old assignment is injective, the number `b` of unchanged incidences whose assigned token is not unchanged satisfies

\[
\boxed{b\le e.}
\]

If one physical RI step has `a<=A`, `c<=C_+`, `e<=C_-`, and the key-fibre bounds above, then:

1. at most `AL_T+C_+L_R` compatibility evaluations are required;
2. the carried matching leaves at most
   \[
   \boxed{u=a+b\le A+C_-}
   \]
   incidences unmatched;
3. at most `A+C_-` augmenting paths restore a complete assignment, or the typed Hall deficit is at most `A+C_-`;
4. carrying and augmenting assignments creates no collateral mass.

The proof is RI5gx--RI5gy plus injectivity of the old assignment and RI5gt--RI5gu.

## Corrected RI6 frontier

The RI maintenance cost is now controlled by per-step record churn and maximum compatible key-fibre sizes. Remaining work is to prove concrete bounds for the arithmetic owner/charge keys, evaluate only the returned within-key boundary, and pay any bounded-deficit typed Hall core.

## Finite check

`scripts/verify_ri_key_local_collateral_epochs.py` generates exact keyed compatibility graphs, mutates typed records, verifies cross-key exclusion, exact key-local reconstruction, the fibre bound, `b<=e`, and the new deficit bound.