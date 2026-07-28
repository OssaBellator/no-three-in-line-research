# GC cause-to-remedy transportation

This note turns exact missing-rectangle cause mass into a complete physical-remedy flow problem. It does not prove GC5 or the no-three-in-line conjecture.

## Exact cause demand

After the canonical Hall-core and missing-rectangle routers, aggregate all failed incidences by exact physical cause `c`. Let `d_c` be the resulting nonnegative integer demand.

Let `R` be a finite dictionary of physical removal, neutralization, or donor-restoration remedies. Each remedy `r` has capacity `k_r`, and the complete compatibility graph records exactly which remedies can pay which causes.

## Integral transportation theorem

Build the capacitated bipartite network

`source -> causes -> remedies -> sink`,

with cause demand on the first arcs, infinite compatibility arcs, and remedy capacities on the last arcs.

Then the maximum paid cause mass equals

`sum_c d_c - max_A (sum_{c in A} d_c - sum_{r in N(A)} k_r)_+`,

where `A` ranges over cause subsets.

Hence all cause mass is paid if and only if every capacitated Hall inequality

`sum_{c in A} d_c <= sum_{r in N(A)} k_r`

holds.

## Canonical failure certificate

When payment fails, choose the least maximizing cause subset `A`. It gives an exact deficient cause/remedy cut with unpaid mass

`sum_{c in A} d_c - capacity(N(A))`.

This cut is retained for the next router. It is not replaced by a global shortage or anonymous reset.

## Composition with existing banks

- cause capacities from the missing-rectangle bank may be used as remedy capacities;
- conservative adverse-source SCCs may replenish remedies only through exact deposited tokens;
- an exhausted remedy, omitted compatibility arc, changed cause label, or dynamic dictionary is an explicit reset or overload.

## Outside the contract

The theorem does not cover one remedy simultaneously paying several cause units without capacity debit, higher-order remedy compatibility not represented by pairwise arcs, or untagged physical operations that change more than one retained cause class.
