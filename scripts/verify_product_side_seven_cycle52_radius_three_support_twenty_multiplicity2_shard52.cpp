#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    520,
    10,
    {{632620ULL,380540ULL}},
    {{2151568ULL,1305056ULL}},
    {{952684ULL,573935ULL,956085ULL,561709ULL}},
    12482974293267331403ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
