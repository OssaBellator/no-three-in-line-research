#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    570,
    10,
    {{1065590ULL,362884ULL}},
    {{4676136ULL,1753714ULL}},
    {{1706844ULL,552104ULL,1638376ULL,573245ULL}},
    16939193131642798275ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
