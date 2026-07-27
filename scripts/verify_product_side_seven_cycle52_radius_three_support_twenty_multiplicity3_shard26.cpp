#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    3,
    3544,
    2600,
    100,
    {{4403760ULL,3055961ULL}},
    {{28851886ULL,20356906ULL}},
    {{7658128ULL,5392636ULL,7534256ULL,5370891ULL}},
    17903848441077875937ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
