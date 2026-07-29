# Eventual quasipolynomials for marker schedules

`docs/513` supplies finite residue correctors for one periodic marker flow.  This
chapter identifies the general finite-block mechanism behind those formulas:
minimum marker cost is eventually affine on each attainable length residue.

Let the available based marker blocks be indexed by `i`.  Block `i` has positive
integer length `ell_i`, rational cost `c_i`, and a rational action-count vector
`a_i`.  Concatenating based blocks preserves marker-state compatibility.

## 1. Eventual residue formula

### Theorem PP3ckj -- PROVED / EVENTUAL MARKER QUASIPOLYNOMIAL

Choose a block `P` of minimum mean cost

```text
mu=c_P/ell_P=min_i c_i/ell_i,
```

and put `L=ell_P`.  For every residue `r mod L` that is attainable by a block
concatenation, there are a rational excess `eta_r` and a least threshold `N_r`
such that

```text
F(N)=mu N+eta_r
```

for every attainable `N>=N_r` with `N congruent r mod L`, where `F(N)` is the
minimum cost of a length-`N` based schedule.

#### Proof

Scale costs so that all reduced excesses

```text
E_i=L c_i-c_P ell_i
```

are nonnegative integers.  For one residue `r`, minimize total reduced excess
over all concatenations having length congruent to `r mod L`; among minimizers,
choose one of least length `N_r`.  The minimum exists because excess is a
nonnegative integer and a zero-excess block of residue zero can be deleted from a
least-length corrector.  Appending copies of `P` realizes every larger length in
the same residue with the same reduced excess.  Conversely every schedule in
that residue has at least the selected excess.  Dividing by `L` gives the stated
formula. ∎

## 2. Finite residue oracle

### Theorem PP3ckk -- PROVED / REDUCED-COST RESIDUE GRAPH

The values `eta_r` and thresholds `N_r` are obtained by a finite shortest-path
problem on the residues `Z/LZ`.  Block `i` gives an arc

```text
s -> s+ell_i mod L
```

with lexicographic weight `(E_i,ell_i)`.  A least lexicographic path from zero to
`r` gives first the minimum reduced excess and then the least corrector length.
The stored predecessor arcs reconstruct an exact correction word.

#### Proof

Every concatenation projects to a residue walk and has the sum of its arc
weights.  Conversely every residue walk is a concatenation.  Nonnegative
lexicographic weights allow deletion of repeated residue cycles unless they
strictly improve the pair, which they cannot.  Hence a finite simple-path search
contains an optimum. ∎

## 3. Action-rate convergence

### Theorem PP3ckl -- PROVED / ALL-LENGTH DETERMINISTIC RATE CERTIFICATE

Let `u_P=a_P/L` be the action-rate vector of the critical block.  For residue
`r`, let the selected corrector have length `N_r` and action vector `A_r`.  The
schedule formed from that corrector and copies of `P` has

```text
||u(N)-u_P||_1 <= ||A_r-N_r u_P||_1/N.
```

Thus deterministic action rates converge with an explicit `O(1/N)` constant on
every attainable residue.

#### Proof

The critical copies contribute exactly their length times `u_P`; only the fixed
corrector contributes a discrepancy.  Divide that fixed discrepancy by total
length. ∎

## 4. Stored exact fixture

The audit `scripts/check_eventual_marker_quasipolynomial.py` uses a length-two
block of cost three and a critical length-three block of cost four.  It verifies
through length 300 that

```text
F(3k)   = 4k,
F(3k+1) = 4k+2  for k>=1,
F(3k+2) = 4k+3.
```

The reduced residue excesses are `0,2/3,1/3`, and the action-rate certificate has
`N` times the `l_1` error at most eight.

## 5. Prime-patching consequence

A finite marker catalogue no longer needs a separate construction for every
large side length.  One critical periodic block plus a finite residue graph gives
an exact eventual cost formula, a deterministic schedule, and an explicit
finite-length rate error on every attainable congruence class.
