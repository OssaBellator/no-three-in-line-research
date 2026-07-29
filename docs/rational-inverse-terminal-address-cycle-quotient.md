# Polynomial terminal-address quotient and restoration cycles

**Branch:** `research/rational-inverse-expansion`

RI5ac--RI5ae reduce active terminal collateral to thirteen canonical rank-two/rank-three words. RI5au--RI5ax reduce blocker prescriptions to nine canonical path/cycle types. RI5af--RI5aj reconstruct prime-field quotient, root, image and scale labels from physical rational-inverse occurrences. This note combines those facts into one complete finite terminal address.

The result removes a recurrence ambiguity. A terminal obstruction may still require arithmetic payment or absorption, but it cannot carry an unbounded independent quotient/coset/scale label history once its physical occurrences and finite word are fixed.

## Terminal record model

Fix an odd prime `p`, put `N=p-1`, and retain the prime-field physical contract of RI5af--RI5aj. Let

\[
K_{\rm occ}=N_{\rm RI}^{\rm occ}\le L_{\rm RI}N^6
\]

be the physical occurrence-address stock from RI5ai.

A **terminal record** consists of:

1. one of the thirteen active interaction words or nine blocker path/cycle types;
2. rank `s<=3` and, for blocker records, overlap `q<=s` and occupancy `1<=t<=N`;
3. at most three exact physical RI occurrence addresses, padded by a null symbol;
4. the declared finite carry, channel, owner, completion and blocker decorations already contained in the external role word.

The physical occurrences are ordered by the fixed role order of the word/type.

## RI5bd -- terminal quotient and secant labels are reconstructed -- PROVED UNDER THE PRIME-FIELD PHYSICAL CONTRACT

For one terminal record, the following data are derived from the finite word/type and its at most three physical occurrences:

- subgroup identity and quotient index;
- every source, root, companion, image and scale coset;
- quotient products and inverses;
- physical direction and signed affine offset of every declared crossed channel;
- the one-target incidence or two-target hyperbola-secant label of RI5ad;
- the path/cycle component decomposition of a blocker prescription.

No item in this list is an independent terminal-state coordinate.

### Proof

RI5af--RI5ah reconstruct subgroup and quotient-coset arithmetic, roots, companion roots, images and scales from one physical occurrence and the declared subgroup order. The crossed direction/offset is computed from the physical board cells in the occurrence address. RI5ad determines whether the fixed terminal word uses one-target incidence or a two-target secant; in the latter case the two ordered physical target occurrences determine the exact secant. RI5au reconstructs the blocker path/cycle type from its prescribed source and target endpoints. The remaining finite decorations are already fields of the external role word. QED.

A change of primitive-root convention, ambient field, occurrence interpretation or external role dictionary is an outer reset.

## RI5be -- polynomial complete terminal stock -- PROVED

Let `K_occ` be any valid complete physical occurrence stock. The number of complete active and blocker terminal records is at most

\[
\boxed{
K_{\rm term}
\le
264N(K_{\rm occ}+1)^3.
}
\]

Consequently, using RI5ai,

\[
\boxed{
K_{\rm term}
\le
264N(L_{\rm RI}N^6+1)^3
=O(L_{\rm RI}^3N^{19}).
}
\]

### Proof

There are at most `13+9=22` word/type choices. Retain at most `12` safe `(s,q)` decorations; this overcounts the actual feasible list. Retain at most `N` occupancy values, using a dummy value for active records. Each of the three ordered occurrence slots has `K_occ+1` choices after adjoining the null symbol. Multiplication gives `22*12*N*(K_occ+1)^3`. The second display substitutes RI5ai. QED.

The exponent is an ambient safe bound, not an optimized count.

## RI5bf -- long terminal histories contain short exact cycles -- PROVED

Inside one fixed external role dictionary and prime-field interpretation, any terminal-record history of length greater than `K_term` repeats a complete record. The first repeated-record segment contains a simple exact terminal cycle of length at most `K_term`.

### Proof

Pigeonhole gives a repeated complete record. Delete closed subwalks from the repeated segment until no internal record repeats. The remaining closed walk is a simple directed cycle and has at most `K_term` vertices. QED.

Because the address is complete, returning to one record returns every reconstructed quotient, scale, direction/offset, secant, owner and blocker field.

## RI5bg -- canonical restoration gate and recurrence router -- PROVED UNDER THE RESTORATION CONTRACT

Fix total orders on the finite terminal fields. Every nonconstant simple exact terminal cycle has a canonical least changing field, a least value on that field, a first edge leaving that value and a first later edge restoring it. The final edge of this excursion is the **terminal restoration gate**, addressed by the complete decorated edge together with the restored field/value.

Every recurrent exact active or blocker terminal cycle then has one continuation:

1. current payment through its selected physical owner or source factor;
2. strict descent in scale, carry, completion debt or blocker rank;
3. physical impossibility of the canonical restoration gate;
4. capacity-one consumption of the exact occurrence/owner/restoration address;
5. invocation of the fixed-edge bank when the restored record is coherent and bank-ready;
6. or an explicit reset in field, role dictionary, physical occurrence, owner, completion or legality interpretation.

If every reachable restoration address is capacity one whenever the first five alternatives do not apply, at most the finite reachable restoration-edge stock of recurrent cycles occurs in the epoch.

### Proof

Apply the finite product-state leave/restore argument to the complete address of RI5bd--RI5be. A nonconstant cyclic coordinate leaves some attained value and must later return because the cycle closes. Least-field, least-value and first-edge conventions make the gate canonical. RI5bf extracts a simple exact cycle. The declared alternatives are edge-local outcomes; capacity-one addresses cannot repeat. A change not represented in the complete record violates the fixed-epoch contract and is returned as an outer reset. QED.

## Updated RI frontier

The purely combinatorial and naming parts of the terminal recurrence problem are now finite and polynomial:

- thirteen active words and nine blocker types;
- at most three physical occurrence addresses;
- reconstructed quotient, scale, direction/offset and secant labels;
- a simple cycle of length at most `K_term`;
- one canonical restoration gate.

The remaining RI6 work is arithmetic and payment specific: classify or absorb the reachable restoration classes, prove physical owner/coherence payment, and verify the final collateral comparison needed to invoke the fixed-edge bank.

## Finite check

`scripts/verify_ri_terminal_address_cycles.py` enumerates small terminal dictionaries, verifies the ambient stock bound, extracts first repeated-record cycles and checks the canonical restoration gate on exhaustive and sampled histories.
