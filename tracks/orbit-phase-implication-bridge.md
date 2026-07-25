# Implication bicycles and the rational quotient gate

OP4b returns an explicit contradictory implication chain when a
protected correction bank has an unsatisfiable rank-at-most-two
projection.  OP4c retains every rank-three clause as a geometric
three-support transversal.

Neither output should be called an order-two rational exception without
an additional proof.  A Boolean switch has two orientations, but this
does not imply that its source-factor geometry lies in the
order-two colour-ratio subgroup classified by the rational inverse
track.

This note supplies the exact bridge and the exact failure output.

1. Every rank-two obstruction compresses to a bounded implication
   bicycle with source-factor provenance on every edge.
2. A rational quotient certificate is audited edge by edge.  If it is
   absent or false, the first offending geometric factor is returned.
3. A certified bicycle obeys the dihedral quotient laws.  Its
   order-two case lies in the alternating-square or loop-and-edge
   template, while a larger colour-ratio subgroup is exposed
   explicitly.
4. Every rank-three protected-bank instance either contains a
   disjoint matching of geometric transversals or has a bounded switch
   kernel whose conditioned residuals are all rank-at-most-two
   instances.

Thus the order-two and rank-three frontiers now meet at one lossless
interface.  The companion
[`orbit-phase-geometric-labels.md`](orbit-phase-geometric-labels.md)
proves OP4g--OP4h: it derives the factor-level rational/carry record
and decides whether the local root pairs admit consistent literal
labels on the whole bicycle.

## OP4d -- source-labelled implication bicycles

Let \(\Psi\) be the OP4a projection on binary correction switches
\(x_1,\ldots,x_m\).  A literal is an orientation assertion

\[
\ell=(x_i=\varepsilon),
\qquad
\bar\ell=(x_i=1-\varepsilon).
\]

A unary clause \((a)\) contributes the implication

\[
\bar a\longrightarrow a.
\]

A binary clause \((a\vee b)\) contributes

\[
\bar a\longrightarrow b,
\qquad
\bar b\longrightarrow a.
\]

Every clause retains its OP4a source factor, its forbidden
orientations, and the variables of each protected support met by that
factor.

### Theorem OP4d -- PROVED

If \(\Psi\) is unsatisfiable, exactly one of the following certificates
can be returned.

1. An empty clause identifies a bad source factor fixed outside the
   protected bank.
2. There are a literal \(\ell\) and two directed simple paths
   \[
   P:\ell\leadsto\bar\ell,
   \qquad
   Q:\bar\ell\leadsto\ell
   \]
   in the implication graph.

In conclusion 2, concatenating \(P\) and \(Q\) gives a closed
**implication bicycle**.  It contains at most

\[
\boxed{4m-2}
\]

implication occurrences.  Every occurrence retains:

1. its source and target orientation literals;
2. its source clause;
3. the original geometric factor behind that clause;
4. the protected-support variables met by the factor.

If a bicycle uses a unary clause, that clause is returned as an
explicit unary-saturation boundary.  Otherwise every edge comes from
one binary forbidden orientation pair.

### Proof

The standard 2-SAT criterion says that unsatisfiability without an
empty clause is equivalent to some \(\ell,\bar\ell\) lying in one
strongly connected component.  Choose shortest directed paths in both
directions.  A shortest path is simple.  The implication graph has
\(2m\) literal vertices, so each path has at most \(2m-1\) edges and
their concatenation has at most \(4m-2\).

The OP4a projection creates each implication from one projected clause
without merging its source-factor record.  Copying that record to the
implication occurrence proves the provenance assertions. \(\square\)

The bicycle is a finite obstruction core.  Factors outside its source
clause set play no role in the contradiction.

## Rational-admissible implication edges

Let

\[
Q=\mathbb F_p^\times/H
\]

be a cyclic multiplicative quotient.  Retain the rational inverse
notation:

- \(R=rH\) is the root coset;
- \(A_\ell\in Q\) is the source quotient label assigned to literal
  \(\ell\);
- \(C_e\in Q\) is the target colour assigned to implication occurrence
  \(e:\ell\to\ell'\).

Call the occurrence **rational-admissible** when its retained geometric
factor proves

\[
\boxed{
A_{\ell'}=R C_e A_\ell^{-1}.
}
\]

This is a certificate, not a default interpretation of a Boolean
edge.  The OP1 ancestor triple, normalized ratio, pole/root parameter,
and quotient-coset labels must justify the displayed identity.

An implication bicycle is rational-admissible when:

1. every literal occurrence has one consistent quotient label;
2. every edge has a colour and root parameter;
3. the displayed identity holds on every occurrence.

The audit is lossless.  If a label is absent or the identity fails, it
returns the first edge and its source geometric factor.

## OP4e -- dihedral classification of a certified bicycle

Let

\[
A_0,A_1,\ldots,A_s=A_0
\]

be a rational-admissible implication bicycle, and let its edge colours
be

\[
C_0,\ldots,C_{s-1}.
\]

Put

\[
L
=
\left\langle
C_iC_j^{-1}:0\leq i,j<s
\right\rangle
\leq Q.
\]

### Theorem OP4e -- PROVED

The certified bicycle has the following exact structure.

1. **Dihedral walk law.**  For every admissible \(j\),
   \[
   A_{2j}
   =
   A_0
   \prod_{t=0}^{j-1}C_{2t+1}C_{2t}^{-1},
   \]
   \[
   A_{2j+1}
   =
   R A_0^{-1}
   \left(\prod_{t=0}^{j}C_{2t}\right)
   \left(\prod_{t=0}^{j-1}C_{2t+1}^{-1}\right).
   \]
2. **Coset confinement.**  For any used base colour \(C_\ast\),
   all even and odd literal labels lie respectively in
   \[
   \boxed{
   A_0L
   \quad\text{and}\quad
   R A_0^{-1}C_\ast L,
   }
   \]
   while all edge colours lie in \(C_\ast L\).
3. **One-colour case.**  If \(|L|=1\), the quotient walk uses at most
   two source vertices: one colour acts by a single involution.
4. **Order-two case.**  If
   \[
   L=\{1,\omega\},
   \qquad\omega^2=1,
   \qquad\omega\ne1,
   \]
   choose \(C_\ast\), put \(A=A_0\), and
   \[
   B=RC_\ast A^{-1}.
   \]
   The entire bicycle lies in exactly one of the following templates.

   - If \(AL\ne BL\), it is contained in the alternating square on
     \[
     \{A,A\omega,B,B\omega\},
     \]
     with at most four quotient edge classes.
   - If \(AL=BL\), it is contained in the two-vertex
     loop-and-edge collapse, with at most three quotient edge classes.

5. **Larger-ratio case.**  If \(|L|\geq3\), the bicycle returns the
   explicit non-order-two colour-ratio subgroup \(L\); it is not an
   RI4 order-two exception.

If the implication occurrences carry arbitrary certified
nonnegative weights of total \(W\), the order-two square has one edge
class of weight at least \(W/4\), and the collapsed template has one
edge class of weight at least \(W/3\).  In either template one colour
has weight at least \(W/2\).

### Proof

The rational-admissibility identity is the quotient involution

\[
\iota_C(A)=RCA^{-1}.
\]

Two consecutive colours satisfy

\[
\iota_D\iota_C(A)=DC^{-1}A.
\]

Induction on the even and odd positions gives the two walk formulae.
Every two-step multiplier lies in \(L\), giving the two source-coset
containments; the definition of \(L\) gives the colour containment.

When \(L\) is trivial, every edge uses one involution, whose components
have at most two vertices.

Now suppose \(L=\{1,\omega\}\).  The two possible colours are
\(C_\ast,C_\ast\omega\), and

\[
\iota_{C_\ast}(A\ell)=B\ell,
\qquad
\iota_{C_\ast\omega}(A\ell)=B\omega\ell
\quad(\ell\in L).
\]

If \(AL\) and \(BL\) differ, these are precisely the four alternating
square edges.  If they agree, write \(B=A\varepsilon\) for
\(\varepsilon\in\{1,\omega\}\).  One colour then acts as the identity
on the two vertices and supplies the loops, while the other acts by
\(\omega\) and supplies the connecting edge.

The edge classes partition the certified occurrence weight.  There
are at most four in the square and at most three in the collapse, so
the heaviest class has the stated weight.  There are at most two
colours. \(\square\)

OP4e imports the exact RI2k/RI4a quotient mechanism, but only after the
edge audit succeeds.  It does not assert that every OP4d source factor
already carries a rational inverse label.

## OP4f -- rank-three matching or bounded switch kernel

Return to the exact OP4a formula \(\Psi\), now allowing clauses of
width three.  Form the three-uniform hypergraph

\[
\mathcal H_3
\]

whose vertices are protected correction switches and whose edges are
the switch scopes of the width-three clauses.  Every hyperedge retains
its source geometric factor and the three protected supports from
OP4c.

Choose any maximal matching

\[
M\subseteq E(\mathcal H_3)
\]

and put

\[
K=\bigcup_{e\in M}e.
\]

### Theorem OP4f -- PROVED

Let \(\nu=|M|\).  Then:

1. \(M\) is a family of \(\nu\) pairwise switch-disjoint geometric
   rank-three transversals.
2. The kernel \(K\) satisfies
   \[
   \boxed{|K|=3\nu}
   \]
   and meets every width-three clause.
3. For every orientation assignment
   \(\eta\in\{0,1\}^K\), exact restriction of \(\Psi\) by \(\eta\)
   leaves a formula of width at most two.
4. Enumerating the \(2^{3\nu}\) kernel assignments and running OP4b
   on every residual is an exact decision procedure:

   - if one residual is satisfiable, its assignment together with
     \(\eta\) is a satisfying protected-bank orientation;
   - if none is satisfiable, every branch returns either an empty
     source clause or one OP4d implication bicycle.

Consequently, for every threshold \(u\geq1\), the rank-three frontier
has the exact alternative:

1. at least \(u\) switch-disjoint geometric transversals; or
2. a kernel of size at most \(3(u-1)\) whose complete residual
   obstruction is a finite family of 2-SAT bicycles.

### Proof

The matching clauses are pairwise switch-disjoint by definition.
Every edge has three vertices, giving \(|K|=3\nu\).

Maximality says that no width-three edge is disjoint from \(K\);
otherwise that edge could be added to \(M\).  Thus every width-three
clause contains a kernel switch.  After fixing all switches in \(K\),
such a clause is either already satisfied and deleted, or loses at
least one false fixed literal and has residual width at most two.
Clauses originally of width at most two remain of width at most two.

Restriction preserves the exact satisfying assignments extending
\(\eta\).  Exhausting every \(\eta\) and applying OP4b therefore proves
the decision statement.  If \(\nu<u\), the kernel bound is
\(|K|=3\nu\leq3(u-1)\). \(\square\)

The matching side is a genuinely geometric dispersion output: its
source factors use disjoint triples of protected correction switches.
The kernel side is a finite interface to OP4d--OP4e and does not require
a rank-three local-lemma estimate.

## Interface after OP4d--OP4f

The protected-bank obstruction now follows a lossless decision tree.

1. OP4f returns a large switch-disjoint family of rank-three
   transversals, or a bounded switch kernel.
2. Conditioning the bounded kernel returns a satisfying orientation,
   an empty fixed factor, or source-labelled OP4d bicycles.
3. Every bicycle is audited for the rational quotient identity.
4. A certified bicycle returns:

   - a one-colour edge/loop component;
   - an order-two alternating square;
   - an order-two loop-and-edge collapse; or
   - an explicit colour-ratio subgroup of order at least three.

5. OP4g--OP4h replace a generic uncertified edge by one of:

   - a three-channel product-carry record;
   - a differing root coset;
   - a complete literal-root compatibility conflict; or
   - a rational-admissible bicycle with all labels supplied.

The remaining frontiers are now precise.

1. **Syndrome payment and defect routing.**
   [`orbit-phase-paid-edge-density.md`](orbit-phase-paid-edge-density.md)
   proves that bank weights do not transfer by logic alone.  With
   factor-conservative edge weights, its OP4i gate already returns
   complete rational-orbit density, one-sided completion deficits, a
   heavy repeated factor, or product-carry growth.
   [`orbit-phase-syndrome-payment.md`](orbit-phase-syndrome-payment.md)
   proves OP4l: at least one third of rank-three correction gain enters
   current source factors, a capacitated Hall failure returns paid
   repeated defects, and any selected bicycle either receives half of
   that payment or leaves the other half on explicit off-core current
   defects.
   [`orbit-phase-defect-router.md`](orbit-phase-defect-router.md)
   proves OP4m: every paid off-core or Hall-reuse family returns a
   heavy current factor, a paid point-star carry family, or quantified
   exact signatures on point-disjoint current defects.  The remaining
   task is recurrence or treatment of one heavy factor.
2. **Order-two RI5 conversion.**  Build and compare the
   row-column-preserving state family for the fixed quotient edge
   selected by the square/collapse template.
3. **Rank-three recurrence.**
   [`orbit-phase-rank-three-router.md`](orbit-phase-rank-three-router.md)
   proves OP4j: every large switch-disjoint matching forces quantified
   product-carry signature growth.
   [`orbit-phase-blocker-ledger.md`](orbit-phase-blocker-ledger.md)
   proves OP4k: exact profile/signature records enter a role-tagged
   state ledger, while a no-growth return is one current recurrent
   fibre of at most \(\Delta_p\) point-disjoint source factors.  The
   remaining arithmetic task is to process that bounded fibre, not to
   invent another ledger.
4. **Other OP3j outputs.**  Resolve the high-overlap action-literal
   kernels and wide action CSPs.

No generic implication edge is identified with a rational orbit, and
no order-two template is declared absorbable before RI5 is proved.

`scripts/verify_phase_implication_bridge.py` exhausts small
unsatisfiable 2-CNF formulas and checks the simple-path bicycle bound
and source provenance.  It checks certified one-colour, order-two
square, order-two collapse, larger-ratio, missing-label, and
invalid-label cases.  It also compares the rank-three matching/kernel
decision procedure with brute force on thousands of formulas and
retains both empty-clause and implication-bicycle branch
certificates.

`scripts/verify_phase_geometric_labels.py` exhausts small prime grids
for the OP4g channel-profile theorem and quotient identities.  It also
compares the OP4h fixed-normalization propagation with brute force and
checks every success and failure output of the complete gate.

`scripts/verify_phase_paid_edge_density.py` checks the OP4i payment
boundary and exhausts the fixed-template divisor-capacity interface on
all really collinear oriented factors for \(p=11\).

`scripts/verify_phase_rank_three_router.py` checks OP4j's finite channel
profiles and endpoint-disjoint carry capacity on every real
non-single-channel factor for \(p=11\).

`scripts/verify_phase_blocker_ledger.py` checks OP4k's exact token
growth, recurrence bounds, weighted capacity gate, and separation by
snapshot and geometric role.

`scripts/verify_phase_syndrome_payment.py` checks OP4l's proportional
payment, capacitated Hall alternative, repeated-defect bound, and
bicycle/off-core split.

`scripts/verify_phase_defect_router.py` checks OP4m's weighted
point-star/matching extraction and its two carry-capacity routes.
