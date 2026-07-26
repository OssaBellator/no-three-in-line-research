# Lifted occurrence-lineage gates for owner identity changes

**Branch:** `research/alternating-core-chain`

AC3oq--AC3ot normalize finite changing-builder semantics when one exact owner
occurrence keeps its identity.  A builder transition may instead replace one
occurrence address by another.  Such a step is not automatically a recreation
of the same owner: it needs an explicit continuation certificate.

This note lifts builder states and owner occurrences into one finite directed
lineage graph.  Every certified occurrence-changing recreation has a canonical
first false-to-true lifted edge.  A transition with no declared continuation
edge is owner replacement, not same-owner recreation.

## Reconstructed occurrence-lineage graph

Fix one finite normalized builder super-epoch with builder-state set `Y`.  For
each `y in Y`, let `Omega_y` be the finite set of exact owner occurrences
recognized in that state.  Form

`V_occ={(y,omega): y in Y, omega in Omega_y}`.

Each vertex has a currentness value

`h(y,omega) in {0,1}`.

For every legal builder transition `e:y->y'`, the builder registry declares a
finite continuation relation

`R_e subseteq Omega_y x Omega_(y')`.

An exact lineage step retains the address `(e,omega,omega')` with
`(omega,omega') in R_e`.  A lineage history is a directed path in the lifted
graph `D_occ` whose vertices are `V_occ` and whose edges are the declared
continuation steps.

The relation may be partial or multi-valued.  The actual transition must record
which exact continuation edge it uses.  Equal symbolic owner names do not
replace this witness.

## AC3ou -- certified identity change is exactly lifted reachability -- PROVED

An occurrence-changing transition from `(y,omega)` to `(y',omega')` is a
same-owner continuation inside the super-epoch exactly when it carries a
registered lifted edge

`(e,omega,omega') in E(D_occ)`.

If no such edge is declared, the new occurrence is classified as owner
replacement or new-owner creation, not recreation of the old exact owner.

### Proof

The reconstructed registry defines same-owner continuation by the relation
`R_e`; hence a registered pair is sufficient.  Conversely, without a relation
edge there is no occurrence-faithful datum identifying the two exact physical
occurrences.  Equality of a symbolic label can arise from unrelated builders or
resources and therefore cannot prove identity. QED.

This is an identity wall, not a ticket hypothesis.  It prevents payment from
being duplicated by silently relabelling a new owner as an old one.

## AC3ov -- every certified lineage recreation has a canonical lifted boundary -- PROVED

Let

`v_0,v_1,...,v_m`

be a certified lineage path beginning after destruction with `h(v_0)=0` and
ending with `h(v_m)=1`.  There is a unique first index `j` such that

`h(v_(j-1))=0` and `h(v_j)=1`.

The exact lifted continuation edge `(v_(j-1),v_j)` is the canonical
occurrence-lineage recreation gate.

### Proof

The truth word along the path begins with zero and ends with one.  Choose the
least index at which it equals one.  Minimality gives zero immediately before
that index, and the least index is unique. QED.

The source and target occurrences may have different addresses and may lie in
different builders.  The continuation witness, not address equality, carries
the lineage.

## AC3ow -- finite lifted gate stock and weighted localization -- PROVED

Write

`Z={v in V_occ:h(v)=0}` and `O={v in V_occ:h(v)=1}`.

Let `P=|V_occ|`.  The number of possible directed false-to-true lifted gates is
at most

`E_occ <= |E(D_occ) intersect (Z x O)| <= |E(D_occ)|`

and also

`E_occ <= |Z|*|O| <= floor(P^2/4)`.

If every lifted vertex has outdegree at most `d_occ`, then

`E_occ <= |Z|*d_occ <= P*d_occ`.

Consequently a weighted family of certified lineage returns of total weight
`W` contains one exact gate address, including transition kind, of weight at
least

`W/(K_occ*E_max)`,

where `E_max` is any displayed gate-stock bound and `K_occ` is the number of
exact continuation kinds.

### Proof

AC3ov maps every return to one false-to-true lifted edge.  The edge-count bounds
are immediate from the legal graph, the bipartite product and the outdegree
sum.  Weighted pigeonhole over edge-kind addresses gives the last statement.
QED.

## AC3ox -- finite occurrence-lineage ticket bound -- PROVED

Give every exact lifted gate address

`(v^-,v^+,kappa_occ)`

an integer capacity `c_occ`, consumed when charged and not restored inside the
reconstructed super-epoch.  Then the number of charged occurrence-changing
recreation episodes is at most

`C_occ=sum c_occ`.

### Proof

AC3ov assigns one exact first false-to-true edge to every certified return.
Charging consumes one unit from its exact address, and no unit is restored. QED.

One lifted edge may make several owner lineages current.  Their lineage or token
addresses remain separate unless a shared-capacity theorem is declared.

## AC3oy -- closure of finite certified occurrence-changing recreation -- PROVED UNDER THE LINEAGE-GATE CONTRACT

Inside one finite reconstructed occurrence super-epoch, suppose every certified
lineage recreation gate follows at least one route:

1. the lifted edge is impossible under the transition rules;
2. traversing it gives an improving or terminal output;
3. traversing it strictly advances another bounded integer potential;
4. it consumes finite unrestorable capacity at its exact lifted address;
5. it leaves the finite occurrence registry and is recorded as a higher outer
   reset.

Then certified occurrence-changing owner recreation cannot sustain an infinite
nonterminal history inside the super-epoch.

### Proof

AC3ov gives every certified return one lifted boundary edge.  AC3ow gives a
finite edge stock.  Routes 1--4 forbid or bound repetition of each edge, and
route 5 exits the super-epoch.  Recreation-free common-owner segments are
bounded by AC3nz. QED.

## Corrected AC4 owner frontier

Finite owner-identity changes are now exact:

- a declared continuation edge gives a finite lifted gate;
- no continuation edge means owner replacement, so old-owner payment cannot be
  reused;
- finite lifted returns close under tickets, descent or terminal output.

The remaining owner frontiers are unbounded or nonreconstructed occurrence
registries, continuation tickets that can themselves be recreated, genuinely
nonadditive resources, and interaction with unresolved availability, conflict,
reverse and arithmetic macro-cycle gates.

## Finite check

`scripts/verify_ac_occurrence_lineage_gates.py` exhausts small builder-state
occurrence families, continuation relations, truth maps and lineage paths.  It
checks the identity wall, canonical first boundary, legal-edge/product/outdegree
bounds, weighted localization and capacity-one ticket accounting.
