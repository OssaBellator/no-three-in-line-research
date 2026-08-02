#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    920,
    10,
    {{855196ULL,583788ULL}},
    {{3503094ULL,2691495ULL}},
    {{1461513ULL,930838ULL,1284211ULL,916415ULL}},
    14788916645976880020ULL
};

int main(int argc,char** argv) { return verify_tier_shard_digest(argc,argv,EXPECTED); }
