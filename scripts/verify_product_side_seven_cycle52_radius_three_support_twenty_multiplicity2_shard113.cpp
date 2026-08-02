#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    1130,
    10,
    {{492264ULL,461430ULL}},
    {{1569053ULL,1499950ULL}},
    {{759794ULL,691543ULL,689482ULL,655879ULL}},
    1162254786787950315ULL
};

int main(int argc,char** argv) { return verify_tier_shard_digest(argc,argv,EXPECTED); }
