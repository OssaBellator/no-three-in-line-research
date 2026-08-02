#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    80,
    10,
    {{1086940ULL,482824ULL}},
    {{3965824ULL,1674513ULL}},
    {{1677146ULL,812199ULL,1894831ULL,711961ULL}},
    5856008537745773282ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
