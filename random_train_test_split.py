import os, random
import shutil

isfile = os.path.isfile
join = os.path.join

directory = 'not-wake-word/'
destination_dir = 'test/'+directory

split_percentage = 20

def percent(total, percent) : 
  
    result = round((total * percent) / 100)
  
    return result 


number_of_files = sum(1 for item in os.listdir(directory) if isfile(join(directory, item)))
split_percent_value =  percent(number_of_files, split_percentage)

for i in range(split_percent_value):

    random_file = random.choice(os.listdir(directory))
    source = directory+random_file

    dest = shutil.move(source, destination_dir)

    print("File {} moved to {}, {} more file to go".format(source, dest, (split_percent_value - i)))


print("{}% percent of {} is {} (round off)".format(split_percentage, number_of_files, split_percent_value))
