# Sparse meet-in-the-middle syndrome trellises for Hall tags

`docs/490` counts Hall-color lists by a full syndrome dynamic program.  When
coordinate lists are small, most syndrome states are unreachable.  This chapter
keeps only reachable syndromes and splits the coordinates into two halves, so an
exact decoder can be much smaller than the ambient `q^r` table.

Let a linear outer tag have parity-check matrix `H` over `F_q`.  Coordinate `j`
returns a finite symbol list `L_j`.  A compatible tag is a word in
`product_j L_j` with syndrome zero.

## 1. Sparse syndrome recurrence

### Theorem PP3chs -- PROVED / REACHABLE-SYNDROME TRELLIS

For a coordinate set `J`, define

```text
F_J(s)=#{x in product_(j in J) L_j : H_J x=s}.
```

Starting from `F_empty(0)=1`, adjoining coordinate `j` updates by

```text
F_(J union {j})(s)=sum_(a in L_j) F_J(s-a H_j).
```

Storing only nonzero entries computes the exact count using only reachable
syndromes.  One predecessor per nonzero state reconstructs a compatible partial
word.

#### Proof

Partition assignments by their final coordinate value.  Syndrome addition is
linear, so the displayed recurrence is exact.  Zero-count states never
contribute later and may be omitted.  A stored predecessor reverses one valid
transition at each coordinate. ∎

## 2. Meet-in-the-middle convolution

### Theorem PP3cht -- PROVED / COMPLEMENTARY-SYNDROME JOIN

For a partition `J=A disjoint union B`, the number of compatible outer tags is

```text
L=sum_s F_A(s) F_B(-s).
```

The sum may be taken only over the smaller sparse support.  If `L>0`, a matching
pair of stored half-witnesses reconstructs one complete Hall color.

#### Proof

A complete word has zero syndrome exactly when the two half syndromes are
opposites.  Every complete assignment has a unique pair of half assignments, so
the product counts and sum neither omit nor duplicate a word. ∎

## 3. Exact reverse-load certificate

### Theorem PP3chu -- PROVED / SPARSE LIST-LOAD AUDIT

If the complementary-syndrome join returns list size `L`, uniform choice among
at least `d` residual Hall actions has reverse load at most `L/d`.  A claimed
bound is audited by the two sparse maps and their join; failure returns a
specific nonzero syndrome count, mismatched witness, or observation with an
excessive list.

#### Proof

At most `L` outer color classes contribute to the observed target and each has
load at most `1/d`.  The trellis and join identities give an exact finite count,
so any failed equality is already a concrete local witness. ∎

## 4. Stored exact fixture

The audit `scripts/check_sparse_mitm_hall_syndromes.py` uses the `[5,2,4]`
Reed--Solomon evaluation code

```text
c_i=a+i b over F_5.
```

Every coordinate list is a cyclic adjacent pair.  All `5^5=3,125`
observations are checked against direct codeword scanning.  The list histogram
is

```text
0:2350, 1:750, 2:25.
```

The two-coordinate half has at most four reachable syndromes and the
three-coordinate half at most eight, versus `5^3=125` ambient syndrome states.
The sharp Hall-color list size is two.

## 5. Prime-patching consequence

Hall privacy can now be certified from small reachable syndrome sets rather than
from every color or every ambient syndrome.  The method is exact, reconstructive,
and especially effective when geometric marker blocks return short symbol lists.
