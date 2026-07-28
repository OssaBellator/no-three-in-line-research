#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    1120,
    10,
    {{441396ULL,370924ULL}},
    {{1446419ULL,1248201ULL}},
    {{699231ULL,564074ULL,653259ULL,560620ULL}},
    3128667511060827642ULL
};

int main(int argc,char** argv) { return verify_tier_shard_digest(argc,argv,EXPECTED); }
