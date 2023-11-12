#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * insert_node - frees a listint_t list
 * @head: pointer to list to be freed
 * @number: number to be inserted
 * Return:  the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
listint_t *current_node = malloc(sizeof(listint_t));
listint_t *new_node = malloc(sizeof(listint_t));
current_node = *head;
new_node->n = number;
if (current_node == NULL || new_node == NULL)
return (NULL);
if (current_node->n > number)
{
new_node->next = current_node;
*head = new_node;
return (new_node);
}
else if (current_node->next == NULL)
{
return add_nodeint_end(head, number);
}
else
{
free(new_node);
return insert_node(&current_node->next, number);
}
}