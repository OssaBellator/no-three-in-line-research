# Arithmetic localization of batched heavy-peel outputs

**Branch:** `research/sparse-algebraic-spread`

SAS5dm--SAS5dq show that a complete nonimproving heavy-record peel returns one quantitatively heavy original repair word, donor repair-word class, designated divisor-scale family or positive-curvature class.  This note runs the existing rational-address machinery on those batched outputs.

The original repair word already has one fixed physical swap.  A donor repair class is spread over an endpoint-disjoint donor family, so one donor is first selected by weighted pigeonhole.  A positive-curvature class is spread over physical donor endpoints, so one original-donor endpoint pair is selected before applying the same third-column reconstruction used for negative curvature.

## Previous quantitative outputs

Put

`K_0=24*binom(N,3)*(N-2)^2`

and let `Omega_peel>0` be the total active-record weight removed by a complete nonimproving peel.

SAS5dp gives at least one of:

1. an original-swap repair word of weight

   `W_O>=Omega_peel/(192*K_0)`;
2. a donor repair-word type with distinct exact-record union weight

   `W_D>=Omega_peel/6912`;
3. designated repaired divisor-scale mass

   `W_L>=Omega_peel/16`;
4. a positive-curvature orientation/endpoint-pair/scope-type class with distinct exact-record union weight

   `W_P>=Omega_peel/18432`;
5. an improving composed move.

The repair word in alternatives 1 and 2 is one fixed member of the twelve-word dictionary from SAS5j.  It is therefore either double-scope or singleton-scope.

## SAS5dr -- original repair-word arithmetic localization -- PROVED

Suppose alternative 1 occurs.

If the selected original repair word is double-scope, one exact primitive parallel-line class carries weight at least

`W_O/[N(N-1)]`

and hence at least

`Omega_peel/[192*K_0*N(N-1)]`.

If the selected word is singleton-scope, one exact row-triple dilation family carries weight at least

`W_O/[4N(N-1)^3]`

and hence at least

`Omega_peel/[768*K_0*N(N-1)^3]`.

### Proof

The original swap is fixed throughout the peel.  Apply SAS5p to a double-scope word and SAS5s to a singleton-scope word.  Substitute the lower bound for `W_O`. QED.

Thus the global original-word branch reaches one one-parameter primitive progression or dilation family without another swap-selection loss.

## Donor-bank size

The donor swaps are pairwise endpoint-disjoint and avoid the two original swap columns.  Therefore their number satisfies

`m_don<=floor((N-2)/2)`.

When an exact record in the distinct donor-word union can be repaired by more than one selected donor, assign it canonically to the least donor in the fixed donor order.  This preserves the total distinct union weight and places every record in exactly one donor fibre.

## SAS5ds -- donor repair-word arithmetic localization -- PROVED

Suppose alternative 2 occurs.  One physical donor swap receives assigned exact-record weight at least

`W_D/m_don>=2W_D/(N-2)`.

For that donor:

1. if the fixed repair word is double-scope, one exact primitive parallel-line class carries weight at least

   `2W_D/[(N-2)N(N-1)]`

   and therefore at least

   `Omega_peel/[3456*(N-2)N(N-1)]`;
2. if the fixed repair word is singleton-scope, one exact row-triple dilation family carries weight at least

   `W_D/[2(N-2)N(N-1)^3]`

   and therefore at least

   `Omega_peel/[13824*(N-2)N(N-1)^3]`.

### Proof

Canonical assignment partitions the distinct union among at most `m_don` donor swaps.  Weighted pigeonhole gives one donor of weight at least `W_D/m_don`, and the endpoint-disjoint bound gives `1/m_don>=2/(N-2)`.  Apply SAS5p or SAS5s inside the selected fixed donor swap and substitute `W_D>=Omega_peel/6912`. QED.

The bounded-reuse gain from SAS5dp is retained: only the unavoidable endpoint-disjoint donor-selection factor is introduced.

## Positive-curvature geometry

Fix the positive-curvature class from alternative 4.  Its orientation is current-only or composed-only; its canonical endpoint-pair role chooses one original swap endpoint and one donor endpoint; and its third-column type is:

1. outside all four swap endpoints;
2. the mate of the selected original endpoint;
3. the mate of the selected donor endpoint.

The original endpoint is one of the two globally fixed original columns.  Canonically assign each distinct record to the least donor occurrence that realizes the selected positive class.  There are at most `N-2` possible physical donor endpoint partners.

## SAS5dt -- positive-curvature fixed-pair and third-column localization -- PROVED

One exact physical original-donor endpoint pair receives positive record weight at least

`W_P/(N-2)`.

For either mate type, the third scope column is already fixed, so one fixed-third-column fibre carries weight at least

`W_P/(N-2)>=Omega_peel/[18432*(N-2)]`.

For the outside-endpoint type, one primitive row-ratio reconstruction address carries weight at least

`W_P/[24*(N-2)(N-1)^2]`

and all records in that address have one exact third column.  Quantitatively this is at least

`Omega_peel/[442368*(N-2)(N-1)^2]`.

### Proof

Canonical assignment partitions the distinct positive union over at most `N-2` physical donor endpoint partners, giving the fixed-pair bound.  The mate types have a named third column by the same transposition argument as SAS5bz.

In the outside type, once the two physical endpoint columns are fixed, collinearity is exactly the equation from SAS5bx.  Its proof does not depend on the sign of mixed curvature.  The safe primitive row-ratio address stock is `24(N-1)^2` by SAS5by, so SAS5ca's weighted localization applies verbatim.  Substitute `W_P>=Omega_peel/18432`. QED.

This extends the exact third-column reconstruction from negative to positive cross curvature.

## SAS5du -- complete arithmetically localized peel router -- PROVED

A complete heavy-record peel has at least one of the following outputs:

1. an improving composed move;
2. an original double-scope primitive line of weight at least

   `Omega_peel/[192*K_0*N(N-1)]`;
3. an original singleton exact dilation family of weight at least

   `Omega_peel/[768*K_0*N(N-1)^3]`;
4. a donor double-scope primitive line of weight at least

   `Omega_peel/[3456*(N-2)N(N-1)]`;
5. a donor singleton exact dilation family of weight at least

   `Omega_peel/[13824*(N-2)N(N-1)^3]`;
6. designated repaired divisor-scale mass at least

   `Omega_peel/16`;
7. a positive mate-type fixed-third-column fibre of weight at least

   `Omega_peel/[18432*(N-2)]`;
8. a positive outside-type exact-third-column reconstruction fibre of weight at least

   `Omega_peel/[442368*(N-2)(N-1)^2]`.

### Proof

Apply SAS5dp.  Alternatives 1, 2 and 4 are refined by SAS5dr, SAS5ds and SAS5dt.  The designated-scale and improving branches are unchanged.  Double- and singleton-scope repair words are exhaustive by SAS5j.  The three positive third-column types are exhaustive by SAS5di and the scope-type dictionary used in SAS5bv. QED.

None of the batched outputs now ends at a free geometric column pair.

## SAS5dv -- arithmetic continuation interface -- PROVED AS AN INTERFACE

The outputs of SAS5du enter the following existing exact structures:

- primitive parallel lines use the reduced-denominator and progression parameters of SAS5m--SAS5p;
- singleton dilation families use the primitive two-gap model of SAS5q--SAS5s;
- designated scale enters the saturated divisor-progression machinery of SAS5bi--SAS5br;
- positive fixed-third-column fibres retain one current-only or composed-only orientation and can be split next by row scale, base row and required-label vector exactly as in SAS5cc--SAS5cg;
- an improving move lowers the nonnegative integer energy.

Therefore the remaining SAS6 task is no longer to localize the batched output arithmetically.  It is to batch compatible parameter values inside one selected progression, dilation or fixed-third-column class, or to classify the resulting recurrent parameter set.

### Proof

The first three entries are the definitions of the cited arithmetic dictionaries.  SAS5dt supplies the positive exact third column; the row-scale/base-row/label split is independent of curvature sign once the physical scope is fixed.  The final entry is the energy interpretation of a negative composed increment. QED.

## Corrected SAS6 frontier

The complete heavy-record branch now terminates in an actual descent or one quantitatively heavy one-parameter arithmetic family:

- an original or donor primitive parallel line;
- an original or donor primitive dilation;
- a designated divisor scale;
- or a positive fixed-third-column class.

The live tasks are to compare or batch their integer parameters, exploit the designated scale against the coprime donor-saturated progression, and handle the remaining high-incidence and reflected-board boundary profiles.

## Finite check

`scripts/verify_sparse_batched_output_arithmetic_localization.py` exhausts the two-fixed-column third-column equation on small boards and samples weighted batched-output systems.  It checks donor-bank and endpoint-partner pigeonhole bounds, the double/single arithmetic stocks and every constant in SAS5dr--SAS5du.