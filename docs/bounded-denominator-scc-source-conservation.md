# Bounded denominators: conservative cyclic source components

## Scope

This note records BDA5cp--BDA5ct. It addresses cyclic source dependencies only under an occurrence-faithful nonamplifying token contract. It does not prove that a concrete arithmetic source system satisfies that contract.

Let the finite source-dependency graph have strongly connected components `C_0,...,C_{R-1}` ordered topologically in the condensation DAG. Every source token has one exact physical lineage address.

Allowed internal source transitions consume one token and create exactly one successor token. The successor lies either in the same strongly connected component or in a later component. Exogenous deposits create explicitly paid new tokens. Terminal restoration use consumes a token.

## BDA5cp: component conservation

Transitions inside one strongly connected component conserve the total token count of that component. Hence cycling inside a source component cannot create net numerator mass.

## BDA5cq: global source count

At every time,

`live tokens + terminally consumed tokens = initial tokens + deposited tokens`.

Consequently the total number of terminal source uses is at most the initial-plus-deposited token stock.

## BDA5cr: cross-component throughput

A single occurrence-faithful token crosses at most `R-1` component boundaries. Therefore the total number of cross-component source transfers is at most

`(R-1)(C_0+D_0)`,

where `C_0` is the initial token count and `D_0` is the total exact deposited-token count.

## BDA5cs: cycle compression

Every directed dependency cycle is contained in one strongly connected component and is harmless for mass accounting under the conservative transition contract. The earlier ranked source potential applies to the condensation DAG after each component is collapsed.

## BDA5ct: exact amplification obstruction

If an internal event creates a token without consuming a predecessor, splits one predecessor into multiple successors, merges or relabels lineages without retaining the complete physical map, or moves backward in the condensation order, that exact event is returned as a source-amplification or lineage-reset obstruction.

## Remaining frontier

This closes cyclic source dependence only when internal transitions are one-for-one and occurrence-faithful. Arithmetic proof of nonamplification, payment or impossibility of the selected wall/source pair, unbounded source dictionaries, and incomplete lineage remain open. BDA6 and the global conjecture are not proved.