#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    840,
    10,
    {{494559ULL,411967ULL}},
    {{2564663ULL,2009859ULL}},
    {{779492ULL,657598ULL,700919ULL,584177ULL}},
    866350994586011106ULL
};

int main(int argc,char** argv) { return verify_tier_shard_digest(argc,argv,EXPECTED); }
