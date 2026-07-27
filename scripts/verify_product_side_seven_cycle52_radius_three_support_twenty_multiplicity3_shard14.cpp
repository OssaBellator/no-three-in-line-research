#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    3,
    3544,
    1400,
    100,
    {{6400098ULL,4974886ULL}},
    {{24666412ULL,19854597ULL}},
    {{11347949ULL,8886433ULL,11563218ULL,8385316ULL}},
    15279610700182069842ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
