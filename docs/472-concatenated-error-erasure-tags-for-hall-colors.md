# Concatenated error--erasure tags for Hall colors

`docs/466` gives Singleton-optimal Reed--Solomon tags over one marker alphabet.
A geometric implementation may realize each field symbol through a shorter
inner marker word.  This chapter proves that outer Hall-color protection and
inner marker protection compose exactly.

Let `C_out subset A^n` encode the proper Hall colors and have minimum Hamming
distance `delta_out`.  Let `phi:A->Sigma^m` be an injective inner marker code of
minimum distance `delta_in`.  Replace every outer symbol by its inner word to
obtain the concatenated code `C` of length `nm`.

## 1. Product distance

### Theorem PP3cey -- PROVED / CONCATENATED DISTANCE PRODUCT

The concatenated Hall-color code satisfies

```text
delta(C) >= delta_out delta_in.
```

#### Proof

Two distinct outer codewords differ in at least `delta_out` symbol positions.
At every differing position their inner words differ in at least `delta_in`
coordinates.  The corresponding coordinate blocks are disjoint, so the total
Hamming distance is at least the product. ∎

## 2. Reverse-load protection

### Theorem PP3cez -- PROVED / CONCATENATED ERROR--ERASURE PRIVACY

If at most `t` concatenated coordinates are altered and at most `e` are erased,
then exact Hall-color privacy is preserved whenever

```text
2t+e < delta_out delta_in.
```

More generally, if a partial observation is compatible with at most `L`
concatenated color tags at one target, uniform choice among at least `d` residual
Hall actions has reverse load at most `L/d`.

#### Proof

Two distinct codewords compatible with the same observation would have mutual
distance at most `2t+e`, contradicting the product-distance bound in the unique
case.  In the list case, at most `L` color classes can contribute to one observed
target, and each contributes at most `1/d`. ∎

## 3. Finite composition audit

### Theorem PP3cfa -- PROVED / BLOCKWISE WITNESS LOCALIZATION

A claimed concatenated protection level has a finite exact audit.  Failure
returns either

1. two outer codewords closer than `delta_out`,
2. two inner words closer than `delta_in`, or
3. one corrupted or erased observation compatible with too many concatenated
   Hall colors.

#### Proof

The two component codes and the finite observation space are finite.  Exhaustive
pair-distance and compatibility checks establish the claim.  Any failed check
is exactly one of the listed witnesses. ∎

## 4. Stored exact fixture

The audit `scripts/check_concatenated_hall_color_tags.py` uses an outer
`[4,2,3]` Reed--Solomon code over `F_5` and a length-two repetition inner code.
It encodes 25 colors in length eight with exact distance six.  The script checks
all 28,825 generated observations with either two errors or one error plus two
erasures and uniquely recovers the color every time.

## 5. Prime-patching consequence

A proper Hall edge color can now be protected through two geometric layers:
an algebraic outer color tag and a locally realizable inner marker word.  The
reverse-load guarantee depends only on the final list ambiguity, while failure
localizes to an outer pair, an inner pair, or one concrete received marker word.
