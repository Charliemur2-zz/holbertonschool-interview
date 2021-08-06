#include "binary_trees.h"
#include <stdlib.h>

/**
 * binary_tree_node - creates a node of a binary tree
 * @parent: pointer to the parent.
 * @value: value of the new node.
 *
 * Return: return a pointer to the new node, or NULL on failure.
 */

binary_tree_t *binary_tree_node(binary_tree_t *parent, int value)
{
	binary_tree_t *new;

	new = malloc(sizeof(binary_tree_t));
	if (!new)
		return (NULL);

	new->left = new->right = NULL;
	new->n = value;
	new->parent = parent;

	return (new);
}
