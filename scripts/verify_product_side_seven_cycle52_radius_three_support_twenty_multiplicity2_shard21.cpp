#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    210,
    10,
    {{1181652ULL,788248ULL}},
    {{4963173ULL,3247950ULL}},
    {{1938775ULL,1247014ULL,1808029ULL,1334457ULL}},
    18208381549471948796ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
