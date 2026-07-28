# Geometric cleaning: conservative cyclic adverse components

## Scope

This note records GC2hn--GC2hr. It treats cyclic target-recreation and donor-destruction dependencies under a complete occurrence-faithful nonamplifying token contract.

Collapse the finite adverse-source dependency graph into strongly connected components `C_0,...,C_{R-1}` ordered topologically. Each adverse token is an exact unit of target recreation or donor destruction and retains one physical predecessor lineage.

An internal transition consumes one adverse precursor token and creates exactly one successor token in the same or a later component. Exogenous adverse deposits are recorded separately. A global-shortage adverse event consumes one token.

## GC2hn: SCC conservation

Transitions inside one strongly connected component preserve its total adverse-token mass. Cycling inside a component therefore cannot create unbounded target recreation or donor destruction.

## GC2ho: global adverse count

At every time,

`live adverse tokens + consumed adverse events = initial adverse tokens + deposited adverse tokens`.

Hence total adverse mass available to close global-shortage progress is bounded by the initial-plus-deposited stock.

## GC2hp: condensation throughput

Each occurrence-faithful token crosses at most `R-1` component boundaries. Thus total cross-component precursor transfers are at most

`(R-1)(C_0+D_0)`.

## GC2hq: cyclic dependency compression

Every directed adverse dependency cycle lies inside one SCC. Under one-for-one conservation it may be collapsed to a single finite component state, after which the ranked adverse-source theorem applies to the condensation DAG.

## GC2hr: exact amplification obstruction

Source-less adverse creation, one-to-many splitting, incomplete target/donor lineage, or a transition outside the retained component map is returned as an exact adverse-amplification or dictionary-reset obstruction.

## Remaining frontier

The theorem does not prove that geometric target recreation and donor destruction are one-for-one. Physical payment of overloaded causes, proof of the conservative lineage contract, unbounded dictionaries, untagged feedback, clean-height preservation, and local resampling remain open. GC5 and the global conjecture are not proved.