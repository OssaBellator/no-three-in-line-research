#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    880,
    10,
    {{464038ULL,480963ULL}},
    {{2595805ULL,2627043ULL}},
    {{722560ULL,758668ULL,666588ULL,711406ULL}},
    1447120913300419263ULL
};

int main(int argc,char** argv) { return verify_tier_shard_digest(argc,argv,EXPECTED); }
