#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    4,
    2392,
    100,
    80,
    {{4246738ULL,3177407ULL}},
    {{20641344ULL,16423028ULL}},
    {{7291121ULL,5332073ULL,7313196ULL,5049986ULL}},
    17854348480538047953ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
