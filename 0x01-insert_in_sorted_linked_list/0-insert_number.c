#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * insert_node - function in C that inserts a number into a sorted singly linked list.
 * @head: pointer to pointer of first node of listint_t list.
 * @number: integer to be included in new node
 * Return: the address of the new node, or NULL if it failed.
 */

listint_t *insert_node(listint_t **head, int number)
{
    listint_t *new = NULL;
    listint_t *temp;

    temp = *head;

    new = malloc(sizeof(listint_t));
    if (new == NULL)
        return (NULL);

    new->n = number;

    if (*head == NULL || temp->n >= new->n)
    {
        *head = new;
        new->next = temp;
    }
    else
    {
        while (temp->next != NULL)
        {
            if (temp->next->n <= new->n)
                temp = temp->next;
            else
                break;
        }
        new->next = temp->next;
        temp->next = new;
    }
    return (new);
}
