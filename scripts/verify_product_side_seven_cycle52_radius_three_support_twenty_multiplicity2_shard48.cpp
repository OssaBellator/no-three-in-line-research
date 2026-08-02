#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    480,
    10,
    {{926436ULL,1211498ULL}},
    {{6387751ULL,6300906ULL}},
    {{1553290ULL,1841772ULL,1444782ULL,2096123ULL}},
    7369468559469468632ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
