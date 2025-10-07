def get_total_scores(class_scores):
    """
    Compute total scores for each student in each section.
    
    Args:
        class_scores (dict): Nested dictionary of the form:
            {
                'Section': {
                    'Student Name': {'Subject1': score1, 'Subject2': score2, ...},
                    ...
                },
                ...
            }
            
    Returns:
        dict: Nested dictionary with total scores:
            {
                'Section': {
                    'Student Name': total_score,
                    ...
                },
                ...
            }
    """
    total_scores = {}
    for section, students in class_scores.items():
        total_scores[section] = {}
        for student, subjects in students.items():
            total_scores[section][student] = sum(subjects.values()) if subjects else 0
    return total_scores

def print_total_scores(total_scores):
    """
    Print total scores in a readable format for any general case.
    
    Args:
        total_scores (dict): Output from get_total_scores.
    """
    for section, students in total_scores.items():
        print(f"Section {section}:")
        if not students:
            print("  No students in this section.")
            continue
        for student, total in students.items():
            print(f"  {student}: {total}")
        print()  # Blank line after each section

# ---------------- Example Usage ----------------
class_scores_example = {
    'A': {
        'Alice Smith': {'Math': 90, 'English': 85, 'Science': 88, 'History': 90, 'PE': 80},
        'Aaron Johnson': {'Math': 85, 'English': 90, 'Science': 88, 'History': 85, 'PE': 62}
    },
    'B': {
        'Brenda Lee': {'Math': 80, 'English': 88, 'Science': 92, 'History': 78, 'PE': 50},
        'Ben Miller': {'Math': 90, 'English': 85, 'Science': 87, 'History': 92, 'PE': 67}
    },
    'C': {}  # Empty section example
}

# Compute totals
totals = get_total_scores(class_scores_example)

# Print nicely
print_total_scores(totals)
