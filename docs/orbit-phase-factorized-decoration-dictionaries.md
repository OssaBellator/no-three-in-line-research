# Factorized physical-decoration dictionaries

**Branch:** `research/orbit-phase-expansion`

OP4aw--OP4az make zero-vector recurrence finite once the complete physical-decoration dictionary has size `K`. This note constructs such a dictionary from finite physical field alphabets and removes reconstructible fields from the independent state stock.

Let the complete decoration record have fields

\[
d=(d_1,\ldots,d_r),
\qquad d_i\in\mathcal D_i,
\qquad |\mathcal D_i|=K_i.
\]

The fields may represent owner, physical occurrence, scale, carry, legality, boundary, context, blocker or payment status. Let `mathcal D` be the subset of compatible tuples.

## OP4ba -- product dictionary bound -- PROVED

\[
\boxed{
|\mathcal D|
\le
\prod_{i=1}^r K_i.
}
\]

Consequently any deterministic zero-vector recurrence on these fields reaches its first repeated decoration within at most

\[
\boxed{\prod_{i=1}^r K_i}
\]

transitions.

### Proof

The compatible dictionary is a subset of the Cartesian product. Apply OP4aw with the displayed cardinality bound. QED.

## OP4bb -- reconstructible-field elimination -- PROVED

Suppose a subcollection of fields `d_j`, `j in R`, is uniquely reconstructible from the fixed quotient profile, the current physical board state and the remaining fields. Then those fields contribute no independent multiplicative factor:

\[
\boxed{
|\mathcal D|
\le
\prod_{i\notin R}K_i.
}
\]

### Proof

Projection onto the nonreconstructible coordinates is injective on compatible decorations: two decorations with the same projected tuple have the same reconstructed fields and hence are equal. QED.

## OP4bc -- polynomial stock criterion -- PROVED

If each nonreconstructible field has stock

\[
K_i\le C_i n^{a_i},
\]

then

\[
\boxed{
|\mathcal D|
\le
\left(\prod_iC_i\right)n^{\sum_i a_i}.
}
\]

Thus a constant number of polynomial physical dictionaries gives a polynomial zero-vector recurrence budget.

### Proof

Multiply the individual bounds and use OP4bb to omit reconstructible fields. QED.

## OP4bd -- least-field dictionary failure router -- PROVED

Fix an order on the declared fields. Every attempted decoration transition has one exact continuation:

1. the new tuple lies in the compatible product dictionary;
2. one least field leaves its declared alphabet;
3. one reconstruction rule is undefined or nonunique;
4. one compatibility relation between fields fails;
5. the transition map is nondeterministic after all declared fields are fixed.

Hence failure of the finite-profile contract is localized to one physical field or one compatibility relation, rather than an unstructured decoration reset.

## OP4be -- factorized zero-vector continuation -- PROVED

Under the factorized contract, every zero-vector history has:

1. at most `prod_{i notin R} K_i - 1` noninitial first-visit tickets;
2. an eventual physical cycle of length at most `prod_{i notin R}K_i`;
3. the OP4ay payment/debt/balanced-cycle continuation on that cycle;
4. or one least-field failure from OP4bd.

## Corrected OP5 frontier

The finite physical-decoration requirement is reduced to proving finite alphabets and reconstruction rules for the actual owner, occurrence, scale, carry, legality, boundary and context fields. Once those stocks are polynomial, zero-vector recurrence is polynomial. Remaining work is the physical score decomposition, payment of positive cycles, concentration of debt and justification of balanced-cycle tickets.

## Finite check

`scripts/verify_phase_factorized_decorations.py` enumerates small factor alphabets, compatible subsets and reconstructible coordinates, checking the product, projection-injectivity and recurrence bounds.