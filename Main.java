import java.util.*;

class BeingZero {
    public boolean isCyclic(int N, int E, int u[], int v[]) {
        // Adjacency List representation
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i <= N; i++) {
            adj.add(new ArrayList<>());
        }

        // Construct the graph
        for (int i = 0; i < E; i++) {
            adj.get(u[i]).add(v[i]);
            adj.get(v[i]).add(u[i]);  // Since it's an undirected graph
        }

        boolean[] visited = new boolean[N + 1];

        // Check for cycles in each connected component
        for (int i = 1; i <= N; i++) {
            if (!visited[i]) {
                if (dfs(i, -1, visited, adj)) {
                    return true;  // Cycle detected
                }
            }
        }
        return false;  // No cycle found
    }

    private boolean dfs(int node, int parent, boolean[] visited, List<List<Integer>> adj) {
        visited[node] = true;

        for (int neighbor : adj.get(node)) {
            if (!visited[neighbor]) {
                if (dfs(neighbor, node, visited, adj)) {
                    return true;
                }
            } else if (neighbor != parent) {
                return true;  // Cycle detected
            }
        }
        return false;
    }

    public static void main(String[] args) {
        BeingZero bz = new BeingZero();

        // Hardcoded Example 1 (Cycle Exists)
        int N1 = 4, E1 = 4;
        int[] u1 = {1, 1, 2, 3};
        int[] v1 = {2, 3, 4, 4};
        System.out.println("Cycle Exists? " + bz.isCyclic(N1, E1, u1, v1));  // Output: true

        // Hardcoded Example 2 (No Cycle)
        int N2 = 4, E2 = 3;
        int[] u2 = {1, 1, 2};
        int[] v2 = {2, 3, 4};
        System.out.println("Cycle Exists? " + bz.isCyclic(N2, E2, u2, v2));  // Output: false
    }
}
