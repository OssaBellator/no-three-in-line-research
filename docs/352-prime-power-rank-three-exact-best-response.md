# Exact rank-three best-response selectors collapse the raw exceptional set

Uniform response laws are useful for exact averaged certificates, but every raw host
has a finite response list. This chapter asks the sharper rank-three-only question:

> What is the smallest literal number of collinear response triples among the
> surviving perfect matchings?

For a canonical raw host `H`, define

\[
m_3(H)
=
\min_{Q\in\operatorname{PM}(H)}\psi_3(Q).
\]

Order response permutations lexicographically and let `Q_3^*(H)` be the first
minimizer.

This is a rank-three selector only. A complete operation also contains background,
rank-one, rank-two, return, selector and labelled child terms.

## 1. Exact minimum and deterministic selector

### Theorem CMR1990 -- PROVED

For every canonical raw host, `m_3(H)`, the number of minimizers, and
`Q_3^*(H)` are deterministic exact functions of its canonical response list.

### Proof

The response list is finite and nonempty. The integer function `psi_3` therefore has
a minimum. Lexicographic tie-breaking selects one unique first minimizer. ∎

The selector manifest stores the source catalogue record digest so the selected
response cannot silently migrate to another raw host.

## 2. Exact rank-three elimination criterion

### Theorem CMR1991 -- PROVED

A raw host admits a response containing no collinear response triple if and only if

\[
\boxed{m_3(H)=0.}
\]

When this holds, `Q_3^*(H)` is an explicit rank-three-free response.

### Proof

`m_3` is the minimum of the nonnegative integer triple counts. It is zero exactly
when at least one count is zero, and the selected minimizer attains it. ∎

This eliminates the literal rank-three response contribution, not necessarily the
complete offspring row.

## 3. Complete minimum distribution

### Theorem CMR1992 -- PROVED

Across all 740 raw hosts,

| `m_3` | 0 | 1 | 4 |
|---:|---:|---:|---:|
| hosts | 729 | 9 | 2 |

No other minimum occurs.

### Proof

Enumerate every response triple count in the canonical catalogue, take the hostwise
minimum and tabulate. ∎

Thus

\[
\boxed{729}
\]

raw hosts have an explicit rank-three-free response.

## 4. Side-five elimination

### Theorem CMR1993 -- PROVED

Every one of the 654 side-five raw hosts satisfies

\[
\boxed{m_3(H)=0.}
\]

Among side-four hosts, 75 have minimum zero and eleven have positive minimum.

### Proof

Tabulate the exact minima by side. ∎

This is stronger than the earlier statement that every side-five host with
denominator at least seventeen has strict uniform rank-three average: deterministic
rank-three elimination holds for all side-five denominator classes.

## 5. Strict, critical and excess hosts

### Theorem CMR1994 -- PROVED

The zero-minimum counts by uniform rank-three sign are

\[
\boxed{
651/651\text{ strict},\qquad
44/44\text{ critical},\qquad
34/45\text{ excess}.
}
\]

Consequently

\[
\boxed{78/89}
\]

critical or excess hosts admit an explicit zero-rank-three response.

### Proof

Link the selector records to the exact canonical slack classification and count by
sign. ∎

A critical or excess uniform average is therefore not, by itself, an obstruction to
rank-three-free deterministic response selection.

## 6. The exact eleven-host hard core

### Theorem CMR1995 -- PROVED

Exactly eleven raw hosts have `m_3(H)>0`. All are side-four excess hosts with

\[
\boxed{S_3=-3.}
\]

Nine have

\[
Z=2,\qquad
\operatorname{hist}(\psi_3)=\{1^1,4^1\},\qquad
m_3=1,
\]

and two have

\[
Z=1,\qquad
\operatorname{hist}(\psi_3)=\{4^1\},\qquad
m_3=4.
\]

The canonical host IDs are:

1. `s4-052ffa4a215a18a9`
2. `s4-0fbc34634d623179`
3. `s4-e40ff6c9796d9cf7`
4. `s4-108c0c435a2c6f4c`
5. `s4-135a89f2e544ae23`
6. `s4-0fa734ca1eb93499`
7. `s4-08b391f7108d0a76`
8. `s4-b61d66dda89f7836`
9. `s4-59ac56096a7f627f`
10. `s4-90525b9981c7d092`
11. `s4-cb701ee28781f0bb`

### Proof

Filter the exact 740-host selector table by positive minimum and inspect the linked
canonical records. The checker fixes both the count and ordered ID list. ∎

This is the exact raw rank-three selector obstruction set through side five.

## 7. Uniform and deterministic policies must remain distinct

### Theorem CMR1996 -- PROVED

The exact uniform quantities `A_3/Z` and the deterministic minimum `m_3` answer
different questions.

1. Uniform-response proofs may use `A_3/Z`.
2. A policy allowed to inspect the current raw host and select one response may use
   the explicit `Q_3^*`.
3. A deterministic selector cannot be substituted into a theorem whose transition
   law is fixed to be uniform without changing that theorem's policy assumptions.
4. Rank-three-free selection does not certify rank-one, rank-two, background,
   return, interface or labelled recurrent terms.

### Proof

The first two quantities are respectively an average over all responses and a
minimum attained by one response. They coincide only under additional conditions.
The remaining claims follow from the scope of the data included in the raw
rank-three selector. ∎

The selector is therefore a strong candidate operation rule and diagnostic, not a
silent rewrite of existing uniform certificates.

## 8. Executable endpoint

### Corollary CMR1997 -- PROVED

`scripts/check_prime_power_rank_three_exact_best_response.py` implements the complete
selector census.

It:

1. validates the canonical 740-host source;
2. recomputes every response triple count;
3. records the exact minimum and all minimizers;
4. publishes the lexicographically first minimizer;
5. verifies the 729/11 and side/sign-specific censuses;
6. fixes the exact eleven-host hard-core list;
7. writes and reloads deterministic selector manifests; and
8. rejects ten independently corrupted manifests.

The complete selector-manifest digest is

\[
\boxed{\texttt{32a20dd3772777fd6341b87f337ca5d0481d0b715e019fb11a7becd31de6e5b0}.}
\]

The next real-fibre computation should attempt the linked rank-three minimizer first,
then evaluate its actual background rank-one/rank-two loads and full labelled child
state. The eleven-host hard core requires correction or nontrivial routing even
before those additional terms are inserted.
