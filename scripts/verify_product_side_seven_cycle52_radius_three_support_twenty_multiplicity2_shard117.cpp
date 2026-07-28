#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    1170,
    10,
    {{427250ULL,484757ULL}},
    {{2228191ULL,2373236ULL}},
    {{670313ULL,713650ULL,597332ULL,719723ULL}},
    1740787177219988686ULL
};

int main(int argc,char** argv) { return verify_tier_shard_digest(argc,argv,EXPECTED); }
