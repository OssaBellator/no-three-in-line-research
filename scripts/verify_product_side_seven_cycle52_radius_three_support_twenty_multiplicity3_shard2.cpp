#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    3,
    3544,
    200,
    100,
    {{5817048ULL,4596184ULL}},
    {{34249610ULL,28692725ULL}},
    {{10105198ULL,8407578ULL,10234882ULL,7540623ULL}},
    14334911769310005031ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
