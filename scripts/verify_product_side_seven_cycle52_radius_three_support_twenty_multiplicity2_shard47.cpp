#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    470,
    10,
    {{1252102ULL,435282ULL}},
    {{4224342ULL,1555420ULL}},
    {{1836529ULL,664446ULL,1769067ULL,667267ULL}},
    13602949510585451809ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
