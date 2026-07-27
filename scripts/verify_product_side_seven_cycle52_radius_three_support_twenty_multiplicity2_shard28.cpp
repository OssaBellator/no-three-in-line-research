#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    280,
    10,
    {{485640ULL,957020ULL}},
    {{1473666ULL,2912370ULL}},
    {{727126ULL,1606408ULL,828453ULL,1418481ULL}},
    1683636985435897178ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
