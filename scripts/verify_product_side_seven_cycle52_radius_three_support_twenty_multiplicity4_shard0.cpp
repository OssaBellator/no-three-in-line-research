#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    4,
    2392,
    0,
    100,
    {{4228626ULL,4892556ULL}},
    {{20016951ULL,21246205ULL}},
    {{6664385ULL,7946426ULL,6896384ULL,7431473ULL}},
    17144806294662027537ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
