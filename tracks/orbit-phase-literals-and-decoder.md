# Canonical phase literals and exact decoder accounting

This note proves the representation-theoretic part of OP1 and the finite
descent part of OP3. The missing work is arithmetic expansion: OP2 must
still show that one of the profitable flips or structured delegations
exists.

## OP1a -- every geometric triple is a rank-three phase constraint

Let \(\mathcal B\) be a family of disjoint O1 orbit blocks. For a block
\(B\) of order \(h_B\), use the alphabet

\[
\mathcal A_B=\mathbb Z/h_B\mathbb Z.
\]

Label \(t\) selects the O1 state \(A_{B,t}\). Since the \(h_B\) states
partition the block's candidate cells, every cell \(e\in B\) has a unique
phase

\[
\operatorname{ph}_B(e)=t
\quad\Longleftrightarrow\quad
e\in A_{B,t}.
\]

### Theorem OP1a -- PROVED

Every real collinear candidate triple \(T\) determines either:

1. no realizable block assignment; or
2. one canonical forbidden partial assignment \(Q_T\) on at most three
   block variables.

Every label preserves the same active row and column sets, and a block of
order \(h\) has exactly \(h=\Omega(h)\) labels.

### Proof

For every block \(B\) met by \(T\), inspect the cells in \(T\cap B\). If
two such cells have different phases, no single state of \(B\) contains
both, so \(T\) is unrealizable. Otherwise assign \(B\) their common phase.
The resulting map is unique because the O1 states partition the cells.
A triple meets at most three blocks, hence the map has rank at most three.
O1 proves the row-column and label-count assertions. \(\square\)

This construction is lossless: it neither invents modular triples nor
forgets real-lift information.

## Carry decoration

The canonical literal \((B,t)\) may be decorated, for each involved cell
\(e=(x,y)\), by the constant-size record

\[
\sigma(e)=
\left(
t,\,
\frac{xy-c_t}{p},\,
\left\lfloor\frac{\alpha x}{p}\right\rfloor,\,
\left\lfloor\frac{\alpha y}{p}\right\rfloor,\,
\operatorname{coset}(B)
\right),
\]

where \(c_t\) is the modular-hyperbola channel of state \(t\), and
\(\alpha\) is the scalar relevant to the checked transition. The product
entry is an integer because \(xy\equiv c_t\pmod p\). Thus every forbidden
triple reads at most three phases and three constant-length carry records.

What remains open in OP1 is a **uniform compression theorem**: OP2 needs to
show that the numerical carry values can be grouped into a bounded family
of signature layers with useful expansion. OP1a alone does not claim that
the range of those integers is bounded independently of \(p\).

[`orbit-phase-carry-fan-router.md`](orbit-phase-carry-fan-router.md)
proves OP1b--OP1e for the geometric factor-fan output of the decoder.
The raw product carry lies in \(\{0,\ldots,p-2\}\), coordinate wraps
have their exact scalar ranges, and a repeated phase factor family
contains one actual point-star.  Channel-pair matching and divisor
bounds then force quantified product- or cross-carry signature growth.
This avoids a generic compression assumption for factor fans, but does
not yet make signature novelty monotone across decoder rounds.

## OP3a -- exact one-flip drift

Let a finite labelled CSP have nonnegative check weights. For an assignment
\(\omega\), write \(\Phi(\omega)\) for the total weight of violated checks.
For a variable \(v\) and an alternative label \(a\), let

- \(D(v,a)\) be the weight of currently violated checks which become
  satisfied after the flip \(v\leftarrow a\);
- \(C(v,a)\) be the weight of currently satisfied checks which become
  violated after that flip.

### Lemma OP3a -- PROVED

\[
\boxed{
\Phi(\omega^{v\leftarrow a})-\Phi(\omega)
=C(v,a)-D(v,a).
}
\]

In particular, \(D(v,a)>C(v,a)\) gives a strict phase-flip improvement.

### Proof

A check not containing \(v\) is unchanged. Among checks containing \(v\),
the only changes are the two disjoint classes counted by \(D\) and \(C\).
Summing their signed weights proves the identity. \(\square\)

For a batch of variables such that no check meets two flipped variables,
the same proof gives

\[
\Phi(\omega')-\Phi(\omega)
=\sum_v\bigl(C(v,a_v)-D(v,a_v)\bigr).
\]

This is the exact hypothesis needed to turn OP2 unique-neighbour checks
into a batch decoder. Without check-disjointness, the cross terms must be
paid explicitly rather than discarded.

## OP3b -- decoder termination with structured growth

Suppose \(\Phi\in\{0,\ldots,P\}\), a structured-core potential satisfies
\(\Xi\in\{0,\ldots,B\}\), and every nonterminal decoder round either:

1. decreases \(\Phi\) by at least one; or
2. leaves \(\Phi\) fixed and increases \(\Xi\) by at least one.

### Lemma OP3b -- PROVED

The decoder terminates after at most

\[
(B+1)\Phi_0+B-\Xi_0
\]

nonterminal rounds.

### Proof

The integer rank

\[
\mathcal R=(B+1)\Phi+(B-\Xi)
\]

is nonnegative. A round of type 2 lowers it by at least one. In a round of
type 1, even if \(\Xi\) resets from \(B\) to \(0\), the drop in
\((B+1)\Phi\) is larger than the largest possible increase in \(B-\Xi\),
so \(\mathcal R\) again drops by at least one. \(\square\)

OP2 and the absorber interfaces must now provide a total oracle returning
a profitable OP3a flip, a strict OP3b structured increment, or a terminal
delegation. Generic bounded degree/codegree does not provide that oracle.

[`orbit-phase-literal-star-router.md`](orbit-phase-literal-star-router.md)
proves OP3c, the exact target-phase refinement of OP3a.  Every
alternative phase destroys the same current incident defect weight,
while possible creations partition into their unique target buckets.
Averaging therefore gives an improving phase whenever
\((h_v-1)D(v)>E(v)\); if no phase improves, every target bucket has
weight at least \(D(v)\).  OP2l--OP2m then route each activated bucket
to a bounded auxiliary transversal, a paid deeper current-literal
kernel, or a residual-disjoint blocker family.

[`orbit-phase-external-collateral.md`](orbit-phase-external-collateral.md)
proves OP2n and OP3d--OP3f.  Residual-disjoint arms project exactly to a
rank-at-most-three action CSP on noncurrent phases, with every external
hard check and weighted soft factor retained.  Arbitrary improving
corrections are audited on their complete supports and may be batched
through a scope-complete primal graph; weighted extraction either
returns an executable additive-gain batch or a paid high-conflict
family with an explicit variable/check witness for every edge.

[`orbit-phase-paid-witness-localization.md`](orbit-phase-paid-witness-localization.md)
proves OP3g--OP3i.  Every bounded-support high-degree centre yields a
variable-overlap star, single-factor star, or variable-rooted factor
fan, and bounded alphabets refine these to repeated action or forbidden
literals.  The weighted organizer keeps either more than \(G/4\) on
wide corrections or more than \(G/12\) on one localized certificate
type.
