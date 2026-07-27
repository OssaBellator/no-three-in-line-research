#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    3,
    3544,
    300,
    100,
    {{6392150ULL,6458168ULL}},
    {{27881020ULL,27065957ULL}},
    {{11591307ULL,11417428ULL,11239407ULL,11360057ULL}},
    5218863638130273781ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
