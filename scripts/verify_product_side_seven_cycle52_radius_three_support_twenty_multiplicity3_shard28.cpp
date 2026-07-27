#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    3,
    3544,
    2800,
    100,
    {{6609442ULL,5226328ULL}},
    {{40248960ULL,32564528ULL}},
    {{11860600ULL,9127032ULL,11165317ULL,9376031ULL}},
    4917294112956063211ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
