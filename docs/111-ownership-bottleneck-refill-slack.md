# Ownership bottleneck versus refill slack

The exceptional-label theorem PP3mh depends on a chosen threshold \(r\). This
chapter removes that arbitrary parameter. The movement side has a bottleneck
balanced-assignment cost, while the refill side has an exact cumulative slack.
Their comparison is a deterministic completion criterion.

## 1. Refill slack identity

For refill label \(B\), recall

\[
S_B=\sum_i\min\{W,\overline e_i(B)\}.
\]

Define its cumulative refill slack by

\[
\Lambda(B)
=
\sum_{i=1}^M
\bigl(W-\overline e_i(B)\bigr)_+,
\]

where \((x)_+=\max\{x,0\}\).

### Proposition PP3mv -- PROVED

For every refill label,

\[
\boxed{S_B=T-\Lambda(B).}
\]

Consequently the PP3mh refill inequality

\[
r+S_B\le T
\]

is equivalent to

\[
\boxed{r\le\Lambda(B).}
\]

#### Proof

For every macro,

\[
\min\{W,\overline e_i(B)\}
=
W-\bigl(W-\overline e_i(B)\bigr)_+.
\]

Sum over \(i\) and use \(MW=T\). ∎

A macro contributes refill slack only when \(B\) has fewer than \(W\)
nonneighbors there. Very bad macro columns are automatically capped and
contribute zero rather than an unbounded penalty.

## 2. Movement ownership bottleneck

Define

\[
r_{\rm own}
=
\min_{\sigma}
\max_A\overline d_{\sigma(A)}(A),
\]

where the minimum is over balanced ownership maps assigning exactly \(W\)
movement labels to every macro.

Also put

\[
\Lambda_*
=
\min_B\Lambda(B).
\]

### Theorem PP3mw -- PROVED

If

\[
\boxed{r_{\rm own}\le\Lambda_*,}
\]

then a saturation-compatible global label matching exists. For the
controller-aware graphs, the full prime-gap-scale patch follows from PP3hq.

#### Proof

Choose a balanced ownership attaining \(r_{\rm own}\). Apply PP3mh with
\(r=r_{\rm own}\). Proposition PP3mv gives, for every refill label,

\[
r+S_B
=
r+T-\Lambda(B)
\le
T.
\]

Therefore the global ownership graph has a perfect matching. ∎

This is a one-number comparison between the two label sides. Sparse exceptional
movement rows are handled by the bottleneck assignment, while sparse exceptional
refill columns are discounted by the positive-part slack.

## 3. Defect-score criterion

Use the upper bounds

\[
\overline d_i(A)\le\rho_i(A),
\qquad
\overline e_i(B)\le\chi_i(B)
\]

from PP3ly. Define

\[
r_{\rm score}
=
\min_{\sigma}
\max_A\rho_{\sigma(A)}(A)
\]

over balanced ownerships, and

\[
\Lambda_{\rm score}(B)
=
\sum_i\bigl(W-\chi_i(B)\bigr)_+,
\qquad
\Lambda_{\rm score,*}
=
\min_B\Lambda_{\rm score}(B).
\]

### Corollary PP3mx -- PROVED

If

\[
\boxed{r_{\rm score}\le\Lambda_{\rm score,*},}
\]

then the controller-aware global allocation and full patch exist.

#### Proof

The true movement bottleneck is at most \(r_{\rm score}\). Since
\(\overline e_i(B)\le\chi_i(B)\),

\[
\bigl(W-\overline e_i(B)\bigr)_+
\ge
\bigl(W-\chi_i(B)\bigr)_+,
\]

so \(\Lambda_*\ge\Lambda_{\rm score,*}\). Apply PP3mw. ∎

## 4. Exact Hall characterization of the bottleneck

For threshold \(r\), let

\[
N_r(X)
=
\{i:\exists A\in X\text{ with }\overline d_i(A)\le r\}.
\]

### Proposition PP3my -- PROVED

The bottleneck value \(r_{\rm own}\) is the least threshold \(r\) for which

\[
\boxed{W|N_r(X)|\ge|X|}
\]

for every movement-label set \(X\).

#### Proof

At threshold \(r\), a balanced ownership with maximum row nondegree at most
\(r\) exists exactly when the threshold ownership host has a perfect matching.
Apply PP3mm. Taking the least feasible threshold gives the statement. ∎

Thus \(r_{\rm own}\) can be computed by sorting the finitely many row
nondegrees and running one capacitated matching test at each candidate threshold.

## 5. Exact failure core at the refill scale

### Corollary PP3mz -- PROVED

If the bottleneck-slack criterion fails, so

\[
r_{\rm own}>\Lambda_*,
\]

choose a refill label \(B_*\) with
\(\Lambda(B_*)=\Lambda_*\). At threshold \(r=\Lambda_*\), there is a Hall set
\(X\) satisfying

\[
W|N_r(X)|<|X|.
\]

Consequently, with

\[
Y=[M]\setminus N_r(X),
\]

one has

\[
\boxed{
\overline d_i(A)>\Lambda_*
\qquad(A,i)\in X\times Y,
}
\]

while the refill label \(B_*\) has only

\[
\boxed{
\sum_i\bigl(W-\overline e_i(B_*)\bigr)_+
=
\Lambda_*
}
\]

units of cumulative local slack.

#### Proof

Threshold \(\Lambda_*\) is below the least feasible ownership threshold, so
PP3my supplies a Hall-deficient set. Its complement rectangle is entirely above
the threshold by definition. The refill identity is the choice of \(B_*\). ∎

The remaining one-sided numerical obstruction is therefore an exact paired core:
a movement-label Hall rectangle whose row nondegrees all exceed the total local
slack of one refill label. This is sharper than either a movement concentration
or refill concentration considered separately.