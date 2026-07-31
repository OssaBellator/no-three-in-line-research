# Independent microcensus before Hall lumpability

`docs/550` verifies exact lumpability for a six-state microscopic transition
system.  Its checker constructs that system from the desired quotient kernels.
This proves a valid lift theorem, but it does not show that an independently
defined geometric gadget has those transitions.  This chapter isolates the
missing evidence.

## 1. Quotient kernels do not determine microgeometry

### Theorem PP3coq -- PROVED / NONUNIQUENESS OF STRONGLY LUMPABLE LIFTS

For each nonnegative quotient entry `k`, both two-state blocks

```text
((ceil(k/2),floor(k/2)),(floor(k/2),ceil(k/2)))
```

and

```text
((k,0),(0,k))
```

have row and column sums `k`.  Replacing every quotient entry by either family
gives two distinct six-state, row-and-column-regular transition systems that are
strongly lumpable to the same three-state Hall kernel.

#### Proof

Every microscopic state in a source fibre sends total multiplicity `k` into the
target fibre, so the quotient entry is `k` independently of the internal block.
The column sums are also `k`, preserving regularity.  The two blocks differ for
positive `k`, hence the lifts are distinct. ∎

## 2. Circular-lift warning

### Theorem PP3cor -- PROVED / INDEPENDENT HALL CENSUS REQUIREMENT

A microscopic table generated from a prescribed quotient kernel cannot certify
that a geometric gadget realizes that kernel.  A realization certificate must
first define and enumerate microscopic states and transitions, and only then
test candidate syndrome partitions for lumpability.

#### Proof

By `PP3coq`, the same quotient has multiple incompatible microscopic lifts.
Constructing one lift from the quotient verifies algebraic consistency but does
not select the geometric one.  Independence of the census from the target
quotient is therefore necessary evidence. ∎

## 3. Exact failure witness contract

### Theorem PP3cos -- PROVED / LUMPABILITY SEARCH OR COUNTEREXAMPLE

Given an independently enumerated transition family and a candidate partition,
exact lumpability is decided by comparing, for every symbol, every pair of states
in one fibre, and every target fibre, their outgoing multiplicity sums.  Failure
has a finite witness `(symbol,state,state',target fibre)`.  The maximum normalized
difference is an exact approximate-lumpability defect when equality fails.

#### Proof

Strong lumpability is precisely equality of those finite sums.  A violated
comparison is a certificate of failure; the maximum violation exhausts all
comparisons and therefore gives the sharp defect for the fixed partition. ∎

## 4. Stored exact audit

The audit `scripts/check_hall_microcensus_independence.py` constructs balanced
and diagonal lifts of both stored quotient kernels.  They are distinct,
row-and-column-sum four, and strongly lumpable to the same quotients.  Every
binary switching word through length seven has identical aggregate evolution in
both lifts.

## 5. Prime-patching consequence

Hall mixing remains arithmetically certified once a quotient kernel is known.
The active frontier is now exactly the independent geometric state census and
partition search, with a required counterexample format if exact lumpability is
false.
