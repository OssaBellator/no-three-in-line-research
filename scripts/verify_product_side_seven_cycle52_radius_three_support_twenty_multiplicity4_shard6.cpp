#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    4,
    2392,
    580,
    100,
    {{5509821ULL,4158847ULL}},
    {{30620762ULL,22389295ULL}},
    {{8122756ULL,6161170ULL,7747740ULL,5721623ULL}},
    11658676560239131698ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
