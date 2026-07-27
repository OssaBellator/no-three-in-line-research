#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    30,
    10,
    {{275396ULL,540220ULL}},
    {{904975ULL,1684808ULL}},
    {{384792ULL,848733ULL,486737ULL,802090ULL}},
    1833162045244562221ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
