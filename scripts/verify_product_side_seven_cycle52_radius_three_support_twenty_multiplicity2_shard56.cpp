#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    560,
    10,
    {{863134ULL,749846ULL}},
    {{4167454ULL,3553104ULL}},
    {{1395438ULL,1157485ULL,1285918ULL,1208205ULL}},
    9318782807487620778ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
