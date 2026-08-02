#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    1010,
    10,
    {{278844ULL,353590ULL}},
    {{4384258ULL,4823070ULL}},
    {{426123ULL,542489ULL,407479ULL,495806ULL}},
    12802408152367890407ULL
};

int main(int argc,char** argv) { return verify_tier_shard_digest(argc,argv,EXPECTED); }
