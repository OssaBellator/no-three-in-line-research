#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    500,
    10,
    {{518756ULL,390052ULL}},
    {{3301430ULL,2210150ULL}},
    {{737380ULL,591114ULL,780982ULL,530375ULL}},
    2680446809043638559ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
