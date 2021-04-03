package BFS;

import java.io.IOException;
import java.net.URISyntaxException;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;
import java.util.AbstractMap.SimpleEntry;

public class BFS {
	
	private static final String[] DIRECTION = {"N", "E", "S", "W"};
	private static final String[] DIRECTION_OPPOSITE = {"S", "W", "N", "E"};
	
	private static final List<SimpleEntry<Integer, Integer>> DIRECTIONS_SCAN = 
		Arrays.asList(new SimpleEntry<Integer, Integer>(1, 0), new SimpleEntry<Integer, Integer>(2, 1), 
				new SimpleEntry<Integer, Integer>(1, 2), new SimpleEntry<Integer, Integer>(0, 1));
	
	private static final List<SimpleEntry<Integer, Integer>> DIRECTION_LEFT = 
			Arrays.asList(new SimpleEntry<Integer, Integer>(-1,-1), 
					new SimpleEntry<Integer, Integer>(0,-1), new SimpleEntry<Integer, Integer>(1,-1));
	
	private static final List<SimpleEntry<Integer, Integer>> DIRECTION_MIDDLE = 
			Arrays.asList(new SimpleEntry<Integer, Integer>(-1,0), new SimpleEntry<Integer, Integer>(1,0));
	
	private static final List<SimpleEntry<Integer, Integer>> DIRECTION_RIGHT =
			Arrays.asList(new SimpleEntry<Integer, Integer>(-1,1), 
					new SimpleEntry<Integer, Integer>(0,1), new SimpleEntry<Integer, Integer>(1,1));

	private static final List<List<SimpleEntry<Integer, Integer>>> DIRECTIONS_SCAN_ALL = Arrays.asList(DIRECTION_LEFT, DIRECTION_MIDDLE, DIRECTION_RIGHT);
	
	private String[][] map;
	private boolean[][] mapVisited;
    private Labyrinth labyrinth;
    String fileName;

    public BFS(String fileName) throws IOException, URISyntaxException {
        labyrinth = new Labyrinth(fileName);
        map = new String[labyrinth.getSize().getKey()][labyrinth.getSize().getValue()];
        mapVisited = new boolean[labyrinth.getSize().getKey()][labyrinth.getSize().getValue()];
        for (int m = 0; m < map.length; m++) {
        	Arrays.fill(map[m], "?");
        }
        this.fileName = fileName;
    }

    public Labyrinth getLabyrinth() {
        return labyrinth;
    }

    public List<String> solve() {
        try {
			return findTreasure();
		} catch (IOException | URISyntaxException e) {
			e.printStackTrace();
			return null;
		}
    }
    
    public LinkedList<String> findTreasure() throws IOException, URISyntaxException {
    	Labyrinth labyrinthCopy = new Labyrinth(fileName);
    	LinkedList<LabyrinthPoint> toVisit = new LinkedList<LabyrinthPoint>();
    	toVisit.add(new LabyrinthPoint(labyrinthCopy.getPosition().getValue(), labyrinthCopy.getPosition().getKey()));
    	
    	while (!toVisit.isEmpty()) {
    		LabyrinthPoint currentPoint = toVisit.remove(toVisit.size() - 1);
    		moveToPoint(currentPoint.getPathToGet(), labyrinthCopy);
	    	SimpleEntry<Integer, Integer> position = labyrinthCopy.getPosition();
	    	
	    	for (int dirNumb = 0; dirNumb < DIRECTION.length; dirNumb++) {
	    		List<List<String>> scan = labyrinthCopy.scanAsString();
	    		int x = DIRECTIONS_SCAN.get(dirNumb).getKey();
	    		int y = DIRECTIONS_SCAN.get(dirNumb).getValue();
	    		
	    		if (scan.get(x).get(y).equals("D")) {
	    			LinkedList<String> toReturn = currentPoint.getPathToGet();
					toReturn.add(DIRECTION[dirNumb]);
					return toReturn;
	    		}
	    	}
	    	
	    	for (int i = 0; i < labyrinthCopy.scanAsString().size();) {
				for (List<SimpleEntry<Integer, Integer>> dir : DIRECTIONS_SCAN_ALL) {
					List<String> scan = labyrinthCopy.scanAsString().get(i);
					makeMap(position, scan, dir);
					i++;
				}
			}
	    	
	    	for (int toGo = 0; toGo < DIRECTION.length; toGo++) {
	    		if (labyrinthCopy.move(DIRECTION[toGo])) {
	    			position = labyrinthCopy.getPosition();
	    			if (!mapVisited[position.getValue()][position.getKey()]) {
	    				toVisit.add(new LabyrinthPoint(position.getValue(), position.getKey(), currentPoint, DIRECTION[toGo]));
	    				mapVisited[position.getValue()][position.getKey()] = true;
	    			}
	    			labyrinthCopy.move(DIRECTION_OPPOSITE[toGo]);
	    		}
	    	}
	    	
	    	labyrinthCopy = new Labyrinth(fileName);
    	}
    	return null;
    }

	private void makeMap(SimpleEntry<Integer, Integer> position, List<String> scan, List<SimpleEntry<Integer, Integer>> dir) {
		for (int dir_pos = 0; dir_pos < dir.size(); dir_pos++) {
			try {
				if (dir.size() == 2 && dir_pos == 1) {
					map[position.getValue() + dir.get(dir_pos).getKey()][position.getKey() + dir.get(dir_pos).getValue()] = scan.get(dir_pos + 1);
				} else {
					map[position.getValue() + dir.get(dir_pos).getKey()][position.getKey() + dir.get(dir_pos).getValue()] = scan.get(dir_pos);
				}
			} catch (ArrayIndexOutOfBoundsException e) {
				continue;
			}
		}
	}

	private void moveToPoint(LinkedList<String> path, Labyrinth mazeRunner) {
		for (String dir : path) {
			mazeRunner.move(dir);
		}
	}
	
    public static void main(String[] args) {
		try {
			BFS bfs = new BFS("map1.txt");
			
			List<String> solution = bfs.solve();
	    	for (int i = 0; i < bfs.map.length; i++) {
	        	for (int j = 0; j < bfs.map[i].length; j++) {
	        		System.out.print(bfs.map[i][j] + " ");
	        	}
	        	System.out.println();
	    	}
	    	System.out.println(solution);
		} catch (IOException e) {
			e.printStackTrace();
		} catch (URISyntaxException e) {
			e.printStackTrace();
		}
	}
	
}
