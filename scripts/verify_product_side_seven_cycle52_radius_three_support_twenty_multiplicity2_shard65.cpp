#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    650,
    10,
    {{395152ULL,472056ULL}},
    {{1676886ULL,1995367ULL}},
    {{626820ULL,692878ULL,549637ULL,690296ULL}},
    10672074734858696060ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
