#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    400,
    10,
    {{798628ULL,556036ULL}},
    {{2576501ULL,1802909ULL}},
    {{1215496ULL,866237ULL,1163834ULL,798914ULL}},
    16705625326510863433ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
