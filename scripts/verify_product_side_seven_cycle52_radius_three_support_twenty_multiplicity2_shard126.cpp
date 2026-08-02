#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    1260,
    10,
    {{401553ULL,532697ULL}},
    {{2897527ULL,3106180ULL}},
    {{629841ULL,823948ULL,554310ULL,735693ULL}},
    3222192598561150535ULL
};

int main(int argc,char** argv) { return verify_tier_shard_digest(argc,argv,EXPECTED); }
