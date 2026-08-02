#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    780,
    10,
    {{429828ULL,386256ULL}},
    {{1335544ULL,1210868ULL}},
    {{692482ULL,624977ULL,655785ULL,536625ULL}},
    13663757452176296805ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
