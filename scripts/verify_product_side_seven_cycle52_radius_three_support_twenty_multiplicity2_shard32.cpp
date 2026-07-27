#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    320,
    10,
    {{418700ULL,280144ULL}},
    {{1454512ULL,945304ULL}},
    {{606299ULL,433302ULL,624884ULL,402518ULL}},
    7141580424024650355ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
