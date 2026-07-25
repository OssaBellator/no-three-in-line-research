# Dependency manifest and effective cutoff audit

PX450 reduces asymptotic exact doubling to a common cutoff and a dependency
audit.  The machine-readable graph is stored in

`proofs/product-entry-invariant-dependencies.json`.

The original audit isolated three numerical witnesses.  They are now supplied:

\[
A_3=320 \quad\text{(PX460)},
\]

\[
d_*(N)=1+\left\lceil\log_2(\log_2\max\{N,2\}+2)\right\rceil
\quad\text{(PX465)},
\]

and

\[
\mathfrak d(N)\le10^{27}N^{1/6}
\quad\text{(PX468)}.
\]

PX473 removes the optional growing packet-family parameter from the active path,
and PX478 gives the explicit common cutoff

\[
\boxed{N_0=10^{4000}}.
\]

## 1. Declared dependency graph

The continuation blocks are

\[
397\text{--}403,\ 404\text{--}410,\ 411\text{--}419,\
420\text{--}427,\ 428\text{--}436,\ 437\text{--}444,
\]

\[
445\text{--}450,\ 451\text{--}455,\ 456\text{--}460,
\ 461\text{--}465,\ 466\text{--}470,\ 471\text{--}473,
\ 474\text{--}478.
\]

### Theorem PX451 -- PROVED

The declared dependency graph is acyclic.  Every move-producing block on a path
to the asymptotic repair theorem has move-space tag

\[
\boxed{\texttt{rectangle_label}},
\]

and every remaining block is tagged `arithmetic_only`.

No terminal dependency uses the deleted individual-point batching theorem or the
obsolete inaccessible-PX63 premise.

### Proof

The block order in the JSON manifest is topological.  Every internal dependency
points to a block with smaller first theorem ID.  The only allowed move-space
tags are declared in the manifest safety rules. \(\square\)

## 2. Repository uniqueness and constant audit

### Theorem PX452 -- PROVED REDUCTION

The repository scanner verifies:

1. every theorem ID from PX397 through PX478 occurs in exactly one theorem
   heading;
2. the two continuation indexes contain exactly those IDs in order;
3. the paired support-four denominator is `32768`;
4. the entry good-bank cylinder factor is nine and destruction denominator is
   eighteen;
5. the rectangle point-type and label-family counts are four and two;
6. the Cartesian incidence constant is `320`;
7. the divisor witness is `10^27 N^(1/6)`;
8. the effective threshold is `N^(3/5)`;
9. the active packet-family count is zero;
10. the explicit cutoff is `10^4000`.

The uniqueness check prevents theorem-number reuse such as the deleted duplicate
PX356--PX361 draft.

## 3. Effective cutoff interface

For effective data \((A_3,\mathfrak d,d_*)\), let

\[
\Delta_*(N)=3+2d_*(N),
\qquad
T(N)=\lceil N^{3/5}\rceil,
\qquad
\eta=\frac1{12}.
\]

Use the corrected paired thinning probability

\[
q_\eta=
\min\left\{
\frac{\eta}{20{,}971{,}520e^{2\Delta_*}\log(2T)},
\frac{\eta T}{32768e^{4\Delta_*}N\mathfrak d(N)}
\right\}.
\]

### Theorem PX453 -- PROVED

The common-cutoff question reduces to finite decidable inequalities:

\[
q_\eta T
\ge
\max\{32,16\Delta_*+4,256e^{2\Delta_*}\},
\]

\[
N-1-2\Delta_*>0,
\]

and the explicit return inequalities of PX477.  The internal rank-three bounds
are already built into the first retained-order condition through the corrected
PX445 constants and \(A_3=320\).

If these inequalities hold for every \(N\ge N_0\), then \(N_0\) is a common
paired spread, divisor, internal-rank-three, terminal-transposition, and return
cutoff for the active PX445--PX450 path.

### Proof

The retained-order inequality supplies every matching-bank and constant-load
minimum.  The partner inequality supplies an allowed atomic terminal
transposition.  PX445--PX446 give the internal gap, PX470 gives the effective
return exponents, and PX473 removes any packet-count term. \(\square\)

## 4. Effectivity resolution

### Theorem PX454 -- PROVED REDUCTION

The formerly abstract cutoff is effective once three witnesses are supplied:

1. an explicit Cartesian incidence constant;
2. an effective divisor cap;
3. an exact nested-depth envelope.

PX460, PX465, and PX468 supply these witnesses.  Therefore every remaining
asymptotic inequality is a finite computable predicate.

### Proof

Substitute the three displayed witnesses into PX453.  All exponentials involve
the explicit logarithmic-logarithmic degree envelope, and every remaining term
is elementary in \(N\). \(\square\)

### Corollary PX455 -- PROVED REDUCTION, RESOLVED

The cutoff frontier isolated by the original audit is discharged as follows:

- PX460 gives \(A_3=320\);
- PX465 gives the exact depth formula;
- PX468 gives \(\mathfrak d(N)\le10^{27}N^{1/6}\);
- PX473 removes the growing packet-family parameter;
- PX478 certifies \(N_0=10^{4000}\).

The remaining exact frontier is no longer asymptotic effectivity.  It is the
finite range below \(10^{4000}\), together with a non-enumerative construction
or absorber that covers that range.

## 5. Verification

Run

```bash
python scripts/verify_product_entry_invariant_dependencies.py
python scripts/verify_product_explicit_cartesian_triples.py
python scripts/verify_product_explicit_nested_depth.py
python scripts/verify_product_explicit_divisor_witness.py
python scripts/verify_product_packet_family_free_path.py
python scripts/verify_product_explicit_common_cutoff.py
```

The repository scanner checks DAG acyclicity, theorem-ID uniqueness, paired-move
safety tags, constants, the two continuation indexes, and the PX478 cutoff root.
The arithmetic scripts verify each effective witness and the cutoff inequalities.
