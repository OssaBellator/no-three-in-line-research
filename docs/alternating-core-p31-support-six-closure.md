# Complete support-six closure of the p=31 three-triple core

## Status

This note keeps AC as the sole active research track and proves AC5os--AC5ou for the explicit `p=31`, `n=30` three-triple state. It completes every six-extra red/blue support distribution.

## AC5os -- complete six-extra support census -- PROVED

For each `a=0,...,6`, choose `a` additional red row addresses and `6-a` additional blue row addresses outside the nine core layer-row addresses. Permute exactly the current retained values on those enlarged supports, fix every outside cell, reject red-blue collisions, and prune whenever the exact partial potential exceeds two.

The exact census is

\[
\begin{array}{c|r|r|r}
(a,6-a)&\text{support choices}&\text{partial states}&\Phi\le2\text{ endpoints}\\
\hline
(0,6)&177{,}100&35{,}678{,}890&0\\
(1,5)&1{,}381{,}380&202{,}363{,}641&0\\
(2,4)&4{,}111{,}250&467{,}355{,}187&0\\
(3,3)&5{,}980{,}000&577{,}440{,}893&0\\
(4,2)&4{,}485{,}000&416{,}388{,}566&0\\
(5,1)&1{,}644{,}500&169{,}065{,}024&0\\
(6,0)&230{,}230&29{,}657{,}917&0.
\end{array}
\]

Thus all

\[
\boxed{18{,}009{,}460}
\]

six-extra support choices close after

\[
\boxed{1{,}897{,}950{,}118}
\]

admissible partial states, with no complete collision-free endpoint of potential at most two.

### Proof

The support universe is partitioned into 32 exact lexicographic shards. For each support, the fixed outside cells are inserted first. The moved values are assigned occurrence-faithfully. Adding one cell increases the exact potential by `binom(k,2)` for each real line containing `k` already assigned points. Every branch ends at a collision, at partial potential greater than two, or at a complete assignment. The committed shard ledgers cover all supports without overlap or omission and contain zero complete assignments. QED.

## AC5ot -- no six-extra endpoint improvement -- PROVED

Every collision-free endpoint supported on the nine core addresses plus at most six additional tagged row addresses satisfies

\[
\boxed{\Phi\ge3}.
\]

The support-three, support-four, and support-five theorems close smaller support layers; AC5os closes exactly six extras.

## AC5ou -- support-six expansion target -- PROVED

Every endpoint of potential two, one or zero differs from the explicit three-triple state on at least seven tagged row addresses outside the nine-address core. Consequently every successful endpoint repair has total tagged layer-row support at least

\[
\boxed{9+7=16}.
\]

This is an endpoint lower bound. A switch path may use a wider temporary support and later restore some addresses.

## Deterministic audit

Compile:

```text
g++ -O3 -std=c++20 -fopenmp scripts/verify_ac_p31_support_six.cpp -o verify_support_six
```

The verifier accepts one shard index from `0` through `31`, reconstructs that shard's distribution and support interval, and asserts its exact support and partial-state counts. The complete shard table is stored in `data/ac-p31-support-six-closure.json`.

Expected totals:

- support choices: `18009460`;
- partial states: `1897950118`;
- complete potential-at-most-two endpoints: `0`.

## Remaining frontier

1. Search the seven-extra support layer for the first potential-at-most-two endpoint or another exact closure.
2. Finish the independent barrier-nine switch component from the same three-triple state.
3. Convert any wider-support endpoint into a legal low-barrier switch ordering.
4. Extract a structural explanation for closure through total support fifteen.
5. Generalize the support lower bound beyond this explicit `p=31` endpoint.

AC6 and the general no-three-in-line conjecture remain open.
