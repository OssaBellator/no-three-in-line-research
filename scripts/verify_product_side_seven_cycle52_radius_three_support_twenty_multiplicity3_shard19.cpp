#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    3,
    3544,
    1900,
    100,
    {{5205218ULL,3922766ULL}},
    {{30557339ULL,23926433ULL}},
    {{9166047ULL,6870435ULL,8773636ULL,6467881ULL}},
    18153953954358039500ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
