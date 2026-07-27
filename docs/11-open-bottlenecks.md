# Open bottlenecks and research roadmap

## 1. Current proof status

The no-three-in-line conjecture remains open.  Through CMR1917 the branch has:

- exact structural/SCC reductions and label-preserving CRT gluing;
- exact rook response laws and line-clean integer budgets;
- a corrected 740-host side-four/five geometric layer;
- exact response-averaged line moments and rank-three slack budgets;
- denominator-preserving Pareto and line-height envelopes;
- primitive geometric witness reconstruction;
- a mechanically checked absolute last-entering owner partition;
- a total witness fate manifest;
- an exact source-to-assignment coefficient bundle;
- nested assignment bounds and one unified outer score;
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

Reverse-topological rational scaling absorbs finite off-diagonal transfers and
clears to one global integer certificate.

## 3. Current finite geometric data

The matching denominator classes expand to exactly 86 side-four and 654 side-five
raw coordinate-labelled hosts.  For every one of these 740 hosts:

1. the exact response denominator is known;
2. every response matching is enumerated;
3. every nonaxis line has exact occupancy capacity;
4. every nonaxis line has exact response-averaged moments `z_1,z_2,z_3`;
5. the complete line-length census is known;
6. the exact rank-three numerator `A_3` is known;
7. the exact rank-three slack `S_3=Z-A_3` is known.

Every response has `Psi(Q)` in `{0,1,2,4}`.  The side-five rank-three row satisfies
`5A_3<=7Z`, with sharper denominator-specific values.

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

show that only the global rank-one incidence moment remains freely host-dependent.

When exact background profiles are unavailable, retain the already-proved
maximum-occupancy, Pareto and line-length upper compilers.  They are fallbacks,
not substitutes for exact averaging when the response law is uniform.

## 5. Rank-three slack allocation

The exact host split is:

| class | side four | side five | total |
|---|---:|---:|---:|
| strict `S_3>0` | 53 | 598 | 651 |
| critical `S_3=0` | 6 | 38 | 44 |
| excess `S_3<0` | 27 | 18 | 45 |

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

This budget is shared by every retained geometric line contribution.  Return and
selector terms must also fit the same parent row after they are inserted.

## 6. Primitive witness source and owner partition

The raw source enumerates:

- rank-one background-pair witnesses;
- rank-two background-point witnesses;
- rank-three response-triple witnesses.

A strict total entry order on all extendable response edges gives

\[
\operatorname{own}(w)=\max_\prec P(w).
\]

The witness family partitions exactly by this owner.  Recurrent retained and
dominated routes must preserve the computed owner.

`check_geometric_owner_fate_manifest.py` recomputes the raw witness set, entry-order
owner and exported coefficient bins.  It rejects missing witnesses, duplicate
witnesses, wrong owners and invalid transfer targets.

## 7. Total fate map and honesty boundary

Every raw witness receives exactly one fate.

1. **Retained:** one coefficient in a recurrent child with the same owner.
2. **Deleted:** zero coefficients and one cited correction-evidence item.
3. **Transferred:** one coefficient in a lower-stratum off-diagonal or auxiliary
   child.
4. **Dominated:** an explicit positive upper multiplicity in a recurrent child with
   the same owner.

The manifest proves totality and prevents silent deletion.  It does not prove the
mathematical validity of a cited deletion, domination or auxiliary-transfer item.

Each nonretained fate therefore creates one explicit rule-specific proof
obligation.

## 8. Exact coefficient handoff

The owner/fate source exports an integer table `c^(r)_j(P)`.

A geometric-to-assignment bundle includes:

- the source manifest;
- a deterministic canonical SHA-256 fingerprint;
- the exact uniform response denominator;
- the downstream labelled edge, pair and triple table.

`check_geometric_assignment_bundle.py` revalidates the source and requires direct
equality with the downstream table.  There is no longer an unchecked aggregation
or copying step between primitive geometry and the assignment LP.

## 9. Publication-grade assignment certificate

For positive integer child weights `X_j`, aggregate verified coefficients before
peeling and define

\[
\Theta_i(e)=6q_i(e)+3j_{2,i}(e)+h_{3,i}(e).
\]

The final manifest stores all contracted duals, one unified outer dual and positive
row slack.  Its exact inequalities prove `AX<X`.

The full proof pipeline is therefore:

\[
\boxed{
\text{raw witnesses}
\to
\text{owner/fate manifest}
\to
\text{exact coefficient bundle}
\to
\text{assignment dual manifest}
\to
AX<X.
}
\]

Every arrow now has an executable equality or completeness checker.  The remaining
work is to prove the rule-specific semantic obligations and find strict duals.

## 10. Immediate execution order

### Priority 1: instantiate the 740 owner/fate sources

For each raw host and retained background/provenance fibre:

1. record the exact background points;
2. record the actual response-edge entry order;
3. enumerate all primitive witnesses;
4. compute the last-entering owner;
5. attach provisional complete state labels;
6. pass the owner/fate completeness checker.

### Priority 2: prove nonretained fate evidence

For every deleted, transferred or dominated witness:

1. identify the exact correction or transition theorem;
2. provide the rule-specific finite input;
3. run or add the corresponding verifier;
4. reject the fate if the evidence cannot be proved;
5. preserve the verified evidence identifier in the source manifest.

The current generic checker is not a substitute for these proofs.

### Priority 3: close the 651 budgeted hosts

For each rank-three-strict host and retained fibre:

1. load `S_3-1`;
2. evaluate exact averaged line costs against the actual background;
3. insert return and selector coefficients;
4. use exact or nested rank-two terms as appropriate;
5. generate one unified outer dual within the shared budget.

### Priority 4: resolve the 89 exceptional hosts

For the 44 critical and 45 excess hosts, test in order:

1. verified genuinely-new witness deletion;
2. nonuniform child weights and owner-preserving labelled routing;
3. exact rather than peeled marginal rows;
4. finer owner/interface state splitting;
5. certified auxiliary or strict off-diagonal transfer.

### Priority 5: publish and eliminate

For each successful recurrent block:

1. export the accepted coefficient bundle;
2. generate all contracted and outer duals;
3. record positive integer row slacks;
4. pass the assignment checker;
5. eliminate certified auxiliary modules through exact rational resolvents;
6. solve remaining collision/local-line SCCs;
7. clear denominators and publish the global CRT quotient.

## 11. Genuine unresolved modules

1. **Actual owner/fate data.** The generic source format is complete, but the 740
   real background/provenance fibres have not all been instantiated.
2. **Rule-specific fate proofs.** Deletion, domination and auxiliary-transfer
   evidence is not yet proved for every nonretained witness.
3. **Budgeted host rows.** The 651 positive rank-three slacks have not all been
   filled with actual line, return and selector coefficients.
4. **Exceptional hosts.** The 89 critical/excess hosts need corrected fate maps,
   weighted routing or finer states.
5. **Reused-support survivors.** Some small-support rows remain explicit.
6. **Collision/local-line SCCs.** Fully labelled recurrent blocks still require
   numerical row certificates.
7. **Global integer quotient.** No complete denominator-cleared certificate has
   been published.

## 12. Corrections that must remain active

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
- Owner-support closure requires every retained recurrent child to carry the
  computed owner.
- A transfer-role declaration is not proof that the transition executes.
- An evidence identifier is not proof of deletion, domination or auxiliary
  subcriticality.
- Silent witness deletion is invalid.
- Passing the owner/fate checker proves completeness and owner syntax only.
- Passing the coefficient bundle proves exact source/table equality only.
- Passing the assignment checker proves arithmetic relative to the verified table.
- Auxiliary resolvent elimination requires an already-proved strict certificate.
- Failure of a coarse upper model does not prove the exact row supercritical.

## 13. Current endpoint

Through **CMR1917**, the data path from primitive geometry to the integer
assignment LP is explicit and independently checkable.  The unresolved core is to
instantiate the actual 740-host fate maps, prove every nonretained semantic
obligation, solve every labelled recurrent row and publish the final strict integer
quotient.
