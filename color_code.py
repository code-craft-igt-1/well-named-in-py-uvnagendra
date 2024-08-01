import configparser
config = configparser.ConfigParser()
config.read('config.ini')
MAJOR_COLORS_LIST = config.get('Colors', 'major_colors').split(',')
MINOR_COLORS_LIST = config.get('Colors', 'minor_colors').split(',')

def get_color_from_pair_number(pair_number):
  zero_based_pair_number = pair_number - 1
  major_index = zero_based_pair_number // len(MINOR_COLORS_LIST)
  if major_index >= len(MAJOR_COLORS_LIST):
    raise Exception('Major index out of range')
  minor_index = zero_based_pair_number % len(MINOR_COLORS_LIST)
  if minor_index >= len(MAJOR_COLORS_LIST):
    raise Exception('Minor index out of range')
  return MAJOR_COLORS_LIST[major_index], MINOR_COLORS_LIST[minor_index]

def get_pair_number_from_color(major_color, minor_color):
  try:
    major_index = MAJOR_COLORS_LIST.index(major_color)
  except ValueError:
    raise Exception('Major color {} does not exist'.format(major_color))
  try:
    minor_index = MINOR_COLORS_LIST.index(minor_color)
  except ValueError:
    raise Exception('Minor color {} does not exist'.format(minor_color))
  return major_index * len(MINOR_COLORS_LIST) + minor_index + 1

def print_reference_manual():
  for i in range(1, len(MAJOR_COLORS_LIST) * len(MINOR_COLORS_LIST) + 1):
    print(f'{i}: {get_color_from_pair_number(i)}')