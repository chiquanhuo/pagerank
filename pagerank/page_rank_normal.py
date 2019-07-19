# -*- coding: utf-8 -*-

import numpy as np


class PageRank(object):

	def __init__(self):
		self.epsilon = 10**(-4)
		self.beta = 0.8
		self.num_nodes = 3

		self.link_nodes = np.zeros((self.num_nodes, self.num_nodes,), dtype=np.int64)
		self.link_matrix = []

		self.new_page_rank = None
		self.old_page_rank = None

	def get_test(self):
		# build a matrix store the i->j when i->j has degree, link_nodes[i,j] =1
		test_file = open('test.dat', 'r')  # get data format: from node, to node; for example: 1,2
		for line in test_file:
			temp_line = line.split(' ')
			self.link_nodes[int(temp_line[0])-1][int(temp_line[1])-1] += 1  # give the initial number
		link_sum = np.sum(self.link_nodes, axis=1)
		i = 0
		self.link_matrix = []
		while i < self.num_nodes:
			temp_link = np.full(self.num_nodes, link_sum[i], dtype=np.float64)
			self.link_matrix.append(temp_link)
			i += 1

		self.link_matrix = self.link_nodes / self.link_matrix  # compute the out degree of node i
		return True

	def compute_page_rank(self):
		self.old_page_rank = np.full(int(self.num_nodes), 1.0/float(self.num_nodes), dtype=np.float64)
		# print self.old_page_rank
		self.new_page_rank = np.zeros(self.num_nodes, dtype=np.float64)
		convergence = np.sum(self.old_page_rank)

		while convergence > float(self.epsilon):
			temp_old_page_rank = np.empty([int(self.num_nodes), int(self.num_nodes)], dtype=np.float64)
			# repeat the rank of node i in every row.
			i = 0
			while i < self.num_nodes:
				temp_old_page_rank[i, :] = self.old_page_rank[i]
				i += 1

			temp_new_rank_matrix = temp_old_page_rank * self.link_matrix
			temp_new_rank_matrix = temp_new_rank_matrix * float(self.beta)
			# get the temp new rank of node j = sum(matrix, col)
			temp_new_rank_j = np.sum(temp_new_rank_matrix, axis=0)
			s = float(np.sum(temp_new_rank_j))
			# print s

			self.new_page_rank = temp_new_rank_j + (1.0-s)/float(self.num_nodes)
			# print self.new_page_rank
			# abs|rnew-rold|
			convergence_arr = np.absolute(self.new_page_rank - self.old_page_rank)
			# sum of difference
			convergence = float(np.sum(convergence_arr))
			self.old_page_rank = self.new_page_rank
			# print self.old_page_rank

		print self.old_page_rank
		print np.sum(self.old_page_rank)

		write_file = open('output1.txt', 'w')
		i = 0
		while i < self.num_nodes:
			write_file.write(str(self.old_page_rank[i]))
			write_file.write('\n')
			i += 1


def main():
	model = PageRank()
	model.get_test()
	model.compute_page_rank()


if __name__ == '__main__':
	main()
