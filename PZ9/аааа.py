import random

def create_numbers_files():
  
    pos_numbers = [random.randint(1, 100) for _ in range(20)]
    neg_numbers = [random.randint(-100, -1) for _ in range(20)]
     
      with open("positive_numbers.txt", "w") as f_pos:
        for num in pos_numbers:
            f_pos.write(str(num) + "\n")
    with open("negative_numbers.txt", "w") as f_neg:
        for num in neg_numbers:
            f_neg.write(str(num) + "\n")
          
      create_numbers_files()

    
