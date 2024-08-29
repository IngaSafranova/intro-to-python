def QuestionsMarks(s):
    # To store the last digit found
    last_digit = -1
    # Flag to check if there is at least one valid pair
    found_pair = False

    for i in range(len(s)):
        #print(range(len(s)))
        if s[i].isdigit():
            current_digit = int(s[i])
            # Check if the sum of the current and last digit is 10
            if last_digit != -1 and last_digit + current_digit == 10:
                # Count the number of question marks between last_digit and current_digit
                num_question_marks = s[last_index + 1:i].count('?')
                if num_question_marks == 3:
                    found_pair = True
                else:
                    return "false"
            # Update the last digit and its index
            last_digit = current_digit
            last_index = i

    return "true" if found_pair else "false"
  
print(QuestionsMarks('?asc9???3xsd?kj??7??h'))