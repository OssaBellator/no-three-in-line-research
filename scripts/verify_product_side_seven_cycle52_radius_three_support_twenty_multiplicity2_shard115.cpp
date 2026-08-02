#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    1150,
    10,
    {{660630ULL,583534ULL}},
    {{2789899ULL,2499085ULL}},
    {{1005306ULL,885364ULL,953983ULL,882225ULL}},
    17913593264151879314ULL
};

int main(int argc,char** argv) { return verify_tier_shard_digest(argc,argv,EXPECTED); }
