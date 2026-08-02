#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    3,
    3544,
    1800,
    100,
    {{7092176ULL,4279954ULL}},
    {{31534459ULL,19409414ULL}},
    {{12693276ULL,7458176ULL,11675532ULL,6811205ULL}},
    4853397229172252623ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
