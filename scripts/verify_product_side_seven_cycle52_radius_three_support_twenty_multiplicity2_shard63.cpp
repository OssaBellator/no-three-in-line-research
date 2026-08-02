#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    630,
    10,
    {{688986ULL,318066ULL}},
    {{3400326ULL,1516088ULL}},
    {{1023497ULL,502259ULL,1019288ULL,470112ULL}},
    16527610734791035772ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
