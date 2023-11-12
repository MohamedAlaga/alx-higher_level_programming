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
    listint_t *new;
    listint_t *current;
    listint_t *prev;
    current = *head;
    prev = NULL;
    new = malloc(sizeof(listint_t));
    if (new == NULL)
        return (NULL);
    new->n = number;
    new->next = NULL;
    if (*head == NULL)
        *head = new;
    else
    {
        while (current != NULL)
        {
            if (current->n > number)
            {
                if (prev == NULL)
                {
                    new->next = current;
                    *head = new;
                    return (new);
                }
                else
                {
                    prev->next = new;
                    new->next = current;
                    return (new);
                }
            }
            prev = current;
            current = current->next;
        }
        prev->next = new;
    }
    return (new);
}
