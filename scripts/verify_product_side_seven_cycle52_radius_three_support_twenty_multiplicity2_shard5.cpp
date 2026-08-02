#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    50,
    10,
    {{598714ULL,1486608ULL}},
    {{2134161ULL,4733120ULL}},
    {{1043989ULL,2334412ULL,1053054ULL,2373441ULL}},
    15780595376752460129ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
