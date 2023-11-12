#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * free_listint - frees a listint_t list
 * @head: pointer to list to be freed
 * Return: void
 */
listint_t *insert_node(listint_t **head, int number)
{
listint_t *current_node = malloc(sizeof(listint_t));
listint_t *new_node = malloc(sizeof(listint_t));
current_node = *head;
new_node->n = number;
if (*head == NULL)
{
new_node->next = NULL;
*head = new_node;
return (new_node);
}
else if (current_node == NULL || new_node == NULL)
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
