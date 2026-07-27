#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    380,
    10,
    {{692666ULL,482714ULL}},
    {{2494090ULL,1814023ULL}},
    {{1081046ULL,746248ULL,1089643ULL,721587ULL}},
    16236183647005793889ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
