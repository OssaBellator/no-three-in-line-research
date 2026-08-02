#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    960,
    10,
    {{477320ULL,441888ULL}},
    {{5991511ULL,4274964ULL}},
    {{760502ULL,719286ULL,689523ULL,606756ULL}},
    9681559467231383948ULL
};

int main(int argc,char** argv) { return verify_tier_shard_digest(argc,argv,EXPECTED); }
