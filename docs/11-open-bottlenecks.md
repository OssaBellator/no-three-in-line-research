# Open bottlenecks and research roadmap

## 1. Current proof status

The no-three-in-line conjecture remains open.  Through CMR1853 the branch has:

- exact structural/SCC reductions and CRT gluing;
- exact rook response laws and line-clean integer budgets;
- geometric prescription multiplicities and exact line energy;
- a corrected 740-host side-four/five geometric layer;
- complete rank-three and longest-line data through side five;
- line-occupancy, moment and background-height compilers;
- nested assignment bounds for rank two and rank three;
- one unified return-selector-geometric outer score;
- a finite label-weighted rational LP for the final Lyapunov search.

No theorem yet proves that every positive minimum of the real-triple potential
becomes zero.

The honesty condition is unchanged:

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

Strict child descent, earlier-depth handoff and first-use resources are
structural arcs only when the chosen response actually executes them.  All owner,
collision, local-line, interface, root, thin and CRT labels remain until exact
state equivalence or honest componentwise domination is proved.

Already-certified auxiliary blocks eliminate through

\[
A+B(I-D)^{-1}C.
\]

Reverse-topological rational scaling glues certified blocks and finite transfers.

## 3. Current finite geometric data

The matching denominator classes expand to exactly:

\[
86
\]

raw side-four hosts and

\[
654
\]

raw side-five hosts.  These 740 coordinate-labelled hosts are the first exact
geometric layer before owner/provenance refinement.

For every raw host:

1. the exact response denominator is known;
2. every response matching is enumerated;
3. every nonaxis grid line has an exact occupancy capacity
   \[
   \tau_G(\ell)=\max_Q|Q\cap\ell|;
   \]
4. the moments
   \[
   M_r(G)=\sum_\ell\binom{\tau_G(\ell)}r
   \]
   are known;
5. the exact uniform rank-three numerator is known;
6. every line length and capacity is included in the completed census.

Every response through side five has `Psi(Q)` in `{0,1,2,4}`.  Thirty-seven
side-four hosts have rank-three row zero.  Side five satisfies `5A_3<=7Z`, with
sharper denominator-specific caps.

The only full-length nonaxis lines are the diagonals.  The main diagonal has
capacity zero.  The anti-diagonal has capacity `d` on an untouched even-side
host, but at most `d-2` on odd side.

## 4. Current geometric certificate choices

For background line loads `h_ell`, the exact deterministic capacity row is

\[
\mathcal C_G(B)
=
\sum_\ell
\left[
 \tau_G(\ell)\binom{h_\ell}{2}
 +\binom{\tau_G(\ell)}2h_\ell
 +\binom{\tau_G(\ell)}3
\right].
\]

If all relevant background lines have load at most `H`, use

\[
\mathcal C_G(B)
\le
\binom H2M_1(G)+HM_2(G)+M_3(G).
\]

For nonuniform heights, use the exact layer expansion

\[
\mathcal C_G(B)
=
M_3(G)
+
\sum_{s\ge2}(s-1)
\sum_{\ell:h_\ell\ge s}\tau_G(\ell)
+
\sum_{s\ge1}
\sum_{\ell:h_\ell\ge s}\binom{\tau_G(\ell)}2.
\]

For exact uniform response laws, use the rook numerator

\[
A_{\mathrm{line}}
=
\sum_xa_1(x)z(x)
+
\sum_{|P|=2}a_2(P)z(P)
+
\sum_{|P|=3}a_3(P)z(P).
\]

For a smaller upper certificate, use nested assignments for ranks two and three.
These methods may be mixed by rank, host or geometric class.

## 5. Final label-weighted LP

Let `x_j>0` be proposed Lyapunov weights on all surviving labelled states.  For
parent `i`, aggregate every child coefficient against `x_j` before peeling and
form

\[
\gamma_i(e;x)
=q_i(e;x)+\frac12J_{2,i}(e;x)+\frac16H_{3,i}(e;x).
\]

The row condition is

\[
\sum_jA_{ij}x_j
\le
\mathcal A_{G_i}(\gamma_i(.;x))<x_i.
\]

All contracted and outer assignment maxima may be replaced by rational dual
variables.  The complete certificate search is therefore one finite rational LP
with constraints

\[
U_{i,u}+V_{i,v}\ge
6q_i((u,v);x)+3j_{2,i}(u,v)+h_{3,i}(u,v)
\]

and strict row objectives below `6x_i`.

A strict rational solution clears to:

- integer state weights;
- signed integer inner and outer dual potentials;
- positive integer row slacks;
- a directly checkable global `Ax<x` certificate after SCC gluing.

Failure of this upper LP is not evidence that the exact row is supercritical.  It
identifies the parent, outer edge class or contracted inner score needing a
sharper geometric model.

## 6. Immediate execution order

### Priority 1: populate the 740-host coefficient layer

For each raw host and each retained background/provenance class, compute:

- exact background line heights;
- `a_1` edge scores;
- exact or nested `a_2` pair scores;
- the already-tabulated `a_3` numerator;
- absolute last-entering owners;
- collision, local-line, interface, root, thin and CRT child labels.

Use the diagonal and rank-three tables immediately rather than recomputing them.

### Priority 2: produce row certificates

For every surviving parent state:

1. aggregate child labels against trial weights;
2. choose exact marginal, occupancy or nested bounds classwise;
3. generate inner assignment duals;
4. generate the unified outer assignment dual;
5. record the strict row slack.

The preferred certificate is one unified dual, not the sum of independently
optimized return, selector and geometric maxima.

### Priority 3: eliminate auxiliary modules

Once thin, fixed-interface or reused-support modules have strict certificates,
eliminate them through exact rational resolvents and update the effective core.

### Priority 4: finish the labelled SCC quotient

Retain every surviving collision/local-line/CRT label, solve the LP on each
recurrent SCC, apply reverse-topological scaling, clear all denominators and
publish the global integer quotient.

## 7. Genuine unresolved modules

1. **Background/provenance fibres.** Actual geometric coefficients are not yet
   populated for every retained owner and interface class.
2. **Return-selector outer rows.** The unified score is proved, but a universal
   strict dual below the required parent weight is not yet known.
3. **Shorter-line rank-one/rank-two rows.** Rank three and full-length lines are
   complete; remaining geometry lies on shorter lines and provenance routing.
4. **Reused-support survivors.** Small-support rows not closed by owner-support,
   moment or line-capacity bounds remain explicit.
5. **Collision/local-line SCCs.** Fully labelled recurrent blocks still need
   numerical row certificates.
6. **Global integer quotient.** No complete denominator-cleared certificate has
   yet been published.

## 8. Corrections that must remain active

- Historical selectors, traces, target lines and destroyed loads are not one
  simultaneous current family.
- Finite scheduler termination is not potential improvement.
- Rank-mass conservation counts distinct prescriptions, not geometric
  multiplicities.
- Background triples become payment only through explicit current labelled charge
  maps.
- Matching normalization does not quotient Euclidean geometry.
- One matching-fibre representative is invalid without exact geometric
  equivalence or honest domination.
- Owner-support closure requires every retained child owner to lie in the claimed
  support.
- Auxiliary resolvent elimination requires an already-proved strict certificate.
- A failed peeled LP may indicate a coarse upper model rather than a true
  recurrent obstruction.

## 9. Current endpoint

Through **CMR1853**, the remaining problem is finite and explicit but unsolved:
populate the true labelled coefficients, solve the assignment-dual LP on every
surviving recurrent block, eliminate certified auxiliaries and publish the final
strict integer quotient.
