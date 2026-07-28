#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    1280,
    7,
    {{635680ULL,469592ULL}},
    {{4305892ULL,2898456ULL}},
    {{946920ULL,706738ULL,879290ULL,654656ULL}},
    12966799060506877054ULL
};

int main(int argc,char** argv) { return verify_tier_shard_digest(argc,argv,EXPECTED); }
