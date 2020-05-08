/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class CousinsInBinaryTree {
	private int depth = 0;
	public boolean isCousins(TreeNode root, int x, int y) {
        
        if(isRoot(root, x, y)) {
			return false;
		}
        int xParent = findParent(root, x, 0);
        int xDepth = this.depth;
        int yParent = findParent(root, y, 0);
        int yDepth = this.depth;
        
        if(xDepth == yDepth && xParent != yParent) {
        	return true;
        } else {
        	return false;
        }
	}
    
    private boolean isRoot(TreeNode root, int x, int y) {
    	return (root.val == x || root.val == y) ? true : false;
	}

    public int findParent(TreeNode root, int x, int depth){

        if(root == null){
            return 0;
        }

        //왼쪽 자식과 일치하는가?
        if(root.left != null && root.left.val == x){
            this.depth = depth;
        	return root.val;
        }
        //오른쪽 자식과 일치하는가?
        if(root.right != null && root.right.val == x){
        	this.depth = depth;
            return root.val;
        }

        return findParent(root.left, x, depth+1) + findParent(root.right, x, depth+1);
    }
}