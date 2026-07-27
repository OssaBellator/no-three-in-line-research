#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    180,
    10,
    {{729008ULL,927750ULL}},
    {{3392179ULL,4065445ULL}},
    {{1185810ULL,1429900ULL,1144312ULL,1508819ULL}},
    16784769552087234267ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
