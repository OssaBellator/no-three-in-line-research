#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    3,
    3544,
    1600,
    100,
    {{5443596ULL,3160465ULL}},
    {{44929457ULL,29856543ULL}},
    {{9200669ULL,5162024ULL,8942845ULL,5226725ULL}},
    4422199473448535567ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
