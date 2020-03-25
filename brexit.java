import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.LinkedList;
import java.util.List;
import java.util.StringTokenizer;

/**
 * Solution to https://open.kattis.com/problems/brexit
 */
public class brexit {
    private List<Integer>[] partnerships;
    private boolean[] leftUnion;
    private int[] leavingNeighbours;

    private final int countryCount; // 2≤C≤200000
    private final int partnershipCount; // 1≤P≤300000
    private final int homeCountry;
    private final int Britain;

    public brexit(BufferedReader br) throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine()); // entire damn file
        countryCount = Integer.parseInt(st.nextToken());
        partnershipCount = Integer.parseInt(st.nextToken());
        homeCountry = Integer.parseInt(st.nextToken()) - 1;
        Britain = Integer.parseInt(st.nextToken()) - 1;

        // initialize
        partnerships = new List[countryCount];
        leftUnion = new boolean[countryCount];
        leavingNeighbours = new int[countryCount];
        for (int i = 0; i < countryCount; i++) {
            partnerships[i] = new LinkedList<>();
        }

        // read edges
        // undirected graph, reading both
        for (int i = 0; i < partnershipCount; i++) {
            st = new StringTokenizer(br.readLine());
            int from = Integer.parseInt(st.nextToken());
            int to = Integer.parseInt(st.nextToken());
            partnerships[from - 1].add(to - 1);
            partnerships[to - 1].add(from - 1);
        }

    }

    /**
     * BFS traversal of graph to leave trade union
     * Leaving only if more than half of neighbouring nodes have left
     */
    public String leaveOrStay() {
        ArrayDeque<Integer> queue = new ArrayDeque<>(countryCount / 2);
        // Britain leaves the union and starts the chain reaction
        //queue.addAll(partnerships[Britain]);
        // ONLY BRITAIN NOW
        queue.add(Britain);
        leftUnion[Britain] = true;

        while (!queue.isEmpty()) {
            int country = queue.poll();

            // we know it shall leave!
            // signal to all neighbours that we have left
            for (int neighbour : partnerships[country]) {
                leavingNeighbours[neighbour]++;
                if (!leftUnion[neighbour] && shouldLeave(neighbour)) {
                    // add to queue and make it leave!
                    queue.add(neighbour);
                    leftUnion[neighbour] = true;
                }
            } // END FOR
        } // END WHILE

        return leftUnion[homeCountry] ? "leave" : "stay";
    }

    /**
     * Leave if >= half of neighbours have left
     */
    private boolean shouldLeave(int country) {
        return leavingNeighbours[country] >= (int) (partnerships[country].size() / 2.0 + 0.5);
    }

    public static void main(String[] args) {
        try (InputStreamReader fr = new InputStreamReader(System.in);
             BufferedReader br = new BufferedReader(fr)) {

            brexit brexit = new brexit(br);
            System.out.println(brexit.leaveOrStay());

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
