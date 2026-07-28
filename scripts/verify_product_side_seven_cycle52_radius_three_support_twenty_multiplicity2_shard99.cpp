#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    990,
    10,
    {{445068ULL,239272ULL}},
    {{6037928ULL,4139098ULL}},
    {{685298ULL,379529ULL,705943ULL,337380ULL}},
    1567631251581117598ULL
};

int main(int argc,char** argv) { return verify_tier_shard_digest(argc,argv,EXPECTED); }
