#include <bits/stdc++.h>
using namespace std;

struct DSU {
    vector<int> p;

    DSU(int n) {
        p.resize(n + 1);
        iota(p.begin(), p.end(), 0);
    }

    int find(int x) {
        return p[x] == x ? x : p[x] = find(p[x]);
    }

    bool unite(int a, int b) {
        a = find(a);
        b = find(b);
        if (a == b) return false;
        p[a] = b;
        return true;
    }
};

void user_logic(int N, int M, const vector<tuple<int,int,int>>& edges) {
    DSU dsu(N);

    long long ans = 0;
    vector<tuple<int,int,int>> pos;

    // Keep every non-positive edge.
    for (auto [u,v,w] : edges) {
        if (w <= 0)
            dsu.unite(u,v);
        else {
            ans += w;
            pos.push_back({w,u,v});
        }
    }

    // Keep only the positive edges necessary for connectivity.
    sort(pos.begin(), pos.end());

    for (auto [w,u,v] : pos) {
        if (dsu.unite(u,v))
            ans -= w;
    }

    cout << ans;
}

int main() {
    int N,M;
    cin >> N >> M;

    vector<tuple<int,int,int>> edges;
    for(int i=0;i<M;i++){
        int a,b,c;
        cin>>a>>b>>c;
        edges.push_back({a,b,c});
    }

    user_logic(N,M,edges);
}