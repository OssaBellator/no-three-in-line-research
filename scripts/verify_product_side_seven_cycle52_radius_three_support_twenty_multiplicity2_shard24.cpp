#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    240,
    10,
    {{426544ULL,569836ULL}},
    {{6377496ULL,5975534ULL}},
    {{640718ULL,832702ULL,609570ULL,916001ULL}},
    9055214726262274039ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
