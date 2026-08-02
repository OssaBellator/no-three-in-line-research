#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    1080,
    10,
    {{343442ULL,302243ULL}},
    {{2491528ULL,1999682ULL}},
    {{523921ULL,446176ULL,487597ULL,445763ULL}},
    14195405686816500006ULL
};

int main(int argc,char** argv) { return verify_tier_shard_digest(argc,argv,EXPECTED); }
