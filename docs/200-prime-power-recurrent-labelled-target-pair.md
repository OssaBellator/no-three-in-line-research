# Recurrent physical targets reduce to labelled-pair deletion or double contraction

CMR763--CMR769 show that repeated neutralised target signatures force physical
cell reintroduction. A physical target can return with different assignments to
the two permutation layers, so one must first stabilise the labelled same-layer
pair before applying matching-host deletion. There are only six possible labelled
pairs for one physical triple. Once one recurs, either one pair cell is
nonessential and can be deleted, or both are essential and contract together.

Fix one exact physical nonaxis target triple

\[
T=\{e_1,e_2,e_3\}.
\]

At every selected occurrence of `T`, choose the lexicographically first pair of
its cells lying in the majority permutation layer. Record the chosen layer and
the unordered pair.

## 1. Six labelled pair types per physical target

### Theorem CMR770 -- PROVED

One physical target triple has at most

\[
\boxed{6}
\]

labelled same-layer pair types.

### Proof

There are two choices of permutation layer and three unordered pairs of target
cells. Only some of these six possibilities can occur as a majority-layer pair,
so six is an upper bound. ∎

The layer label is retained because essentiality and deletion are properties of
one matching host, not of an unlabelled physical cell set.

## 2. Physical recurrence forces labelled-pair recurrence

### Theorem CMR771 -- PROVED

If the same physical target `T` occurs in `K` target episodes, then one labelled
same-layer pair type occurs in at least

\[
\boxed{
\left\lceil\frac K6\right\rceil
}
\]

episodes.

For every integer `lambda>=2`, either one labelled pair occurs at least `lambda`
times or

\[
\boxed{K\le6(\lambda-1).}
\]

### Proof

Partition the occurrences among the at most six types from CMR770 and apply the
pigeonhole principle. ∎

Thus a repeatedly returning physical target cannot migrate indefinitely between
layer assignments without repeating one matching-host prescription.

## 3. A nonessential pair cell deletes the target

Let one recurrent labelled type be

\[
(\ell,P),
\qquad
P=\{a,b\},
\]

where `a,b` are compatible selected edges of the layer-`ell` matching host `H`.

### Theorem CMR772 -- PROVED

If at least one edge of `P` is nonessential in `H`, then there is an edge
`f in P` such that

\[
\boxed{\operatorname{PM}(H-f)\ne\varnothing.}
\]

Deleting `f`

1. preserves a layer perfect matching;
2. makes the labelled target `T` inactive;
3. cannot activate any previously inactive matching prescription.

### Proof

Choose a nonessential edge `f` of `P`. By definition, some perfect matching of
`H` avoids `f` and survives in `H-f`. Every occurrence of `T` in the labelled
type uses both cells of `P`, hence uses `f`; deleting it kills the target. Passing
to a subhost cannot create a new extendable prescription. ∎

Only one pair edge is needed to kill the target; simultaneous pair deletion is
not assumed.

## 4. Two essential pair cells contract exactly

### Theorem CMR773 -- PROVED

If both compatible edges `a,b` of `P` are essential in `H`, then

\[
\boxed{
\operatorname{PM}(H)
\cong
\{a,b\}
\times
\operatorname{PM}(H-V(P)).
}
\]

The factor side decreases by exactly two. After contraction, occurrence of the
original three-cell target is controlled by the residual singleton prescription

\[
\boxed{T\setminus P,}
\]

which has rank one.

### Proof

Every perfect matching contains both essential edges. They are compatible, so
their four endpoints are distinct. Restricting a perfect matching to the
remaining vertices gives a perfect matching of `H-V(P)`. Conversely, adjoining
`a,b` to any residual perfect matching gives a perfect matching of `H`. The
constructions are inverse. The target has three cells and two are contracted,
leaving one residual cell. ∎

The rank-one trigger enters the existing anchored, essential-transfer,
matching-preserving deletion, or fixed-certificate machinery.

## 5. Complete labelled-pair action

### Corollary CMR774 -- PROVED

Every active labelled target-pair recurrence in one matching host reaches exactly
one of the following structural actions.

1. **Matching-preserving deletion.** At least one pair edge is nonessential and is
   deleted as in CMR772.
2. **Double essential contraction.** Both pair edges are essential and contract as
   in CMR773, reducing the factor side by two and transferring the target to rank
   one.

### Proof

Either both edges are essential or at least one is not. Apply CMR772 or CMR773. ∎

No third matching-space case remains.

## 6. Returns after the labelled-pair action are already paid

### Theorem CMR775 -- PROVED

After the action CMR774:

1. if a deleted pair edge later returns, it enters the stored-avoidance,
   deletion-ancestry, unit-wall, and reintroduction alternatives CMR720--CMR747;
2. if both pair edges contracted, the owner side has strictly decreased and the
   rank-one residual target enters CMR636--CMR655;
3. if the layer, host, factor, routing, or envelope owner changes, the event uses
   the finite owner stock already recorded by CMR693, CMR716, and CMR743.

### Proof

The first assertion is the returned-edge theory CMR720--CMR747. The second is the
exact factorisation CMR773 followed by the existing rank-one recursion. The third
is the definition of the owner-labelled stock. ∎

## 7. Recurrent physical-target endpoint

### Corollary CMR776 -- PROVED

A recurrent physical target inside a fixed envelope reaches at least one of:

1. at most `6(lambda-1)` occurrences without a labelled type recurring `lambda`
   times;
2. matching-preserving deletion of one recurrent labelled-pair cell;
3. double essential contraction and strict side descent;
4. a rank-one residual target handled by the established factor recursion;
5. returned-edge ancestry or exact reintroduction payment;
6. finite owner change, envelope expansion, or a strict potential improvement.

Consequently a recurrent physical target cannot remain an anonymous one-cell
return loop. After finite layer-assignment stock it exposes a fixed compatible
pair, and that pair is either deleted or contracted.

### Proof

Use CMR771 to stabilise the labelled type, CMR774 for the matching-host action,
and CMR775 for later returns and owner changes. ∎

No all-`n` theorem is claimed. The six-type recurrence, nonessential deletion,
double-essential factorisation, and rank-one transfer are checked in
[`scripts/verify_prime_power_recurrent_labelled_target_pair.py`](../scripts/verify_prime_power_recurrent_labelled_target_pair.py).
