# Exact side-four blockers of all zero-rank-three responses

CMR1990--CMR1997 isolate eleven side-four raw hosts for which every available
response has positive rank-three load.  This chapter proves that the eleven-host list
is exactly a finite transversal family, identifies its three inclusion-minimal
blockers, and supplies a canonical executable manifest.

The side-four base host has fixed forbidden set

\[
F_0=\{(i,i):0\le i<4\}\cup\{(0,1)\}.
\]

Before any partial-matching deletion is imposed, it has six response permutations.

## 1. Exact base response table

### Theorem CMR1998 -- PROVED

The six perfect matchings avoiding `F_0`, with their literal numbers of collinear
response triples, are

| permutation | rank-three triples |
|---|---:|
| `(2,0,3,1)` | 0 |
| `(2,3,0,1)` | 0 |
| `(2,3,1,0)` | 0 |
| `(3,0,1,2)` | 1 |
| `(3,2,0,1)` | 0 |
| `(3,2,1,0)` | 4 |

Hence the base family contains exactly four zero-rank-three responses and two
positive responses.

### Proof

Enumerate the `4!` permutations, reject every permutation using a fixed forbidden
edge, and test each of the four choose three response-point triples by the integer
determinant criterion.  Exactly the displayed six permutations survive and have the
displayed counts. ∎

## 2. Deletion sets as response blockers

For a canonical partial-matching deletion set `D`, let

\[
\operatorname{PM}(D)=\operatorname{PM}(F_0\cup D).
\]

Let `Z_0` be the four zero-rank-three base responses.  Regard every response as its
four-edge set.

### Theorem CMR1999 -- PROVED

A canonical deletion set has positive minimum rank-three response load if and only if

1. `D` intersects every edge set in `Z_0`; and
2. `PM(D)` is nonempty.

### Proof

If `D` misses one zero response, that response remains available, so the minimum is
zero.  Conversely, if `D` hits all four zero responses, every surviving response is
one of the two positive responses from CMR1998.  Nonemptiness ensures that the
minimum is defined and positive. ∎

Thus positive-minimum hosts are precisely nonempty canonical transversals of the
zero-response hypergraph.

## 3. Inclusion-minimal blockers

### Theorem CMR2000 -- PROVED

The exact inclusion-minimal canonical blockers are

\[
\boxed{
\{(0,2),(2,0)\},\qquad
\{(0,2),(3,1)\},\qquad
\{(1,3),(3,1)\}.
}
\]

### Proof

Enumerate every partial matching on the admissible side-four edge set.  Keep the sets
meeting all four zero-response edge sets and having a surviving response.  Test each
retained set against all proper retained subsets.  Exactly the displayed three are
minimal. ∎

### Corollary CMR2001 -- PROVED

Every positive-minimum canonical side-four deletion set contains at least one of the
three blockers in CMR2000.

### Proof

Every finite transversal contains an inclusion-minimal transversal.  CMR2000 lists
all inclusion-minimal canonical transversals. ∎

## 4. Complete canonical blocker census

### Theorem CMR2002 -- PROVED

Exactly eleven canonical deletion matchings hit all four zero responses while leaving
at least one response.  Their deletion-size distribution is

\[
\boxed{3\text{ of size }2,\qquad6\text{ of size }3,\qquad2\text{ of size }4.}
\]

Their exact host IDs coincide, in the same canonical order, with the eleven
positive-minimum host IDs of CMR1996.

### Proof

Enumerate every canonical partial matching on the admissible edge set and apply the
two conditions in CMR1999.  The eleven retained records have the displayed size
counts.  Reconstruct their catalogue IDs and compare the ordered list directly with
the selector manifest. ∎

## 5. Surviving positive responses

### Theorem CMR2003 -- PROVED

Among the eleven blocker hosts:

1. nine retain both positive base responses and have minimum rank-three load one;
2. two retain only `(3,2,1,0)` and have minimum rank-three load four.

Equivalently, the hard-core minimum distribution is

\[
\boxed{[[1,9],[4,2]].}
\]

### Proof

For every blocker, re-enumerate the perfect matchings of `F_0 union D` and compare
with the base response table of CMR1998. ∎

## 6. Exact hard-core equivalence

### Theorem CMR2004 -- PROVED

For canonical side-four raw hosts, the following conditions are equivalent:

1. the exact rank-three selector minimum is positive;
2. the deletion matching blocks every zero-rank-three base response;
3. the deletion matching contains one of the three minimal blockers of CMR2000 and
   leaves a response;
4. the host ID belongs to the eleven-host list in CMR1996.

### Proof

CMR1999 gives `1 iff 2`; CMR2000--CMR2001 give `2 iff 3`; CMR2002 identifies the
resulting host IDs with the selector list, giving `2 iff 4`. ∎

This is a classification theorem, not merely a census coincidence.

## 7. Executable endpoint

### Corollary CMR2005 -- PROVED

`scripts/check_prime_power_rank_three_zero_response_blockers.py` implements the full
classification.  It reconstructs the base response table, the four zero-response
edge sets, all canonical partial-matching transversals, the three minimal blockers,
the eleven surviving hosts, their response lists, and the exact selector-list
equality.

The canonical blocker-manifest digest is

\[
\texttt{94713659dd58fea0ccb015d4a5ce25e447c766ebd2936fff696f39ce1e539fc3}.
\]

Its built-in mutation suite rejects ten independently corrupted manifests.

The theorem concerns the raw rank-three response geometry only.  It does not prove
that any background-dependent or labelled recurrent row is strict.
