#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    4,
    2392,
    1180,
    100,
    {{4883671ULL,3657672ULL}},
    {{30556288ULL,25402649ULL}},
    {{8920257ULL,6660138ULL,8563368ULL,6122180ULL}},
    7039424060371606348ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
