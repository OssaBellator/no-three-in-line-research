#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    3,
    3544,
    700,
    100,
    {{3599282ULL,2996682ULL}},
    {{28811477ULL,25488200ULL}},
    {{6485138ULL,5387842ULL,5846703ULL,4862868ULL}},
    17881519169292883135ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
