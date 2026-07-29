# Alternating-core weighted layer shortfall bank

This note records AC5by--AC5cc. It composes the layered incidence and bad-layer witness results with the exact obstruction-capacity bank. It does not prove the concrete geometric layer estimates.

## Contract

Fix a target retained-degree/reverse-load ratio `theta >= 0`. Every exact conditioned menu layer `i` retains:

- reverse load `D_i >= 0`;
- retained forward degree `d_i >= 0`;
- an exact obstruction class `lambda(i)` from a finite dictionary `L`;
- occurrence-faithful initial capacity and recorded deposits for every class.

Define the local ratio shortfall

` s_i = (theta D_i - d_i)_+ `

and the aggregate shortfall

` S = (theta sum_i D_i - sum_i d_i)_+ `.

## Theorem block

### AC5by — local shortfall domination

`S <= sum_i s_i`.

Thus all aggregate failure mass is covered by exact local layer shortfall; no unlabelled global deficit is introduced.

### AC5bz — exact class partition

For each obstruction class `lambda`, let

`Q_lambda = sum_{i: lambda(i)=lambda} s_i`.

Then `sum_lambda Q_lambda = sum_i s_i`. Every unit of local shortfall keeps its layer occurrence and exact class.

### AC5ca — capacity payment

If `Q_lambda <= C_lambda + D_lambda` for every class, the entire aggregate shortfall is paid. In particular `S` is paid.

### AC5cb — overload witness

If classwise payment fails, the least class with

`Q_lambda > C_lambda + D_lambda`

is an exact obstruction overload. When `S >= epsilon sum_i D_i`, either this overload occurs or the paid account contains at least that much charged shortfall.

### AC5cc — reset boundary

Changing the target ratio, omitting layer identity, moving shortfall between obstruction classes, allowing negative cancellation, or introducing unrecorded capacity is outside the theorem and returns reset.

## Proof

For every layer, `theta D_i - d_i <= s_i`. Summing and taking the positive part gives AC5by. AC5bz is the exact partition by retained class. AC5ca and AC5cb are the classwise capacity alternative already used by the obstruction bank.

## Remaining physical work

The theorem reduces AC5 to concrete lower bounds for `d_i/D_i`, exact assignment of a failed layer to an obstruction class, and arithmetic bounds for class capacities and deposits. It does not establish those estimates or AC5.