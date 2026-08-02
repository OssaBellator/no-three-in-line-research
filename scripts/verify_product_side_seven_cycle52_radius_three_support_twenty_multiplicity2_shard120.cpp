#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    1200,
    10,
    {{735474ULL,762052ULL}},
    {{4514229ULL,4092952ULL}},
    {{1182148ULL,1187945ULL,1084192ULL,1140778ULL}},
    2735525392471744800ULL
};

int main(int argc,char** argv) { return verify_tier_shard_digest(argc,argv,EXPECTED); }
