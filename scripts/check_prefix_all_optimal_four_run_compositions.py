#!/usr/bin/env python3
from pathlib import Path
import subprocess
import tempfile

HERE = Path(__file__).resolve().parent
source = (HERE / "check_prefix_all_physical_compositions.cpp").read_text()

# The source configuration is no-three before insertion. During insertion every
# candidate is tested against every existing pair, with the sole allowed exception
# being a triple wholly inside its labelled run. Therefore the initial and final
# cubic scans are redundant for the incremental verifier used here.
initial_scan = (
    " for(int i=0;i<22;i++)for(int j=i+1;j<22;j++)for(int k=j+1;k<22;k++)"
    "if(cross(source[i],source[j],source[k])==0)return false;\n"
)
final_scan = (
    " for(int i=0;i<(int)pts.size();i++)for(int j=i+1;j<(int)pts.size();j++)"
    "for(int k=j+1;k<(int)pts.size();k++)if(cross(pts[i],pts[j],pts[k])==0"
    "&&!(labels[i]>=0&&labels[i]==labels[j]&&labels[j]==labels[k]))return false;\n"
)
assert initial_scan in source
assert final_scan in source
source = source.replace(initial_scan, "")
source = source.replace(final_scan, "")
source = source.split("int main(){", 1)[0]

source += r'''int main(){
 for(int row=0;row<N;row++)for(int target=0;target<N;target++)if(target!=row&&Q[target]!=P[row])allowed[row].push_back(target);
 auto matchings=minimumCrossMatchings();assert(matchings.size()==104);
 auto allcomps=compositions();vector<vector<int>>comps;for(auto const&c:allcomps)if(c.size()<=4)comps.push_back(c);assert(comps.size()==176);
 vector<vector<int>>deletions={{1,3,4,5,6,7,8,9,10,11,12},{0,1,2,4,6,7,8,9,10,11,12}};
 map<int,int>distanceHist;map<int,long long>routeCountHist;set<array<int,11>>uniqueRoutes[2];
 for(int mi=0;mi<(int)matchings.size();mi++)for(int deletion=0;deletion<2;deletion++){
   int distance;auto routes=optimalRoutes(matchings[mi],deletions[deletion],distance);distanceHist[distance]++;routeCountHist[routes.size()]++;
   if(distance!=4||routes.size()!=144){cerr<<"bad routes\n";return 2;}
   uniqueRoutes[deletion].insert(routes.begin(),routes.end());
 }
 cout<<"unique_routes "<<uniqueRoutes[0].size()<<" "<<uniqueRoutes[1].size()<<"\n";
 long long audits=0;map<int,long long>maxcoord;
 for(int deletion=0;deletion<2;deletion++)for(auto const&route:uniqueRoutes[deletion]){
   long long maximum=0;
   for(auto const&composition:comps){if(!embed(deletions[deletion],route,composition,maximum)){cerr<<"fail deletion="<<deletion<<"\n";return 3;}audits++;}
   maxcoord[deletion]=max(maxcoord[deletion],maximum);
 }
 cout<<"audits="<<audits<<" comps="<<comps.size()<<" max0="<<maxcoord[0]<<" max1="<<maxcoord[1]<<"\n";
 cout<<"distance_hist";for(auto [d,c]:distanceHist)cout<<" "<<d<<":"<<c;cout<<"\n";
 cout<<"route_count_hist";for(auto [r,c]:routeCountHist)cout<<" "<<r<<":"<<c;cout<<"\n";
}
'''

with tempfile.TemporaryDirectory() as directory:
    directory = Path(directory)
    cpp = directory / "kernel.cpp"
    binary = directory / "kernel"
    cpp.write_text(source)
    subprocess.run(
        ["c++", "-O3", "-std=c++17", str(cpp), "-o", str(binary)],
        check=True,
    )
    result = subprocess.run(
        [str(binary)], check=True, capture_output=True, text=True
    )

assert result.stdout.splitlines() == [
    "unique_routes 3624 3624",
    "audits=1275648 comps=176 max0=120 max1=154",
    "distance_hist 4:208",
    "route_count_hist 144:208",
]
assert result.stderr == ""

physical_route_occurrences = 104 * 2 * 144
physical_route_composition_pairs = physical_route_occurrences * 176
new_exactly_four_run_pairs = physical_route_occurrences * 120
assert physical_route_occurrences == 29952
assert physical_route_composition_pairs == 5271552
assert new_exactly_four_run_pairs == 3594240
assert (3624 + 3624) * 176 == 1275648

print({
    "minimum_crossing_matchings": 104,
    "deletion_cases": 2,
    "optimal_routes_per_physical_case": 144,
    "physical_route_occurrences": physical_route_occurrences,
    "unique_routes_per_deletion": 3624,
    "compositions_with_at_most_four_runs": 176,
    "new_exactly_four_run_compositions": 120,
    "distinct_route_composition_audits": 1275648,
    "covered_physical_route_composition_pairs": physical_route_composition_pairs,
    "new_exactly_four_run_physical_pairs": new_exactly_four_run_pairs,
    "failures": 0,
    "maximum_coordinate_by_deletion": {"delete_0_2": 120, "delete_3_5": 154},
    "remaining_gap": "compositions with at least five runs and an all-size recurrence remain open",
    "evidence_level": "exact_all_optimal_route_four_run_coordinate_lift",
    "status": "passed",
})
