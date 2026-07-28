#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    850,
    10,
    {{377280ULL,490534ULL}},
    {{2540229ULL,2782240ULL}},
    {{587849ULL,791824ULL,531610ULL,659138ULL}},
    8314562979571188860ULL
};

int main(int argc,char** argv) { return verify_tier_shard_digest(argc,argv,EXPECTED); }
