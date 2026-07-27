#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    20,
    10,
    {{442152ULL,485218ULL}},
    {{1358498ULL,1422240ULL}},
    {{623234ULL,821618ULL,814284ULL,650456ULL}},
    10542156272579548948ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
