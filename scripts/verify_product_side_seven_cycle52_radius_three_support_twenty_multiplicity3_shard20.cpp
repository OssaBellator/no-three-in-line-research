#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    3,
    3544,
    2000,
    100,
    {{4912632ULL,4230024ULL}},
    {{24609044ULL,21813621ULL}},
    {{8523632ULL,7261420ULL,8070294ULL,6655266ULL}},
    13076377016111339538ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
