#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    1140,
    10,
    {{788210ULL,730568ULL}},
    {{2578320ULL,2390872ULL}},
    {{1221980ULL,1122450ULL,1118349ULL,1066310ULL}},
    6103704461218321733ULL
};

int main(int argc,char** argv) { return verify_tier_shard_digest(argc,argv,EXPECTED); }
