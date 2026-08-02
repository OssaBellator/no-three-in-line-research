#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    1160,
    10,
    {{941564ULL,334208ULL}},
    {{4064809ULL,1502311ULL}},
    {{1415213ULL,490451ULL,1328485ULL,496575ULL}},
    9121395323374095906ULL
};

int main(int argc,char** argv) { return verify_tier_shard_digest(argc,argv,EXPECTED); }
