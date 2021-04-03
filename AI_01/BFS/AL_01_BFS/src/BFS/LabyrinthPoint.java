package BFS;

import java.util.LinkedList;

public class LabyrinthPoint {
	private Integer x;
	private Integer y;
	/**
	 * Path what to do to get to this point.
	 */
	private LinkedList<String> pathToGet = new LinkedList<String>();
	/**
	 * Previous element from where you can get to this element.
	 */
	private LabyrinthPoint parent;
	
	/**
	 * Used for starting point.
	 * @param x X coordinate.
	 * @param y Y coordinate.
	 */
	public LabyrinthPoint(Integer x, Integer y) {
		this.x = x;
		this.y = y;
	}
	
	/**
	 * Creates elements with full pathToGet.
	 * @param x X coordinate.
	 * @param y Y coordinate.
	 * @param parent Previous element
	 * @param path Direction from parent element to get to this element.
	 */
	public LabyrinthPoint(Integer x, Integer y, LabyrinthPoint parent, String path) {
		this.x = x;
		this.y = y;
		pathToGet.addAll(parent.getPathToGet());
		pathToGet.add(path);
		this.parent = parent;
	}
	
	public LinkedList<String> getPathToGet() {
		return pathToGet;
	}

	public void setPathToGet(LinkedList<String> pathToGet) {
		this.pathToGet = pathToGet;
	}

	public LabyrinthPoint getParent() {
		return parent;
	}

	public void setParent(LabyrinthPoint parent) {
		this.parent = parent;
	}

	public int getX() {
		return x;
	}

	public void setX(int x) {
		this.x = x;
	}

	public int getY() {
		return y;
	}

	public void setY(int y) {
		this.y = y;
	}
}
