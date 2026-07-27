#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    3,
    3544,
    800,
    100,
    {{3518306ULL,3027808ULL}},
    {{16368216ULL,14499783ULL}},
    {{6268546ULL,5292350ULL,5610835ULL,4818305ULL}},
    12170455306990093592ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
