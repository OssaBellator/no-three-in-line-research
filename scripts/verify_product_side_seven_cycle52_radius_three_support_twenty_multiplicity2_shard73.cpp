#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    730,
    10,
    {{494384ULL,590374ULL}},
    {{1603679ULL,1948454ULL}},
    {{791809ULL,920325ULL,746482ULL,885868ULL}},
    13362156138260302353ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
