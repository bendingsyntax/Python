#Daniel De Jesus
#11/05/17

#comments---------------------------------

#imports----------------------------------

#input------------------------------------
def menu():
	print("please select an option")
	print("1. hello_name")
	print("2. make_abba")
	print("3. make_tags")
	print("4. make_out_word")
	print("5. extra_end")
	print("6. first_two")
	print("7. first_half")
	print("8. without_end")
	print("9. combo_string")
	print("10. non_start")
	print("11. left2")
	print("12. exit")
	selection = int(input(">>"))
	
	if selection == 1:
		name = input("Please enter your name.")
		print(hello_name(name))
	elif selection == 2:
		a = input("Please enter a character")
		b = input("Please enter another character")
		print(make_abba(a, b))
	elif selection == 3:
		tag = input("Please enter a tag")
		word = input("Please enter a word")
		print(make_tags(tag, word))
	elif selection == 4:
		out = input("please enter the out bounds")
		word = input("please enter a word")
		print(make_out_word(out, word))
	elif selection == 5:
		end = input("please enter a word")
		print(extra_end(end))
	elif selection == 6:
		two = input("please enter a word or characters")
		print(first_two(two))
	elif selection == 7:
		halfs = input("Please enter a word or characters")
		print(first_half(halfs))
	elif selection == 8:
		mid = input("please enter a word")
		print(without_end(mid))
	elif selection == 9:
		first = input("Please enter the first word")
		second = input("Please enter the second word")
		print(combo_string(first, second))
	elif selection == 10:
		a = input("Please enter a word")
		b = input("Please enter another word")
		print(non_start(a, b))
	elif selection == 11:
		left = input("Please enter a word")
		print(left2(left))
	elif selection == 12:
		exit
	else:
		print("invalid selection")
		menu()											


#functions--------------------------------

def hello_name(name):
  ans = "Hello " + name + "!"
  return ans
  
def make_abba(a, b):
  ans = a + b + b + a
  return ans
  
def make_tags(tag, word):
  o_tag = "<" + tag + ">"
  c_tag = "</" + tag + ">"
  ans = o_tag + word + c_tag
  return ans
  
def make_out_word(out, word):
  num = len(out) / 2
  o_out = out[:num]
  c_out = out[num:]
  ans = o_out + word + c_out
  return ans
  
def extra_end(str):
  
  twoEnd = str[-2:]
  ans = twoEnd + twoEnd + twoEnd
  return ans
  
def first_two(str):
  if len(str) <= 2:
    return str
  ans = str[:2]
  return ans
  
def first_half(str):
  total = int(round(float(len(str) / 2)))
  half = str[:total]
  return half 
  
def without_end(str):
  total = len(str) - 1
  middle = str[1:total]
  return middle 
  
def combo_string(a, b):
  first_str = len(a)
  second_str = len(b)
  if first_str > second_str:
    combo = b + a + b
  elif second_str > first_str:
    combo = a + b + a
  return combo
  
def non_start(a, b):
  first_str = a[1:]
  second_str = b[1:]
  ans = first_str + second_str
  return ans
  
def left2(str):
  first = str[:2]
  last = str[2:]
  ans = last + first
  return ans

#main-------------------------------------
def main():
	menu()
	
main()
