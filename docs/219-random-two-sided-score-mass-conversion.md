# Random two-sided score failure converts to target-size source structure

The remaining numerical initial-allocation frontier after PP3alc--PP3alt is a
nontrivial movement ownership Hall bottleneck or a defect score truncated at
`T` without a genuinely dead row.  The random two-sided local Ore theorem
PP3nb--PP3nd bypasses both ownership issues.

Once every movement and refill fibre has a fixed controller margin, failure of
the random two-sided score condition forces one normalized row or column score
to have order `T`.  Its numerator then has order `RT`.  That numerator is the
sum of exactly two terms already converted in PP3ali--PP3alq:

- a fixed-label same-slot anchor row or column;
- a fixed-macro movement or refill controller-defect mass.

Thus the initial controller-aware allocation problem is conditionally closed by
one random two-sided test.  The remaining conditions are geometric conversion
and source-valid-host interfaces, not ownership arithmetic.

## 1. Uniform denominator regime

Use the controller-defect scores

```text
rho_i(A)
=
min{T,(B_i+U_i(A))/((1-gamma)R-a_i(A))},

chi_i(B)
=
min{T,(A_i+V_i(B))/((1-gamma)R-b_i(B))}.
```

Assume that for one fixed `delta>0`,

```text
a_i(A)<=(1-gamma-delta)R,
b_i(B)<=(1-gamma-delta)R
```

for every macro and numerical label.  PP3alh shows that failure of this regime
already yields a target-size source star or credited endpoint bank.

### Proposition PP3alu -- PROVED

Under the uniform margin assumption,

```text
rho_i(A)>=s
```

implies

```text
B_i+U_i(A)>=delta R s,
```

and

```text
chi_i(B)>=s
```

implies

```text
A_i+V_i(B)>=delta R s.
```

The statement remains valid when the score is truncated at `T`.

#### Proof

Every movement denominator is at least `delta R`.  If the untruncated ratio is
below `T`, multiply the score inequality by the denominator.  If the score is
`T`, the untruncated ratio is at least `T`, so the same argument applies.  The
refill statement is transposed. ∎

Hence score truncation itself is a mass certificate once denominator collapse
has been excluded.

## 2. Complementary score failure

Let `h` be the random two-sided slack from PP3nc:

```text
h=2T sqrt(log(4MT)/W)=o(T).
```

### Theorem PP3alv -- PROVED

Suppose the uniform denominator regime holds and there is an incompatible triple
`(i,A,B)` satisfying

```text
rho_i(A)+chi_i(B)>T-h.
```

Then at least one of the following four masses is larger than

```text
delta R(T-h)/4:
```

1. `B_i`, the fixed-macro refill controller-defect mass;
2. `U_i(A)`, the fixed movement-label anchor-row mass;
3. `A_i`, the fixed-macro movement controller-defect mass;
4. `V_i(B)`, the fixed refill-label anchor-column mass.

#### Proof

One of `rho_i(A),chi_i(B)` is larger than `(T-h)/2`.  Proposition PP3alu gives
that the corresponding numerator is larger than `delta R(T-h)/2`.  One of its
two summands is therefore larger than `delta R(T-h)/4`. ∎

For sufficiently large `m`, `h<T/2`.  Every mass in the theorem is then at least
`delta RT/8`.

## 3. Conversion of every large score

### Theorem PP3alw -- PROVED / CONDITIONAL CONVERSION INTERFACE

At the slab-optimal scales, a complementary score failure from PP3alv has one of
the following outcomes.

1. A fixed-label anchor row or column of mass `Omega(RT)`, hence a target-size
   source star or endpoint-disjoint anchor bank by PP3ali--PP3all.
2. A fixed-macro movement or refill controller-defect core of mass `Omega(RT)`,
   hence a target-size blocker star or full resource bank by the transposed form
   of PP3alo--PP3alq.
3. A strict paid controller-shadow improvement.
4. Robust final-state direct completion.
5. A positive-density ambient unary, rank-three, or rank-four foreign support
   core.
6. An explicit source, transition, anchor, Hall, alternating,
   distinguished-endpoint, or endpoint-host obstruction.
7. Controller-puncture reserve exhaustion or failure of the initial robust
   certificate.

#### Proof

Apply PP3alv.  Convert anchor masses with PP3ali--PP3all.  Convert macro-total
controller-defect masses with PP3alo--PP3alq and its movement/refill transpose.
Those theorems feed the marked-star, recapture-free, ambient-support, and final-
state allocation chains. ∎

The scale is much stronger than necessary on the anchor side: PP3alk needs only
`Omega(R)` fixed-label anchor mass, while PP3alv supplies `Omega(RT)`.

## 4. Initial random two-sided closure

### Theorem PP3alx -- PROVED / CONDITIONAL COMBINED CONVERSION INTERFACE

Assume the slab-optimal architecture and apply the explicit random two-sided
slack `h` from PP3nc.  Then the initial controller-aware allocation has exactly
one of the following outcomes.

1. Some movement or refill fibre lacks a fixed positive controller margin, and
   PP3alc--PP3alh supplies a target star or fixed-label resource bank.
2. Every fibre has a fixed positive margin and every incompatible triple obeys

   ```text
   rho_i(A)+chi_i(B)<=T-h.
   ```

   Then PP3nd gives balanced two-sided ownership, local Ore matchings in every
   macro, and the full prime-gap-scale patch.
3. The score condition fails, and PP3alw converts its `Omega(RT)` numerator mass.

#### Proof

Use PP3alh to split off denominator collapse.  In the uniform denominator branch,
apply PP3nd.  Its success gives item 2; its failure gives an incompatible triple
as in PP3alv and hence item 3. ∎

This theorem does not require solving the one-sided ownership Hall problem.  A
nontrivial Hall bottleneck, capped refill concentration, or score truncation may
exist, but the independent random two-sided allocation either bypasses it or
forces converted mass.

## 5. Consequences for the old numerical frontiers

### Corollary PP3aly -- PROVED

Under the conversion interfaces already recorded through PP3alq, none of the
following is an independent initial numerical obstruction:

1. a movement ownership Hall bottleneck at a threshold below `T`;
2. the extreme true bottleneck `r_own=T`;
3. score truncation `rho_i(A)=T` or `chi_i(B)=T` without a dead true row;
4. capped fixed-label anchor concentration;
5. a pair of moderate complementary defect scores;
6. globally vanishing blocker density with one collapsed label.

Every such branch either completes through PP3nd or enters a target-size
star/bank conversion.

### Corollary PP3alz -- PROVED

The remaining initial-allocation frontier is geometric rather than numerical:

1. uniformly preparing the marked or endpoint-bank source-valid hosts produced
   by the conversion theorems;
2. converting the ambient unary/rank-three/rank-four support cores;
3. controlling controller-puncture reserve exhaustion;
4. branches requiring one-step monotone potential descent instead of robust
   final allocation;
5. branches that cannot use the slab-optimal random two-sided architecture.

The no-three-in-line conjecture remains unproved.
