# Exact operation rollback from the eleven-host rank-three core

CMR1998--CMR2013 classify the eleven side-four hosts whose canonical response family
contains no rank-three-free response. This chapter asks a different structural
question from occurrence deletion: how many edges of the canonical deletion matching
must be **restored** before a zero-rank-three response becomes available?

For a hard-core host `H` with canonical deletion matching `D`, a rollback is a subset
`R subseteq D`. The restored host uses deletion matching `D\R`. Define

\[
\rho(H)=\min\{|R|:\min_{Q\in\operatorname{PM}(D\setminus R)}\psi_3(Q)=0\}.
\]

Rollback changes the parent operation. It is not a payment inside the original row.

## 1. Finite rollback existence

### Theorem CMR2022 -- PROVED

Every one of the eleven hard-core hosts has finite rollback distance.

### Proof

Removing the entire deletion matching recovers the undeleted side-four base host,
which has four zero-rank-three responses by CMR1998. Hence the finite set in the
definition of `rho(H)` is nonempty. ∎

## 2. Exact rollback-distance distribution

### Theorem CMR2023 -- PROVED

The exact distribution is

\[
\boxed{10\text{ hosts with }\rho=1,\qquad1\text{ host with }\rho=2.}
\]

Consequently the independent sum of minimum rollback distances is

\[
\boxed{12.}
\]

### Proof

For each hard-core deletion matching, enumerate its subsets in increasing cardinality.
Reconstruct the restored canonical host and test every restored response for literal
rank-three collinearity. Ten hosts first succeed at cardinality one and one first
succeeds at cardinality two. ∎

## 3. The unique distance-two host

### Theorem CMR2024 -- PROVED

The unique host with rollback distance two is

\[
\boxed{\texttt{s4-59ac56096a7f627f}}
\]

with deletion matching

\[
D=\{(0,2),(1,3),(2,0),(3,1)\}.
\]

Every one-edge rollback still contains one of the three minimal blockers of CMR2000.
Its exact minimum two-edge rollback options are

\[
\{(0,2),(1,3)\},\qquad
\{(0,2),(3,1)\},\qquad
\{(2,0),(3,1)\}.
\]

### Proof

Directly inspect the four one-edge restorations. Each remaining deletion set still
contains a minimal zero-response blocker. Exhaustive testing of the six two-edge
subsets gives exactly the displayed three successful rollback sets. ∎

## 4. Complete minimum-option census

### Theorem CMR2025 -- PROVED

Across the eleven hosts there are exactly

\[
\boxed{21}
\]

minimum-cardinality rollback options. Their per-host option-count distribution is

\[
\boxed{2\text{ hosts with one option},\quad8\text{ with two},\quad1\text{ with three}.}
\]

The 21 options land in 13 distinct restored canonical hosts. Nineteen options restore
one zero response and two options restore two zero responses.

### Proof

After the minimum distance of each host is known, retain every successful rollback of
that exact size. Canonically reconstruct the restored host ID and count its
zero-rank-three responses. ∎

## 5. Uniform slack after rollback

### Theorem CMR2026 -- PROVED

Every minimum rollback option restores a deterministic zero-rank-three response, but
none restores a uniformly strict rank-three row. The restored uniform slacks are

\[
\boxed{19\text{ options with }S_3=-2,\qquad2\text{ with }S_3=-1.}
\]

### Proof

Recompute `Z-A_3` on every restored canonical host. The exact distribution is the one
displayed. Thus rollback removes the deterministic positive minimum but does not
make the uniform average strict. ∎

## 6. Two exact structural currencies

### Theorem CMR2027 -- PROVED

For the eleven hard-core hosts:

1. fixed-response rank-three occurrence deletion has independent burden 17;
2. minimum operation rollback has independent distance 12.

These are exact but incomparable currencies.

### Proof

The first total is CMR2009. The second is CMR2023. Occurrence deletion modifies the
witness accounting while holding the selected operation fixed; rollback changes the
canonical deletion matching and therefore the response family. ∎

### Corollary CMR2028 -- PROVED

The numerical difference `17-12=5` is not reusable slack in either policy. A proof
may use rollback only after proving that the parent operation is permitted to restore
the specified deletion restrictions and after rebuilding all affected state and fate
data.

## 7. Executable endpoint

### Corollary CMR2029 -- PROVED

`scripts/check_prime_power_rank_three_hard_core_rollback.py` reconstructs every
hard-core host, exhaustively searches rollback subsets, verifies minimum distances and
all minimum options, and links every restored host back to the canonical catalogue.

Its exact manifest digest is

\[
\texttt{6663bcaa9504dc361a65b230ef88e39919e80acdca93647a95c103a10e8c487b}.
\]

The built-in mutation suite rejects ten independently corrupted manifests.

This chapter classifies a possible operation change. It does not prove that such a
rollback is legal in the actual parent policy or that the resulting complete labelled
row is strict.
