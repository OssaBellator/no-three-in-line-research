#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    900,
    10,
    {{360937ULL,536493ULL}},
    {{2680106ULL,3083355ULL}},
    {{578966ULL,826845ULL,515442ULL,750645ULL}},
    587821386895714243ULL
};

int main(int argc,char** argv) { return verify_tier_shard_digest(argc,argv,EXPECTED); }
