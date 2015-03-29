/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    bool isSameTree(TreeNode *p, TreeNode *q) {
        bool right_same=1;
        bool left_same=1;
        if((p==NULL)&&(q==NULL))
            return true;
        else if((p==NULL)||(q==NULL))
            return false;
            
        if(p->val!=q->val)
            return false;
            
        if((p->left==NULL)&&(q->left==NULL))
            right_same=isSameTree(p->right,q->right);
        else if((p->left!=NULL)&&(q->left!=NULL)){
            left_same=isSameTree(p->left,q->left);
            right_same=isSameTree(p->right,q->right);
        }
        else
            return false;
        
            
        if((right_same==false)||(left_same==false))
            return false;
        else
            return true ;
    }
};
