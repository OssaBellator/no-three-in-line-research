# Open bottlenecks and research roadmap

## 1. Current proof status

The no-three-in-line conjecture remains open.  The branch contains a large
finite-response and structural-descent theory, but no theorem yet forces every
positive minimum of the real-triple potential to become zero.

The decisive honesty correction remains CMR1190--CMR1197:

> finite scheduler termination is not potential improvement.

A completion must exhibit an actual lower-potential response or an exact weighted
inequality which guarantees one.

## 2. What is now structurally closed

The proved chain includes:

1. inherited parent banks, Hall walls, closure envelopes and exchange ancestry;
2. primitive-height, line-clean, carry, token, packet and cycle-erasure geometry;
3. exact rollback, SCC, protected/free, unit-wall and child products;
4. minimum-face restriction, host-representable contraction and owner-normalized
   loss/restoration ledgers;
5. target handoff, protected execution, loaded-line and star response banks;
6. terminal blocker covers as exact deficiency-one unit walls;
7. small full-grid classifications through side six, with inherited-coordinate
   scope retained for residual factors;
8. last-entering collateral credits and exact rational spectral certificates.

No routing, blocker, wall, fixed-core, small-factor or owner-reset recurrence
remains anonymous.

## 3. Product and fixed-interface triangularity is solved

CMR1318--CMR1325 prove the previously open product-gluing step.

A one-coordinate product response changes edges in one residual factor only.
Every newly created triple therefore has its last-entering owner edge in that
factor, even when the triple also contains fixed-core or sibling-factor cells.
Contraction creates no new credit, and a fully fixed target is answered at its
existing lifted owner.

The selected structural owner graph is finite and acyclic.  Its global offspring
matrix is block upper triangular, so

\[
\rho(A)=\max_i\rho(A_{ii}).
\]

Arbitrarily large but finite off-diagonal cross-factor collateral changes only
the scale of the Lyapunov weights.  It is no longer a separate subcriticality
obstruction.

## 4. Exact same-owner matrices and coarse upper quotients

At one finite owner, complete state-target pairs give exact credit classes.
Any geometric compression

\[
\pi:\Sigma_{\mathrm{exact}}\to\overline\Sigma
\]

has exact coarse row sums.  Componentwise maxima over exact rows produce an
honest upper quotient `Ahat`.

A certificate

\[
\widehat A v<v
\]

lifts to every exact host state.  It may be stored as finite strict integer
inequalities after clearing denominators.  Deterministic response laws suffice
once the weight vector is fixed.

This removes the need to assume exact lumpability of line-height or carry classes.

## 5. Extension-free target banks

For one target cell `e` and opposite matching `O`, the complete response family is

\[
\operatorname{PM}(K_{n,n}\setminus(O\cup\{e\})).
\]

Every response has a canonical realizing forbidden extension.

If `D_n` is the derangement number, the bank size is exactly

\[
D_n\frac{n-2}{n-1}.
\]

Put

\[
\lambda_n=\frac{n!(n-1)}{D_n(n-2)}.
\]

Then `lambda_n<=4`, while every allowed edge has marginal at most `1/(n-2)`.
Thus corrected candidate counts satisfy

\[
\mathbb E N(R)
\le
\frac{V_1^e}{n-2}
+
\lambda_n
\left[
\frac{V_2^e}{(n)_2}
+
\frac{V_3^e}{(n)_3}
\right].
\]

The same sharp rank-one coefficient controls unavailable-edge use.  Complete
blockage still gives strict unit-wall descent.

The fixed-extension optimization problem is therefore closed for averaging.

## 6. Exact line profiles and pair moments

Axis lines contribute no response-state triples.  Every subset of a nonaxis line
is matching-compatible.

For

\[
o_L=|O\cap L|,
\qquad
g_L=|G\cap L|,
\qquad
m_L=|M_G\cap L|,
\]

the corrected counts are

\[
V_1=\sum_L\binom{o_L}{2}(g_L-m_L),
\]

\[
V_2=\sum_Lo_L
\left[\binom{g_L}{2}-\binom{m_L}{2}\right],
\]

\[
V_3=\sum_L
\left[\binom{g_L}{3}-\binom{m_L}{3}\right].
\]

The exact pair moments are

\[
\sum_L\binom{o_L}{2}=\binom n2,
\qquad
\sum_L\binom{g_L}{2}=P_2(G),
\qquad
\sum_L\binom{m_L}{2}=\binom{|M_G|}{2}.
\]

Residual rank plus dyadic bands for `(o_L,g_L,m_L)` gives at most

\[
3(2+\lfloor\log_2n\rfloor)^3
\]

profile classes, with explicit pair-moment tail and band envelopes.

## 7. Exact all-target line-composition kernel

For a nonaxis line with `o` opposite-layer cells, `m` targeted-layer cells and
`u` unselected cells, summing all extension-free banks through the targeted
layer gives

\[
\sum_eV_1^e=n\binom o2u,
\]

\[
\sum_eV_2^e
=o\left[(n-1)mu+n\binom u2\right],
\]

\[
\sum_eV_3^e
=(n-2)\binom m2u
+(n-1)m\binom u2
+n\binom u3.
\]

The exact destroyed target incidence is

\[
m\binom{o+m-1}{2}
\]

in that layer and

\[
3\binom{o+m}{3}
\]

across both layers.

After inserting the sharp response probabilities, a strict global symmetric
kernel inequality gives an improving target-cell response.

## 8. The new obstruction: independent lines are too coarse

CMR1372 gives a realizable full-grid state at side five with exact target
incidence

\[
3\Phi(S)=6
\]

but independent-line extension-free upper kernel

\[
\frac{160}{11}>6.
\]

This is not a counterexample to improvement.  It proves that pair moments and
independent line maxima alone cannot certify improvement.

The missing gain must use at least one of:

- shared response-edge assignment across several lines;
- primitive-height scarcity and line-energy distribution;
- prefix, quotient or carry cancellation;
- a stronger joint law for rank-two/rank-three response prescriptions;
- cross-line weighted credits rather than independent line weights.

## 9. Recommended next lemmas

1. **Cross-line edge assignment.**  Express the symmetric kernel as an edge-weighted
   matching cost so one response edge pays all lines through it only once.
2. **Height-band joint moment.**  Bound the total rank-two/rank-three kernel inside
   one primitive-height band using the existing prefix and carry ledgers.
3. **Diagonal upper quotient.**  Populate exact rows for the rank/profile/height
   classes and search for a rational `Av<v` certificate.
4. **Thin and prime-field diagonal blocks.**  Replace nonroot prefix depth with a
   direct line-distribution certificate.
5. **CRT diagonal assembly.**  Retain collision/local-line classes in each local
   factor, then use the already-proved structural triangularity.

## 10. Computational priorities

- Enumerate exact extension-free offspring rows by line profile and owner edge for
  small inherited coordinate sets.
- Solve exact rational linear programs for candidate Lyapunov weights.
- Measure the gap between independent-line kernel bounds and exact bank
  expectations, split by primitive height.
- Test whether rank-two/rank-three pair marginals admit useful negative-correlation
  or assignment inequalities.
- Verify block-diagonal certificates before adding finite off-diagonal product
  terms.

## 11. Current proved endpoint

Through **CMR1373**:

- product and fixed-interface offspring are exactly block triangular;
- arbitrary coarse geometric classes have honest upper quotients;
- extension-free bank sizes and rank-one marginals are exact;
- higher-rank probability loss is at most four;
- line profiles and pair moments give explicit dyadic envelopes;
- all-target candidate sums have a closed line-composition kernel;
- independent linewise domination is explicitly insufficient.

There is still no complete proof.  The next genuine advance must be a cross-line
same-owner inequality or an exact subcritical diagonal certificate.
