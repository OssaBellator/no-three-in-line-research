#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    4,
    2392,
    280,
    100,
    {{8854171ULL,3074772ULL}},
    {{48104878ULL,18442760ULL}},
    {{16942013ULL,5480731ULL,15819174ULL,5468426ULL}},
    6137969857602763612ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
