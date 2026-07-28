#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    580,
    10,
    {{1438976ULL,748138ULL}},
    {{4606420ULL,2457355ULL}},
    {{2347880ULL,1215488ULL,2236216ULL,1189877ULL}},
    8402579686058060180ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
