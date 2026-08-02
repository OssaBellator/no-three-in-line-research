#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    460,
    10,
    {{1395664ULL,1007418ULL}},
    {{7166721ULL,4625283ULL}},
    {{2219878ULL,1465696ULL,2089637ULL,1679086ULL}},
    5944945430537609933ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
