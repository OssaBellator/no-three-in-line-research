#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    4,
    2392,
    380,
    100,
    {{5284463ULL,3771951ULL}},
    {{38170524ULL,24900473ULL}},
    {{9128638ULL,6402119ULL,8731796ULL,6205348ULL}},
    1231252113985398192ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
