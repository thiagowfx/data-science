#!/usr/bin/env python2
"""Calculates the number of deaths per book in the 'Song of Ice and Fire' series (aka Game of Thrones)."""

import csv
import numpy as np
import matplotlib.pyplot as plt

BOOKS = ('GoT', 'CoK', 'SoS', 'FfC', 'DwD')

def read_dataset():
    # i-th element (zero-indexed) with value n means that n deaths happened in (i+1)-th book
    book_deaths = len(BOOKS) * [0]

    with open('character-deaths.csv', 'r') as dataset_file:
        dataset = csv.DictReader(dataset_file)

        for row in dataset:
         book_of_death = row["Book of Death"]
     
         if book_of_death.isdigit():
             book_deaths[int(book_of_death) - 1] += 1
         
    return book_deaths
    
def plot_graph_bar(book_deaths):
    y_pos = np.arange(len(book_deaths))
    
    plt.bar(y_pos, book_deaths, align = 'center', alpha = 0.5)
    plt.xticks(y_pos, BOOKS)
    plt.xlabel('Book')
    plt.ylabel('Deaths')
    plt.title('Deaths by Book')
    
    plt.savefig('book_deaths.png')

if __name__ == '__main__':
    plot_graph_bar(read_dataset())