#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    420,
    10,
    {{2016042ULL,332804ULL}},
    {{6316808ULL,1125892ULL}},
    {{3265868ULL,544749ULL,3180167ULL,545390ULL}},
    3162344281037951680ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
