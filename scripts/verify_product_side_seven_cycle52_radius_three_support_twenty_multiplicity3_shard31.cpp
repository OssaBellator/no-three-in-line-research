#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    3,
    3544,
    3100,
    100,
    {{6915908ULL,7248120ULL}},
    {{42478392ULL,40462500ULL}},
    {{12370404ULL,12824279ULL,10912654ULL,12059798ULL}},
    9218704767626605724ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
