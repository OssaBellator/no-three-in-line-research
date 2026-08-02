#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    3,
    3544,
    2400,
    100,
    {{4901230ULL,3914810ULL}},
    {{59371428ULL,46813489ULL}},
    {{8294827ULL,7020908ULL,8800046ULL,6275305ULL}},
    1893542477527105416ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
