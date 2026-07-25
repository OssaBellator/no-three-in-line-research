# Adaptive near-uniform source-valid derangements

The fixed-power thinning PP3jn gives source-valid endpoint permutations with
one-cell probability \(O(1/q)\). For the line-energy endpoint, a near-uniform
constant is more useful. This chapter chooses the secondary bank size adaptively,
removes every unary and transition event by deleting only \(o(q)\) indices, and
obtains a source-valid derangement with one-cell probabilities

\[
rac{1+o(1)}q.
\]

## 1. Adaptive bank size

Let the original resource bank have size

\[
Q=\Omega(m^{21/40})
\]

and let its unary forbidden graph have density

\[
	heta_m=rac{|E(F_Q)|}{Q^2}=o(1).
\]

Fix any constant

\[
0<\kappa<rac1{40}.
\]

Choose an integer \(q=q(m)\) satisfying

\[
q	o\infty,\qquad
q\le m^\kappa,\qquad
	heta_m q=o(1).
\]

For example, when \(	heta_m>0\), one may take

\[
q=\left\lfloor
\min\{m^\kappa,	heta_m^{-1/2}\}
ightfloor
\]

after an immaterial lower truncation tending to infinity; when \(	heta_m=0\),
take \(q=\lfloor m^\kappafloor\).

### Proposition PP3nq -- PROVED

A uniform \(q\)-subset of the \(Q\) endpoint indices has expected unary-edge
count

\[
oxed{o(q).}
\]

It also has expected anchored-transition count

\[
oxed{o(q).}
\]

#### Proof

The unary expectation is

\[
rac{(q)_2}{(Q)_2}|E(F_Q)|
=O(	heta_m q^2)
=o(q).
\]

By PP3je, the complete transition population is

\[
O(QmD_m+Q^2).
\]

The random-subset expectation is therefore

\[
O\left(rac{q^3mD_m}{Q^2}+rac{q^3}{Q}ight).
\]

After division by \(q\), the first term is

\[
O\left(m^{-1/20+2\kappa+o(1)}ight)=o(1),
\]

and the second is \(o(1)\). ∎

## 2. Complete deletion of unary and transition classes

### Theorem PP3nr -- PROVED

There is a \(q\)-endpoint subbank for which:

1. the unary forbidden graph has \(o(q)\) edges;
2. the anchored transition family has \(o(q)\) events;
3. the normalized high-support source-validity expression of PP3jl is \(o(1)\).

After deleting every endpoint index incident with one of the unary edges or
transition events, the remaining bank has size

\[
q'=(1-o(1))q
\]

and has no unary-invalid arc and no anchored transition event.

#### Proof

Add the unary count divided by \(q\), the transition count divided by \(q\), and
the PP3jl normalized high-support expression to one nonnegative random objective.
PP3nq and PP3jl show that its expectation is \(o(1)\). Choose a subset no worse
than the expectation.

The union of all endpoints used by the unary edges and transition events has size
at most twice the first count plus three times the second, hence \(o(q)\). Delete
that union. All remaining source-pattern counts can only decrease. ∎

This is stronger than maximum-degree regularization: both troublesome classes
vanish identically on the retained bank.

## 3. Exact remaining low-event mass

Include every fixed point as a unary bad event, so the selected permutation is a
derangement.

### Proposition PP3ns -- PROVED

On the bank of PP3nr, the PP3ix local bad-event mass satisfies

\[
oxed{\lambda\lerac3{q'}.}
\]

#### Proof

Only three low-support classes remain.

1. One fixed-point event uses a given left or right resource and contributes
   \(1/q'\).
2. At most \(q'-1\) transposition events use a fixed resource. Each has
   probability \(1/(q')_2\), for total at most \(1/q'\).
3. At most
   \[
   2inom{q'-1}{2}=(q'-1)(q'-2)
   \]
   directed 3-cycle events use a fixed resource. Each has probability
   \(1/(q')_3\), again totaling at most \(1/q'\).

Add the three contributions. ∎

Therefore PP3nk gives, for every off-diagonal arc,

\[
\Pr(\pi(i)=j\mid	ext{avoid low events})
\le
rac{e^{24/q'}}{q'}.
\]

## 4. Conditioning on the high-support source events

Let \(\mathcal G\) be the event that no support-rank-four anchored pair and no
support-rank-at-least-four inserted triple occurs.

### Theorem PP3nt -- PROVED

The low-event-conditioned law satisfies

\[
\Pr(\mathcal G)=1-o(1).
\]

After conditioning also on \(\mathcal G\), the resulting source-valid derangement
satisfies

\[
oxed{
\Pr(\pi(i)=j\mid	ext{complete source validity})
\le
rac{1+o(1)}{q'}
}
\]

for every off-diagonal assignment.

#### Proof

The PP3jl normalized high-support expression is \(o(1)\) on the retained bank.
Under the low-event-conditioned rank-two and rank-three spread of PP3nk, its
expected high-support invalid-event count remains \(o(1)\). Markov's inequality
gives \(\Pr(\mathcal G)=1-o(1)\).

For an off-diagonal arc \(E\),

\[
\Pr(E\mid\mathcal G,	ext{avoid low})
\le
rac{\Pr(E\mid	ext{avoid low})}
{\Pr(\mathcal G\mid	ext{avoid low})}
\le
rac{e^{24/q'}}{q'(1-o(1))}
=
rac{1+o(1)}{q'}.
\]

∎

Thus source validity no longer costs an unspecified constant in one-cell spread.

## 5. Consequence for owner-line energy

### Corollary PP3nu -- PROVED

Use a Hall-derived target set \(\mathcal A\) satisfying PP3nm, and let

\[
H_0=\sum_i h_{ii},\qquad
\mathcal W=\sum_{i,j}h_{ij}.
\]

On the adaptive source-valid bank, at least one of the following holds.

1. A source-valid derangement strictly decreases the owner-line load.
2. The incidence system is asymptotically extremal:
   \[
   oxed{H_0=(1+o(1))|\mathcal A|}
   \]
   and
   \[
   oxed{\mathcal W=(1-o(1))q'|\mathcal A|.}
   \]

#### Proof

The complete source-valid law has off-diagonal one-cell probabilities at most
\((1+arepsilon_{q'})/q'\), where \(arepsilon_{q'}=o(1)\), and fixed-point
probability zero. Repeat PP3nl--PP3nn with this effective distortion. If the
improvement inequality fails, PP3nn gives the two displayed asymptotics. ∎

The remaining rich-line obstruction is therefore a near-complete incidence
design even after full source validity is imposed: almost every target cell has a
unique current owner line and is reachable from almost every possible owner.