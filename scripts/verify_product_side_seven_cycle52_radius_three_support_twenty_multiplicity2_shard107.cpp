#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    1070,
    10,
    {{516550ULL,368429ULL}},
    {{3142351ULL,2255818ULL}},
    {{805867ULL,527439ULL,735929ULL,547604ULL}},
    9459744099503416523ULL
};

int main(int argc,char** argv) { return verify_tier_shard_digest(argc,argv,EXPECTED); }
