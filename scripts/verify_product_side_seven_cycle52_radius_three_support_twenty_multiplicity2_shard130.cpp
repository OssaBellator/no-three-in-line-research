#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2, 3840, 1300, 10,
    {{305460ULL,327892ULL}},
    {{5327852ULL,5326142ULL}},
    {{471530ULL,542727ULL,459606ULL,443298ULL}},
    8890744816044984291ULL
};

int main(int argc,char** argv) { return verify_tier_shard_digest(argc,argv,EXPECTED); }
