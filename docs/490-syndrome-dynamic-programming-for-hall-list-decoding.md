# Syndrome dynamic programming for Hall list decoding

`docs/484` filters Cartesian products of inner marker lists through an outer
Hall-color code.  Exhausting every outer color is unnecessary when the outer
code is linear.  This chapter replaces color scanning by an exact syndrome
dynamic program.

Let `C subset F_q^n` be a linear outer color code with parity-check matrix
`H` of rank `r`.  At coordinate `j`, the inner geometric decoder returns a
symbol list `L_j subset F_q`.

## 1. Exact syndrome recurrence

### Theorem PP3cha -- PROVED / SYNDROME LIST COUNT

For a partial coordinate set `0,...,i-1`, let `D_i(s)` be the number of partial
words choosing `x_j in L_j` whose partial syndrome is `s in F_q^r`.  Then

```text
D_0(0)=1,
D_0(s)=0 for s!=0,
D_(i+1)(s)=sum_(x in L_i) D_i(s-H_i x).
```

The exact number of outer Hall colors compatible with all block lists is
`D_n(0)`.

#### Proof

Every partial assignment has one syndrome.  Appending symbol `x` adds column
`H_i x`; grouping assignments by their new syndrome gives the recurrence.
A full word belongs to `C` exactly when its syndrome is zero. ∎

## 2. Complexity and reconstruction

### Theorem PP3chb -- PROVED / FINITE SYNDROME DECODER

The recurrence uses at most `q^r` syndrome states per coordinate and

```text
O(n q^r max_j |L_j|)
```

field-state transitions.  Storing one predecessor for every nonzero table entry
reconstructs a compatible Hall color whenever `D_n(0)>0`.

If `I` is an information set of `C`, then

```text
D_n(0) <= product_(j in I) |L_j|.
```

#### Proof

The transition count is immediate from the table dimensions.  Backtracking
predecessors reverses the recurrence.  Projection of a codeword onto an
information set is injective, so each compatible codeword gives a distinct
tuple in the listed Cartesian product. ∎

## 3. Reverse-load certificate

### Theorem PP3chc -- PROVED / SYNDROME-CONTROLLED HALL LOAD

If the syndrome recurrence returns list size `L`, and every surviving color
class contributes reverse load at most `1/d`, then the observed Hall target has
load at most

```text
L/d.
```

The complete DP table is a finite certificate.  Failure returns one coordinate
list, one syndrome transition, or one reconstructed excess color.

#### Proof

Exactly `L` outer color classes survive, by `PP3cha`.  Summing their individual
loads gives `L/d`.  Every claimed count and predecessor is a finite field
identity. ∎

## 4. Stored exact fixture

The audit `scripts/check_syndrome_hall_list_decoding.py` uses the `[4,2,3]`
Reed--Solomon evaluation code over `F_5`.  Its syndrome state space has size
`25`, equal to the number of outer colors but independent of the list-product
size.

Each coordinate list is a singleton or pair.  Across all `15^4=50,625`
observations, the syndrome count agrees with direct filtering.  The exact list
distribution is

```text
0 colors: 36,100 observations
1 color : 13,425 observations
2 colors:  1,100 observations.
```

The sharp size-two witness has list sizes `(1,2,2,2)`.

## 5. Prime-patching consequence

Hall-color list decoding now scales with syndrome space rather than with the
number of possible geometric list combinations.  The output is an exact color
count, a reconstructed color, or a concrete syndrome witness for residual
ambiguity.
