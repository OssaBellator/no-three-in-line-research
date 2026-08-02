#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    300,
    10,
    {{2098390ULL,1738750ULL}},
    {{6252462ULL,5288542ULL}},
    {{3565267ULL,2821374ULL,3526323ULL,2791190ULL}},
    11051023198654571322ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
