from itertools import permutations
import random
from copy import deepcopy
from PIL import Image, ImageDraw, ImageFont
import datetime

def distance(p1, p2):
	return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2) ** 0.5

def total_distance(points):
	return sum([distance(point, points[index + 1]) for index, point in enumerate(points[:-1])])


def cartesian_matrix(coordinates):
	'''
	Creates a distance matrix for the city coords using straight line distances
	computed by the Euclidean distance of two points in the Cartesian Plane.
	'''
	matrix = {}
	for i, p1 in enumerate(coordinates):
		for j, p2 in enumerate(coordinates):
			matrix[i,j] = distance(p1,p2)
	return matrix

def read_coords(file_handle):
	coords = []
	for line in file_handle:
		x,y = line.strip().split(',')
		coords.append((float(x), float(y)))
	return coords

def tour_length(matrix, tour):
	"""Sum up the total length of the tour based on the distance matrix"""
	result = 0
	num_cities = len(list(tour))
	for i in range(num_cities):
		j = (i+1) % num_cities
		city_i = tour[i]
		city_j = tour[j]
		result += matrix[city_i, city_j]
	return result

def all_pairs(size, shuffle = random.shuffle):
	r1 = list(range(size))
	r2 = list(range(size))
	if shuffle:
		shuffle(r1)
		shuffle(r2)
	for i in r1:
		for j in r2:
			yield(i,j) # yield is an iterator function
			# for each call of the generator it returns the next value in yield

# Tweak 1
def swapped_cities(tour):
	"""
	Generator to create all possible variations where two 
	cities have been swapped
	"""
	ap = all_pairs(len(tour))
	for i,j in ap:
		if i < j:
			copy = deepcopy(tour)
			copy[i], copy[j] = tour[j], tour[i]
			yield copy

# Tweak 2
def reversed_sections(tour):
	"""
	Generator to return all possible variations where the
	section between two cities are swapped.
	It preserves entire sections of a route,
	yet still affects the ordering of multiple cities in one go.
	"""
	ap = all_pairs(len(tour))
	for i,j in ap:
		if i != j:
			#print("indices from:",i, "to", j)
			copy = deepcopy(tour)
			if i < j:
				copy[i:j+1] = reversed(tour[i:j+1])
			else:
				copy[i+1:] = reversed(tour[:j])
				copy[:j] = reversed(tour[i+1:])
			if copy != tour: # not returning same tour
				yield copy

def init_random_tour(tour_length):
	tour = list(range(tour_length))
	random.shuffle(list(tour))
	return tour

def write_tour_to_img(coords, tour, title, img_file):
	padding = 20
	# shift all coords in a bit
	coords = [(x+padding,y+padding) for (x,y) in coords]
	maxx, maxy = 0,0
	for x,y in coords:
		maxx = max(x,maxx)
		maxy = max(y,maxy)
	maxx += padding
	maxy += padding
	img = Image.new("RGB",(int(maxx), int(maxy)), color=(255,255,255))
	
	font=ImageFont.load_default()
	d=ImageDraw.Draw(img);
	num_cities = len(tour)
	for i in range(num_cities):
		j = (i+1) % num_cities
		city_i = tour[i]
		city_j = tour[j]
		x1,y1 = coords[city_i]
		x2,y2 = coords[city_j]
		d.line((int(x1), int(y1), int(x2), int(y2)), fill=(0,0,0))
		d.text((int(x1)+7, int(y1)-5), str(i), font=font, fill=(32,32,32))
	
	
	for x,y in coords:
		x,y = int(x), int(y)
		d.ellipse((x-5, y-5, x+5, y+5), outline=(0,0,0), fill=(196,196,196))
	
	d.text((1,1), title, font=font, fill=(0,0,0))
	
	del d
	img.save(img_file, "PNG")

def hc(init_function, move_operator, objective_function, max_evaluations):
	'''
	Hillclimb until either max_evaluations is 
	reached or we are at a local optima.
	'''
	best = init_function()
	best_score = objective_function(best)
	
	num_evaluations = 1
	
	while num_evaluations < max_evaluations:
		# move around the current position
		move_made = False
		for next in move_operator(best):
			if num_evaluations >= max_evaluations:
				break
			
			next_score = objective_function(next)
			num_evaluations += 1
			if next_score < best_score:
				best = next
				best_score = next_score
				move_made = True
				break # depth first search
		if not move_made:
			break # couldn't find better move - must be a local max
	return (num_evaluations, best_score, best)


def do_hc_evaluations(evaluations, move_operator, init_function, objective_function, coords):
	max_evaluations = evaluations
	then = datetime.datetime.now()
	num_evaluations, best_score, best = hc(init_function, move_operator, objective_function, max_evaluations)
	now = datetime.datetime.now()

	print("computation time ", now - then)
	print("best score:", best_score)
	print("best route:", best)
	filename = "test"+str(max_evaluations)+".PNG"
	write_tour_to_img(coords, best, filename, open(filename, "ab"))

def sa_hc(init_function, move_operator, objective_function, max_evaluations, number_tweaks):
	'''
	Steepest Ascent Hillclimb until either max_evaluations is 
	reached or we are at a local optimum.
	'''
	S = init_function()
	S_score = objective_function(S)
	num_evaluations = 1
	while num_evaluations < max_evaluations:
		# move around the current position
		move_made = False
		for next in move_operator(S):
			R = next
			R_score = objective_function(R)
			
			for i in range(number_tweaks):
				num_evaluations += 1
				if num_evaluations >= max_evaluations:
					break
				W = move_operator(S).__next__()
				W_score = objective_function(W)
				if W_score < R_score:
					R = W
					R_score = W_score
			if R_score < S_score:
				print(S_score)
				S = R
				S_score = R_score
				move_made = True
				break # depth first search
		if not move_made:
			break # couldn't find better move - must be a local max
	return (num_evaluations, best_score, best)

def sa_hc_wr(init_function, move_operator, objective_function, max_evaluations, number_tweaks):
	'''
	Steepest Ascent Hillclimb with replacement until either max_evaluations is 
	reached or we are at a local optimum.
	'''
	S = init_function()
	S_score = objective_function(S)
	best = S 
	best_score = S_score
	num_evaluations = 1

	while num_evaluations < max_evaluations:
		# move around the current position
		move_made = False
		for next in move_operator(S):
			R = next
			R_score = objective_function(R)
			
			for i in range(number_tweaks):
				num_evaluations += 1
				if num_evaluations >= max_evaluations:
					break
				W = move_operator(S).__next__()
				W_score = objective_function(W)
				if W_score < R_score:
					R = W
					R_score = W_score
			S = R
			S_score = R_score
			if S_score < best_score:
				print(best_score)
				best = S
				best_score = S_score
				move_made = True
				break # depth first search
		if not move_made:
			break # couldn't find better move - must be a local max
	return (num_evaluations, best_score, best)

def evaluate_hc(hc_func, evaluations, move_operator, init_function, objective_function, coords, number_tweaks):
	max_evaluations = evaluations
	then = datetime.datetime.now()
	num_evaluations, best_score, best = hc_func(init_function, move_operator, objective_function, max_evaluations, number_tweaks)
	now = datetime.datetime.now()

	print("computation time ", now - then)
	print("best score:", best_score)
	print("best route:", best)
	filename = "test"+str(max_evaluations)+".PNG"
	write_tour_to_img(coords, best, filename, open(filename, "ab"))


def main():
	init_function = lambda: init_random_tour(len(coords))
	objective_function = lambda tour: tour_length(matrix, tour)

	with open('city100.txt', 'r') as coord_file:
		coords = read_coords(coord_file)
	matrix = cartesian_matrix(coords)

	evaluate_hc(sa_hc_wr, 100000, reversed_sections, init_function, objective_function, coords, 200)

if __name__ == "__main__":
	main()
