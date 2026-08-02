#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    4,
    2392,
    780,
    100,
    {{4945601ULL,3531294ULL}},
    {{32622543ULL,23246273ULL}},
    {{7655405ULL,5444441ULL,7533438ULL,5117444ULL}},
    3281681937089769951ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
