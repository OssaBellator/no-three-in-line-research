#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    4,
    2392,
    1980,
    100,
    {{5803527ULL,4057775ULL}},
    {{44165080ULL,31402420ULL}},
    {{9618083ULL,6520597ULL,8862808ULL,6467127ULL}},
    5938082048004485873ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
