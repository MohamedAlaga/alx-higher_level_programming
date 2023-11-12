#include <stdlib.h>
#include "lists.h"
/**
 * free_listint - frees a listint_t list
 * @head: pointer to list to be freed
 * Return: void
 */
listint_t *insert_node(listint_t **head, int number)
{
if(add_nodeint_end(head, number))
return (*head);
else
return (NULL);
}