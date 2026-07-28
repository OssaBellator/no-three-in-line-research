#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    1240,
    10,
    {{439061ULL,421120ULL}},
    {{2884649ULL,2677776ULL}},
    {{652488ULL,625560ULL,618725ULL,593848ULL}},
    13178814025061252983ULL
};

int main(int argc,char** argv) { return verify_tier_shard_digest(argc,argv,EXPECTED); }
