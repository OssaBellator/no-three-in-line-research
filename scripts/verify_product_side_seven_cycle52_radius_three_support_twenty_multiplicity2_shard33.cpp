#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    330,
    10,
    {{234364ULL,212558ULL}},
    {{688492ULL,630718ULL}},
    {{331069ULL,372962ULL,347980ULL,266162ULL}},
    3155208086192315161ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
