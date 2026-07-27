#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    4,
    2392,
    1580,
    100,
    {{7768073ULL,4544458ULL}},
    {{61275621ULL,40799345ULL}},
    {{12833495ULL,7510941ULL,13211508ULL,7178980ULL}},
    4380135539162214536ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
