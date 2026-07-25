# Finite outer-reset quotient and repeated macro-edge localization

**Branch:** `research/alternating-core-chain`

AC3jr--AC3ju make the alternating transition oracle total inside one exact
outer profile.  The remaining nonterminal output is an outer reset changing
one of the fields listed by AC3jt.  This note assembles those resets into one
finite directed quotient.

The result is intentionally exact about its limitation.  First traversal of a
directed outer edge is finite progress.  Repetition of the same decorated edge
is not declared progress unless an additional theorem supplies a capacity-one
ticket, payment, strict arithmetic descent, or a terminal output.  Thus the
remaining AC4 obligation is localized to repeated decorated macro edges rather
than generic profile churn.

## Outer profiles

Fix finite alphabets for the fields retained by AC3jt:

- arithmetic/context and same-denominator non-scalar data;
- owner-token kind and the AC3jz status chart;
- active base-host construction;
- protected-bank contract;
- envelope epoch;
- any finite reset-witness kind needed by the transition rule.

Let `mathcal P_out` be the set of exact outer profiles and put

\[
P=|\mathcal P_{\rm out}|.
\]

An outer reset changes at least one field, so it is a directed edge

\[
e=(\alpha,\beta),\qquad \alpha\ne\beta.
\]

Give every reset one canonical decoration `delta` from an alphabet of size at
most `R`.  The decoration may record the least changed field, owner-status
route, arithmetic transition kind, host-construction witness, protected
contract witness, or envelope-reset kind.  It does not contain the full
matching state; matching and blocker-host churn are already bounded inside an
epoch by AC3js.

Let

\[
\mathcal E_{\rm out}
\subseteq
\{(\alpha,\beta,\delta):
  \alpha,\beta\in\mathcal P_{\rm out},\ \alpha\ne\beta,\
  \delta\in[R]\}
\]

be the set of realizable decorated reset edges.

## AC3ka -- finite decorated outer-edge stock -- PROVED

The ambient decorated edge stock satisfies

\[
\boxed{
|\mathcal E_{\rm out}|
\le
R P(P-1).
}
\]

If the outer fields have alphabet sizes `p_1,...,p_s`, then the safe profile
bound is

\[
\boxed{P\le\prod_{i=1}^s p_i.}
\]

These bounds are finite.  They are polynomial in the board parameter only when
every field alphabet and the decoration alphabet have proved polynomial
bounds.  This note does not infer such bounds merely from finiteness.

### Proof

There are `P` choices for the source profile, at most `P-1` different target
profiles, and at most `R` decorations.  Multiplication gives the first bound.
The second is the Cartesian-product bound for the field dictionary. QED.

## Epoch ceiling

Let `M` be a common upper bound for the number of nontrivial internal
transitions inside any one outer epoch before the AC3ju oracle returns an
improving state, paid menu, accepted arithmetic chamber, terminal
literal/resource profile, or outer reset.  AC3js supplies such an `M` after
fixing its parameters `n,L,lambda,B`.

For a history which has not yet terminated, let:

- `E_seen` be the set of distinct decorated outer edges already traversed;
- `c` be the number of internal transitions in the current epoch since the most
  recent outer reset.

Thus

\[
0\le c\le M.
\]

Define

\[
\boxed{
\Xi_{\rm out}
=(M+1)|E_{\rm seen}|+c.
}
\]

## AC3kb -- first-edge and internal-step potential -- PROVED

The potential `Xi_out` strictly increases on each of the following events.

1. **Internal epoch step:** the outer profile and `E_seen` are fixed and
   `c` increases by one.
2. **First traversal of a decorated outer edge:** the new edge is inserted into
   `E_seen` and the new epoch counter is reset to zero.

It has ceiling

\[
\boxed{
\Xi_{\rm out}
\le
(M+1)R P(P-1)+M.
}
\]

Consequently a nonterminal history containing no repeated decorated outer edge
has at most

\[
\boxed{
(M+1)R P(P-1)+M
}
\]

progress events after its initial record.

### Proof

An internal step increases `c` by one.  Before a first edge traversal the old
counter is at most `M`; after traversal the potential changes from

\[
(M+1)q+c
\]

to

\[
(M+1)(q+1),
\]

which is larger because `c\le M`.  AC3ka bounds the number of seen edges and
`c\le M`, giving the ceiling. QED.

## AC3kc -- repeated macro-edge localization -- PROVED

Every nonterminal history longer than the AC3kb ceiling contains two reset
episodes with the same exact decorated edge

\[
(\alpha,\beta,\delta).
\]

Thus all of the following agree between the two episodes:

- the complete source outer profile;
- the complete target outer profile;
- the least changed outer field;
- the canonical reset-witness decoration;
- the AC3jz owner-status route when owner interpretation changes.

The underlying matching states, exact owner tokens, and exact arithmetic
witnesses need not agree unless they are included in the decoration.  Repeated
macro-edge localization therefore does not by itself erase the intervening
history.

For weighted reset episodes of total weight `W`, one decorated edge class
carries weight at least

\[
\boxed{
\frac{W}{R P(P-1)}
}
\]

when `P>=2`.  If `P=1`, no outer reset exists.

### Proof

If no edge repeated, every reset would be a first traversal, so AC3kb would
bound the history.  The agreement statement is the definition of equality of
decorated edges.  Weighted pigeonhole over the AC3ka stock gives the final
bound. QED.

## Capacity-one macro tickets

A repeated decorated edge is **certifiably progressive** when each nonterminal
traversal consumes one previously unused ticket from a finite ticket universe
`mathcal T_out`, and no ticket can be restored inside the global closure
attempt.  A ticket address may refine the decorated edge by an exact arithmetic
support, owner token, protected contract, envelope witness, or another proved
capacity-one resource.

Let

\[
Q=|\mathcal T_{\rm out}|.
\]

Track also `T_used`, the set of consumed macro tickets, and define

\[
\boxed{
\Xi_{\rm glob}
=(M+1)(|E_{\rm seen}|+|T_{\rm used}|)+c.
}
\]

## AC3kd -- conditional global outer closure -- PROVED UNDER MACRO-TICKET CONTRACT

Assume every nonterminal outer reset is one of:

1. the first traversal of its decorated edge;
2. a traversal consuming a previously unused capacity-one macro ticket;
3. a transition with a separately proved strict bounded potential increase;
4. an improving state, accepted arithmetic chamber, paid executable menu, or
   terminal literal/resource output.

After absorbing every potential in alternative 3 into the finite ticket or
bounded-potential dictionary, every nonterminal event strictly increases
`Xi_glob`, whose safe ceiling is

\[
\boxed{
(M+1)(R P(P-1)+Q)+M.
}
\]

Hence the global outer transition system terminates after at most that many
internal/new-edge/ticket events before a terminal output.

Conversely, without a macro ticket, payment theorem, or another strict bounded
potential for a repeated decorated edge, AC3kd does not apply.  That repeated
edge is the exact residual AC4 recurrence witness.

### Proof

Internal steps and first edges are AC3kb.  A new ticket increases
`|T_used|` by one; even when `c` resets from `M` to zero, multiplication by
`M+1` makes the new value strictly larger.  The finite edge and ticket stocks
and `c\le M` give the ceiling.  Alternative 3 is included only after its own
strict bounded counter is appended lexicographically or encoded into the
finite global counter.  A bounded strictly increasing integer cannot support
an infinite nonterminal history. QED.

## Consequence

The remaining AC4 termination problem has two exact components.

1. Give polynomial bounds for the outer profile, decoration and macro-ticket
   alphabets needed in the prime-minus-one application.
2. For every repeated decorated edge from AC3kc, prove a terminal output,
   current payment, strict arithmetic descent, or a capacity-one macro ticket.

Generic arithmetic/context churn, owner reinterpretation, host-construction
change, protected-contract change and envelope change are no longer acceptable
unlabelled outputs.  They must appear as one finite decorated edge, and only
its exact repetition remains a possible global recurrence.

## Finite check

`scripts/verify_ac_outer_reset_quotient.py` exhausts representative profile,
decoration, epoch and ticket budgets; checks every internal, first-edge and
new-ticket potential transition; enumerates short decorated-edge histories;
and verifies the weighted concentration and all displayed ceilings.
