#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    1090,
    10,
    {{340224ULL,292504ULL}},
    {{5455228ULL,4548032ULL}},
    {{519014ULL,429439ULL,482152ULL,419727ULL}},
    6179261871308072922ULL
};

int main(int argc,char** argv) { return verify_tier_shard_digest(argc,argv,EXPECTED); }
