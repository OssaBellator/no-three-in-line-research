# Open bottlenecks and research roadmap

## 1. Current proof status

The no-three-in-line conjecture remains open.  Through CMR1901 the branch has:

- exact structural/SCC reductions and label-preserving CRT gluing;
- exact rook response laws and line-clean integer budgets;
- geometric prescription multiplicities and exact line energy;
- a corrected 740-host side-four/five geometric layer;
- complete rank-three and full-length-line data through side five;
- exact occupancy and response-averaged line-moment compilers;
- denominator-preserving Pareto and background-height envelopes;
- exact rank-three residual line budgets;
- nested assignment bounds and one unified outer score;
- a raw primitive-witness routing checker;
- a denominator-cleared labelled assignment-certificate checker.

No theorem proves that every positive minimum of the real-triple potential becomes
zero.

The honesty condition remains:

> finite response, finite resource use and structural descent are not by
> themselves potential improvement.

A completion must exhibit a lower-potential response or an exact weighted
inequality guaranteeing one.

## 2. Closed structural components

Last-entering ownership makes the complete labelled offspring matrix block upper
triangular after exact SCC contraction:

\[
\rho(A)=\max_i\rho(A_{ii}).
\]

All owner, collision, local-line, interface, root, thin and CRT labels remain until
exact equivalence or honest componentwise domination is proved.

Already-certified auxiliary modules eliminate through

\[
A+B(I-D)^{-1}C.
\]

Reverse-topological rational scaling then absorbs finite off-diagonal transfers
and clears to one global integer certificate.

## 3. Current finite geometric data

The matching denominator classes expand to exactly 86 side-four and 654 side-five
raw coordinate-labelled hosts.  For every one of these 740 hosts:

1. the exact response denominator is known;
2. every response matching is enumerated;
3. every nonaxis line has exact occupancy capacity `tau_G(ell)`;
4. every line has exact response-averaged moments `z_1,z_2,z_3`;
5. the complete line-length/occupancy census is known;
6. the exact uniform rank-three numerator `A_3` is known;
7. the anti-diagonal capacity is known exactly.

Every response has `Psi(Q)` in `{0,1,2,4}`.  Side five satisfies `5A_3<=7Z`, with
sharper exact denominator entries.

## 4. Exact response-averaged geometric rows

For each line,

\[
z_r(G,\ell)
=
\sum_{Q\in\operatorname{PM}(G)}
\binom{|Q\cap\ell|}{r}.
\]

For actual background loads `h_ell`, the exact uniform-response numerator is

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

The global identities

\[
\sum_\ell z_2(G,\ell)=Z(G)\binom d2,
\qquad
\sum_\ell z_3(G,\ell)=A_3(G)
\]

show that the total pair coefficient is fixed by side and denominator and the
triple coefficient is already tabulated.  Only the total rank-one incidence
moment varies freely.

For a uniform height cap `H`, the exact response-averaged layer has:

- 13 side-four and 90 side-five Pareto triples;
- only 48 triples active for some integer `H`;
- terminal phases by `H=2` on side four and `H=4` on side five.

The maximum-occupancy and line-length envelopes remain valid fallbacks, but the
exact averaged row should be used whenever the response law is uniform.

## 5. Rank-three slack as a line budget

For every raw host,

\[
S_3=Z-A_3.
\]

The exact classification is:

| class | side four | side five | total |
|---|---:|---:|---:|
| strict `S_3>0` | 53 | 598 | 651 |
| critical `S_3=0` | 6 | 38 | 44 |
| excess `S_3<0` | 27 | 18 | 45 |

For a strict host, after exact rank-three payment, the remaining geometric
numerator is

\[
R_G(h)
=
\sum_\ell
\left[
 \binom{h_\ell}{2}z_1(G,\ell)
 +h_\ell z_2(G,\ell)
\right].
\]

The scalar geometric row is strict exactly when

\[
R_G(h)\le S_3-1.
\]

This may be published as explicit nonnegative line budgets whose total is at most
`S_3-1`.

Across the 651 strict hosts:

| isolated active-line profile | active host-line pairs | individually fitting `S_3-1` | hosts with at least one fit | hosts with every active line fitting |
|---|---:|---:|---:|---:|
| load one | 34,618 | 27,192 | 594 | 26 |
| load two | 72,192 | 16,838 | 492 | 0 |

These are exact component tests.  A complete row still requires the sum of every
retained line, return and selector coefficient to fit the shared budget.

## 6. Raw primitive-witness routing

The geometric source manifest records each actual primitive candidate before
aggregation.

### Rank one

For every extendable response edge, list each unordered background pair collinear
with it.

### Rank two

For every extendable response pair, list each background point on its line.

### Rank three

For every extendable collinear response triple, list its unique primitive witness.

Every witness receives one declared child label.  Exact set equality with the
recomputed witness family proves no candidate was omitted or duplicated.
Aggregation by `(rank,child,prescription)` exports the geometric coefficient table
for the assignment manifest.

`scripts/check_geometric_candidate_routing_manifest.py` validates perfect
matchings, extendability, geometric incidence and witness conservation.  Its
self-test accepts 500 systems containing 6,063 witnesses and rejects ten corrupted
manifests.

The checker does not infer the semantic correctness of the child label.  Owner,
collision, interface and CRT rules need their own transition verification.

## 7. Corrected-row fate map

A raw witness may enter a corrected or upper table only through one explicit fate:

1. retained and routed to a labelled recurrent child;
2. removed by a verified genuinely-new correction;
3. transferred to a separately certified off-diagonal or auxiliary state;
4. honestly dominated by a declared upper coefficient.

The raw routing manifest certifies the domain of this fate map.  The final
coefficient generator must certify the image.  Silent deletion is invalid.

## 8. Publication-grade assignment manifest

For positive integer child weights `X_j`, aggregate every declared labelled
coefficient numerator before peeling.  Row `i` uses

\[
\Theta_i(e)=6q_i(e)+3j_{2,i}(e)+h_{3,i}(e).
\]

The downstream certificate stores:

- state weights;
- one denominator per row;
- all labelled edge, pair and triple coefficient numerators;
- complete rank-two contracted duals;
- complete rank-three inner and middle duals;
- one unified outer dual;
- one positive integer row slack.

The exact row inequalities are

\[
U_{i,u}+V_{i,v}\ge\Theta_i((u,v))
\]

and

\[
\sum_uU_{i,u}+\sum_vV_{i,v}
\le
6D_iX_i-\delta_i.
\]

`scripts/check_label_weighted_assignment_certificate.py` recomputes host perfect
matchings and extendable prescriptions, validates every coefficient and dual
surface and accepts only complete recurrent blocks.  Passing the checker proves
`AX<X` relative to the declared exact or componentwise upper coefficient table.

## 9. Immediate execution order

### Priority 1: generate exact raw routing manifests

For each retained background/provenance fibre:

1. specify the exact raw host and background points;
2. enumerate all rank-one, rank-two and rank-three primitive witnesses;
3. attach provisional child labels;
4. pass the raw routing checker;
5. preserve the witness-level file as the source of the aggregate coefficients.

### Priority 2: certify label semantics and correction

For every raw witness:

1. verify the absolute last-entering owner;
2. attach collision, local-line, interface, root, thin and CRT labels;
3. record any corrected deletion or off-diagonal transfer;
4. verify that the fate map is complete;
5. aggregate only after these checks pass.

### Priority 3: close the 651 budgeted hosts

For each strict rank-three host and retained fibre:

1. load the exact `S_3-1` budget;
2. evaluate exact line moments against the actual background heights;
3. insert return and selector scores;
4. use exact or nested rank-two coefficients as needed;
5. generate one unified outer dual within the shared budget.

### Priority 4: resolve the 89 exceptional hosts

For the 44 critical and 45 excess hosts, test in order:

1. corrected genuinely-new witness deletion;
2. nonuniform child weights and labelled routing;
3. exact rather than peeled marginals;
4. finer owner/interface state splitting;
5. auxiliary transfer or honest off-diagonal descent.

### Priority 5: publish and eliminate

For every successful recurrent row:

1. export the labelled integer coefficient table;
2. generate all contracted and outer duals;
3. record positive integer slack;
4. pass the arithmetic checker;
5. eliminate certified auxiliaries through exact resolvents;
6. solve the remaining collision/local-line SCCs and assemble the CRT quotient.

## 10. Genuine unresolved modules

1. **Semantic routing.** Raw geometric witnesses are checkable, but the correct
   owner/provenance child label is not populated for every state.
2. **Corrected fate maps.** The 89 exceptional hosts require explicit deletions,
   weighted routing, state refinement or off-diagonal transfer.
3. **Budgeted host rows.** The 651 positive rank-three slacks have not yet all been
   filled with actual line, return and selector coefficients.
4. **Reused-support survivors.** Some small-support rows remain explicit.
5. **Collision/local-line SCCs.** Fully labelled recurrent blocks still require
   numerical row certificates.
6. **Global integer quotient.** No complete denominator-cleared certificate has
   been published.

## 11. Corrections that must remain active

- Historical selectors, traces, target lines and destroyed loads are not one
  simultaneous current family.
- Finite scheduler termination is not potential improvement.
- Rank-mass conservation counts distinct prescriptions, not geometric
  multiplicities.
- Background triples become payment only through explicit current labelled charge
  maps.
- Matching normalization does not quotient Euclidean geometry.
- One matching-fibre representative is invalid without exact geometric equivalence
  or honest domination.
- Owner-support closure requires every retained child owner to lie in the claimed
  support.
- Auxiliary resolvent elimination requires an already-proved strict certificate.
- Failure of an occupancy, Pareto or peeled upper model may indicate a coarse
  certificate, not a supercritical exact row.
- Passing the raw routing checker proves witness conservation, not semantic label
  correctness.
- Passing the assignment checker proves arithmetic relative to declared
  coefficients, not the geometric correctness of the coefficient generator.

## 12. Current endpoint

Through **CMR1901**, the remaining problem is finite and explicit but unsolved:
generate semantically correct witness-level routing and correction maps, use exact
response-averaged line moments and rank-three slack to certify the surviving rows,
publish accepted integer manifests, eliminate auxiliary blocks and assemble the
final global quotient.
