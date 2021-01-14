original_str = "The quick brown rhino jumped over the extremely lazy fox"

num_words_list = []
original_str_lst = original_str.split()

for word in original_str_lst:
    num_words_list.append(len(word))

print(num_words_list)
