#include<stdio.h>
#include<stdlib.h>
struct Node{
    int data;
    struct Node* right;
    struct Node* left;
};
struct Node* create(int value){
    struct Node *t=(struct Node *)malloc(sizeof(struct Node));
    t->data=value;
    t->left=t->right=NULL;
    return t;
}
struct Node* insert(struct Node* root,int value){
    if (root==NULL)
    {
        root=newnode(value);
        return root;
    }
     if (value<root->data)
    {
        root->left= (create(root->left,value));
    }
    else
    {
        root->right=(create(root->right,value));
    }
    return root;
}
void inorder(struct Node* root)
{
    if (root!=NULL)
    {
        inorder(root->left);
        printf("%d\n",root->data);
        inorder(root->right);
    }
}

int main()
{
    struct Node *root=NULL;
    root=insert(root,10);
    root=insert(root,20);
    root=insert(root,30);
    inorder(root);
    return 0;
}