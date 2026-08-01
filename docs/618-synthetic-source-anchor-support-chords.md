# Synthetic source-anchor support chords

`docs/612` embedded unary runs as row-column-distinct collinear point sets.  This
chapter adds two explicit anchor points to each run line, turning every unary
node into a source-pair blocker in a finite coordinate model.

## 1. Anchored run embedding

### Theorem PP3cvu — PROVED / DISTINCT ANCHOR-AND-INSERTION RESOURCES

For every ordered composition of eleven unary nodes, there is an integer
embedding with:

- two anchor points on each run line;
- globally distinct rows for all anchors and inserted points;
- globally distinct columns for all anchors and inserted points;
- no collinear triple using more than one run label.

All 1,024 compositions are constructed by the canonical greedy algorithm.  The
largest absolute coordinate used is 419.

#### Proof

Start from the `docs/612` run embedding.  Add anchors one at a time on the
corresponding run line, skipping every used row or column and every coordinate
that creates a mixed-label triple.  The checker verifies the completed geometry
for all compositions. ∎

## 2. Exact source-pair incidence

### Theorem PP3cvv — PROVED / ELEVEN ANCHORED BLOCKERS PER ENCODING

Each unary node lies on the line through the two anchors of its maximal unary
run.  Therefore every encoding in the selected profile has exactly eleven
anchor-pair/inserted-point collinear triples.

At encoded size thirty with nine binary nodes, the family size is
`168212023980`, so the aggregate anchored blocker count is

```text
1850332263780,
```

with exact mean eleven.

#### Proof

There are exactly eleven unary nodes in the profile.  The two run anchors and
each run point are collinear, while the mixed-run audit is zero.  Multiply by the
exact profile count. ∎

## 3. Interface status

### Theorem PP3cvw — PROVED / SYNTHETIC-ANCHOR TYPE SEPARATION

The anchored geometry is a complete finite source-chord model, but it does not
identify the anchors with retained source cells in the prime-patching
construction and assigns no removal credit to them.

#### Proof

The checker creates anchors from the encoded run list alone.  No map from these
coordinates to the active source configuration is used. ∎
