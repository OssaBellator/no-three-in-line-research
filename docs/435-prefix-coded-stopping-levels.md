# Prefix-coded stopping levels for sequential marker repairs

`docs/429` allows different sources to stop at different safe marker depths when
the stopping level is intrinsically recoverable from the final target.  This
chapter removes that intrinsic-recoverability assumption: a short prefix-free
schedule code may be appended to the stopped repair word.

The statements are abstract action-graph facts.  The remaining geometric task
is to realize the code symbols by bounded-collateral moves.

## 1. Encoded stopping-level composition

Let the source set be partitioned into stopping classes `X_1,...,X_m`.  Class
`i` has a repair kernel with reverse load at most `lambda_i`.  Appending one
binary schedule symbol retains at least a fraction `p` of the currently valid
words, where `0<p<1`.  Give class `i` a binary prefix codeword of length
`ell_i`.

### Theorem PP3car -- PROVED / PREFIX-CODED STOPPING COMPOSITION

If the appended codeword is recoverable from the final target, then the
combined conditioned kernel has reverse load at most

```text
max_i lambda_i p^(-ell_i).
```

#### Proof

After `ell_i` schedule symbols, conditioning increases the class-`i` load by at
most `p^(-ell_i)`.  Prefix-freeness makes the stopping class uniquely decodable
from the target, so a target column receives predecessors from only one class.
Taking the largest class load proves the claim. ∎

Thus nonintrinsic stopping levels cost code length, not the number of stopping
levels.

## 2. Exact minimax feasibility

For a proposed risk `R`, put

```text
L_i(R)=floor(log_(1/p)(R/lambda_i)).
```

with `L_i(R)=-infinity` when `R<lambda_i/p`.  Equivalently, `L_i(R)` is the
largest positive integer `ell` for which

```text
lambda_i p^(-ell)<=R.
```

### Theorem PP3cas -- PROVED / STOPPING-LEVEL KRAFT TEST

There is a binary prefix code with risk at most `R` if and only if every
`L_i(R)>=1` and

```text
sum_i 2^(-L_i(R))<=1.
```

#### Proof

Any feasible code has `ell_i<=L_i(R)`, hence Kraft's inequality and monotonicity
of `2^(-ell)` give the displayed condition.  Conversely, lengths `L_i(R)`
satisfy Kraft's inequality, so the Kraft--McMillan theorem supplies a binary
prefix code with those lengths, and each class risk is at most `R`. ∎

## 3. Finite exact optimization

### Theorem PP3cat -- PROVED / FINITE STOPPING-RISK CANDIDATES

For `m>=2`, an optimal binary stopping code exists with every code length at
most `m-1`.  Consequently its optimal risk belongs to the finite set

```text
{lambda_i p^(-ell):1<=i<=m, 1<=ell<=m-1}.
```

#### Proof

Delete every unary internal vertex from an optimal prefix tree.  Along a
root-to-leaf path of depth `d`, each internal vertex then has a sibling subtree
containing a different leaf.  Hence the tree has at least `d+1` leaves and
`d<=m-1`.  The risk is the maximum of the finitely many class risks, so at an
optimum it equals one of them. ∎

This gives an exact finite search: sort the candidate risks and apply
`PP3cas`.

## 4. Revised boundary frontier

Stopping-depth ambiguity is now a coding problem.  A geometric audit may stop
each source at its first safe depth, measure the level loads, and ask only for
short recoverable schedule symbols.  Failure returns a finite Kraft overload
rather than an unstructured collision family.

## 5. Exact diagnostic

Run

```bash
python scripts/check_prefix_coded_stopping_levels.py
```

The script enumerates every binary length vector through the finite depth bound
for four stopping classes and verifies the exact optimum and Kraft decision.
