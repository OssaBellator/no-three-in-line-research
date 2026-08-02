#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    1210,
    10,
    {{626550ULL,500188ULL}},
    {{4047561ULL,3345162ULL}},
    {{984428ULL,758387ULL,971841ULL,739191ULL}},
    13574711017486657864ULL
};

int main(int argc,char** argv) { return verify_tier_shard_digest(argc,argv,EXPECTED); }
