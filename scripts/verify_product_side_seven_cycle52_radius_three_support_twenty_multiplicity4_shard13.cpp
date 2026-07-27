#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    4,
    2392,
    1280,
    100,
    {{3758673ULL,3291475ULL}},
    {{26438341ULL,21497250ULL}},
    {{6310580ULL,5544994ULL,6066696ULL,5288007ULL}},
    8144832165213751731ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
