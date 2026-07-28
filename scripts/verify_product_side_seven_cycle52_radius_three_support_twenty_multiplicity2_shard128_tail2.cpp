#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    1288,
    2,
    {{136284ULL,122708ULL}},
    {{1334990ULL,1140252ULL}},
    {{196397ULL,191186ULL,187184ULL,162904ULL}},
    6909944594185390875ULL
};

int main(int argc,char** argv) { return verify_tier_shard_digest(argc,argv,EXPECTED); }
