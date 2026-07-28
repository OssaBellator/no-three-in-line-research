# Cross-block identification of local quotient states

CMR2246--CMR2253 produce one denominator-cleared integer package for one recurrent block.
A global assembly must first decide which local states in different blocks denote the same
mathematical state. This chapter fixes an exact finite identification surface.

## Theorem CMR2254 — PROVED AS AN INTERFACE

Every supplied integer recurrent block receives one canonical block ID and must validate
independently through CMR2246--CMR2253.

The complete local state registry of a block is reconstructed from the common-weight row
sources embedded in that block. No user-supplied local-state list is trusted.

## Theorem CMR2255 — PROVED

Every local state reference

\[
(\text{block ID},\text{local state ID})
\]

must have exactly one link to one nonempty global state ID. The link family covers every
local state exactly: missing links, duplicate links and links to unknown block states are
rejected.

## Theorem CMR2256 — PROVED

For every global state class, all local members must have identical semantic core

\[
\boxed{(\text{role},\text{stratum},\text{owner}).}
\]

Thus one global class cannot merge recurrent and auxiliary states, different strata, or
different owner records merely by assigning them the same global name.

## Theorem CMR2257 — PROVED

Each global state record publishes its complete canonically ordered member list, member
blocks, class size, semantic core and record digest.

Classes of size one remain explicit. Shared classes are not inferred from equal local
strings; they are determined only by the supplied exact links.

## Theorem CMR2258 — PROVED

The checker reconstructs the block-overlap graph induced by shared global state classes. An
edge joins two blocks exactly when some global state has a local member in both blocks.

The complete edge set and digest are published for the weight-synchronization layer.

## Theorem CMR2259 — PROVED

The certificate publishes exact counts of blocks, local states, global classes, shared
classes, maximum class size, overlap edges and global roles. Every aggregate is reconstructed
from the linked local registries.

## Theorem CMR2260 — HONEST IDENTITY BOUNDARY

A passed certificate proves exact consistency and complete coverage relative to the supplied
local-to-global links. It does not prove that two linked local records genuinely denote the
same external mathematical state, or that two unlinked records are genuinely distinct.

## Corollary CMR2261 — EXECUTABLE ENDPOINT

`scripts/check_prime_power_cross_block_state_identification.py` validates every integer block,
reconstructs all local states, requires exact link coverage, rejects semantic drift inside a
global class and publishes canonical global-state and block-overlap records.

The checker was syntax-compiled in the publication environment. No genuine multi-block state
identification table is yet supplied.
