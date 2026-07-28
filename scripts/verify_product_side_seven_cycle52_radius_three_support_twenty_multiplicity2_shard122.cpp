#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    1220,
    10,
    {{671992ULL,519896ULL}},
    {{3121210ULL,2495202ULL}},
    {{1013882ULL,755767ULL,964480ULL,833490ULL}},
    8162915674535461669ULL
};

int main(int argc,char** argv) { return verify_tier_shard_digest(argc,argv,EXPECTED); }
