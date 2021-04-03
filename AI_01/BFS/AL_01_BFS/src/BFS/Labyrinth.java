package BFS;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.net.URISyntaxException;
import java.util.ArrayList;
import java.util.List;
import java.util.AbstractMap.SimpleEntry;

public class Labyrinth {
	
    private List<List<Integer>> map;
    private List<List<String>> rawMap;
    private List<List<String>> rightMap;
    private Integer x;
    private Integer y;
	
    public Labyrinth(String fileName) throws IOException, URISyntaxException {
    	
    	File file = new File(this.getClass().getResource(fileName).toURI());
        BufferedReader reader = new BufferedReader(new FileReader(file));
        String fileLine;
        map = new ArrayList<List<Integer>>();
        rawMap = new ArrayList<List<String>>();
        rightMap = new ArrayList<List<String>>();
        Integer lineNumber = 0;
        while ((fileLine = reader.readLine()) != null) {
            List<Integer> line = new ArrayList<Integer>();
            List<String> rawLine = new ArrayList<String>();
            List<String> rightMapLine = new ArrayList<String>();
            for (int lineValue = 0; lineValue < fileLine.length(); lineValue++) {
            	String lineValueString = Character.toString(fileLine.charAt(lineValue));
            	if (lineValueString.equals("*")) {
            		lineValueString = "*";
            	} else if (lineValueString.equals(" ")) {
            		lineValueString = "1";
            	}
            	rawLine.add(lineValueString);
            	rightMapLine.add(Character.toString(fileLine.charAt(lineValue)));
                if (Character.toString(fileLine.charAt(lineValue)).equals("*")) {
                    line.add(-1);
                } else if (fileLine.charAt(lineValue) == 's') {
                    line.add(0);
                    x = lineValue;
                    y = lineNumber;
                } else if (fileLine.charAt(lineValue) == 'D') {
                    line.add(-2);
                } else {
                    line.add(5);
                }
            }
            lineNumber++;
            map.add(line);
            rawMap.add(rawLine);
            rightMap.add(rightMapLine);
        }
    }
    
    public boolean move(String heading) {
        if (heading.equals("N") && (y > 0) && ((map.get(y - 1).get(x) >= 0) || (map.get(y - 1).get(x) == -2))) {
            y -= 1;
            return true;
        } else if (heading.equals("E") && (x < map.get(y).size() - 1) && ((map.get(y).get(x + 1) >= 0) || (map.get(y).get(x + 1) == -2))) {
            x += 1;
            return true;
        } else if (heading.equals("S") && (y < map.size() - 1) && ((map.get(y + 1).get(x) >= 0) || (map.get(y + 1).get(x) == -2))) {
            y += 1;
            return true;
        } else if (heading.equals("W") && (x > 0) && ((map.get(y).get(x - 1) >= 0) || (map.get(y).get(x - 1) == -2))) {
            x -= 1;
            return true;
        }
        return false;
    }

    public List<List<Integer>> scan() {
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        for (int i = x - 1; i < x + 2; i++) {
            List<Integer> line = new ArrayList<Integer>();
            for (int j = y - 1; j < y + 2; j++) {
                if (j >= 0 && map.size() > j && i >= 0 && map.get(j).size() > i) {
                    line.add(map.get(j).get(i));
                } else {
                    line.add(-1);
                }
            }
            result.add(line);
        }
        return result;
    }

    public List<List<String>> scanAsString() {
        List<List<String>> result = new ArrayList<>();
        for (int i = x - 1; i < x + 2; i++) {
            List<String> line = new ArrayList<>();
            for (int j = y - 1; j < y + 2; j++) {
                if (j >= 0 && map.size() > j && i >= 0 && map.get(j).size() > i) {
                    line.add(rawMap.get(j).get(i));
                } else {
                    line.add("#");
                }
            }
            result.add(line);
        }
        return result;
    }

    public SimpleEntry<Integer, Integer> getPosition() {
        return new SimpleEntry<Integer, Integer>(x, y);
    }

    public SimpleEntry<Integer, Integer> getSize() {
        if (map != null && map.get(0) != null) {
            return new SimpleEntry<Integer, Integer>(map.size(), map.get(0).size());
        }
        return null;
    }
    
    public List<List<String>> getMap() {
    	return rightMap;
    }
    
}
