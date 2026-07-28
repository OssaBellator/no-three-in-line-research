#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2, 3840, 1320, 10,
    {{224840ULL,427684ULL}},
    {{660436ULL,1217933ULL}},
    {{303169ULL,737637ULL,377311ULL,555926ULL}},
    13572297940413613278ULL
};

int main(int argc,char** argv) { return verify_tier_shard_digest(argc,argv,EXPECTED); }
