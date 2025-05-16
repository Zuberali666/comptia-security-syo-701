import time
import random
from datetime import datetime
from tabulate import tabulate

def display_question(question, options, time_left):
    print(f"\n⏳ Time left: {int(time_left)} seconds")
    print(question)
    for key, value in options.items():
        print(f"{key}. {value}")

def septer():
    return input("Enter your answer (a/b/c/d): ")

def evaluate_answer(user, correct_answer, options):
    if user.lower() == correct_answer:
        print("✅ Correct answer!")
        return True
    else:
        print("❌ Wrong answer.")
        print("You selected:", options.get(user.lower(), "Invalid option"))
        print("-" * 40)
        return True  # Still return True to move on


def shuffle_options(q_data):
    # Original options as list of (key, value)
    original_options = list(q_data["options"].items())
    correct_answer_key = q_data["answer"]
    correct_answer_value = q_data["options"][correct_answer_key]

    # Extract only values and shuffle
    option_values = [val for key, val in original_options]
    random.shuffle(option_values)

    # Reassign keys a, b, c, d
    new_keys = ['a', 'b', 'c', 'd']
    shuffled_options = {k: v for k, v in zip(new_keys, option_values)}

    # Find new key for the correct answer value
    for k, v in shuffled_options.items():
        if v == correct_answer_value:
            new_correct_answer = k
            break

    return shuffled_options, new_correct_answer

def ask_question(q_data, time_left, start_time, time_limit):
    # Show time and question first
    print(f"\n⏳ Time left: {int(time_left)} seconds")
    print(q_data["question"])

    # Show table if available
    if "table" in q_data:
        print(tabulate(q_data["table"]["data"], headers=q_data["table"]["headers"], tablefmt="grid"))

    # Shuffle and display options
    shuffled_options, new_correct_answer = shuffle_options(q_data)
    for key, value in shuffled_options.items():
        print(f"{key}. {value}")

    # Time check
    current_time = time.time()
    if current_time - start_time >= time_limit:
        print("\n⛔ Time's up!")
        return False, False

    # User input and evaluation
    user_input = septer()
    correct = user_input.lower() == new_correct_answer
    evaluate_answer(user_input, new_correct_answer, shuffled_options)

    return True, correct


def main():
    username = input("Enter your name: ").strip()
    time_limit = 60  # seconds
    start_time = time.time()
    correct_count = 0
    completed_count = 0

    questions = [
        {
            "question": "1. Matt is updating the organization's threat assessment process. What category of control is Matt implementing?",
            "options": {
                "a": "Operational",
                "b": "Technical",
                "c": "Corrective",
                "d": "Managerial"
            },
            "answer": "d"
      
        }, 
        {
            "question": "2. Jade's organization recently suffered a security breach that affected stored credit card data. Jade's primary concern is the fact that the organization is subject to sanctions for violating the provisions of the Payment Card Industry Data Security Standard. What category of risk is concerning Jade?",
            "options": {
                "a": "Strategic",
                "b": "Compliance",
                "c": "Operational",
                "d": "Financial"
            },
            "answer": "b"
     
        },
        {
            "question": "3. Chris is responding to a security incident that compromised one of his organization's web servers. He believes that the attackers defaced one or more pages on the website. What cybersecurity objective did this attack violate?",
            "options": {
                "a": "Confidentiality",
                "b": "Nonrepudiation",
                "c": "Integrity",
                "d": "Availability"
            },
            "answer": "c"
     
        },
        {
            "question": "4. Gwen is exploring a customer transaction reporting system and discovers the table shown here. What type of data minimization has most likely been used on this table?",
            "table": {
                "data": [
                  [1023, "$46,438", "11/3/2020", "**** **** **** 1858"],
                  [1024, "$83,007", "9/22/2020", "**** **** **** 8925"],
                  [1025, "$42,289", "7/19/2020", "**** **** **** 8184"],
                  [1026, "$10,119", "8/4/2020", "**** **** **** 5660"],
                  [1027, "$24,223", "7/16/2020", "**** **** **** 8823"],
                  [1028, "$57,657", "7/8/2020", "**** **** **** 3691"],
                  [1029, "$94,558", "2/10/2020", "**** **** **** 8371"],
                  [1030, "$33,570", "5/17/2020", "**** **** **** 8661"],
                  [1031, "$96,829", "3/20/2020", "**** **** **** 3711"],
                  [1032, "$32,487", "12/17/2020", "**** **** **** 4868"],
                  [1033, "$29,055", "6/14/2020", "**** **** **** 1698"],
                  [1034, "$14,932", "5/4/2020", "**** **** **** 8844"],
                  [1035, "$20,734", "1/19/2020", "**** **** **** 9030"],
                  [1036, "$90,210", "6/2/2020", "**** **** **** 1946"],
                  [1037, "$36,104", "6/11/2020", "**** **** **** 1595"],
                  [1038, "$81,171", "3/13/2020", "**** **** **** 9520"],
                  [1039, "$57,738", "4/4/2020", "**** **** **** 1612"],
                  [1040, "$60,712", "5/25/2020", "**** **** **** 8166"],
                  [1041, "$37,572", "1/22/2020", "**** **** **** 6566"],
                  [1042, "$21,496", "12/17/2020", "**** **** **** 4009"]
                ],
                "headers": ["Order Number", "Amount", "Date", "Credit Card Number"]
            },
            "options": {
                "a": "Destruction",
                "b": "Masking",
                "c": "Tokenization",
                "d": "Hashing"
            },
            "answer": "b"
     
        },
        {
            "question": "5. Tonya is concerned about the risk that an attacker will attempt to gain access to her organization's database server. She is searching for a control that would discourage the attacker from attempting to gain access. What type of security control is she seeking to implement?",
            "options": {
                "a": "Preventive",
                "b": "Detective",
                "c": "Corrective",
                "d": "Deterrent"
            },
                "answer": "d"
     
        }, 
        {
            "question": "6. Greg is implementing a data loss prevention system. He would like to ensure that it protects against transmissions of sensitive information by guests on his wireless network. What DLP technology would best meet this goal?",
            "options": {
                "a": "Watermarking",
                "b": "Pattern recognition",
                "c": "Host-based",
                "d": "Network-based"
            },
                "answer": "d"
     
        },
        {
            "question": "7. What term best describes data that is being sent between two systems over a network connection?",
            "options": {
                "a": "Data at rest",
                "b": "Data in transit",
                "c": "Data in processing",
                "d": "Data in use"
            },
            "answer": "b"
    
        },
        {
            "question": "8. Tina is tuning her organization's intrusion prevention system to prevent false positive alerts. What type of control is Tina implementing?",
            "options": {
                "a": "Technical control",
                "b": "Physical control",
                "c": "Managerial control",
                "d": "Operational control"
            },
            "answer": "a"
        },
        {
            "question": "9. Which one of the following is not a common goal of a cybersecurity attacker?","options": {
                "a": "Disclosure",
                "b": "Denial",
                "c": "Alteration",
                "d": "Allocation"
            },
            "answer": "d"
        },
        {
            "question": "10. Tony is reviewing the status of his organization's defenses against a breach of their file server. He believes that a compromise of the file server could reveal information that would prevent the company from continuing to do business. What term best describes the risk that Tony is considering?",
            "options": {
                "a": "Strategic",
                "b": "Reputational",
                "c": "Financial",
                "d": "Operational"
                },
                "answer": "d"
        },
        {
            "question": "11. Which one of the following data elements is not commonly associated with identity theft?",
            "options": {
                "a": "Social Security number",
                "b": "Driver's license number",
                "c": "Frequent flyer number",
                "d": "Passport number"
                },
                "answer": "c"
        },
        {
            "question": "12. What term best describes an organization's desired security state?",
            "options": {
                "a": "Control objectives",
                "b": "Security priorities",
                "c": "Strategic goals",
                "d": "Best practices"
                },
                "answer": "a"
        },
        {
            "question": "13. Lou mounted the sign below on the fence surrounding his organization's datacenter. What control type best describes this control?",
            "options": {
                "a": "Compensating",
                "b": "Detective",
                "c": "Physical",
                "d": "Deterrent"
                },
                "answer": "d"
        },
        {
            "question":"14. What technology uses mathematical algorithms to render information unreadable to those lacking the required key?",
            "options":{
                "a": " Data loss prevention",
                "b": "Data obfuscation",
                "c": "Data minimization",
                "d": "Data encryption"
                },
                "answer": "d"
        },
        {
            "question":"15. Greg recently conducted an assessment of his organization's does not use full-disk encryption on laptops. What type of control gap exists in this case?",
            "options":{
                "a": " Detective",
                "b": "Corrective",
                "c": "Deterrent",
                "d": "Preventive"
                },
                "answer": "d"
        },
         {
            "question":"16. What compliance regulation most directly affects the operations of a health-care provider?",
            "options":{
                "a": "HIPAA",
                "b": "PCI DSS",
                "c": "GLBA",
                "d": "SOX"
                },
                "answer": "a"
        },
         {
            "question":"17. Nolan is writing an after action report on a security breach that took place in his organization. The attackers stole thousands of customer records from the organization's database. What cybersecurity principle was most impacted in this breach?",
            "options":{
                "a": " Availability",
                "b": "Nonrepudiation",
                "c": "Confidentiality",
                "d": "Integrity"
                },
                "answer": "c"
        },
         {
            "question":"18. Which one of the following objectives is not one of the three main objectives that information security professionals must achieve to protect their organizations against cybersecurity threats?",
            "options":{
                "a": "Integrity",
                "b": "Nonrepudiation",
                "c":  "Availability",
                "d": "Confidentiality"
                },
                "answer": "b"
        },
         {
            "question":"19. Which one of the following data protection techniques is reversible when conducted properly?",                                            
            "options":{
                "a": "Tokenization",
                "b": " Masking",
                "c": " Hashing",
                "d": " Shredding"
                },
                "answer": "a"
        },
         {
            "question":"20. Which one of the following statements is not true about compensating controls under PCI DSS?",
            "options":{
                "a": "  Controls used to fulfill one PCI DSS requirement may be used to compensate for the absence of a control needed to meet another requirement.",
                "b": "Controls must meet the intent of the original requirement.",
                "c": "Controls must meet the rigor of the original requirement.",
                "d": "Compensating controls must provide a similar level of defense as the original requirement."
                },
                "answer": "a"
        },
    ]

    random.shuffle(questions)

    print(f"\n🕒 {username}, your quiz has started! You have {time_limit} seconds to finish.\n")

    for q in questions:
        current_time = time.time()
        time_left = time_limit - (current_time - start_time)

        if time_left <= 0:
            print("\n⛔ Time's up!")
            break

        answered, correct = ask_question(q, time_left, start_time, time_limit)
        if not answered:
            break
        completed_count += 1
        if correct:
            correct_count += 1

    total_time = time.time() - start_time
    print("=" * 50)
    print(f"🎉 Quiz finished, {username}!")
    print(f"✅ Questions answered: {completed_count}")
    print(f"✔️ Correct answers: {correct_count}")
    print(f"⏱️ Total time used: {total_time:.2f} seconds")
    print("=" * 50)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("quiz_results.txt", "a") as file:
        file.write(f"User: {username} | Time: {timestamp}\n")
        file.write(f"  Questions answered: {completed_count}\n")
        file.write(f"  Correct answers: {correct_count}\n")
        file.write(f"  Total time: {total_time:.2f} seconds\n")
        file.write("-" * 40 + "\n")

    print("💾 Results saved to 'quiz_results.txt'.")

if __name__ == "__main__":
    main()
