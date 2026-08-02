#include "product_side_seven_cache_engine.hpp"

const std::array<CaseData,64> CASES = {{
#include "data/product_side_seven_multiplicity9_0.inc"
#include "data/product_side_seven_multiplicity9_1.inc"
}};

int main(int argc,char**argv) {
    return verify_tier(argc,argv,CASES,9,64,15111175ULL);
}
