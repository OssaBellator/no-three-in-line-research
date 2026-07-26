#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    4,
    2392,
    680,
    100,
    {{5141457ULL,4043072ULL}},
    {{34476740ULL,29309655ULL}},
    {{7914701ULL,6080386ULL,7918135ULL,5647942ULL}},
    11675003001759290027ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
