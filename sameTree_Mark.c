3/29 CodeInterview

Question:

Given two binary trees, write a function to check if they are equal or not.

Two binary trees are considered equal if they are structurally identical and the nodes have the same value.

/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
bool isSameTree(struct TreeNode *p, struct TreeNode *q) {
	/* check structure */
	if(p == NULL && q == NULL){
		return 1;
	}else if(p != NULL && q == NULL){
	    return 0;
	}else if(p == NULL && q != NULL){
	    return 0;
	}
	
	/* check val */
	if(p->val != q->val) {
		return 0;
	}
	    
	return (isSameTree(p -> right, q -> right) && isSameTree(p -> left, q -> left));
}