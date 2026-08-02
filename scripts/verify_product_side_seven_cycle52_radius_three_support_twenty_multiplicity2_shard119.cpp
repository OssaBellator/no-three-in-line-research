#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    1190,
    10,
    {{770953ULL,462102ULL}},
    {{4045828ULL,2344488ULL}},
    {{1174814ULL,698139ULL,1122444ULL,687655ULL}},
    4487626094761021039ULL
};

int main(int argc,char** argv) { return verify_tier_shard_digest(argc,argv,EXPECTED); }
