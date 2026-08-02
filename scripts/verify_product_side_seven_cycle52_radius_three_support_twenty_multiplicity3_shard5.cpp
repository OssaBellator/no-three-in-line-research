#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    3,
    3544,
    500,
    100,
    {{11171978ULL,6825064ULL}},
    {{45878006ULL,31913022ULL}},
    {{20045993ULL,11769433ULL,18734156ULL,11899396ULL}},
    17374652970419326891ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
