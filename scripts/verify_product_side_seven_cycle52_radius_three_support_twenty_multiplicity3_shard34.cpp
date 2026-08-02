#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    3,
    3544,
    3400,
    100,
    {{3873002ULL,6509196ULL}},
    {{49636428ULL,58997491ULL}},
    {{6528807ULL,11402184ULL,6719053ULL,10559014ULL}},
    3142633351817514366ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
