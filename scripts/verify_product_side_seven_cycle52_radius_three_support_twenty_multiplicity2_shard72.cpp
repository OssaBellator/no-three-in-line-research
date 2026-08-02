#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    720,
    10,
    {{389450ULL,331130ULL}},
    {{1315242ULL,1133977ULL}},
    {{581011ULL,510888ULL,568797ULL,460716ULL}},
    15152283108699527779ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
