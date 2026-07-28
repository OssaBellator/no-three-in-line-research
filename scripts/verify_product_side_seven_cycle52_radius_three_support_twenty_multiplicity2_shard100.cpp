#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    1000,
    10,
    {{226824ULL,444034ULL}},
    {{3678348ULL,4607164ULL}},
    {{345812ULL,697446ULL,336313ULL,674465ULL}},
    11512103508428254606ULL
};

int main(int argc,char** argv) { return verify_tier_shard_digest(argc,argv,EXPECTED); }
