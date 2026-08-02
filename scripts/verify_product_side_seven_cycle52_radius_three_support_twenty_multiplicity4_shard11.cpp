#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    4,
    2392,
    1080,
    100,
    {{4709436ULL,3825399ULL}},
    {{35453073ULL,30098760ULL}},
    {{7168836ULL,5934517ULL,7120880ULL,5830942ULL}},
    16641707327491079352ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
