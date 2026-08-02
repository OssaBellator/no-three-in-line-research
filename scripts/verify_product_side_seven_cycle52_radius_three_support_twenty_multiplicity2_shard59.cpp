#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    590,
    10,
    {{917006ULL,373358ULL}},
    {{3123694ULL,1342837ULL}},
    {{1372453ULL,586116ULL,1272481ULL,555880ULL}},
    12218205667181486697ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
