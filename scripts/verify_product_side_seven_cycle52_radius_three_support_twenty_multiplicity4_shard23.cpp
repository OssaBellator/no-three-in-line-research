#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    4,
    2392,
    2280,
    100,
    {{5389029ULL,5338754ULL}},
    {{52264513ULL,46557415ULL}},
    {{8480369ULL,8664290ULL,8722010ULL,7900957ULL}},
    12832317832074138104ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
