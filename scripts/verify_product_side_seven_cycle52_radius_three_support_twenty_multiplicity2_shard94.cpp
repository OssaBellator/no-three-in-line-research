#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    940,
    10,
    {{426436ULL,901174ULL}},
    {{1809994ULL,3381187ULL}},
    {{689913ULL,1407384ULL,581113ULL,1294213ULL}},
    2609057623375550414ULL
};

int main(int argc,char** argv) { return verify_tier_shard_digest(argc,argv,EXPECTED); }
