#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    4,
    2392,
    480,
    100,
    {{4222004ULL,3626774ULL}},
    {{27070528ULL,21962260ULL}},
    {{6641795ULL,5769278ULL,6386903ULL,5293527ULL}},
    16120744542518780924ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
