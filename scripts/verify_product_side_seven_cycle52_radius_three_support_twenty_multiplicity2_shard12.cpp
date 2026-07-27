#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    120,
    10,
    {{654912ULL,1018294ULL}},
    {{4023288ULL,4952680ULL}},
    {{1042561ULL,1513539ULL,1016692ULL,1712559ULL}},
    14137670081341765779ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
