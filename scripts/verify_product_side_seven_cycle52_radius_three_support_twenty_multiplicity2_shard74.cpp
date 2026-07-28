#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    740,
    10,
    {{467834ULL,495104ULL}},
    {{1615334ULL,1718500ULL}},
    {{770812ULL,777725ULL,711483ULL,739781ULL}},
    16486546947670781079ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
