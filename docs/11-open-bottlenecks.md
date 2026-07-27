# Open bottlenecks and research roadmap

## 1. Current proof status

The no-three-in-line conjecture remains open. Through CMR1933 the branch has:

- exact structural/SCC reductions and label-preserving CRT gluing;
- exact rook response laws and line-clean integer budgets;
- a corrected 740-host side-four/five geometric layer;
- exact response-averaged line moments and rank-three slack budgets;
- primitive geometric witness reconstruction;
- absolute last-entering owners and total witness fate maps;
- exact source-to-assignment coefficient bundles;
- injective destroyed-current-triple cancellation;
- exact average and uniform destruction-credit slacks;
- nested assignment bounds and one unified outer score;
- a denominator-cleared labelled assignment-certificate checker.

No theorem proves that every positive minimum of the real-triple potential becomes
zero.

The honesty condition remains:

> finite response, finite resource use and structural descent are not by themselves
> potential improvement.

A completion must exhibit a lower-potential response or an exact weighted
inequality guaranteeing one.

## 2. Closed structural components

Last-entering ownership makes the labelled offspring matrix block upper triangular
after exact SCC contraction:

\[
\rho(A)=\max_i\rho(A_{ii}).
\]

All owner, collision, local-line, interface, root, thin and CRT labels remain until
exact equivalence or honest componentwise domination is proved.

Already-certified auxiliary modules eliminate through

\[
A+B(I-D)^{-1}C.
\]

Reverse-topological rational scaling absorbs finite off-diagonal transfers and
clears to one global integer certificate.

## 3. Current finite geometric data

The corrected geometric layer contains 86 side-four and 654 side-five raw hosts.
For every one of these 740 hosts:

1. the exact response denominator is known;
2. every response matching is enumerated;
3. every nonaxis line has exact occupancy capacity;
4. every nonaxis line has exact response-averaged moments `z_1,z_2,z_3`;
5. the exact rank-three numerator and slack are known.

The exact rank-three split is:

| class | side four | side five | total |
|---|---:|---:|---:|
| strict `S_3>0` | 53 | 598 | 651 |
| critical `S_3=0` | 6 | 38 | 44 |
| excess `S_3<0` | 27 | 18 | 45 |

## 4. Exact averaged geometric rows

For actual background line loads `h_ell`,

\[
A_G(B)
=
\sum_\ell
\left[
 \binom{h_\ell}{2}z_1(G,\ell)
 +h_\ell z_2(G,\ell)
 +z_3(G,\ell)
\right].
\]

The identities

\[
\sum_\ell z_2(G,\ell)=Z(G)\binom d2,
\qquad
\sum_\ell z_3(G,\ell)=A_3(G)
\]

fix the total pair and triple moments.

For a strict host, after exact rank-three payment,

\[
R_G(h)
=
\sum_\ell
\left[
 \binom{h_\ell}{2}z_1(G,\ell)
 +h_\ell z_2(G,\ell)
\right]
\]

must satisfy

\[
R_G(h)\le S_3-1.
\]

Maximum-occupancy, Pareto and line-length compilers remain valid fallbacks when the
exact background profile is unavailable.

## 5. Primitive witnesses and exact owners

The raw source enumerates:

- rank-one background-pair witnesses;
- rank-two background-point witnesses;
- rank-three response-triple witnesses.

A strict total response-edge order gives

\[
\operatorname{own}(w)=\max_\prec P(w).
\]

Every witness receives exactly one fate:

1. retained in a recurrent child with the same owner;
2. deleted with rule-specific evidence;
3. transferred to a lower-stratum off-diagonal or auxiliary child;
4. dominated by an explicit positive upper multiplicity in the same owner class.

The generic owner/fate checker proves completeness, owner preservation and exact
coefficient export. It does not prove an arbitrary evidence identifier.

## 6. Exact source-to-coefficient handoff

The owner/fate source exports an integer table `c^(r)_j(P)`. The downstream bundle
contains the source inline, its canonical SHA-256 fingerprint, the exact denominator
and the labelled edge/pair/triple table.

`check_geometric_assignment_bundle.py` requires direct equality with the source
export. There is no unchecked copying or aggregation step between primitive
geometry and the assignment LP.

## 7. Destroyed-current-triple cancellation

Let `P` be the exact point set before the response operation and `R` the removed
subset. The destroyed current triples are exactly

\[
\mathcal D(P,R)
=
\{T\in\binom P3:T\text{ collinear and }T\cap R\ne\varnothing\}.
\]

A cancellation manifest must satisfy:

1. deleting the declared indices leaves exactly the source background;
2. every deleted witness has one unique cancellation identifier;
3. every identifier maps to one actual member of `\mathcal D(P,R)`;
4. no destroyed triple credit is reused.

If `C` is the reserved image, define

\[
U=|\mathcal D(P,R)|-|C|.
\]

For every response,

\[
N_{\rm raw}(Q)-|\mathcal D(P,R)|
\le
B(Q)-U.
\]

Thus unused destroyed triples remain as exact potential credits after all deleted
witnesses are paid.

## 8. Exact strictness from unused destruction credit

Let

\[
A_B=\sum_QB(Q),
\qquad
M_B=\max_QB(Q),
\qquad
Z=|\operatorname{PM}(G)|.
\]

Define

\[
\Sigma_{\rm avg}=ZU-A_B,
\qquad
\Sigma_{\rm all}=U-M_B.
\]

- `Sigma_avg>0` proves at least one improving response.
- `Sigma_all>0` proves every response improves.

Any proved numerator upper bound `L` may replace `A_B`. In nested assignment
currency,

\[
6l_1+3l_2+l_3<6ZU
\]

is sufficient. If one outer assignment maximum `M` controls every `B(Q)`, then
`M<U` proves uniform improvement.

## 9. Publication-grade assignment certificate

After source, fate semantics, cancellation and coefficient linkage are verified,
positive integer child weights are aggregated before peeling. The final manifest
stores every contracted dual, one unified outer dual and positive row slack.
Passing every recurrent row proves `AX<X`.

The complete checked pipeline is now

\[
\boxed{
\text{raw geometry}
\to
\text{owner/fate source}
\to
\text{destroyed-credit certificate}
\to
\text{exact coefficient bundle}
\to
\text{assignment dual manifest}
\to
AX<X.
}
\]

## 10. Immediate execution order

### Priority 1: instantiate actual removal geometry

For each of the 740 raw hosts and each retained background/provenance fibre:

1. record the exact pre-response point set;
2. record the points actually removed;
3. verify the surviving ordered background;
4. enumerate the actual destroyed current triples;
5. record the response-edge entry order.

### Priority 2: certify deletion fates

For every deleted witness:

1. first test whether it admits injective destroyed-triple cancellation;
2. reserve one exact destroyed current triple when it does;
3. reject duplicate credit use;
4. retain the witness if no valid cancellation or other proved correction exists;
5. preserve the accepted evidence in the owner/fate source.

### Priority 3: prove the remaining fate semantics

For transferred or dominated witnesses:

1. verify the exact child state and owner/provenance labels;
2. verify strict structural descent or an already-certified auxiliary target;
3. verify every domination multiplicity by an explicit upper argument;
4. reject any fate whose evidence cannot be proved.

### Priority 4: close the 651 budgeted hosts

For each rank-three-strict host and retained fibre:

1. load `S_3-1`;
2. add unused destruction credit `U`;
3. evaluate exact response-averaged line costs;
4. insert return and selector coefficients;
5. use exact or nested rank-two terms as needed;
6. generate one unified outer dual.

### Priority 5: resolve the 89 exceptional hosts

For the 44 critical and 45 excess hosts, test:

1. injective destroyed-triple cancellation;
2. corrected genuinely-new witness deletion;
3. nonuniform child weights and owner-preserving routing;
4. exact rather than peeled marginal rows;
5. finer owner/interface state splitting;
6. certified off-diagonal or auxiliary transfer.

### Priority 6: publish and eliminate

For each successful recurrent block:

1. export the accepted cancellation-certified coefficient bundle;
2. generate all contracted and outer duals;
3. record positive integer row slacks;
4. pass the arithmetic checker;
5. eliminate certified auxiliary modules through exact rational resolvents;
6. solve remaining collision/local-line SCCs;
7. clear denominators and publish the global CRT quotient.

## 11. Genuine unresolved modules

1. **Actual pre-response geometry.** The generic cancellation format is complete,
   but the true point/removal data are not populated for all 740 fibres.
2. **Non-cancellation fate proofs.** Some deletion, domination and transfer evidence
   still needs rule-specific verification.
3. **Budgeted host rows.** The 651 strict hosts have not all combined `S_3-1`, `U`,
   line, return and selector coefficients.
4. **Exceptional hosts.** The 89 critical/excess hosts still need corrected or
   weighted fate maps.
5. **Reused-support survivors.** Some small-support rows remain explicit.
6. **Collision/local-line SCCs.** Fully labelled recurrent blocks still need strict
   numerical certificates.
7. **Global integer quotient.** No complete denominator-cleared certificate has
   been published.

## 12. Corrections that must remain active

- Historical selectors, traces, target lines and destroyed loads are not one
  simultaneous current family.
- Finite scheduler termination is not potential improvement.
- Rank-mass conservation counts prescriptions, not geometric multiplicities.
- Matching normalization does not quotient Euclidean geometry.
- Silent witness deletion is invalid.
- One destroyed triple cannot pay two deleted witnesses.
- Unused destruction credit is valid only for the actual operation's point and
  removal data.
- A transfer-role declaration does not prove the transition executes.
- An evidence identifier does not prove deletion, domination or auxiliary
  subcriticality.
- Passing source, cancellation and coefficient checkers proves their stated finite
  equalities only.
- Auxiliary resolvent elimination requires an already-proved strict certificate.
- Failure of a coarse upper model does not prove the exact row supercritical.

## 13. Current endpoint

Through **CMR1933**, the data path from primitive geometry to exact scalar
improvement and the integer assignment LP is explicit and independently checkable.
The unresolved core is to instantiate the actual 740-host removal/fate data, prove
all remaining semantic obligations, solve every labelled recurrent row and publish
the final strict integer quotient.
