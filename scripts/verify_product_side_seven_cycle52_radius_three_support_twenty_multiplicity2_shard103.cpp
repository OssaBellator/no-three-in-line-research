#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    1030,
    10,
    {{564452ULL,342996ULL}},
    {{1747012ULL,1102559ULL}},
    {{787188ULL,525699ULL,847569ULL,465422ULL}},
    15081963100796215239ULL
};

int main(int argc,char** argv) { return verify_tier_shard_digest(argc,argv,EXPECTED); }
