#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    410,
    10,
    {{659778ULL,369358ULL}},
    {{2193134ULL,1231478ULL}},
    {{979691ULL,567110ULL,964822ULL,536168ULL}},
    5749020248150475417ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
