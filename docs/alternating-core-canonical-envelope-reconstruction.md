# Canonical reconstruction of AC3v repair envelopes

**Branch:** `research/alternating-core-chain`

AC3v permits each repair to carry any private envelope containing every cell
used by one of its local states.  This is safe but introduces discretionary
set-valued data: different supersets can describe the same transition family.
AC3lv shows that arbitrary envelope subsets may have exponential state entropy.

The scope-completion proof does not need this discretion.  The union of the
actual local states is the unique smallest valid envelope, and rebuilding the
canonical primal graph from those minimal envelopes preserves AC3v and AC3w
exactly.  This note therefore removes the private envelope subset as an
independent outer-profile field whenever the transition-state family itself is
fixed canonically.

The generator of that state family may still have nonpolynomial entropy.  The
result removes duplicated envelope data; it does not by itself make an
arbitrary menu dictionary polynomial.

## Finite local state families

Retain the AC3v notation.  Let `Omega` be a finite physical cell universe and
`Z` a fixed common state.  Repair `j` has a finite private local-state family

\[
\mathcal X_j\subseteq 2^{\Omega\setminus Z}.
\]

Define its canonical minimal envelope

\[
\boxed{
P_j^{\min}
=
\bigcup_{S\in\mathcal X_j}S.
}
\]

For a common-state family `Z_alpha`, the analogous canonical common envelope is

\[
B^{\min}
=
\bigcup_\alpha Z_\alpha.
\]

Whenever an existing valid construction used a common envelope `B` and private
envelopes `P_j`, the canonical envelopes are subsets of those originals and
therefore preserve every declared common/private disjointness relation.

## AC3mf -- unique minimal envelope -- PROVED

For every finite local-state family `X_j`, the set `P_j^min` is:

1. a valid envelope containing every state in `X_j`;
2. the unique smallest valid envelope under inclusion;
3. a deterministic function of the exact physical state family;
4. bounded by
   \[
   \boxed{
   |P_j^{\min}|
   \le
   \sum_{S\in\mathcal X_j}|S|.
   }
   \]

If the family has at most `m_j` states and every state uses at most `e_j`
private cells, then

\[
\boxed{|P_j^{\min}|\le m_je_j.}
\]

### Proof

Every state is a subset of its union, so the union is a valid envelope.  Any
other valid envelope contains every state and therefore contains their union.
This proves uniqueness and minimality.  Determinism and the size bounds follow
directly from the definition. QED.

## Canonical minimal-envelope primal graph

Build the AC3v primal graph exactly as before, replacing every discretionary
private envelope by `P_j^min`.  Thus distinct repairs are adjacent when:

1. their minimal envelopes overlap;
2. one potential-factor scope meets both minimal envelopes;
3. one hard-constraint scope meets both minimal envelopes;
4. their private paid-token sets overlap, as in AC3w.

Every local legality test is evaluated on the actual chosen state, not merely
on the envelope.

## AC3mg -- AC3v and AC3w remain exact for minimal envelopes -- PROVED

Let `I` be independent in the canonical minimal-envelope primal graph and
choose one state `S_j in X_j` for every `j in I`.  Under the same local legality
hypotheses as AC3v:

1. the chosen private states are pairwise cell-disjoint;
2. their joint state satisfies every hard constraint;
3. every scoped potential factor meets at most one selected repair;
4. the exact AC3v potential-additivity identity holds;
5. the exact AC3w common/private payment identity holds.

### Proof

By AC3mf, every chosen state is contained in its minimal envelope.  Independence
therefore implies that selected states are disjoint.  A factor or constraint
scope meeting two selected states would meet both corresponding minimal
envelopes and create an edge, contradicting independence.  The factor-by-factor
and constraint-by-constraint proof of AC3v now applies verbatim.  Paid-token
overlap is unchanged, so AC3w also applies verbatim. QED.

No factor, rich-line triple, protected clause or higher-order cross-repair
condition is lost by shrinking to the cells which some state can actually use.

## AC3mh -- discretionary envelope supersets only add conflicts -- PROVED

Suppose `P_j` is any valid envelope for `X_j`, so

\[
P_j^{\min}\subseteq P_j.
\]

Let `G_min` be the canonical primal graph built from the minimal envelopes and
`G_sup` the graph built from the arbitrary supersets, with the same factor,
constraint and paid-token registries.  Then

\[
\boxed{E(G_{\min})\subseteq E(G_{\rm sup}).}
\]

Consequently:

1. every family independent in `G_sup` is also independent in `G_min`;
2. replacing supersets by minimal envelopes never invalidates a previously
   legal product;
3. the minimal graph may remove artificial conflicts and permit additional
   products, all of which are safe by AC3mg;
4. potential and payment values of every actual state are unchanged.

### Proof

Envelope overlap persists under taking supersets.  Likewise, any factor or
constraint scope meeting two minimal envelopes also meets the corresponding
supersets.  Paid-token edges are identical.  Hence every edge of `G_min` occurs
in `G_sup`.  The remaining statements follow from graph inclusion and the fact
that local states, factors, constraints and paid sets were not changed. QED.

Thus choosing larger envelopes is conservative but unnecessary.  It must not
be treated as mathematical progress or as an independent epoch state.

## State-incidence changes

Fix a finite state-address set `Theta` and a realization map

\[
S:\Theta\to2^{\Omega\setminus Z}.
\]

Let

\[
I_S
=
\{(\theta,x):x\in S_\theta\}
\subseteq\Theta\times\Omega
\]

be its state-cell incidence relation.  Then

\[
P^{\min}(S)
=
\{x:\exists\theta\ (\theta,x)\in I_S\}.
\]

For two generators with different address sets, replace `Theta` by their union
and interpret a missing state address as the empty state.

## AC3mi -- envelope changes are projections of state-incidence changes -- PROVED

For two exact realization maps `S,S'` on the same padded address set,

\[
\boxed{
P^{\min}(S)\triangle P^{\min}(S')
\subseteq
\pi_\Omega(I_S\triangle I_{S'}).
}
\]

Therefore

\[
\boxed{
|P^{\min}(S)\triangle P^{\min}(S')|
\le
|I_S\triangle I_{S'}|.
}
\]

Every changed envelope cell has a canonical least state-address witness whose
cell incidence changed.  If `|Theta|<=M` and `|Omega|<=A`, the exact
state-address/cell/direction decoration stock is at most

\[
\boxed{2MA.}
\]

### Proof

If a cell belongs to exactly one of the two envelope unions, then it occurs in
at least one state on that side and in no state on the other.  Hence at least
one incidence pair containing that cell lies in the incidence symmetric
difference.  Projection and cardinality give the two displays.  Fixed orders
select the least changed cell and least witnessing state address. QED.

A polynomial decoration bound requires a polynomial state-address stock or a
separate polynomial generator dictionary.  The theorem does not infer such a
bound from finiteness alone.

## AC3mj -- monotone state-family evolution induces monotone envelopes -- PROVED

For two finite state families,

\[
\mathcal X\subseteq\mathcal X'
\quad\Longrightarrow\quad
\boxed{P^{\min}(\mathcal X)\subseteq P^{\min}(\mathcal X').}
\]

Thus adding alternatives can only enlarge the minimal envelope and deleting
alternatives can only shrink it.  Along a monotone state-family history, the
minimal envelope changes strictly at most `|Omega|` times.

### Proof

The union over a subfamily is contained in the union over the larger family.
The strict-change bound is the monotone subset potential AC3lx on the physical
cell universe. QED.

The state family itself may change many times without changing its envelope;
such changes belong to the transition-family generator, not to an independent
envelope counter.

## AC3mk -- envelope outer-profile reduction -- PROVED UNDER THE CANONICAL STATE-FAMILY CONTRACT

Assume every installed repair bank declares:

- one exact finite state-address family or one canonical state generator;
- the complete physical realization of each state;
- the fixed common-state family;
- the exact factor, constraint and paid-token registries.

Require its private and common envelopes to be the canonical unions of those
states.  Then the envelope subsets are derived fields and need not appear as
independent coordinates in the AC3ka outer profile.

Under this contract:

1. fixed state generators force fixed envelopes by AC3mf;
2. AC3v and AC3w remain exact by AC3mg;
3. arbitrary envelope supersets are deleted without loss by AC3mh;
4. a changed envelope is caused by a changed state-cell incidence or generator
   field by AC3mi;
5. monotone state-family changes yield a monotone envelope potential by AC3mj;
6. an envelope change with no generator or physical-realization change is
   impossible.

### Proof

The envelope is the deterministic union of the exact states.  AC3mg proves that
this canonical choice satisfies every scope-completion and payment theorem,
while AC3mh removes any need for larger discretionary supersets.  AC3mi and
AC3mj classify all possible changes of the derived union.  Therefore storing
the envelope again as an independent outer field duplicates its generator. QED.

This theorem does **not** remove or bound:

- the entropy of an arbitrary transition-state family;
- changes in physical realization, state-address ancestry or owner assignment;
- the factor, hard-constraint or protected registries used by AC3v;
- a global condition whose scope is not represented in those registries;
- the active-layer or blocker-layer base hosts.

If an implementation deliberately uses a larger discretionary envelope for
algorithmic reasons, that choice may be retained operationally, but it carries
no theorem-level identity and cannot be counted as a distinct mathematical
outer profile under AC3mk.

## Consequence

A second set-valued outer field has been reduced safely.  The private AC3v
envelope is the unique union of the exact local states, the minimal-envelope
primal graph is scope-complete, and arbitrary supersets only add artificial
conflicts.  Envelope changes are inherited from state-incidence or generator
changes rather than counted as independent set resets.

The remaining set-state frontier is now concentrated on the actual transition
family generators, active and protected/hard registries, and any base host not
already reconstructed by AC3me.

## Finite check

`scripts/verify_ac_canonical_envelope_reconstruction.py` exhausts all state
families on a three-cell universe, verifies unique minimal envelopes and every
valid superset, checks more than a quarter-million state-incidence comparisons,
all monotone family inclusions, canonical-versus-superset graph monotonicity and
scope-completion on all three-repair envelope systems.
