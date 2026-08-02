#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    4,
    2392,
    1680,
    100,
    {{6042211ULL,3879075ULL}},
    {{33357244ULL,21558956ULL}},
    {{8464972ULL,5500910ULL,8852913ULL,5597856ULL}},
    14864804958552868545ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
