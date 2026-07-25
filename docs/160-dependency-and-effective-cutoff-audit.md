# Dependency manifest and effective cutoff audit

PX450 reduces asymptotic exact doubling to a common cutoff and a dependency
audit. The machine-readable graph is stored in

`proofs/product-entry-invariant-dependencies.json`.

The dependency path is now audited through PX492. Every move-producing block is
tagged `rectangle_label`; every other block is `arithmetic_only`. The current
root is the rational-divisor cutoff

\[
\boxed{N_3=10^{2900}}.
\]

## 1. Declared dependency graph

### Theorem PX451 -- PROVED

The declared dependency graph is acyclic. Every move-producing block on a path
to the active root has move-space tag

\[
\boxed{\texttt{rectangle_label}},
\]

and every remaining block is tagged `arithmetic_only`.

No terminal dependency uses the deleted individual-point batching theorem or
the obsolete inaccessible-PX63 premise.

### Proof

The JSON block order is topological: each internal dependency has smaller first
theorem ID. The manifest lists the only permitted move-space tags. \(\square\)

## 2. Repository uniqueness and constant audit

### Theorem PX452 -- PROVED REDUCTION

The repository scanner verifies:

1. every theorem ID from PX397 through PX492 occurs in exactly one theorem
   heading;
2. the continuation indexes contain exactly those IDs in order;
3. the paired support-four denominator is `32768`;
4. the entry good-bank cylinder factor is nine and the destruction denominator
   is eighteen;
5. the Cartesian incidence constant is `A_3=320`;
6. the active divisor witness is
   `mathfrak d(N)<=10^59 N^(16/109)`;
7. the active packet-family count is zero;
8. the active cutoff is `10^2900`.

The uniqueness check prevents theorem-number reuse such as the deleted duplicate
PX356--PX361 draft.

## 3. Effective cutoff interface

Let

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

and the explicit four-return and two-variable-return inequalities.

If these hold for every \(N\ge N_0\), then \(N_0\) is a common paired spread,
divisor, internal-rank-three, terminal-transposition, and return cutoff for the
active PX445--PX450 path.

### Proof

The retained-order inequality supplies every matching-bank minimum and the
internal rank-three margin. The partner inequality supplies an allowed atomic
terminal transposition. PX470 supplies the effective return exponents, while
PX473 removes any packet-count term. \(\square\)

## 4. Effectivity resolution

### Theorem PX454 -- PROVED REDUCTION

The formerly abstract cutoff becomes effective once three witnesses are
supplied:

1. an explicit Cartesian incidence constant;
2. an effective divisor cap;
3. an exact nested-depth envelope.

PX460 and PX465 supply the first and third witnesses. PX468 supplied the first
effective divisor cap; PX485 and PX490 subsequently improved it.

### Corollary PX455 -- PROVED REDUCTION, RESOLVED

The original cutoff frontier is discharged by the chain

\[
\text{PX478}:10^{4000},
\qquad
\text{PX482}:10^{3650},
\qquad
\text{PX487}:10^{2950},
\qquad
\text{PX492}:10^{2900}.
\]

The active numerical data are

\[
A_3=320,
\]

\[
d_*(N)=1+\left\lceil\log_2(\log_2\max\{N,2\}+2)\right\rceil,
\]

\[
\mathfrak d(N)\le10^{59}N^{16/109}.
\]

The remaining exact frontier is not asymptotic effectivity. It is the finite
range below \(10^{2900}\), requiring a structural bridge or interval-specific
maximal-divisor theorem.

## 5. Verification

Run

```bash
python scripts/verify_product_entry_invariant_dependencies.py
python scripts/verify_product_explicit_cartesian_triples.py
python scripts/verify_product_explicit_nested_depth.py
python scripts/verify_product_packet_family_free_path.py
python scripts/verify_product_explicit_common_cutoff.py
python scripts/verify_product_compressed_common_cutoff.py
python scripts/verify_product_fourteenth_divisor_cutoff.py
python scripts/verify_product_rational_divisor_cutoff.py
```

The scanner checks DAG acyclicity, theorem-ID uniqueness, move-space tags,
constants, continuation indexes, and the PX492 cutoff root.
