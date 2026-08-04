#!/usr/bin/env python3
from pathlib import Path
import subprocess
import tempfile

HERE = Path(__file__).resolve().parent
source = (HERE / "check_prefix_all_physical_compositions.cpp").read_text()
source = source.replace(
    "auto matchings=minimumCrossMatchings();assert(matchings.size()==104);auto comps=compositions();assert(comps.size()==1024);",
    "auto matchings=minimumCrossMatchings();assert(matchings.size()==104);auto allcomps=compositions();vector<vector<int>> comps;for(auto const&c:allcomps)if(c.size()<=3)comps.push_back(c);assert(comps.size()==56);",
)
source = source.replace(
    "auto route=routes.front();long long maximum=0;int passed=0;\n"
    "   for(auto const&composition:comps){if(embed(deletions[deletion],route,composition,maximum))passed++;audits++;}\n"
    "   if(passed!=1024){cerr<<\"fail matching=\"<<mi<<\" deletion=\"<<deletion<<\" passed=\"<<passed<<\"\\n\";return 3;}\n"
    "   coordinateHist[deletion][maximum]++;cases++;",
    "long long maximum=0;long long passed=0;\n"
    "   for(auto const&route:routes)for(auto const&composition:comps){if(embed(deletions[deletion],route,composition,maximum))passed++;audits++;}\n"
    "   if(passed!=(long long)routes.size()*(long long)comps.size()){cerr<<\"fail matching=\"<<mi<<\" deletion=\"<<deletion<<\" passed=\"<<passed<<\" expected=\"<<routes.size()*comps.size()<<\"\\n\";return 3;}\n"
    "   coordinateHist[deletion][maximum]++;cases++;",
)
assert "routes.front()" not in source

with tempfile.TemporaryDirectory() as directory:
    directory = Path(directory)
    cpp = directory / "kernel.cpp"
    binary = directory / "kernel"
    cpp.write_text(source)
    subprocess.run(["c++", "-O3", "-std=c++17", str(cpp), "-o", str(binary)], check=True)
    result = subprocess.run([str(binary)], check=True, capture_output=True, text=True)

assert result.stdout.splitlines() == [
    "matchings=104 cases=208 compositions=56 audits=1677312",
    "distance_hist 4:208",
    "optimal_route_count_hist 144:208",
    "deletion=0 maxcoord 120:104",
    "deletion=1 maxcoord 154:104",
]
assert result.stderr == ""
print({
    "minimum_crossing_matchings": 104,
    "deletion_cases": 2,
    "optimal_routes_per_case": 144,
    "compositions_with_at_most_three_runs": 56,
    "route_composition_audits": 1677312,
    "failures": 0,
    "maximum_coordinate_by_deletion": {"delete_0_2": 120, "delete_3_5": 154},
    "status": "passed",
})
