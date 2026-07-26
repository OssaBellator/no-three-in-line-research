#include "product_side_seven_cache_engine.hpp"

const std::array<CaseData,164> CASES = {{
#include "data/product_side_seven_multiplicity10_0.inc"
#include "data/product_side_seven_multiplicity10_1.inc"
#include "data/product_side_seven_multiplicity10_2.inc"
#include "data/product_side_seven_multiplicity10_3.inc"
}};

int main(int argc,char**argv) {
    return verify_tier(argc,argv,CASES,10,164,61678543ULL);
}
