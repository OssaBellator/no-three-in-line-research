# Additive boundary-ledger import for exact root-return gates

**Branch:** `research/alternating-core-chain`

AC3tn--AC3tr quotient chronological exact root-return gates by every finite auxiliary boundary field.
The remaining boundary-state obstruction may be an unbounded numerical balance which is not finite but
is updated additively by each completed gate.  This note imports the finite-control one-counter
machinery at the gate level.  Sign-coherent gate cycles give a common rank, while mixed signs reduce to
one invariant residue, one primitive lift and finite chronological relation gates.  Every control-word
length bound is obtained by multiplying the gate count by the existing root-return word bound.

## Additive root-boundary model

Fix one strongly connected component of the auxiliary gate graph.  Let:

- `Y` be its auxiliary state set, with `q=|Y|>=1`;
- `E` be its finite legal gate-edge set;
- edge `e:y->y'` be one completed exact root-return gate;
- `b_e` be its integer boundary-ledger increment, with `|b_e|<=B`;
- every gate have underlying control-word length at most `L_gate`.

The complete boundary state is `(y,c)`, where `c` is the additive ledger.  Assume the **additive
boundary Markov contract**:

1. legality, terminal status and the next edge depend only on `(y,c)`;
2. executing `e` sends `(y,c)` to `(y',c+b_e)` and completes atomically;
3. every other future-relevant payment, owner, phase, capacity and history field is represented in `y`;
4. any change of the graph, increments, root-return words or update law is an outer reset.

A simple directed gate cycle has at most `q` edges and ledger drift of magnitude at most `qB`.

## AC3ts -- sign-coherent gate cycles have a common boundary rank -- PROVED

If every directed gate cycle has nonnegative ledger drift, choose a root `r` and let `d(y)` be the
minimum drift of a directed path from `r` to `y`.  Then

`-(q-1)B<=d(y)<= (q-1)B`

and every edge `e:y->y'` has reduced increment

`b_e+d(y)-d(y')>=0`.

Consequently

`H_+(c,y)=c-d(y)`

is nondecreasing along every gate.  If every directed cycle has nonpositive drift, the symmetric
construction gives a nonincreasing integer rank.

If all cycle drifts are strictly positive, every `q` completed gates increase `H_+` by at least one.
For a physical ledger interval of width `R`, the epoch has fewer than

`q*(R+2(q-1)B+1)`

completed gates and fewer than

`q*(R+2(q-1)B+1)*L_gate`

underlying control edges.  The sign-reversed statement is identical.

### Proof

A minimum-drift path may be chosen simple: deleting a repeated closed segment of nonnegative drift
cannot increase its drift.  Hence it has at most `q-1` edges and the displayed absolute bound.  The
optimality inequality `d(y')<=d(y)+b_e` gives the reduced increment.  Summing along a gate proves
monotonicity.

In the strict branch the zero-reduced-increment edge graph is acyclic, since a directed zero cycle
would have zero original drift.  Therefore every `q` edges include at least one unit of positive
reduced increment.  The physical range of `c` and the two path-potential extremes give an `H_+` range
of width at most `R+2(q-1)B`; partition a path into blocks of `q` gates. QED.

## AC3tt -- exact residue and primitive lift for mixed gate cycles -- PROVED

Assume positive and negative directed gate cycles both occur.  Choose one simple root path `P_y` from
`r` to each `y` and put

`p(y)=drift(P_y)`.

For an edge `e:y->y'`, define

`a_e=p(y)+b_e-p(y')`

and

`g=gcd{|a_e|:e in E}`.

Then `g` is the gcd of all directed closed-walk ledger drifts.  If `g>0`, every gate preserves

`xi=c-p(y) mod g`.

After fixing `xi`, the normalized lift

`ell=(c-p(y)-xi)/g`

has edge increment

`alpha_e=a_e/g`

with

`|alpha_e|<=(2q-1)B/g`

and increment gcd one.  If `g=0`, the integer `c-p(y)` is exactly invariant and every directed closed
walk has zero ledger drift.

### Proof

For each target `y'`, choose one directed return path `R_(y',r)`.  The two rooted closed walks

`P_y e R_(y',r)`

and

`P_(y') R_(y',r)`

have drift difference exactly `a_e`.  Hence the gcd of all directed closed-walk drifts divides every
`a_e`.  Conversely, telescoping `a_e=p(y)+b_e-p(y')` around any directed closed walk expresses its
drift as a sum of edge addresses, so `g` divides every closed-walk drift.  The two gcds are therefore
equal.  The residue and lift update identities follow by substitution.  Simple root paths have at most
`q-1` edges, giving `|a_e|<=(2q-1)B`. QED.

## AC3tu -- chronological primitive lift relations at gate level -- PROVED

In the mixed branch with `g>0`, enumerate the exact nonzero-drift simple cycles of the normalized lift.
Let their positive and negative drift extrema be `P` and `N`, and let their exact address stock have
size `s`.

Every primitive nonnegative zero-sum count relation contains at most

`P+N`

simple cycles, and the safe relation-address stock is

`K_rel=binom(P+N+s,s)-1`.

Using canonical shortest gate paths between cycle bases, every relation has one chronological root
macro of at most

`L_rel_gate=(2q-1)(P+N)+(q-1)`

completed gates.  Its underlying control word has length at most

`L_rel_gate*L_gate`.

The macro's only lift drift is its bounded connector defect.  Applying the same primitive-relation
construction to the finite defect alphabet gives either a common macro-boundary rank or a finite stock
of exact chronological root returns.

### Proof

Apply AC3td--AC3tl to the finite gate graph with control size `q` and normalized increments
`alpha_e`.  Every simple gate cycle has length at most `q`; the opposite-sign partial-sum argument gives
the `P+N` relation bound and the nonnegative-vector count gives `K_rel`.  Canonical connectors use at
most `q-1` gates, so AC3tj gives the displayed gate length.  Each gate expands to at most `L_gate`
control edges.  The second-level defect conclusion is AC3tk--AC3tl with the same gate dictionary. QED.

## AC3tv -- bounded additive boundary stock -- PROVED

If the physical ledger lies in an interval of width `R`, the exact boundary-state stock is at most

`N_add=q*(R+1)`.

Every legal gate history of at least `N_add` completed gates repeats one exact state `(y,c)`.  A
least-ending repeat is a simple exact gate cycle of at most `N_add` gates and at most
`N_add*L_gate` underlying control edges.

Under erasure, descent, finite-ticket, impossibility or reset treatment of every simple exact cycle,
the fixed additive-boundary epoch terminates.

### Proof

There are `q` auxiliary states and `R+1` ledger values.  Pigeonhole and least-ending cycle extraction
give the cycle and length bounds.  The finite-state closure argument is AC3ss/AC3tr. QED.

## AC3tw -- additive root-boundary router -- PROVED UNDER THE DECLARED CONTRACTS

Every exact root-return epoch with one additive boundary ledger has one continuation:

1. a common increasing or decreasing boundary rank from sign-coherent gate cycles;
2. an explicit strict-sign gate and control-edge budget when the ledger is bounded;
3. an exact invariant residue and primitive lift in a mixed-sign SCC;
4. finite chronological primitive-relation gates, followed by a macro rank or exact root returns;
5. finite exact-state closure when the ledger itself is bounded;
6. an unbounded zero-sum-free lift residual carrying the complete nonzero net drift;
7. or one additive-update, legality, omitted-field, gate-word or outer-reset contract failure.

### Proof

Apply AC3ts in the sign-coherent branches, AC3tt--AC3tu in the mixed branch and AC3tv whenever the
ledger is physically bounded.  AC3tf isolates the zero-sum-free residual.  All excluded hypotheses are
named failures. QED.

## Corrected AC4 numerical frontier

One unbounded additive payment or capacity balance at root boundaries no longer forces an
identity-sensitive infinite state.  It is a finite-control one-counter system at the gate scale and
therefore reduces to a common rank, an invariant residue and primitive lift, or finite chronological
relation gates with every underlying control-word loss explicit.

The remaining numerical work is discharge of unticketed additive macro relations and auxiliary cycles,
multiple coupled or nonadditive unbounded balances, unbounded zero-sum-free lift residuals, dynamic
control graphs, omitted guards or ownership fields, and changes of law not declared as outer resets.

## Finite check

`scripts/verify_ac_additive_boundary_ledger.py` samples strongly connected finite gate graphs with
integer boundary increments and bounded control-word lengths.  It checks sign-coherent shortest-path
ranks, strict-cycle budgets, exact gcd/residue/lift identities, primitive opposite-sign relations,
chronological connector bounds and bounded exact-state repetition.
