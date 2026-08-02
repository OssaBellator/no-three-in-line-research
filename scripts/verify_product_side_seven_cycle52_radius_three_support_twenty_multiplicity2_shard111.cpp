#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    1110,
    10,
    {{701996ULL,694670ULL}},
    {{2171259ULL,2195202ULL}},
    {{1164815ULL,1109292ULL,1091319ULL,1061700ULL}},
    10104821057997949307ULL
};

int main(int argc,char** argv) { return verify_tier_shard_digest(argc,argv,EXPECTED); }
