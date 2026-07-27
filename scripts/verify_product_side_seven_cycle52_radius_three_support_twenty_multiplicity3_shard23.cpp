#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    3,
    3544,
    2300,
    100,
    {{9808878ULL,4561504ULL}},
    {{64595027ULL,33188193ULL}},
    {{17387127ULL,8015079ULL,17456995ULL,8127971ULL}},
    9882995509441515575ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
