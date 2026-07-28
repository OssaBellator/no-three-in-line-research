#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    950,
    10,
    {{606708ULL,871230ULL}},
    {{3632108ULL,4563210ULL}},
    {{982859ULL,1359498ULL,844508ULL,1260104ULL}},
    11676461390096745129ULL
};

int main(int argc,char** argv) { return verify_tier_shard_digest(argc,argv,EXPECTED); }
