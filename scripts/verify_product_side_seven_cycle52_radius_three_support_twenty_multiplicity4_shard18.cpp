#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    4,
    2392,
    1780,
    100,
    {{4860380ULL,3354182ULL}},
    {{37929958ULL,26845024ULL}},
    {{7604985ULL,5287787ULL,7677471ULL,5406203ULL}},
    14735579502432110373ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
