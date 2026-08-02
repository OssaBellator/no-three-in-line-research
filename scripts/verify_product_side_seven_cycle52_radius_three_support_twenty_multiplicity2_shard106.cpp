#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    1060,
    10,
    {{982628ULL,411114ULL}},
    {{4478252ULL,2082759ULL}},
    {{1458627ULL,613517ULL,1432051ULL,639611ULL}},
    11786549827740883811ULL
};

int main(int argc,char** argv) { return verify_tier_shard_digest(argc,argv,EXPECTED); }
