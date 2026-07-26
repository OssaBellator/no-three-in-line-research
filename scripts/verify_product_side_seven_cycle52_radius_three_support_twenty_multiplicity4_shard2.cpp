#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    4,
    2392,
    180,
    100,
    {{5897928ULL,5589872ULL}},
    {{25036685ULL,23895638ULL}},
    {{9065985ULL,8914440ULL,9042029ULL,8597078ULL}},
    2103545732133771940ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
