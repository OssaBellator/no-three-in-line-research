# Geometric-cleaning integrated physical remedy-height flow

This note records GC2jl--GC2jp. It composes physical source issuance with the integrated remedy/height/cause network in one comparison.

## Contract

Fix physical source classes `P`, remedy classes `R`, height-source classes `H` and cause classes `C`. Retain complete relations `P -> R`, `R -> H` and `H -> C`. Existing remedy and height balances, physical source mass and cause demands are integral. A physical source unit funds one retained remedy-height path.

## Theorem block

### GC2jl — four-layer physical network

Physical source mass and existing remedy/height balances feed one integral `P -> R -> H -> C` network with exact node capacities.

### GC2jm — simultaneous remedy issuance

Maximum flow chooses physical remedy issuance and remedy-height routing simultaneously. No preliminary remedy allocation is required.

### GC2jn — complete cut criterion

Every cause is paid exactly when each physical/remedy/height/cause cut has capacity at least total cause demand.

### GC2jo — canonical mixed cleaning cut

Failure returns one canonical minimum cut retaining exact physical source, remedy, height-source and cause classes. Its deficit equals unpaid cause mass.

### GC2jp — reset boundary

Changed height costs, omitted compatibility, hidden issuance, splitting, source-less creation or nonadditive remedy effects return reset or amplification.

## Finite audit

Run `python scripts/verify_gc_integrated_physical_remedy_height_flow.py`.

The audit checks 5,000 systems: 17,460 physical-source, 17,349 remedy, 17,505 height and 17,549 cause classes; 97,557 compatibility arcs; 44,032 cause-demand units; 39,164 paid and 4,868 unpaid units; 1,367 deficient systems; and 6 cases where greedy remedy preissuance loses a feasible simultaneous route.

## Scope

The theorem does not construct the geometric graph, prove its height costs, or handle untagged feedback. It does not prove GC5 or the no-three-in-line conjecture.
