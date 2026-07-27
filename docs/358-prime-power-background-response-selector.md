# Exact background-dependent response selectors

The raw rank-three selector minimizes only `W_3(Q)`. Once a surviving background is
fixed, rank-one and rank-two triples can change the true best response. This chapter
uses the complete line-incidence kernel to compute the exact new-triple score of every
response and publishes the deterministic full selector.

Let `B` be an ordered finite background disjoint from the response grid and define

\[
N_B(Q)=W_1(Q;B)+W_2(Q;B)+W_3(Q).
\]

## 1. Exact response records

### Theorem CMR2038 -- PROVED

For every canonical host, background and response, the checker computes
`(W_1,W_2,W_3)` by literal collinearity. It independently recomputes `W_2` and `W_3`
from the response line-incidence kernel, and the two methods agree exactly.

### Proof

The literal enumeration follows the primitive rank definition. Kernel equality is
CMR2031--CMR2032. ∎

## 2. Post-response triple identity

### Theorem CMR2039 -- PROVED

For every response,

\[
\boxed{\Psi(B\cup Q)=\Psi(B)+N_B(Q).}
\]

### Proof

Partition every post-response triple by its number of response points. Rank zero is
exactly a background triple; ranks one, two and three sum to `N_B(Q)`. ∎

## 3. Independence of the minimizing response from removed prehistory

Suppose actual pre-response points `P` and removed set `R` satisfy `P\R=B`, and put

\[
T=|\mathcal D(P,R)|=\Psi(P)-\Psi(B).
\]

### Theorem CMR2040 -- PROVED

For every available response,

\[
\boxed{\Delta\Psi(Q)=N_B(Q)-T.}
\]

Consequently

\[
\boxed{\arg\min_Q\Delta\Psi(Q)=\arg\min_QN_B(Q).}
\]

The removed prehistory changes the sign threshold through `T`, but not the minimizing
response once `B` and the response family are fixed.

### Proof

Subtract `Psi(P)=Psi(B)+T` from CMR2039. The term `T` is independent of `Q`. ∎

## 4. Deterministic full selector

Order responses lexicographically by permutation. Define

\[
N_B^*=\min_QN_B(Q)
\]

and let `Q_B^*` be the first minimizer.

### Theorem CMR2041 -- PROVED

`Q_B^*`, `N_B^*`, and the number of minimizers are deterministic functions of the
canonical host and background. For any actual operation with destroyed count `T`,
`Q_B^*` strictly improves the real-triple potential exactly when

\[
\boxed{N_B^*<T.}
\]

### Proof

The response family is finite and every score is an exact integer. Apply CMR2040. ∎

## 5. Raw-selector penalty

Let `Q_3^*` be the canonical lexicographic minimizer of `W_3(Q)`. Define

\[
\pi_B=N_B(Q_3^*)-N_B^*.
\]

### Theorem CMR2042 -- PROVED

The penalty is an exact nonnegative integer. The raw rank-three selector has minimum
full score if and only if `pi_B=0`; it equals the deterministic full selector if and
only if it also wins the lexicographic tie-break.

### Proof

`N_B^*` is the minimum of the finite response scores and `Q_3^*` is one available
response. Equality characterizes membership in the minimizer set; lexicographic
equality gives the selected representative. ∎

### Corollary CMR2043 -- PROVED

A zero-rank-three raw response may still have positive selector penalty because of
rank-one or rank-two background triples. Therefore raw rank-three elimination cannot
be used as a complete background selector without this check.

## 6. Deterministic stress census

### Theorem CMR2044 -- PROVED

A deterministic 400-system regression containing 5,077 response records and 1,260
background points has:

- rank occurrence totals `(1782,4102,3603)`;
- 240 systems in which `Q_3^*` has minimum full score;
- 234 systems in which it is also the lexicographic full selector;
- 166 systems in which the selected response changes;
- 160 systems with strictly positive penalty;
- total penalty 239;
- penalty distribution `[[0,240],[1,107],[2,36],[3,9],[4,7],[5,1]]`.

### Proof

Generate the fixed pseudorandom host/background sequence with seed 2038 and run the
exact certificate on every system. ∎

These systems demonstrate certificate completeness and genuine selector instability.
They do not estimate the distribution on the still-unpopulated real owner/provenance
fibres.

## 7. Executable endpoint

### Corollary CMR2045 -- PROVED

`scripts/check_prime_power_background_response_selector.py` validates one arbitrary
canonical host/background certificate, checks direct/kernel agreement response by
response, publishes the exact full selector and raw-selector penalty, runs the fixed
400-system regression, and rejects twelve independent corruptions.

The remaining operation-specific datum required for strict improvement is the true
destroyed-current-triple count `T`, together with proof that the supplied background
is the actual survivor set.
