#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    490,
    10,
    {{607096ULL,1111374ULL}},
    {{5216043ULL,6015518ULL}},
    {{935872ULL,1690018ULL,882649ULL,1814947ULL}},
    5474747236930159619ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
