#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    4,
    2392,
    1880,
    100,
    {{6648856ULL,5313884ULL}},
    {{43485293ULL,33615316ULL}},
    {{10568367ULL,8597320ULL,10558691ULL,8608212ULL}},
    14452785419276235217ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
