# Status and honesty ledger

**Last updated:** 26 July 2026

## External status

The classical no-three-in-line conjecture

\[
D(n)=2n
\]

remains open.  This repository does **not** contain a complete proof.

The collision-free theorem ledger is split across:

- `proofs/composite-modulus-theorem-index-live.md` through CMR747;
- `proofs/composite-modulus-theorem-index-live-continuation.md` through CMR869;
- `proofs/composite-modulus-theorem-index-live-continuation-2.md` through CMR1197;
- `proofs/composite-modulus-theorem-index-live-continuation-3.md` from CMR1198
  through the current CMR1373 range.

## What is structurally closed

The selected-minimum execution now has finite canonical forms for:

- same-value rollback and lowering-expansion core contraction;
- nested normalized hosts and permanent minimum-loss witnesses;
- host-representable minimum-core contraction;
- selected routing and strict child products;
- unit Hall walls and complete wall trees;
- protected/free, exchange-SCC and exact product decompositions;
- low-rank cross-factor coupling boxes;
- fixed-core target lifting and owner-independent restoration ancestry;
- terminal fixed-target, loaded-line and small-side response banks.

These results prove finite response and strict structural descent.  They do not
by themselves prove that a positive minimum becomes zero.

## Last-entering ownership and product triangularity

Every newly created physical triple has one absolute last-entering labelled edge.
In a one-coordinate product response, all entering edges lie in the active factor.
Fixed-core and sibling-factor cells may occur in the triple, but receive no owner
charge.

Every surviving triple keeps its old owner through restriction and contraction.
A target which becomes wholly fixed is answered at its unique lifted owner.
Therefore fixed interfaces do not create upward offspring.

The complete selected structural owner system is a finite DAG.  After topological
ordering, the global credit-reproduction matrix is block upper triangular:

\[
A=
\begin{pmatrix}
A_{11}&B_{12}&\cdots\\
0&A_{22}&\cdots\\
\vdots&\vdots&\ddots
\end{pmatrix}.
\]

Hence

\[
\rho(A)=\max_i\rho(A_{ii}).
\]

Finite cross-factor and fixed-interface collateral affects only the scaling of
local Lyapunov weights.  The unresolved spectral work is entirely in the
same-owner diagonal blocks.

## Exact classes and upper quotients

At one finite owner, exact state-target pairs form a finite credit-class system.
Any proposed geometric compression

\[
\pi:\Sigma_{\mathrm{exact}}\to\overline\Sigma
\]

has exact coarse offspring rows.  Taking the componentwise maximum over every
exact row in one coarse fibre gives an honest upper quotient `A_hat`.

If

\[
\widehat A v<v,
\]

then the lifted vector satisfies the exact inequality on every state and host.
The certificate can be stored as strict integer inequalities after clearing row
and weight denominators.  Once `v` is fixed, deterministic bank rows suffice;
rowwise randomization gives no additional existence power.

## Extension-free target banks

Fix one target cell `e` outside the opposite matching `O` and put

\[
H_e=K_{n,n}\setminus(O\cup\{e\}).
\]

The union over all forbidden extensions through `e` is exactly

\[
\operatorname{PM}(H_e).
\]

Every response in this family has a canonical realizing forbidden extension.

Let `D_n` be the derangement number.  The response-bank size is exact:

\[
\boxed{
|\operatorname{PM}(H_e)|
=D_n\frac{n-2}{n-1}.
}
\]

Define

\[
\lambda_n
=
\frac{n!(n-1)}{D_n(n-2)}.
\]

For every `n>=4`,

\[
\lambda_n\le4,
\]

and `lambda_n` tends to `e`.

Every allowed response edge has marginal at most

\[
\frac1{n-2}.
\]

Compatible rank-two and rank-three prescriptions have probabilities at most

\[
\frac{\lambda_n}{(n)_2},
\qquad
\frac{\lambda_n}{(n)_3}.
\]

Thus, for corrected extension-free candidate counts `V_r^e`,

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

Restricted-host unavailable edges use the same sharp rank-one coefficient.
Complete blockage still minimalizes to an exact deficiency-one unit wall.

## Corrected line profiles

For a response graph `G`, old matching `M`, and opposite matching `O`, put

\[
M_G=M\cap E(G),
\]

and on each real line `L` define

\[
o_L=|O\cap L|,
\qquad
g_L=|E(G)\cap L|,
\qquad
m_L=|M_G\cap L|.
\]

Axis lines contribute no response-state triple.  On every nonaxis line, all cells
are matching-compatible.  Therefore the corrected candidate counts are

\[
V_1=\sum_L\binom{o_L}{2}(g_L-m_L),
\]

\[
V_2=\sum_Lo_L
\left[
\binom{g_L}{2}-\binom{m_L}{2}
\right],
\]

\[
V_3=\sum_L
\left[
\binom{g_L}{3}-\binom{m_L}{3}
\right].
\]

The old-state subtraction is essential.

The exact pair moments are

\[
\sum_L\binom{o_L}{2}=\binom n2,
\qquad
\sum_L\binom{g_L}{2}=P_2(G),
\qquad
\sum_L\binom{m_L}{2}=\binom{|M_G|}{2}.
\]

Using residual rank and dyadic bands for `(o_L,g_L,m_L)` gives at most

\[
3B_n^3,
\qquad
B_n=2+\lfloor\log_2n\rfloor,
\]

coarse profile classes.  Exact pair moments give explicit population-tail and
rankwise band envelopes.

## Exact line-composition kernel

For disjoint layers `O,M`, let a nonaxis line contain:

- `o` cells of `O`;
- `m` cells of `M`;
- `u` unselected board cells.

Summing the extension-free candidate counts over every target cell `e in M`
gives exactly

\[
\sum_eV_1^e(L)=n\binom o2u,
\]

\[
\sum_eV_2^e(L)
=o\left[(n-1)mu+n\binom u2\right],
\]

\[
\sum_eV_3^e(L)
=(n-2)\binom m2u
+(n-1)m\binom u2
+n\binom u3.
\]

The destroyed target incidence in that layer is

\[
m\binom{o+m-1}{2}.
\]

After adding both layers, the exact target contribution is

\[
3\binom{o+m}{3}.
\]

Inserting the sharp extension-free probability coefficients defines a symmetric
line kernel `K_n`.  If

\[
\sum_L\mathcal K_n(o_L,m_L,u_L)<3\Phi(S),
\]

some target-cell response strictly improves the potential.

## Why independent line bounds do not close the proof

At `n=5`, the disjoint permutations

\[
M=(0,1,2,4,3),
\qquad
O=(1,3,4,0,2)
\]

have two target lines.  Their exact total target incidence is

\[
3\Phi(S)=6,
\]

but the independent-line extension-free upper kernel is

\[
\frac{160}{11}>6.
\]

This does not show that the state lacks an improving response.  It proves that
pair moments and independent linewise maxima are too coarse to certify one.
The next theorem must use cross-line correlation, shared response-edge assignment,
primitive height, quotient/carry or prefix structure.

## Finite full-grid evidence and scope

On standard full grids and verified common-affine copies:

- side three dirty target responses are clean;
- every dirty side-four state has an ambient strict response;
- every dirty side-five state has an ambient strict response;
- at side six, almost every dirty state improves immediately or after at most two
  equal target responses; twelve physical one-layer traps remain, and a recorded
  clean two-layer state gives a lowering expansion.

These finite classifications do **not** transfer by arbitrary relabelling to
scattered residual factors.  Real collinearity always remains in original parent
coordinates.

## Corrections retained

- Sequential two-layer rematching may reoccupy an old first-layer cell.
- Historical target lines and stars are not simultaneous families.
- One edge return may serve several neutralizations in one absence run.
- Removing one essential edge gives Hall deficiency exactly one.
- Aggressive batch deletion is branch-local.
- Differently masked leaf unions are not automatically one matching host.
- Conditioning on one support edge does not fix the other two layer labels.
- Finite scheduler termination is not potential improvement.
- Old response-layer edges and subsets create no new collateral and must be
  subtracted.
- The dyadic zero band is additional: `B_n=2+floor(log_2 n)`.
- Candidate prescriptions have at most, not exactly, `(n-r)!` restricted-bank
  completions.
- Standard-grid finite classifications do not apply to scattered residual
  coordinates.
- The side-six closed one-layer graph has six two-cycles and twelve feeder states,
  not fixed points.

## Current open frontier

1. **Cross-line same-owner certificate.**  Use response-edge assignment,
   primitive-height, prefix, quotient and carry information to improve the exact
   line-composition kernel.
2. **Subcritical upper quotient.**  Construct a host-uniform coarse matrix with an
   exact rational or integer certificate `Av<v`.
3. **Prime-field and thin regimes.**  Prove the same diagonal certificate without
   a nonroot prefix-depth budget.
4. **Arbitrary side lengths.**  Complete balanced/CRT assembly while retaining
   collision and local-line credit classes.

## Bottom line

There is no complete proof.  Through **CMR1373**, product and fixed-interface
coupling are spectrally triangular, exact extension-free bank probabilities are
known, and the same-owner problem has a rigorous line-profile and line-composition
form.  The remaining obstruction is a genuine cross-line quantitative inequality,
not an uncontrolled recurrence or matching-structure endpoint.
